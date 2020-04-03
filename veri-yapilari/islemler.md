---
description: Python üzerinde veri yapıları işlemleri
---

# 🚧 Veri Yapılarında İşlemler

## 👀  Veri Yapılarına Hızlı Bakış

| Tip | Açıklama | Örnek |
| :--- | :--- | :--- |
| ​[List](https://www.programiz.com/python-programming/list)​ | `liste = [1, 2]` | `liste[index]` |
| ​[Set](https://www.programiz.com/python-programming/set)​ | `kume = {1.0, "Hello", (1, 2, 3)}` | `kume.add(1)` |
| ​[Dictionary](https://www.programiz.com/python-programming/dictionary)​ | `site = {"adi":"yemreak"}` | `site['adi']` |
| ​[Tuple](https://www.programiz.com/python-programming/tuple)​ | `konum = (1, 2)` | `x, y = konum` |

## 📚 Birleştirme İşlemi \(Zip\)

* Birden fazla list yada benzeri yapıları birleştirmek için kullanılır.

```python
key = ['name', 'age', 'height', 'weight', 'hair', 'eyes', 'has dog']
value = ['Dylan', 28, 167.5, 56.5, 'brown', 'brown', True]

zipped = zip(key_list, value_list) # <zip object at 0x7f2ae4e91508>
list(zipped) # [('name', 'Dylan'), ('age', 28), ('height', 167.5), ('weight', 56.5), ('hair', 'brown'), ('eyes', 'brown'), ('has dog', True)]
dict(zipped) # {'name': 'Dylan', 'age': 28, 'height': 167.5, 'weight': 56.5, 'hair': 'brown', 'eyes': 'brown', 'has dog': True}

# Zip işlemini geri alma
key_list, value_list = zip(*zipped)
```

## 💱 Dönüşüm İşlemleri

```python
example_list = ['a', 'b', 23, 10, True, 'a', 10]
example_tuple = tuple(example_list)
example_set = set(example_tuple)
example_list = list(example_set)

print(example_tuple)
print(example_set)
print(example_list) # Set yapısından dolay tekrarlı verileri kaybederiz

# ('a', 'b', 23, 10, True, 'a', 10)
# {True, 10, 'a', 23, 'b'}
# [True, 10, 'a', 23, 'b']
```

## 🔍 Arama İşlemleri \(Searching\)

* Arama işlemlerinin temeli `in` ile yapılmaktadır.
* Tekrarlama işlemleri `for <key> in <yapı>:` ile yapılmaktadır

```python
if 'has dog' in me_dict:
    pass
```

{% hint style="success" %}
Arama işlemi `KeyError` \(_tanımsız değişkenler ile işlem yapma_\) sorunu ortadan kaldırır.
{% endhint %}

## 🥾 Sıralama İşlemleri \(Sorting\)

Sırala işlemleri `sorted` metodu ile yapılmaktadır.

* Eğer yapıda farklı elemanlar var ise `map(<type>, <yapı>)` ile `sorted` fonksiyonu kullanılır
* Eğer `dict` verilerinde anahtar-veri \(_key-value_\) olarak sıralamak istersek `dict.items()` yapısı kullanılır

```python
print(sorted(map(str, example_tuple)))
print(sorted(map(str, example_set)))
print(sorted(me_dict.items())) # Key-Value değerlerini
print(sorted(me_dict)) # Sadece değerleri sıralar

sort(list) # sadece sıralar veri döndürmez
```

## 👬 Kopyalama İşlemleri

Kopyalama işlemleri için **shallow copy** ya da **deep copy** seçenekleri mevcuttur.

> 💁‍♂️ Özetle objelerin birbirinden bağımsız olmasını istiyorsanız, deep copy kullanın

| 🌫️ Shallow Copy | 🕳 Deep Copy |
| :--- | :--- |
| Obje yeniden oluşturulur | Obje yeniden oluşturulur |
| Objenin her bir **referansı kopyalanır** ve yeniye aktarılır | Objenin her bir **değeri tek tek kopyalanır** ve yeniye aktarılır |
| Kopyalanan objenin referansı alındığından orijinal ile **bağlantılıdır** | Her bilgi tek tek kopyalandığından orijinal ile **bağlantısı yoktur** |
| Herhangi bir değişiklik diğerini de **etkiler** | Herhangi bir değişiklik diğerini **etkilemez** |

```python
import copy
li1 = [1, 2, [3,5], 4]

# Shallow copy
li2 = copy.copy(li1)

# Deep copy
li3 = copy.deepcopy(li1)

# Slice ile deep copy
li4 = li1[:]
```

{% hint style="warning" %}
📢 Objenin kopyalama davranışlarını değiştirmek için `__copy__`, `__deepcopy__` metotları override edilir
{% endhint %}

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [YEmoji](https://emoji.yemreak.com/kullanim/baglantilar) yapısına uygun oluşturulmuş:

* 📃  [copy in Python \(Deep Copy and Shallow Copy\)](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/) 
* 📃 [How do I copy an object in Python?](http://effbot.org/pyfaq/how-do-i-copy-an-object-in-python.htm)
* 👪 [Emulating pass-by-value behavior in python](https://stackoverflow.com/a/9762918/9770490)
* 📖 [copy  — Shallow and deep copy operations](https://docs.python.org/3/library/copy.html)

alanlarına bakabilirsin.
{% endhint %}

## 🤸‍ Comprehensions

Tek satır ile yapı oluşturmadır.

* 🤯 Daha anlaşılır
* 💨 Daha hızlı

### **🏗️ Verimli Yapı:**

```python
squares = [x**2 for x in range(10)] # Liste tanımlama
square_lut = {x: x**2 for x in range(10)} # Dict tanımlama
```

### **🗑️ Eski yapı:**

```python
squares = []
square_lut = {}
for x in range(10):
    squares.append(x**2)
    square_lut[x] = x**2
```

### **💫 Çoklu anahtar ile tekrarlama**

```python
me_dict_dtypes = {k: type(v) for k, v in me_dict.items()}
print(me_dict_dtypes)

# {'name': <class 'str'>, 'age': <class 'int'>, 'height': <class 'float'>, 'weight': <class 'float'>, 'hair': <class 'str'>, 'eyes': <class 'str'>, 'has dog': <class 'bool'>, 'favorite color': <class 'str'>, 'nieces/nephews': <class 'int'>}
```

