---
description: Python üzerinde rastgelelik işlemleri ve random paketi
---
# 🎲 Rastgelelik

## 👀 Hızlı Bakış

* Python üzerindeki rastgelelik `random` paketi ile yönetilir

## 🔢 Rastgele Sayı Üretme

```python
import randoom

# 0 ile 1 arasındaki rastgele sayı döndürür (0 <= x < 1.0)
random.random()  # 0.38872204424977774

# Verilen aralıkta herhangi bir ondalık sayı döndürür (a <= x < b)
random.uniform(1,100)  # 52.19820527331601

# Verilen tam sayı aralağında herhangi bir tamsayı değeri döndürür (a <= x < b)
random.randint(1,100)  # 86

# a, b, c için 
random.randrange(1,11,3). # 1
```

## 🗳 Rastgele Sayı Seçimi

```python
import random

numbers = range(10)

# 50 sayı arasında rastegele 3 sayı seçme ve liste olarak döndürme
random.sample(numbers, 3)  # [1, 19, 16]

# Verilen listeyi karıştırma
random.shuffle(numbers)
numbers  # [4, 8, 7, 3, 2, 1, 6, 5, 9, 0]

# Liste içerisinden rastgele bir sayı seçme
random.choice(numbers)  # 4
```

## 🔗 Faydalı Bağlantılar

* [Python Random Modülü](https://medium.com/python/python-random-mod%C3%BCl%C3%BC-a0de3ec02ff)
