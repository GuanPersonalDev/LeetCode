---
title: 45. Jump Game II
number: 45
difficulty: Medium
tags: [貪婪, 陣列]
link: https://leetcode.com/problems/jump-game-ii/
---

# 45. Jump Game II

[題目連結](https://leetcode.com/problems/jump-game-ii/)

## 題目摘要

`nums[i]` 是在位置 i 最多能跳的距離，保證能到達最後一格，求最少跳幾次。

## 解法一：貪婪分層

### 思路

把跳躍想成一層一層的 BFS：

- `current_jump_limit`：目前這一跳最遠能到的位置（這一層的邊界）
- `farthest_index`：掃過這一層時，下一跳最遠能到的位置
- 每走到一層的邊界（`i == current_jump_limit`），就必須再跳一次，邊界更新成 `farthest_index`

迴圈只跑到倒數第二格：站在最後一格時不需要再跳。

### 複雜度

- 時間：O(n)
- 空間：O(1)

### 程式碼

<<< ./implement_45.py{python}

### 圖解

<TraceViewer src="45/greedy_bfs" />
