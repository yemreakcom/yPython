---
description: Python üzerinde döngüler
---

# 💫 Döngüler

## 🔰 Neden Kullanılır

* Tekrarlı işlemler için kullanılan yapıdır
* Kod tekrarlarından kurtarır

## 🏗️ For Yapısı

```python
sayilar = [6, 5, 3, 8, 4, 2, 5, 4, 11]
toplam = 0 # Toplam değeri tutacak değişken

for sayi in sayilar: # Liste üzerinde döngü ile ilerleme
  toplam = toplam + sayi

print("Toplam değer:", sum) # Toplam Değer: 48
```

### 🍢 Tek Satırlı For Döngüsü

```python
values = [item.value for item in Fruit]  # [4, 5, 6]
values = set(item.value for item in Fruit)  # {4, 5, 6}
```

### 🔀 İki Liste Üzerinde Paralel Kullanım

```python
for num, cheese, color in zip([1,2,3], ['manchego', 'stilton', 'brie'],
                              ['red', 'blue', 'green']):
    print('{} {} {}'.format(num, color, cheese))

# 1 red manchego
# 2 blue stilton
# 3 green brie
```

## 👁‍🗨 Range Fonksiyonu

* Python 2'deki `xrange` metoduna eş değerdir.
* `generator` tipinde veri döndürür
* Sadece döngüler ile verilerine erişilebilir

```python
# for i in <range>:
for i in range(0,3):
    print(i)
```

| Kullanım | Çıktı |
| :--- | :--- |
| `range(10)` | `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]` |
| `range(2, 8)` | `[2, 3, 4, 5, 6, 7]` |
| `range(2, 20, 3)` | `[2, 5, 8, 11, 14, 17]` |
| `reversed(range(3))` | `2 1 0` |

## 🚧 While Döngüsü

```python
sayac = 0

while sayac < 3:
    print("Döngü içinde")
    sayac = sayac + 1
else:
    print("Döngü dışında")

# Döngü içinde
# Döngü içinde
# Döngü içinde
# Döngü dışında
```

## 🛑 Break / Continue

```python
for deger in "string":
    if deger == "i":
        break # Döngüyü sonlandırır
    if deger == "t"
        continue # Döngüdeki adımı sonlandırır
    print(deger)

print("Son")
```

```text
s
r
Son
```

