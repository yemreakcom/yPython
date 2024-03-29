---
description: Struct benzeri özelleştirilmiş veri sınıfları
---

# 🍎 Data Classes

## 🔰 Nedir?

* 🗃️ Değişkenleri olan ve diğer dillerdeki struct yapısına benzeyen sınıflardır
* 🌟 `__init__`, `__repr__` gibi metotları otomatik olarak tanımlanır
* 💁‍♂️ `namedTuple` gibidir ama değişkenlere sahip olup, varsayılan değer atamalarını destekler

```python
from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0  # Varsayılan değer atama


p = Point(1.5, 2.5)  # z değeri verilmediği için varsayılan değer atanır

print(p)  # Point(x=1.5, y=2.5, z=0.0)


class C:
    x: int
    y: int = field(repr=False)
    z: int = field(repr=False, default=10)
    t: int = 20
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi [YEmoji](https://emoji.yemreak.com/kullanim/baglantilar) yapısına uygun oluşturulmuş:

* [👪 C-like structures in Python](https://stackoverflow.com/a/45426493/9770490)
* [📖 dataclasses - DataClasses](https://docs.python.org/3/library/dataclasses.html)

bağlantılara bakabilirsin.
{% endhint %}

## 🕖 Post-init Yapısı

* ⏳Değişken tanımlamalarından sonra `field(init=false)` olarak tanımlanan değişkenler için tekrardan bir `init` işlemi yapılır&#x20;
* 👷‍♂️ `__post__init__` metodu ile `init` işlemi tamamlandıktan sonra, değişkenleri kullanarak yeni değerler üretebilir ve değişkenlere atayabiliriz

```python
@dataclass
class C:
    a: float
    b: float
    c: float = field(init=False)  # __post_init__ içerisinde tanımlanacak

    def __post_init__(self):
        self.c = self.a + self.b
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi [YEmoji](https://emoji.yemreak.com/kullanim/baglantilar) yapısına uygun oluşturulmuş:

* [📖 dataclasses - DataClasses](https://docs.python.org/3/library/dataclasses.html)

bağlantılara bakabilirsin.
{% endhint %}

## 🍎 Key - value çifti içeren `dict` üretme

* `dataclass` verilerini `dict` yapısında oluşturmayı sağlar
* `yaml`, `json` gibi alanlarda çalışırken faydalıdır

```python
from dataclasses import dataclass, asdict

@dataclass
class Point:
     x: int
     y: int

@dataclass
class C:
     mylist: list[Point]

p = Point(10, 20)
assert asdict(p) == {'x': 10, 'y': 20}

c = C([Point(0, 0), Point(10, 4)])
assert asdict(c) == {'mylist': [{'x': 0, 'y': 0}, {'x': 10, 'y': 4}]}

```
