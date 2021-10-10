---
description: Python ile birleştirme, zip işlemleri
---
# 📚 Birleştirme

## 🗃 Zip

```python
key = ['name', 'age', 'height', 'weight', 'hair', 'eyes', 'has dog']
value = ['Dylan', 28, 167.5, 56.5, 'brown', 'brown', True]

zipped = zip(key_list, value_list) # <zip object at 0x7f2ae4e91508>
list(zipped) # [('name', 'Dylan'), ('age', 28), ('height', 167.5), ('weight', 56.5), ('hair', 'brown'), ('eyes', 'brown'), ('has dog', True)]
dict(zipped) # {'name': 'Dylan', 'age': 28, 'height': 167.5, 'weight': 56.5, 'hair': 'brown', 'eyes': 'brown', 'has dog': True}

# Zip işlemini geri alma
key_list, value_list = zip(*zipped)
```

## 🌟 Pointer

```python
# Dict objelerini tanımlama
pycon = {2016: "Portland", 2018: "Cleveland"}
europython = {2017: "Rimini", 2018: "Edinburgh", 2019: "Basel"}

# 2 Dict objesini pointer ile birleştirme
{**pycon, **europython}  # {2016: 'Portland', 2018: 'Edinburgh', 2017: 'Rimini', 2019: 'Basel'}

```

## 🎡 For Döngüsü

```python
# Dict objelerini tanımlama
pycon = {2016: "Portland", 2018: "Cleveland"}
europython = {2017: "Rimini", 2018: "Edinburgh", 2019: "Basel"}

merged = pycon.copy()
for key, value in europython.items():
    merged[key] = value
merged  # {2016: 'Portland', 2018: 'Edinburgh', 2017: 'Rimini', 2019: 'Basel'}
```

## ♊️ Walrus Operatörü

```python
# Dict objelerini tanımlama
pycon = {2016: "Portland", 2018: "Cleveland"}
europython = {2017: "Rimini", 2018: "Edinburgh", 2019: "Basel"}

(merged := pycon.copy()).update(europython)
# {2016: 'Portland', 2018: 'Edinburgh', 2017: 'Rimini', 2019: 'Basel'}
```

## 🥣 Union Operatörü

```python
# Dict objelerini tanımlama
pycon = {2016: "Portland", 2018: "Cleveland"}
europython = {2017: "Rimini", 2018: "Edinburgh", 2019: "Basel"}

# Güncel dict yapısı en sağdaki dict değerlerini referans alır
# 2018 değerleri farklıdır

pycon | europython
# {2016: 'Portland', 2018: 'Edinburgh', 2017: 'Rimini', 2019: 'Basel'}

europython | pycon
# {2016: 'Portland', 2018: 'Cleveland', 2017: 'Rimini', 2019: 'Basel'}

pycon |= europython
pycon  # {2016: 'Portland', 2018: 'Edinburgh', 2017: 'Rimini', 2019: 'Basel'}

# Union operatörü ile farklı veri tipini ekleme
# Tuple listesi olsa bile dict yapısına uygun hale alınıp eklenir
pycon |= [(2020: "USA")]  

pycon
# {2016: 'Portland', 2018: 'Edinburgh', 2017: 'Rimini', 2019: 'Basel', 2020: 'USA'}
```

## 🔗 Faydalı Bağlantılar

* [Simpler Updating of Dictionaries](https://realpython.com/python39-new-features/#simpler-updating-of-dictionaries)
