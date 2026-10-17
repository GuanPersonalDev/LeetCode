---
title: 134. Gas Station
number: 134
difficulty: Medium
tags: [貪婪, 陣列]
link: https://leetcode.com/problems/gas-station/
---

# 134. Gas Station

[題目連結](https://leetcode.com/problems/gas-station/)

## 題目摘要

環狀路線上有 n 個加油站，`gas[i]` 是站 i 能加的油、`cost[i]` 是開到下一站要花的油，找出能繞一圈的起點（保證唯一），不行就回傳 -1。

## 解法一：油箱歸零換起點

### 思路

兩個觀察：

1. 總油量 `sum(gas)` 少於總消耗 `sum(cost)`，怎樣都繞不完 → `-1`
2. 從 `start_index` 出發，開到站 i 時油箱變負，代表 `start_index` 到 i 之間**任何一站**當起點都到不了 i+1，
   起點直接跳到 `i + 1`、油箱歸零重來

總油量足夠時，最後留下的 `start_index` 就是答案。

### 複雜度

- 時間：O(n)
- 空間：O(1)

### 程式碼

<<< ./implement_134.py{python}

### 圖解

<TraceViewer src="134/reset_start" />
