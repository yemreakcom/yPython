---
description: Python'da koşul yapılarının kullanımı
---

# ⚖️ Koşullar

## 🎌 Koşul Yapıları

If içerisine yazılan koşul otomatik olarak `bool` değişkenine dönüştürülür, değer `True` ise içindeki kodlar çalıştırılır.

* `None`, `""`, `0` gibi değerler `False` değerine denktir
* `:` ile if / else satırı sonlandırılır
* Tab ⭾ kadar boşluk atılırsa if scope\*'u içerisinde olur

## 👮‍♂️ If / Elif / Else Yapısı

```python
num = float(input("Sayı giriniz: "))
if num >= 0:
    if num == 0:
        print("Sıfır")
    elif num == 1:
        print("Bir")
    else:
        print("Pozitif sayı")
else:
    print("Negatif sayı")
```

## 🍢 Tek Satır If Yapısı \(Ternary If\)

```python
fruit = 'Apple'
isApple = True if fruit == 'Apple' else False
```

## 📋 Çoklu If Koşulları

```python
if any(s in line for s in ('string1', 'string2', ...)):
```

