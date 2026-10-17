<script setup lang="ts">
import { withBase } from 'vitepress'
import { data as problems } from '../problems.data'
</script>

<template>
  <table class="problem-list">
    <thead>
      <tr><th>#</th><th>題目</th><th>難度</th><th>標籤</th></tr>
    </thead>
    <tbody>
      <tr v-for="p in problems" :key="p.number">
        <td>{{ p.number }}</td>
        <td><a :href="withBase(p.url)">{{ p.title }}</a></td>
        <td><span class="difficulty" :class="p.difficulty.toLowerCase()">{{ p.difficulty }}</span></td>
        <td>{{ p.tags.join('、') }}</td>
      </tr>
    </tbody>
  </table>
</template>

<style scoped>
.difficulty.easy { color: var(--vp-c-green-1); }
.difficulty.medium { color: var(--vp-c-yellow-1); }
.difficulty.hard { color: var(--vp-c-red-1); }
</style>
