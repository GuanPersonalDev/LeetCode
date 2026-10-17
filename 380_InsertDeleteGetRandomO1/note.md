---
title: 380. Insert Delete GetRandom O(1)
number: 380
difficulty: Medium
tags: [雜湊表, 設計]
link: https://leetcode.com/problems/insert-delete-getrandom-o1/
---

# 380. Insert Delete GetRandom O(1)

[題目連結](https://leetcode.com/problems/insert-delete-getrandom-o1/)

## 題目摘要

設計 `RandomizedSet`，`insert`、`remove`、`getRandom`（每個元素被選到的機率相同）平均都要 O(1)。

## 解法一：陣列 + 雜湊表

### 思路

陣列加雜湊表：

- `data`：存所有元素，`getRandom` 直接 `random.choice` 就是 O(1)
- `map`：值 → 它在 `data` 裡的索引，讓 `insert`、`remove` 能 O(1) 判斷存不存在
- **刪除的技巧**：陣列中間刪除是 O(n)，所以把**最後一個元素搬到被刪除的位置**、更新它在 `map` 的索引，
  再 `pop()` 掉最後一格

### 複雜度

- 時間：三個操作平均 O(1)
- 空間：O(n)

### 程式碼

<<< ./implement_380.py{python}

### 圖解

這是設計題，需要依序呼叫多個方法，圖解工具目前一次只能追蹤一個方法，所以這題沒有動態圖解。
