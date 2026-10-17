---
title: 274. H-Index
number: 274
difficulty: Medium
tags: [陣列, 計數排序]
link: https://leetcode.com/problems/h-index/
---

# 274. H-Index

[題目連結](https://leetcode.com/problems/h-index/)

## 題目摘要

`citations[i]` 是第 i 篇論文的被引用次數，求 h 指數：最大的 h，使得至少有 h 篇論文各被引用至少 h 次。

## 解法一：計數

### 思路

h 不可能超過論文數 n，所以用長度 n + 1 的 `counter` 做計數：

- `counter[k]` = 被引用 k 次的論文數；超過 n 次的一律算在 `counter[n]`
- 從 h = n 往下找，`cited_count` 累加「被引用至少 i 次」的論文數，第一個 `cited_count >= i` 的 i 就是答案

不用排序，計數陣列取代了排序。

### 複雜度

- 時間：O(n)
- 空間：O(n)

### 程式碼

<<< ./implement_274.py{python}

### 圖解

<TraceViewer src="274/counting" />
