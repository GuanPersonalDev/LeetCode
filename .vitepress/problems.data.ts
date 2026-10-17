import { createContentLoader } from 'vitepress'

export interface Problem {
  number: number
  title: string
  difficulty: string
  tags: string[]
  url: string
}

declare const data: Problem[]
export { data }

export default createContentLoader('*/note.md', {
  transform(raw): Problem[] {
    return raw
      // 只收題目資料夾（<編號>_<題名>），排除 templates/ 等
      .filter(({ url }) => /^\/\d+_/.test(url))
      .map(({ url, frontmatter }) => ({
        number: Number(frontmatter.number),
        title: frontmatter.title,
        difficulty: frontmatter.difficulty ?? '',
        tags: frontmatter.tags ?? [],
        // 載入器給的是 rewrites 之前的網址（/xx/note），換成實際頁面的 /xx/
        url: url.replace(/note$/, ''),
      }))
      .sort((a, b) => a.number - b.number)
  },
})
