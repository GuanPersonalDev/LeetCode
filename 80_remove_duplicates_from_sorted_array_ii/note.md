---
title: 80. Remove Duplicates from Sorted Array II
number: 80
difficulty: Medium
tags: [雙指標, 陣列]
link: https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
---

# 80. Remove Duplicates from Sorted Array II

[題目連結](https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

## 題目摘要

已排序的陣列 `nums`，原地移除多餘的重複元素，讓每個值**最多出現兩次**，回傳留下的個數。

## 解法一：與倒數第二個比較

### 思路

`current_index` 是下一個要寫入的位置。對每個 `n`：

- 前兩個元素一定保留（`current_index < 2`）
- 之後只要 `n` 比結果區**倒數第二個**元素大，就代表這個值在結果區還不到兩個，可以保留

因為陣列已排序，和 `nums[current_index - 2]` 比就能知道會不會變成第三個重複。

### 複雜度

- 時間：O(n)
- 空間：O(1)，原地修改

### 程式碼

<<< ./implement_80.py{python}

### 圖解

<TraceViewer src="80/compare_second_last" />
