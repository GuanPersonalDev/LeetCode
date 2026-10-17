import DefaultTheme from 'vitepress/theme'
import type { Theme } from 'vitepress'
import TraceViewer from './TraceViewer.vue'
import ProblemList from './ProblemList.vue'

export default {
  extends: DefaultTheme,
  enhanceApp({ app }) {
    app.component('TraceViewer', TraceViewer)
    app.component('ProblemList', ProblemList)
  },
} satisfies Theme
