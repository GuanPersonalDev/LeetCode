---
title: 42. Trapping Rain Water
number: 42
difficulty: Hard
tags: [雙指標, 陣列]
link: https://leetcode.com/problems/trapping-rain-water/
---

# 42. Trapping Rain Water

[題目連結](https://leetcode.com/problems/trapping-rain-water/)

## 題目摘要

給一個非負整數陣列 `height`，每個元素是寬度 1 的牆高，求下雨後能接住多少單位的水。

## 解法一：雙指標

### 思路

一格能裝的水 = `min(左側最高, 右側最高) - 自己的高度`。

左右各放一個指標，並各自記住目前看過的最高牆 `left_max`、`right_max`。
哪一側的最高牆比較矮，那一側下一格的水位就已經確定（另一側一定有更高的牆擋著），
所以移動較矮那一側的指標、累加水量即可，不需要事先算出每格兩側的最高值。

### 複雜度

- 時間：O(n)，每格只被走過一次
- 空間：O(1)

### 程式碼

<<< ./implement_42.py{python}

### 圖解

<TraceViewer src="42/two_pointers" />
