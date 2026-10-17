---
title: 13. Roman to Integer
number: 13
difficulty: Easy
tags: [雜湊表, 字串]
link: https://leetcode.com/problems/roman-to-integer/
---

# 13. Roman to Integer

[題目連結](https://leetcode.com/problems/roman-to-integer/)

## 題目摘要

把羅馬數字字串 `s` 轉成整數。羅馬數字通常由大到小排列，但像 `IV`、`CM` 這種「小的在大的左邊」代表相減。

## 解法一：相鄰比較

### 思路

用字典 `roman_list` 查每個符號的值，從左到右掃一次：

- 如果**下一個符號比目前的大**，目前這個符號屬於減法組合（例如 `IV` 的 `I`），就從 `total` **扣掉**
- 否則直接**加上**

這樣不必特別辨識六種減法組合，只要比較相鄰兩個符號的大小。

### 複雜度

- 時間：O(n)
- 空間：O(1)，字典大小固定

### 程式碼

<<< ./implement_13.py{python}

### 圖解

<TraceViewer src="13/compare_next" />
