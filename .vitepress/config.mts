import { readdirSync, readFileSync, existsSync } from 'node:fs'
import { resolve } from 'node:path'
import { defineConfig } from 'vitepress'

const root = resolve(__dirname, '..')

// 只收錄有 note.md 的題目資料夾，依題號排序
function problemSidebar() {
  return readdirSync(root, { withFileTypes: true })
    .filter((d) => d.isDirectory() && /^\d+_/.test(d.name) && existsSync(resolve(root, d.name, 'note.md')))
    .map((d) => {
      const text = readFileSync(resolve(root, d.name, 'note.md'), 'utf8')
      const title = text.match(/^title:\s*(.+)$/m)?.[1].trim() ?? d.name
      return { number: parseInt(d.name, 10), text: title, link: `/${d.name}/` }
    })
    .sort((a, b) => a.number - b.number)
    .map(({ text, link }) => ({ text, link }))
}

export default defineConfig({
  lang: 'zh-TW',
  title: 'LeetCode 解題筆記',
  description: '每題用過的解法與逐步動態圖解',
  base: '/LeetCode/',
  srcDir: '.',
  srcExclude: ['**/node_modules/**', '.venv/**', '.idea/**', 'templates/**', '.claude/**', 'README.md'],
  rewrites: { ':dir/note.md': ':dir/index.md' },
  cleanUrls: true,
  lastUpdated: true,
  markdown: { math: false },
  themeConfig: {
    nav: [{ text: '題目列表', link: '/' }],
    sidebar: [{ text: '題目', items: problemSidebar() }],
    outline: { label: '本頁內容' },
    docFooter: { prev: '上一題', next: '下一題' },
    lastUpdated: { text: '最後更新' },
    socialLinks: [{ icon: 'github', link: 'https://github.com/GuanPersonalDev/LeetCode' }],
  },
})
