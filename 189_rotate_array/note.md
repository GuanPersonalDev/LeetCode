---
title: 189. Rotate Array
number: 189
difficulty: Medium
tags: [陣列, 雙指標]
link: https://leetcode.com/problems/rotate-array/
---

# 189. Rotate Array

[題目連結](https://leetcode.com/problems/rotate-array/)

## 題目摘要

把陣列 `nums` 往右旋轉 k 步，原地修改。

## 解法一：三次反轉

### 思路

三次反轉：

1. 整個陣列反轉 → 原本最後 k 個元素跑到最前面，但順序是反的
2. 反轉前 k 個 → 恢復它們的順序
3. 反轉剩下的 n - k 個 → 恢復它們的順序

`k %= n` 處理 k 比陣列長的情況。反轉本身用頭尾雙指標交換。

### 複雜度

- 時間：O(n)
- 空間：O(1)

### 程式碼

<<< ./implement_189.py{python}

### 圖解

<TraceViewer src="189/three_reverses" />

::: tip 圖解說明
圖解只追 `rotate` 這一層，所以每一步看到的是**一整次反轉完成後**的陣列；`reverse` 內部的逐次交換不會展開。
:::
