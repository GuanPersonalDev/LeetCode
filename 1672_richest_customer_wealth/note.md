---
title: 1672. Richest Customer Wealth
number: 1672
difficulty: Easy
tags: [陣列, 矩陣]
link: https://leetcode.com/problems/richest-customer-wealth/
---

# 1672. Richest Customer Wealth

[題目連結](https://leetcode.com/problems/richest-customer-wealth/)

## 題目摘要

`accounts[i][j]` 是第 i 位客戶在第 j 家銀行的存款，求最富有客戶的總資產。

## 解法一：逐列加總

### 思路

逐一加總每位客戶的存款 `sum`，比目前最大值 `max` 大就更新。

### 複雜度

- 時間：O(m × n)
- 空間：O(1)

### 程式碼

<<< ./implement_1672.py{python}

### 圖解

<TraceViewer src="1672/row_sum" />

## 可以再優化的地方

變數 `max`、`sum` 蓋掉了 Python 內建函式，這個函式裡就不能再用 `max()`、`sum()`。
換個名字之後，也可以直接寫成 `return max(sum(row) for row in accounts)`。
