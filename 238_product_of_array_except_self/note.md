---
title: 238. Product of Array Except Self
number: 238
difficulty: Medium
tags: [陣列, 前綴積]
link: https://leetcode.com/problems/product-of-array-except-self/
---

# 238. Product of Array Except Self

[題目連結](https://leetcode.com/problems/product-of-array-except-self/)

## 題目摘要

回傳陣列 `answer`，`answer[i]` 是 `nums` 中除了 `nums[i]` 以外所有元素的乘積，不能用除法。

## 解法一：左右兩趟乘積

### 思路

`answer[i]` = （i 左邊所有數的乘積）×（i 右邊所有數的乘積）。

- 第一趟從左往右：`answer[i]` 先放左側乘積 `left_product`，再把 `nums[i]` 乘進去
- 第二趟從右往左：`answer[i]` 乘上右側乘積 `right_product`，再把 `nums[i]` 乘進去

直接用輸出陣列存左側乘積，額外空間只有兩個變數。

### 複雜度

- 時間：O(n)
- 空間：O(1)（不計輸出陣列）

### 程式碼

<<< ./implement_238.py{python}

### 圖解

<TraceViewer src="238/prefix_suffix" />
