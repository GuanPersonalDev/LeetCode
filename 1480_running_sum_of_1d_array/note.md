---
title: 1480. Running Sum of 1d Array
number: 1480
difficulty: Easy
tags: [陣列, 前綴和]
link: https://leetcode.com/problems/running-sum-of-1d-array/
---

# 1480. Running Sum of 1d Array

[題目連結](https://leetcode.com/problems/running-sum-of-1d-array/)

## 題目摘要

回傳前綴和陣列：`runningSum[i] = nums[0] + … + nums[i]`。

## 解法一：原地累加

### 思路

原地累加：從第 1 格開始，每格加上前一格（前一格已經是到它為止的總和）。

### 複雜度

- 時間：O(n)
- 空間：O(1)，直接改寫輸入陣列

### 程式碼

<<< ./implement_1480.py{python}

### 圖解

<TraceViewer src="1480/in_place" />
