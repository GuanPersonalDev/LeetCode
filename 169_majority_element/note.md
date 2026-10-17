---
title: 169. Majority Element
number: 169
difficulty: Easy
tags: [陣列, 投票演算法]
link: https://leetcode.com/problems/majority-element/
---

# 169. Majority Element

[題目連結](https://leetcode.com/problems/majority-element/)

## 題目摘要

找出陣列中出現次數超過一半的元素（保證存在）。

## 解法一：投票抵銷

### 思路

Boyer-Moore 投票法：`num` 是目前的候選人，`counter` 是它的淨票數。

- 票數歸零時，換目前這個數當候選人
- 遇到和候選人相同的數 +1，不同的 -1

多數元素的數量比其他所有元素加起來還多，互相抵銷後最後留下的一定是它。

### 複雜度

- 時間：O(n)
- 空間：O(1)

### 程式碼

<<< ./implement_169.py{python}

### 圖解

<TraceViewer src="169/boyer_moore" />
