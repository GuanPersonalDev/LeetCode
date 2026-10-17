---
title: 135. Candy
number: 135
difficulty: Hard
tags: [貪婪, 陣列]
link: https://leetcode.com/problems/candy/
---

# 135. Candy

[題目連結](https://leetcode.com/problems/candy/)

## 題目摘要

一排小孩各有評分 `ratings`，每人至少一顆糖，評分比相鄰的人高就要拿得比對方多，求最少要發幾顆。

## 解法一：上下坡計數

### 思路

先假設每人一顆（`total_count = l`），再一段一段處理「上坡」與「下坡」：

- 評分和前一個一樣：不受限制，跳過
- **上坡**：連續上升時，第 k 個上坡位置要比起點多 k 顆，`increase_step` 逐次累加
- **下坡**：連續下降同理，由坡底往回看也是 1、2、3⋯⋯，`decrease_step` 逐次累加
- **山頂**同時被上坡與下坡算到一次，只需要取兩者中較大的，所以扣掉 `min(increase_step, decrease_step)`

一次掃完，不用額外陣列。

### 複雜度

- 時間：O(n)
- 空間：O(1)

### 程式碼

<<< ./implement_135.py{python}

### 圖解

<TraceViewer src="135/slopes" />
