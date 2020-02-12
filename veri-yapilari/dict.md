---
description: 'Python obje, json veya anahtar-değer (key-value) çifti yapısı (dict)'
---

# 📙 Dict

## 👀 Hızlıca Göz Atalım

Verilerin anahtarlara \(_key_\) göre saklandığı `list` yapısıdır.

* Her _key_ değeri eşsiz \(_unique_\) olmalıdır
* _Key_ değerleri **ana değişkenleri** olabilir, `list`, `tuple` gibi listeler olamaz

> Alttaki işlemlerin her biri `dict` objesinin alt işlemidir.

## 💠 Dict İşlemleri

| İşlem | Açıklama |
| :--- | :--- |
| `dict[<key>]` & `get(<key>)` | Anahtar ile veri alma, veri yoksa hata fırlatır |
| `dict[<key>] = <değer>` | Belirli anahtara değer atama |
| `<key> in dict` | Anahtar `dict`'e var mı kontrolü |
| `json.dumps(dict)` | `dict`'i `str`'a çevirme |
| `json.loads(re.sub("//.*","",str,flags=re.MULTILINE))` | JSON'u yorum satırlarını atarak okuma |
| `dict( (a,1) for a in <list>)` | `<liste>`'nin her elamanı ile 1'i eşleyen dict |
| `copy_dict ? {**dict}` | `dict` kopyalama |

## 🏗 Obje Tanımlama

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

## 📜 JSON İşlemleri

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

## 🐣 Verilere Erişim

```python
my_dict = {'name':'Jack', 'age': 26}

# Output: Jack
print(my_dict['name'])

# Output: 26
print(my_dict.get('age'))

search_age = 26

for name in my_dict.keys():
    print(name) # Jack
    
for age in my_dict.values():
    print(age) # 26

# Anahtar ve değerlere erişme
for name, age in my_dict .items():
    if age == search_age:
        print(name) # Jack
        
```

## 🔗 Dict için Faydalı Bağlantılar

* [`Dict`'i `str`'a çevirme](https://stackoverflow.com/a/4547331/9770490)
* [`Dict`'ten hızlı bir yöntem var mı](https://stackoverflow.com/a/40694623/9770490)
* [`Dict` kopyalama](https://stackoverflow.com/a/53413487/9770490)

