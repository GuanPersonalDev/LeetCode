<script setup lang="ts">
import { computed, onBeforeUnmount, onMounted, ref, watch } from 'vue'
import { withBase } from 'vitepress'

interface Step {
  line: number
  vars: Record<string, unknown>
  note?: string
  return?: unknown
}

interface TraceCase {
  input: Record<string, unknown>
  result: unknown
  steps: Step[]
}

interface Trace {
  title: string
  source: string
  code: string[]
  range: [number, number]
  view: { arrays: Record<string, string[]>; scalars: string[] }
  cases: Record<string, TraceCase>
}

const props = defineProps<{ src: string }>()

const trace = ref<Trace | null>(null)
const error = ref('')
const caseName = ref('')
const index = ref(0)
const playing = ref(false)
const speed = ref(1)
let timer: ReturnType<typeof setInterval> | undefined

onMounted(async () => {
  try {
    const res = await fetch(withBase(`/traces/${props.src}.json`))
    if (!res.ok) throw new Error(`${res.status} ${res.statusText}`)
    trace.value = await res.json()
    caseName.value = Object.keys(trace.value!.cases)[0]
  } catch (e) {
    error.value = `無法載入圖解 ${props.src}：${(e as Error).message}`
  }
})

onBeforeUnmount(stop)

const current = computed(() => trace.value?.cases[caseName.value])
const steps = computed(() => current.value?.steps ?? [])
const step = computed<Step | undefined>(() => steps.value[index.value])
const prev = computed<Step | undefined>(() => steps.value[index.value - 1])
const lastIndex = computed(() => Math.max(steps.value.length - 1, 0))

const codeLines = computed(() => {
  if (!trace.value) return []
  const [first, last] = trace.value.range
  return trace.value.code.slice(first - 1, last).map((text, i) => ({ no: first + i, text }))
})

const changed = (name: string) =>
  prev.value !== undefined && JSON.stringify(prev.value.vars[name]) !== JSON.stringify(step.value?.vars[name])

const format = (value: unknown) => (value === undefined ? '—' : JSON.stringify(value))

// 字串當成字元陣列畫；尚未賦值或不是序列時視為空
const asList = (value: unknown): unknown[] =>
  Array.isArray(value) ? value : typeof value === 'string' ? [...value] : []

const arrays = computed(() => {
  if (!trace.value || !step.value) return []
  return Object.entries(trace.value.view.arrays).map(([name, pointers]) => {
    const values = asList(step.value!.vars[name])
    const before = prev.value ? asList(prev.value.vars[name]) : values
    // 以整段追蹤的最大值當刻度，播放時長條高度才不會跳動
    const max = Math.max(
      1,
      ...steps.value.flatMap((s) => asList(s.vars[name]).filter((v): v is number => typeof v === 'number')),
    )
    const cells = values.map((value, i) => ({
      value,
      height: typeof value === 'number' ? Math.max(value / max, 0) : null,
      changed: prev.value !== undefined && JSON.stringify(before[i]) !== JSON.stringify(value),
      // 每個指標固定一列，相鄰格子的長名稱才不會疊在一起
      slots: pointers.map((p) => (step.value!.vars[p] === i ? p : null)),
    }))
    return { name, cells, hasBars: cells.some((c) => c.height !== null) }
  })
})

const scalars = computed(() =>
  (trace.value?.view.scalars ?? []).map((name) => ({ name, value: step.value?.vars[name], changed: changed(name) })),
)

function stop() {
  playing.value = false
  clearInterval(timer)
}

function play() {
  if (index.value >= lastIndex.value) index.value = 0
  playing.value = true
  timer = setInterval(() => {
    if (index.value >= lastIndex.value) return stop()
    index.value++
  }, 700 / speed.value)
}

const toggle = () => (playing.value ? stop() : play())
const go = (delta: number) => {
  stop()
  index.value = Math.min(Math.max(index.value + delta, 0), lastIndex.value)
}

watch(caseName, () => {
  stop()
  index.value = 0
})
watch(speed, () => {
  if (playing.value) {
    stop()
    play()
  }
})
</script>

<template>
  <div class="trace-viewer">
    <p v-if="error" class="tv-error">{{ error }}</p>
    <p v-else-if="!trace" class="tv-loading">載入圖解中…</p>
    <template v-else-if="step">
      <div class="tv-header">
        <strong>{{ trace.title }}</strong>
        <select v-if="Object.keys(trace.cases).length > 1" v-model="caseName" aria-label="測資">
          <option v-for="name in Object.keys(trace.cases)" :key="name" :value="name">{{ name }}</option>
        </select>
        <code class="tv-input">{{ format(current!.input) }}</code>
      </div>

      <div class="tv-body">
        <pre class="tv-code"><code><span
          v-for="l in codeLines"
          :key="l.no"
          class="tv-line"
          :class="{ active: l.no === step.line }"
        ><span class="tv-no">{{ l.no }}</span>{{ l.text || ' ' }}</span></code></pre>

        <div class="tv-state">
          <div v-for="arr in arrays" :key="arr.name" class="tv-array">
            <div class="tv-label">{{ arr.name }}</div>
            <div class="tv-cells">
              <div
                v-for="(cell, i) in arr.cells"
                :key="i"
                class="tv-cell"
                :class="{ changed: cell.changed, pointed: cell.slots.some(Boolean), text: cell.height === null }"
              >
                <div v-if="arr.hasBars" class="tv-bar-area">
                  <div v-if="cell.height !== null" class="tv-bar" :style="{ height: `${cell.height * 100}%` }" />
                </div>
                <div class="tv-value">{{ typeof cell.value === 'number' || typeof cell.value === 'string' ? cell.value : format(cell.value) }}</div>
                <div class="tv-index">{{ i }}</div>
                <div class="tv-pointers">
                  <div v-for="(p, k) in cell.slots" :key="k" class="tv-slot">
                    <span v-if="p" class="tv-pointer">{{ p }}</span>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <table v-if="scalars.length" class="tv-scalars">
            <tbody>
              <tr v-for="s in scalars" :key="s.name" :class="{ changed: s.changed }">
                <th>{{ s.name }}</th>
                <td>{{ format(s.value) }}</td>
              </tr>
            </tbody>
          </table>

          <p class="tv-note">
            <template v-if="'return' in step">回傳 <code>{{ format(step.return) }}</code></template>
            <template v-else-if="step.note">{{ step.note }}</template>
            <template v-else>&nbsp;</template>
          </p>
        </div>
      </div>

      <div class="tv-controls">
        <button type="button" :disabled="index === 0" aria-label="上一步" @click="go(-1)">◀</button>
        <button type="button" class="tv-play" :aria-label="playing ? '暫停' : '播放'" @click="toggle">{{ playing ? '❚❚' : '▶' }}</button>
        <button type="button" :disabled="index >= lastIndex" aria-label="下一步" @click="go(1)">▶▶</button>
        <input v-model.number="index" type="range" min="0" :max="lastIndex" aria-label="步驟" @input="stop" />
        <span class="tv-counter">{{ index + 1 }} / {{ steps.length }}</span>
        <select v-model.number="speed" aria-label="速度">
          <option :value="0.5">0.5×</option>
          <option :value="1">1×</option>
          <option :value="2">2×</option>
          <option :value="4">4×</option>
        </select>
      </div>
    </template>
  </div>
</template>

<style scoped>
.trace-viewer {
  margin: 16px 0;
  padding: 16px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 8px;
  background: var(--vp-c-bg-soft);
  container-type: inline-size;
}
.tv-header {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px 12px;
  margin-bottom: 12px;
}
.tv-input {
  font-size: 12px;
  overflow-wrap: anywhere;
}
.tv-body {
  display: grid;
  grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
  gap: 16px;
}
/* 依播放器本身的寬度切換，側欄展開時內容欄比視窗窄很多 */
@container (max-width: 760px) {
  .tv-body {
    grid-template-columns: minmax(0, 1fr);
  }
}
.tv-code {
  margin: 0;
  padding: 8px 0;
  overflow-x: auto;
  font-size: 12.5px;
  line-height: 1.6;
  background: var(--vp-code-block-bg);
  border-radius: 6px;
}
.tv-line {
  display: block;
  padding-right: 12px;
  white-space: pre;
  transition: background-color 0.15s;
}
.tv-line.active {
  background: var(--vp-c-brand-soft);
  box-shadow: inset 3px 0 0 var(--vp-c-brand-1);
}
.tv-no {
  display: inline-block;
  width: 2.5em;
  margin-right: 8px;
  text-align: right;
  color: var(--vp-c-text-3);
  user-select: none;
}
.tv-state {
  min-width: 0;
}
.tv-label {
  font-family: var(--vp-font-family-mono);
  font-size: 13px;
  color: var(--vp-c-text-2);
}
.tv-array {
  margin-bottom: 12px;
}
.tv-cells {
  display: flex;
  gap: 3px;
  overflow-x: auto;
  padding: 0 24px 4px;
}
.tv-cell {
  flex: 0 0 28px;
  /* 指標名稱比格子寬時往兩側溢出，不撐開格子 */
  min-width: 0;
  text-align: center;
  font-family: var(--vp-font-family-mono);
  font-size: 12px;
}
.tv-cell.text {
  flex: 0 0 auto;
  min-width: 28px;
  padding: 0 4px;
}
.tv-cell.text .tv-value {
  border: 1px solid var(--vp-c-divider);
  border-radius: 4px;
  padding: 2px 4px;
}
.tv-cell.text.pointed .tv-value {
  border-color: var(--vp-c-brand-1);
}
.tv-bar-area {
  display: flex;
  align-items: flex-end;
  height: 72px;
  border-bottom: 1px solid var(--vp-c-divider);
}
.tv-bar {
  width: 100%;
  background: var(--vp-c-default-3);
  border-radius: 3px 3px 0 0;
  transition: height 0.25s, background-color 0.25s;
}
.tv-cell.pointed .tv-bar {
  background: var(--vp-c-brand-2);
}
.tv-cell.changed .tv-bar {
  background: var(--vp-c-warning-2);
}
.tv-value {
  margin-top: 2px;
}
.tv-cell.changed .tv-value {
  color: var(--vp-c-warning-1);
  font-weight: 600;
}
.tv-index {
  color: var(--vp-c-text-3);
  font-size: 10px;
}
.tv-slot {
  display: flex;
  justify-content: center;
  height: 18px;
}
.tv-pointer {
  padding: 0 3px;
  font-size: 10px;
  line-height: 16px;
  color: var(--vp-c-white);
  background: var(--vp-c-brand-1);
  border-radius: 3px;
  white-space: nowrap;
}
.tv-scalars {
  display: table;
  margin: 8px 0;
  font-family: var(--vp-font-family-mono);
  font-size: 13px;
}
.tv-scalars th,
.tv-scalars td {
  padding: 4px 10px;
}
.tv-scalars tr {
  transition: background-color 0.25s;
}
.tv-scalars tr.changed {
  background: var(--vp-c-warning-soft);
}
.tv-note {
  min-height: 1.6em;
  margin: 8px 0 0;
  color: var(--vp-c-text-1);
}
.tv-controls {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 8px;
  margin-top: 12px;
}
.tv-controls button,
.tv-controls select,
.tv-header select {
  padding: 2px 10px;
  border: 1px solid var(--vp-c-divider);
  border-radius: 6px;
  background: var(--vp-c-bg);
  color: var(--vp-c-text-1);
  cursor: pointer;
}
.tv-controls button:disabled {
  opacity: 0.4;
  cursor: default;
}
.tv-controls input[type='range'] {
  flex: 1 1 120px;
  accent-color: var(--vp-c-brand-1);
}
.tv-counter {
  font-family: var(--vp-font-family-mono);
  font-size: 12px;
  color: var(--vp-c-text-2);
}
.tv-error {
  color: var(--vp-c-danger-1);
}
</style>
