---
title: 121. Best Time to Buy and Sell Stock
number: 121
difficulty: Easy
tags: [陣列, 動態規劃]
link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
---

# 121. Best Time to Buy and Sell Stock

[題目連結](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## 題目摘要

`prices[i]` 是第 i 天的股價，只能買一次、賣一次（先買後賣），求最大獲利；沒有獲利就回傳 0。

## 解法一：記住最低價

### 思路

一路往右掃，記住**到目前為止的最低價** `min_price`：

- 今天比最低價還低 → 更新最低價（今天不可能是賣出日，直接 `continue`）
- 否則計算「今天賣出」的獲利 `p - min_price`，比目前最佳的大就更新 `max_profit`

### 複雜度

- 時間：O(n)
- 空間：O(1)

### 程式碼

<<< ./implement_121.py{python}

### 圖解

<TraceViewer src="121/track_min" />
