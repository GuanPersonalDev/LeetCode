---
title: 55. Jump Game
number: 55
difficulty: Medium
tags: [貪婪, 陣列]
link: https://leetcode.com/problems/jump-game/
---

# 55. Jump Game

[題目連結](https://leetcode.com/problems/jump-game/)

## 題目摘要

`nums[i]` 是在位置 i 最多能跳的距離，從第 0 格出發，判斷能不能到達最後一格。

## 解法一：剩餘步數

### 思路

`s` 代表「走到目前這格時，還剩下多少步可以用」：

- 走進新的一格前若 `s < 0`，表示上一格就已經沒步數了，到不了這裡，回傳 `False`
- 這一格的跳躍力 `n` 比剩餘步數多，就換成用這一格的（`s = n`）
- 往下一格走要花一步，`s -= 1`

整個陣列都走得進去就回傳 `True`。

### 複雜度

- 時間：O(n)
- 空間：O(1)

### 程式碼

<<< ./implement_55.py{python}

### 圖解

<TraceViewer src="55/remaining_steps" />
