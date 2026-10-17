---
name: add-note
description: >
  為一個 LeetCode 題目新增或補充解題筆記（note.md）與動態圖解（trace_*.py），並驗證、commit。
  觸發時機：使用者說「幫我新增 42 題的筆記」「把 135 寫成 note」「這題幫我做圖解」「補一個解法到筆記」，
  或任何要把某題整理進網站的意圖。直接處理，不必再問是否允許修改。
---

# 新增解題筆記

網站是 VitePress，每題資料夾（`<編號>_<題名>/`）裡有 `note.md` 才會被收錄。
圖解由 `leetviz` 以 `sys.settrace` 實際執行使用者的解法、逐行錄下變數，網站的 `<TraceViewer>` 播放。

## 可以動與不能動的檔案

- **可直接新增、修改並 commit**：該題的 `note.md`、`trace_*.py`
- **不可修改、不可新增**：任何 `implement_*.py`（使用者自己的解題練習）。
  解法有錯或想改寫時，只給說明與片段
- 資料夾名稱有錯字也不改名（網址會跟著變）
- push 是對外動作，每次都先問

## 流程

### 1. 確認題目與解法

- 找到 `<編號>_*/implement_*.py`，完整讀過。**沒有解法檔就停下來**，請使用者先寫解法
- `git log --follow -p -- <解法檔>` 看歷史：若較早的版本用的是**不同的解法**（不只是小幅優化），
  列給使用者，問要不要也寫進筆記。舊版本不能被追蹤（只有現存的檔案能被執行），只能用文字與片段記錄
- 已經有 `note.md` 時是「補充」：保留原有內容，只加新的段落

### 2. 寫 `note.md`

以 `templates/note.md` 為底稿，完整範例參考 `42_trapping_rain_water/note.md`。

- frontmatter：`title`（`<編號>. <官方英文題名>`）、`number`、`difficulty`（Easy / Medium / Hard）、
  `tags`（中文）、`link`（`https://leetcode.com/problems/<slug>/`）。題名、難度、slug 不確定就查官網，不要猜
- **題目摘要**：用自己的話兩三句講清楚，不要整段貼題目原文
- **思路、複雜度**：描述**使用者這份程式碼實際的做法**，不是換成你認為更好的解法。
  有更好的做法可以另起一段「可以再優化的地方」
- **程式碼**：`<<< ./implement_<編號>.py{python}`
- **踩過的坑**：只寫使用者說過的、或 git 歷史看得出來的；沒有就整節刪掉，不要編
- 一題多個解法：「解法一」「解法二」⋯⋯各自一節，每節都有思路／複雜度／程式碼／圖解

### 3. 寫 `trace_<編號>.py`

```python
from leetviz import trace_solution

trace_solution(
    title="<解法名>",
    source="implement_<編號>.py",          # 相對於這個 trace 檔
    method="Solution.<方法名>",
    cases={"基本：...": {"<參數名>": <值>}, "邊界：...": {...}, "複雜：...": {...}},  # 參數名要跟方法簽名一致
    arrays={"<陣列變數>": ["<指標變數>", ...]},
    scalars=["<要顯示的數值變數>", ...],
    notes={"<原始碼那一行去掉縮排後的完整文字>": "<這一步在做什麼>"},
    out="<編號>/<解法英文代稱>",             # 對應 <TraceViewer src="<編號>/<解法英文代稱>" />
)
```

- `cases`：**三類都要有**，每類組數不限，名稱以類別開頭（例如 `"基本：[2,0,2]"`、`"邊界：單一元素"`），
  依「基本 → 邊界 → 複雜」的順序排：
  1. **基本**：最簡單、剛好能說明演算法為什麼成立的輸入
  2. **邊界**：題目限制（Constraints）的極端值，例如最短長度、全部相同、空陣列（限制允許時）、k 大於長度、答案為 0／-1
  3. **複雜**：較長或情況交錯的輸入，通常包含 LeetCode 的官方範例
  - 所有輸入都必須符合題目的 Constraints，不放題目不允許的輸入
  - 每組都要夠小（上限 1000 步，超過會報錯）
- `arrays`：會被畫成長條格子的 list 變數；指標是存索引的 int 變數。值不是數字的 list 也能畫，只是沒有長條
- `scalars`：累計值、目前最大值、計數器這類
- `notes`：鍵必須和原始碼那一行 `strip()` 後**完全相同**，對不到會報錯。只挑關鍵的幾行寫
- 每一步顯示的是「反白那一行**執行前**」的變數
- 一題多個解法 → 每個解法各一個 trace 檔（`trace_<編號>_<代稱>.py`），`out` 各自不同

**不做圖解的情況**（筆記照寫，省略 `<TraceViewer>`，並告訴使用者原因）：

- 資料結構是 linked list、tree、graph：播放器目前只會畫陣列與數值
- 設計題（例如 380）需要依序呼叫多個方法：tracer 一次只追一個方法
- 主要邏輯在另一個函式裡：tracer 只追 `method` 本身，不展開它呼叫的函式

### 4. 驗證

在 LeetCode repo 根目錄執行：

```bash
npm run trace
npm run build
```

- `npm run trace` 沒有報錯；打開 `public/traces/<編號>/<代稱>.json`，確認每個 case 的 `result` 等於題目範例的預期答案
- `npm run build` 成功
- 有圖解時，用 `npx vitepress preview --port 4173` 開 `http://localhost:4173/LeetCode/<資料夾>/`，
  按幾次「下一步」確認指標與數值合理、說明有出現。預覽伺服器啟動時會快取檔案，重新 build 後要重啟它
- `git status` 確認沒有任何 `implement_*.py` 被改動

### 5. Commit

只 add 這次新增或修改的 `note.md`、`trace_*.py`，訊息用 `docs: add note for <編號>`（補充時用 `docs: update note for <編號>`），
署名照當下環境的 commit 規則。完成後回報網址路徑與步數，並問要不要 push（push 到 `master` 就會自動部署）。
