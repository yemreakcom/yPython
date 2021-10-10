---
description: Python ile veri veya objeleri sıralama yani sorting işlemi
---
# 🚄 Sıralama

## 💠 Sıralama Metotları

| Sort                      | Sorted                                 |
| ------------------------- | -------------------------------------- |
| Objenin kendisini sıralar | Objenin sıralanmış kopyasını oluşturur |
| Obje içeriği güncellenir  | Obje içeriği değişmez                  |

```python
mylist = [1, 5, 4]
sorted(mylist) # [1, 4, 5]  mylist = [1, 5, 4]
mylist.sort()  # [1, 4, 5]  mylist = [1, 4, 5]
```

## 📙 `dict` Objesi Sıralama

* 🔑 `dict` objeleri sıralanırken varsayılan olarak `key` değerlerine göre sıralanırlar

```python
mydict = {"a": 1, "e": 0, "b": 2}

sorted(mydict)           # ['a', 'b', 'e']
sorted(mydict.keys())    # ['a', 'b', 'e']
sorted(mydict.values())  # [0, 1, 2]
sorted(mydict.items())   # [('a', 1), ('b', 2), ('e', 0)]

sorted(mydict, key=lambda x: x.key)   #  'str' object has no attribute 'key'
sorted(mydict, key=lambda x: x.value) #  'str' object has no attribute 'value'
```

## 🍎 Çok Değişkenli Obje Sıralama

* 🏗️ Eğer sıralanacak objede birden fazla değişken varsa, `sorted(<obje>, key=<func>)` yapısı ile istenen objeyi referans eden fonksiyon ile sıralama işlemi yapılır
  * ⭐ Örnek fonksiyon: `lambda x: x.value` ile `x` objesinin `value` elemanına göre sırala demiş oluyoruz
* 💁‍♂️ Sıralama işleminde obje içerisindeki belirli elemanların sıralı halini almak isterseniz, `sorted(map(<func>, <param1>, <param2>)) `yapısını kullanın
  * ⭐ Örnek olarak: `sorted(map(lambda p: p.x, points))` ile point elemanlarının x değerlerinin sıralı halini alırsınız

```python
class Temp():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"Temp({self.x}, {self.y})"
    def __repr__(self):
        return f"Temp({self.x}, {self.y})"

temp = [Temp(1, 2), Temp(2, 3), Temp(3, 4)]  

sorted(temp, key=lambda x: x.y)   # [Temp(4,1), Temp(5,2), Temp(3,8)]
sorted(temp, key=lambda x: x.x)   # [Temp(3,8), Temp(4,1), Temp(5,2)]

sorted(map(lambda x: x.y, temp))  # [1, 2, 8]
sorted(map(lambda x: x.y, temp))  # [3, 4, 5]
```
