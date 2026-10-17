---
title: 412. Fizz Buzz
number: 412
difficulty: Easy
tags: [數學, 字串, 模擬]
link: https://leetcode.com/problems/fizz-buzz/
---

# 412. Fizz Buzz

[題目連結](https://leetcode.com/problems/fizz-buzz/)

## 題目摘要

回傳 1 到 n 的字串陣列：3 的倍數換成 `Fizz`、5 的倍數換成 `Buzz`、兩者皆是換成 `FizzBuzz`，其餘放數字本身。

## 解法一：字串累加

### 思路

用字串累加，不必特別寫「同時是 3 和 5 的倍數」的判斷：
是 3 的倍數就接上 `Fizz`、是 5 的倍數再接上 `Buzz`，最後字串還是空的才放數字。

### 複雜度

- 時間：O(n)
- 空間：O(1)（不計輸出陣列）

### 程式碼

<<< ./implement_412.py{python}

### 圖解

<TraceViewer src="412/concat" />

## 可以再優化的地方

變數名稱 `str` 蓋掉了 Python 內建的 `str`，在這個函式裡之後就不能再用 `str(i)`，換個名字（例如 `word`）比較安全。
