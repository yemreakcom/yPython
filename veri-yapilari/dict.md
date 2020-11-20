---
description: 'Python obje, json veya anahtar-değer (key-value) çifti yapısı (dict)'
---

# 📙 Dict

## 🔰 Ne Amaçla Kullanılır

* Verilerin anahtar - değer yapısına göre saklandığı `list` yapısıdır
* Her anahtar değeri eşsiz olmak zorundadır
* Aynı anahtar değerine sahip yeni bir anahtar oluşturulamayacağından veriler, anahtarın üzerine yazılır
* Anahtar değerleri primitive değişkenler dışında seçilemez \(`list`, `tuple` olamaz\)

{% hint style="warning" %}
📢 Dict içerisinde yer almayan anahtarlar kullanıldığında hata oluşur, bu sebeple `defaultdict` yapısını kullanmanız önerilir
{% endhint %}

> ## ⭐ Basit Örnekler

```python
# empty dictionary
my_dict = {}
# dictionary with integer keys
my_dict = {1: 'apple', 2: 'ball'}
# dictionary with mixed keys
my_dict = {'name': 'John', 1: [2, 4, 3]}
# using dict()
my_dict = dict({1:'apple', 2:'ball'})
# from sequence having each item as a pair
my_dict = dict([(1,'apple'), (2,'ball')])
```

## 📜 Json Kullanımı

```python
import json

my_dict = {}

# JSON'ı okuma
with open("some.json", "r", encoding="utf-8") as file:
    my_dict = json.load(file)

# JSON'ı dosyaya yazdırma
with ("new.json", "w", encoding="utf-8") as file:
    file.write(json.dumb(my_dict, indent=4))
```

## ✨ Verileri Güncelleme

```python
# Dict objelerini tanımlama
pycon = {2016: "Portland", 2018: "Cleveland"}
europython = {2017: "Rimini", 2018: "Edinburgh", 2019: "Basel"}

# 2 Dict objesini pointer ile birleştirme
{**pycon, **europython}  # {2016: 'Portland', 2018: 'Edinburgh', 2017: 'Rimini', 2019: 'Basel'}

# 2 Dict objesini döngü yapısı ile birleştirme
merged = pycon.copy()
for key, value in europython.items():
    merged[key] = value
merged  # {2016: 'Portland', 2018: 'Edinburgh', 2017: 'Rimini', 2019: 'Basel'}

# Update metodu ile birleştirme
pycon.update(europython)  # None
pycon  # {2016: 'Portland', 2018: 'Edinburgh', 2017: 'Rimini', 2019: 'Basel'}

# Walrus operatörü ile güncelleme
(merged := pycon.copy()).update(europython)  # {2016: 'Portland', 2018: 'Edinburgh', 2017: 'Rimini', 2019: 'Basel'}

# Union operatörü ile

# Güncel dict yapısı en sağdaki dict değerlerini referans alır, 2018 değerleri farklıdır
pycon | europython  # {2016: 'Portland', 2018: 'Edinburgh', 2017: 'Rimini', 2019: 'Basel'}
europython | pycon  # {2016: 'Portland', 2018: 'Cleveland', 2017: 'Rimini', 2019: 'Basel'}

pycon |= europython
pycon  # {2016: 'Portland', 2018: 'Edinburgh', 2017: 'Rimini', 2019: 'Basel'}

# Union operatörü ile farklı veri tipini ekleme
pycon |= [(2020: "USA")]  # Tuple listesi olsa bile dict yapısına uygun hale alınıp eklenir
pycon  # {2016: 'Portland', 2018: 'Edinburgh', 2017: 'Rimini', 2019: 'Basel', 2020: 'USA'}
```

{% hint style="warning" %}
📢 Detaylı bilgi için [Simpler Updating of Dictionaries](https://realpython.com/python39-new-features/#simpler-updating-of-dictionaries) alanına bakabilirsin
{% endhint %}

## 🌟 `DefaultDict` ile Varsayılan Değer

* Dict içerisinde olmayan bir anahtar kullanılması durumunda `KeyError` verilir, `defaultdict` yapısında önceden tanımlanan fonksiyon çalıştırılır
* Basit bir olaymış gibi gözükse de, `dict` yapısı büyük projelerde çok fazla hatalara sebep olmaktadır

```python
from collections import defaultdict
europe = defaultdict(lambda: "", {"Norway": "Oslo", "Spain": "Madrid"})
africa = defaultdict(lambda: "", {"Egypt": "Cairo", "Zimbabwe": "Harare"})

# Union ile defaultdict birleştirme
europe | africa
# defaultdict(<function <lambda> at 0x7f0cb42a6700>,
#   {'Norway': 'Oslo', 'Spain': 'Madrid', 'Egypt': 'Cairo', 'Zimbabwe': 'Harare'})

# Pointer ile defaultdict'ten dict oluşturma
{**europe, **africa}  # {'Norway': 'Oslo', 'Spain': 'Madrid', 'Egypt': 'Cairo', 'Zimbabwe': 'Harare'}

libraries = { "collections": "Container datatypes", "math": "Mathematical functions" }
libraries |= {"zoneinfo": "IANA time zone support"}
libraries  # {'collections': 'Container datatypes', 'math': 'Mathematical functions', ': 'IANA time zone support'}

# Defaultdict'e tuple objesini ekleme
libraries |= [("graphlib", "Functionality for graph-like structures")]
libraries
{'collections': 'Container datatypes', 'math': 'Mathematical functions',
 'zoneinfo': 'IANA time zone support',
 'graphlib': 'Functionality for graph-like structures'}
```

