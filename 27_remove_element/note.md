---
title: 27. Remove Element
number: 27
difficulty: Easy
tags: [雙指標, 陣列]
link: https://leetcode.com/problems/remove-element/
---

# 27. Remove Element

[題目連結](https://leetcode.com/problems/remove-element/)

## 題目摘要

原地移除陣列 `nums` 中所有等於 `val` 的元素，回傳剩下的個數 k，前 k 格放剩下的元素（順序不限）。

## 解法一：覆寫保留

### 思路

`result_len` 同時是「已保留的個數」和「下一個要寫入的位置」。
`i` 掃過每個元素，只要不等於 `val` 就寫到 `nums[result_len]`，再把 `result_len` 加一。
等於 `val` 的元素直接跳過，自然會被後面保留的元素覆蓋。

### 複雜度

- 時間：O(n)
- 空間：O(1)，原地修改

### 程式碼

<<< ./implement_27.py{python}

### 圖解

<TraceViewer src="27/overwrite" />
