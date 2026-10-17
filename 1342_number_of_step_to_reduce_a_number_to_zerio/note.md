---
title: 1342. Number of Steps to Reduce a Number to Zero
number: 1342
difficulty: Easy
tags: [數學, 位元運算]
link: https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
---

# 1342. Number of Steps to Reduce a Number to Zero

[題目連結](https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/)

## 題目摘要

給整數 `num`，偶數就除以 2、奇數就減 1，問幾步會變成 0。

## 解法一：模擬

### 思路

照題目模擬：`num` 不為 0 就持續操作並計數。

### 複雜度

- 時間：O(log num)
- 空間：O(1)

### 程式碼

<<< ./implement_1342.py{python}

### 圖解

<TraceViewer src="1342/simulate" />

## 可以再優化的地方

`num / 2` 在 Python 3 會得到浮點數（14 → 7.0），結果剛好正確，但數字很大時浮點數會失去精度。
整數除法用 `num // 2`（或位元運算 `num >>= 1`）比較穩。
