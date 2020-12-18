---
description: 'Python ile kopyalama, copy, deep copy ve shallow copy işlemleri'
---

# 👯‍♀️ Kopyalama

## 👀 Hızlı Bakış

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

## 🆚 Shallow ve Deep Copy

| 🌫️ Shallow Copy | 🕳 Deep Copy |
| :--- | :--- |
| Referans kopyalar | Değer kopyalar |
| Obje yeniden oluşturulur | Obje yeniden oluşturulur |
| Objenin her bir **referansı kopyalanır** ve yeniye aktarılır | Objenin her bir **değeri tek tek kopyalanır** ve yeniye aktarılır |
| Kopyalanan objenin referansı alındığından orijinal ile **bağlantılıdır** | Her bilgi tek tek kopyalandığından orijinal ile **bağlantısı yoktur** |
| Herhangi bir değişiklik diğerini de **etkiler** | Herhangi bir değişiklik diğerini **etkilemez** |

## 📜 DeepCopy Hakkında

* Deepcopy işlemi `cls` ile yeniden sınıf objesi oluşturmak ile benzerdir
* Alttaki örnekteki `class2` ile `class3` benzer işlevi görmektedir

```python
from copy import deepcopy

class AnyClass:
    x: int
    y: int
    
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y
        

class1 = AnyClass(1, 2)
class2 = deepcopy(aclass)
class3 = AnyClass(class1.x, class2.y)
# class2 ile class3 benzer işlevi görmektedir
        
```

## 🔗 Faydalı Bağlantılar

* 📃 [Python Shallow Copy and Deep Copy](https://www.programiz.com/python-programming/shallow-deep-copy)
* 👪 [deepcopy override clarification](https://stackoverflow.com/questions/57181829/deepcopy-override-clarification)
* 📃  [copy in Python \(Deep Copy and Shallow Copy\)](https://www.geeksforgeeks.org/copy-python-deep-copy-shallow-copy/) 
* 📃 [How do I copy an object in Python?](http://effbot.org/pyfaq/how-do-i-copy-an-object-in-python.htm)
* 👪 [Emulating pass-by-value behavior in python](https://stackoverflow.com/a/9762918/9770490)
* 📖 [copy  — Shallow and deep copy operations](https://docs.python.org/3/library/copy.html)

