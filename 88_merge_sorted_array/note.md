---
title: 88. Merge Sorted Array
number: 88
difficulty: Easy
tags: [雙指標, 排序]
link: https://leetcode.com/problems/merge-sorted-array/
---

# 88. Merge Sorted Array

[題目連結](https://leetcode.com/problems/merge-sorted-array/)

## 題目摘要

把已排序的 `nums2`（n 個）合併進已排序的 `nums1`（前 m 個有效、後 n 格是 0），結果原地存在 `nums1`。

## 解法一：由後往前合併

### 思路

**從後面往前填**，就不會覆蓋到 `nums1` 還沒處理的元素：

- `current_index` 從 `m + n - 1` 往前，是要寫入的位置
- `nums1_progress`、`nums2_progress` 分別指向兩個陣列還沒放的最大值
- 每次挑兩者中較大的放進 `current_index`，對應的指標往前一格
- 其中一邊用完時，直接搬另一邊剩下的

### 複雜度

- 時間：O(m + n)
- 空間：O(1)

### 程式碼

<<< ./implement_88.py{python}

### 圖解

<TraceViewer src="88/merge_from_back" />

## 可以再優化的地方

`else` 分支只會在兩個指標都 `>= 0` 時進入，所以 `a`、`b` 那兩行的 `if ... else 0` 永遠用不到，
可以直接寫成 `a = nums1[nums1_progress]`。另外 `elif nums2_progress < 0` 那段其實可以省略：
nums2 用完時，nums1 剩下的元素本來就已經在正確的位置上，迴圈條件改成 `while nums2_progress >= 0` 即可。
