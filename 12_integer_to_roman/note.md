---
title: 12. Integer to Roman
number: 12
difficulty: Medium
tags: [雜湊表, 數學, 字串]
link: https://leetcode.com/problems/integer-to-roman/
---

# 12. Integer to Roman

[題目連結](https://leetcode.com/problems/integer-to-roman/)

## 題目摘要

把整數 `num`（1 ≤ `num` ≤ 3999）轉成羅馬數字。每個十進位位數各自轉換，
其中 4 和 9 要用「小的符號放在大的左邊」表示，例如 `IV`、`CM`。

## 解法一：逐位數轉換

### 思路

每個位數（千、百、十、個）的寫法規則都一樣，只是用的符號不同。
所以用一張表記下每個位數的 `(位值, 一, 五, 十)` 三個符號，例如百位是 `(100, "C", "D", "M")`；
千位因為 `num` 最大 3999，只會用到 `M`，五和十留空字串。

從千位往個位走，每一位：

1. `d = num // value` 取出這一位的數字，`num %= value` 把它去掉
2. 依 `d` 分四種情況組字串：
   - `d == 9`：`一 + 十`（例如 `CM`）
   - `5 <= d <= 8`：`五 + 一 × (d - 5)`（例如 `DCC`）
   - `d == 4`：`一 + 五`（例如 `CD`）
   - `0 <= d <= 3`：`一 × d`，`d = 0` 時剛好是空字串

### 複雜度

- 時間：O(1)，固定走四個位數
- 空間：O(1)

### 程式碼

<<< ./implement_12.py{python}

### 圖解

<TraceViewer src="12/digit_by_digit" />
