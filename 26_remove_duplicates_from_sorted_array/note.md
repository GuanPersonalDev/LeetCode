---
title: 26. Remove Duplicates from Sorted Array
number: 26
difficulty: Easy
tags: [雙指標, 陣列]
link: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
---

# 26. Remove Duplicates from Sorted Array

[題目連結](https://leetcode.com/problems/remove-duplicates-from-sorted-array/)

## 題目摘要

給一個已排序的陣列 `nums`，原地移除重複元素，讓每個值只留一個，回傳留下的個數 k（前 k 格即結果）。

## 解法一：快慢指標

### 思路

快慢雙指標：

- `result_index` 指向「結果區」最後一個元素
- `i` 往右掃整個陣列；遇到和 `nums[result_index]` 不同的值，表示出現新數字，
  `result_index` 往前一格並把新數字寫進去

因為陣列已排序，相同的值一定相鄰，只要跟結果區的最後一個比較就好。

### 複雜度

- 時間：O(n)
- 空間：O(1)，原地修改

### 程式碼

<<< ./implement_26.py{python}

### 圖解

<TraceViewer src="26/two_pointers" />
