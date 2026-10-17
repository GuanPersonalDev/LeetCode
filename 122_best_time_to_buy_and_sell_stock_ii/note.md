---
title: 122. Best Time to Buy and Sell Stock II
number: 122
difficulty: Medium
tags: [貪婪, 陣列]
link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
---

# 122. Best Time to Buy and Sell Stock II

[題目連結](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

## 題目摘要

`prices[i]` 是第 i 天的股價，可以買賣任意多次（同時最多持有一股），求最大總獲利。

## 解法一：累加每段上漲

### 思路

任何一段上漲都可以拆成「每天漲一點」的總和，所以只要**把每一次相鄰兩天的上漲都吃下來**：
`prices[i] > prices[i-1]` 時，把差額加進 `profit`。下跌的日子不交易。

### 複雜度

- 時間：O(n)
- 空間：O(1)

### 程式碼

<<< ./implement_122.py{python}

### 圖解

<TraceViewer src="122/sum_rises" />
