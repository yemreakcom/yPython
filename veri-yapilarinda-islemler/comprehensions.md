---
description: Python ile compréhensions (tek satırlı yapı) işlemleri
---
# 🤸‍ Comprehensions

## 👀 Hızlı Bakış

* 🦄 Tek satır ile yapı oluşturmadır.
* 🤯 Daha anlaşılır
* 💨 Daha hızlı

```python
# Verimli Yapı
squares = [x**2 for x in range(10)] # Liste tanımlama
square_lut = {x: x**2 for x in range(10)} # Dict tanımlama

# Verimsiz (eski) yapı
squares = []
square_lut = {}
for x in range(10):
    squares.append(x**2)
    square_lut[x] = x**2
```

## **💫 Çok Anahtarlı Veriler**

```python
me_dict_dtypes = {k: type(v) for k, v in me_dict.items()}
print(me_dict_dtypes)

# {'name': <class 'str'>, 'age': <class 'int'>, 'height': <class 'float'>, 'weight': <class 'float'>, 'hair': <class 'str'>, 'eyes': <class 'str'>, 'has dog': <class 'bool'>, 'favorite color': <class 'str'>, 'nieces/nephews': <class 'int'>}
```
