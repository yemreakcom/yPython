---
description: Python liste yapısı (list)
---

# 📋 List

## 🔰 List Yapısını Tanıyalım

* 🍱 Birden fazla veriyi saklamak için kullanılan değişkendir. \(array\)
* 🩹 Birbirinden farklı değişkenleri tutabilir \(_confused list_\)
* 👯‍♀️ Aynı değişken birden fazla tekrar edebilir
* 👀 Hızlıca göz atmak için [buraya](https://www.programiz.com/python-programming/list) buraya bakabilirsin

## 💎 List Metotları

| List Metotları | Açıklama |
| :--- | :--- |
| `len(list)` | Karakter sayısı |
| `list.append(<value>)` | Eleman ekleme |
| `del list[i]` | `i`. elemanı silme |
| `list.remove(elem)` | `elem`'i silme |
| `list[i]` veya `list.get(i)` | `i`. karakter |
| `list[-i]` | `len-i`. karakter |
| `list[i:]` | `i`. eleman ve sonrasındakiler |
| `list[:i]` | `i`. elemana kadar \(`i` dahil değil\) olanlar |
| `list[i:j]` | `i`. eleman ve `j`. elemana kadar \(`j` dahil değil\) olanlar |
| list\[:\] |  |
| `[5] * i` | `i` tane 5 sayısı \(`i=3` için `[5, 5, 5]`\) |

## 🍢 Tek Satır List Yapısı

*  İstenen koşullardaki elemanların listesini verir

```python
[<değişken> for <değişken> in <dizi | liste | menzil> if <koşul>]
example = [x for x in range(0, 5) if x != 20]
```

## 👮‍♂️ İki Listenin Sıralı Farkı

```python
a = [1, 2, 20, 6, 210]
b = set([6, 20, 1])
[x for x in a if x not in b]
```

> [Converting a list to a set changes element order](https://stackoverflow.com/a/9792680)

## 🙄 İki Listenin Sırasız Farkı

```python
a = [1, 2, 20, 6, 210]
b = [1, 2, 210]
list3 = list(set(list1) - set(list2))
```

> [Remove all values within one list from another list?](https://stackoverflow.com/a/30353802)

