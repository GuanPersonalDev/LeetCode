---
title: 876. Middle of the Linked List
number: 876
difficulty: Easy
tags: [Linked List, 快慢指標]
link: https://leetcode.com/problems/middle-of-the-linked-list/
---

# 876. Middle of the Linked List

[題目連結](https://leetcode.com/problems/middle-of-the-linked-list/)

## 題目摘要

回傳單向 linked list 的中間節點；長度為偶數時回傳中間兩個中的第二個。

## 解法一：快慢指標

### 思路

快慢指標：`slow` 一次走一步、`fast` 一次走兩步。
`fast` 走到尾端（`fast` 或 `fast.next` 為 `None`）時，`slow` 剛好走了一半，就是中間節點。
偶數長度時 `fast` 會停在 `None`，`slow` 正好落在中間偏右那個，符合題目要求。

### 複雜度

- 時間：O(n)
- 空間：O(1)

### 程式碼

<<< ./implement_876.py{python}

### 圖解

播放器目前只會畫陣列與數值，還不支援 linked list 節點，所以這題沒有動態圖解。
