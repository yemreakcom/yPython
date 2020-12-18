---
description: Python üzerinde veri yapıları işlemleri
---

# 🚧 Veri Yapılarında İşlemler

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

## 👬 Kopyalama İşlemleri

Kopyalama işlemleri için **shallow copy** ya da **deep copy** seçenekleri mevcuttur.

> 💁‍♂️ Özetle objelerin birbirinden bağımsız olmasını istiyorsanız, deep copy kullanın

| 🌫️ Shallow Copy | 🕳 Deep Copy |
| :--- | :--- |
| Referans kopyalar | Değer kopyalar |
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

bağlantılarına bakabilirsin.
{% endhint %}

