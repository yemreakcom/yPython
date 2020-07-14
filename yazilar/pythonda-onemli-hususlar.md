---
description: >-
  Python için bilmeniz, öğrenmeniz, faydalı olacak konular ve derlediğim
  bilgiler
---

# 🌟 Python'da Önemli Hususlar

## 📂 Proje Yapını ve Ortamını Belirle

* 🏗️ Alttaki tüm dosya & dizinler `root` yani proje dizininde olmalıdır
* 📈 Projende verimlilik için`venv` komutu ile sanal bir python ortamı oluşturman tavsiye edilir
  * 👷‍♂️`python3 -m venv venv` komutu ile `venv` isimli sanal ortamı oluşturursun
  * 🌃 Oluşturulan sanal ortam, bilgisayarındaki python paketlerinden etkilenmez ve onları etkilemez
  * 💁‍♂️ Sanallaştırma ile paket sürümlerindeki çakışmalardan kurtulmuş olursun

| 📃 Dosya İsmi | 💎 Açıklama |
| :--- | :--- |
| `LICENSE` | Projenin lisans bilgilerini taşır \(Apache, MIT vs\) |
| `README` | Projen hakkında açıklamalar ve dokümanlarına bağlantılara burada yer verirsin |
| `requirements.txt` | Projenin bağımlılıklarını tutar, `pip freeze > requirements.txt` komutu ile oluşturulur ve `pip install -r requirements.txt` komutu ile indirilir |
| `tests` | Projenin test metotlarının hepsi, `tests` dizininde saklanmalıdır |

## 🤷‍♂️ Boşluk veya Tab Herhangi Birini Seç

* 🤯  Her ikisini birden kullanmaya çalışma, python bunu idare edemeyebilir
* 💫 Her proje için kendi tarzına göre boşluk ve tab verilerini birbirileri arasında dönüştür
* 🎯 Sadece tek bir yapıyı kullan, çok sık değiştirme

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Python Pro Tips](https://dev.to/jmau111/python-pro-tips-27cb) alanına bakabilirsin.
{% endhint %}

## 📝 Değişken Tiplerini de Belirt

* 🙄 Değişken tipleri ile de mi uğraşacağım demeyin, tipler gereksiz uğraş değil avantajdır
* 🤯 Objenin tipini bilmemek, kodda karmaşıklığa sebep olacaktır
* 🧐 `typing` modülü içerisinden `Dict`, `List` gibi sınıflar ile değişkenlerin tipini linter için belirle
* 💁‍♂️ Tipleri bilen linter size doğru ve uygun kod önerileri de sunacaktır
* 👷‍♂️ Değişken tiplerini de kontrol ettirmek istersen `mypy` modülüne bakabilirsin

> 👨‍💻 Alttaki kod parçasında yazım sırasında önerilerin düzgün olduğunu fark edeceksiniz

```python
from typing import Dict

class YEmreAk:

    def __init__(self):
        self.job = "Analyzing"
    
people: Dict[str, YEmreAK] = {}
people["Ben"] = YEmreAk()
people["Ben"].job = "🦅"
```

## 💎 Değişkenlere Farklı Tipler Atama

* 👮‍♂️ Her farklı obje için farklı isimlendirme yapılmalı
* 🙄 Aynı değişkene birden farklı obje atılması verimliliği artırmıyor

```python
# Hatalı kullanım
items = 'a b c d'  # This is a string...
items = items.split(' ')  # ...becoming a list
items = set(items)  # ...and then a set

# Doğru kullanım
item_str = "a b c d"
item_list = item_str.split(" ")
item_set = set(item_list)
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Dynamic Typing](https://docs.python-guide.org/writing/structure/#dynamic-typing) alanına bakabilirsin.
{% endhint %}

## 📦 Kütüphanelerden İşine Yarayanları Dahil Et

* 🤯 Paketin veya modülün tüm metotlarını `from ypackage import *` şeklinde dahil etme kodunu karmaşıklaştırır
* 👨‍💼 Sadece ihtiyacın olan metotları dahil et `from ypackage import write_file` ve kodunda kullan
* 💁‍♂️ Çok fazla metoduna ihtiyacın varsa ve kategorize etmek istersen `import cache` şeklinde dahil et `cache.counter = 5` olarak kullan

## 📖 Dictionary için `get` Kullan 

* 📈 Sözlükte olmazsa hata vermez, varsayılanı alırsın
* 💠 Switch-case yapıları için de kullanabilirsin

```python
team = {
   "productor": "Lionsgate",
   "actor": "Keanu Reeves",
   "director": "Chad Stahelski" 
}

actress = team["bullet"] # KeyError: 'bullet'
actress = team.get("bullets", 2000000)

# Switch - Case kullanımı
handlers = {
   "hello": greeting,
   "exit": good_bye,
}
handlers.get(response, smile)()
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Python Pro Tips](https://dev.to/jmau111/python-pro-tips-27cb) alanına bakabilirsin.
{% endhint %}

## 🆔 `==` ile `is` aynı değildir

* 💡 Öncelikle `==` eşitlik sorgularken, `is` adres bilgisi \(veya id\) sorgular
* 💁‍♂️ Primitif değişkenlerde \(`int`, `bool` … \) adresler değil değerler tutulur,`is` ile `==` eş değerdir
* 👮‍♂️ Objeler ve `list`, `dict` gibi tipler için eş değer değildir

```python
x = 111
y = 111
id(x) # 4457849408
id(x) # 4457849408
x is y # True
x == y # True

a = [1, 2, 3]
b = [1, 2, 3]
a is b # False
a == b # True
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Python Pro Tips](https://dev.to/jmau111/python-pro-tips-27cb) alanına bakabilirsin.
{% endhint %}

##  👮‍♂️ If - Else Yapılarını Kısaltın

* 🚄 _Uzun yapı 1_ gibi tekrarlı kontrolleri liste içerisine alın 
* 🧐 Oluşturduğunuz liste için `and` için `all` veya `or` için `any` metotlarını da kullanabilirsiniz
* 👮‍♂️ Switch - Case yapıları için, `dict` objesi tanımlayın
  * 💾  Yapılacak fonksiyonları `dict` içerisine kaydedin
  * 🐣 `dict` üzerinden `get` metodu ile fonksiyonları çağırın
  * 🤯 Kod karmaşıklığını azaltacaktır
  * 📈 CPU kullanımını azaltıp, RAM kullanımı artıracaktır

```python
# Uzun yapı 1
if myvar == 1 or myvar == 7 or myvar == 9:
    pass
    
# Kısa yapı 1
if myvar in [1,7,9]:
    pass

# Uzun yapı 2
if iwant:
    var = 1
else:
    var = 2

# Kısa yapı 2 (ternary)
var = 1 if iwant else 2

# Uzun yapı 3
if response == "hello":
    greeting()
elif response == "exit":
    good_bye()
else:
    smile()

# Kısa yapı 3
handlers = {
   "hello": greeting,
   "exit": good_bye,
}
handlers.get(response, smile)()
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Switch Case Kullanmadan Kod Yazabilmek](https://www.buraksenyurt.com/post/switch-case-kullanmadan-kod-yazabilmek) alanına bakabilirsin.
{% endhint %}

## 🍢 Tek Satır Yapılarını Kullan

* `list` ve `dict` gibi yapılar için tek satırlık yapılar ile işini hızlıca halledebilirsin
* `[ expression for item in list if conditional ]` yapısı ile `list`oluşturabilirsin
* `{ expression for item in dict if conditional }` yapısı ile `dict`oluşturabilirsin
* `[on_true] if [expression] else [on_false]` yapısı ile koşullu atama yapabilirsin
* `a < b < c` gibi zincirleme yapıları python destekler

```python
from typing import Dict, List

a = 1
b = 2
a, b = b, a 
a  # 2
b  # 1

c = 5
a < b < c == a < b and b < c  # True

y = 2
x = "Success!" if (y == 2) else "Failed!"  # 'Success!'

mylist: List[int] = [i for i in range(10)]     # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
squares: List[int] = [x**2 for x in range(7)]  # [0, 1, 4, 9, 16, 25, 36, 49]

[1, 2, 3, 4, 5][0:5:2]  # [1, 3, 5]

def some_function(a):
    return (a + 5) / 2
    
my_formula: List[float] = [some_function(i) for i in range(10)]
my_formula  # [2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0]

filtered: List[int] = [i for i in range(20) if i%2==0]
filtered  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]

MAIN_SYMBOLS: List[str] = ["Y", "E"]
values: Dict[str, int] = {MAIN_SYMBOL: 0 for MAIN_SYMBOL in MAIN_SYMBOLS}
values  # {'Y': 0, 'E': 0}

dict1 = { 'a': 1, 'b': 2 }
dict2 = { 'b': 3, 'c': 4 }
merged = { **dict1, **dict2 }
merged  # {'a': 1, 'b': 3, 'c': 4}
```

## 🤹‍♂️ Sık Kullanılabilecek İşlemleri Bil

* `set` küme yapısı ile sadece eşsiz verileri tutarsın
* `max` yapısı ile verilen `key`'e göre en yüksek değerleri bul
* `map` yapısı ile üzerinde gezinebilir \(ilst, set vs\) verilerde her veri için fonksiyon çalıştır
* `collections.Counter` yapısı ile veri listesi içerisindeki elemanları say
* `dateutil.parser.parse` ile loglardan zaman bilgilerini rastgele konumlarda da olsa çek
* `chardet` ile dosya içerisindeki metinleri inceleyebilirsin

```python
# Eşsiz verileri bulma
mylist = [1, 1, 2, 3, 4, 5, 5, 5, 6, 6]
set(mylist)  # {1, 2, 3, 4, 5, 6}

# Sayıca en çok olan değeri bulma 
test = [1, 2, 3, 4, 2, 2, 3, 1, 4, 4, 4]
max(set(test), key = test.count)  # 4

# Map ile her eleman için işlem yapma
mywords = ['sentence', 'fragment']
list(map(lambda x: x.upper(), mywords))  # ['SENTENCE', 'FRAGMENT']

mylist = [1, 1, 2, 3, 4, 5, 5, 5, 6, 6]
c = Counter(mylist)         # Counter({1: 2, 2: 1, 3: 1, 4: 1, 5: 3, 6: 2})
Counter("aaaaabbbbbccccc")  # Counter({'a': 5, 'b': 5, 'c': 5})

# pip3 install python-dateutil 
logline = 'INFO 2020-01-01T00:00:01 Happy new year, human.'
timestamp = parse(logline, fuzzy=True)  # 2020-01-01 00:00:01

# pip install chardet
chardetect somefile.txt
somefile.txt: ascii with confidence 1.0
```

## 🔤 String İşlemlerine Hakim Ol

* 🌟 En çok kullanılan değişken türlerindendir ve hayatında çoooook sık karşılaşacaksın
* 💁‍♂️ String bir `char` dizisi olduğundan `list` özelliklerini de taşır `string[başlangıç:son:adım]`

```python
mystring = "The quick brown fox"

mystring.title()             # 'The Quick Brown Fox'
mylist = mystring.split(' ') # ['The', 'quick', 'brown', 'fox']
mystring = " ".join(mylist)  # 'The quick brown fox'

"abcdefg"[::-1]        # 'gfedcba'
[1, 2, 3, 4, 5][::-1]  # [5, 4, 3, 2, 1]
"abcdefdn nimt"[::2]   # 'aced it'

import emoji
emoji.emojize('Python is :thumbs_up:') # 'Python is 👍'
emoji.demojize('Python is 👍')         # 'Python is :thumbs_up:'

mywords = ['sentence', 'fragment']
list(map(lambda x: x.upper(), mywords))  # ['SENTENCE', 'FRAGMENT']


s1 = """Multi line strings can be put
        between triple quotes. It's not ideal
        when formatting your code though"""

print (s1)
# Multi line strings can be put
#         between triple quotes. It's not ideal
#         when formatting your code though
        
s2 = ("You can also concatenate multiple\n" +
        "strings this way, but you'll have to\n"
        "explicitly put in the newlines")

print(s2)
# You can also concatenate multiple
# strings this way, but you'll have to
# explicitly put in the newlines
```

## 💠 Fonksiyonları Efektif Kullan

* 💁‍♂️ Fonksiyonlar birden fazla değişken döndürebilir \(`tuple`\) ve bunu efektif kullanmak yararınadır
* 🏷️ Parametre ve dönüş bilgilerini `typing` modülü ile belirt
* 🔚 Dönüş tipi `-> <tip>` şeklinde belirtilir

```python
from typing import Tuple

def get_user(id: int) -> Tuple[str, str]:
    # fetch user from database
    # ....
    name = "YEmreAk"
    symbol = "🦅"
    return name, symbol # Tuple[str, str]

name, birthdate = get_user(7)
```

## 🍎 Class Yapıları İle OOP Kodlama Yap

* 🤯 İç içe karmaşık fonksiyonlar yerine sınıf yapıları ile anlaşılabilir bir düzen kur
* 🍏 `dataclass` ile veri sınıfları tanımla
* 💠 `__repr__`, ve `__eq__` metotları otmatik olarak tanımlanır
* 💎`type` zorunluluğu olduğundan ileride veri atama sorunlarını engeller

> 📢Python içerisinde `this` yerine `self` ile sınıf varlıklarına  erişilir

```python
from dataclasses import dataclass

@dataclass
class Card:
    rank: str
    suit: str
    
card = Card("Q", "hearts")

card == card # True
card.rank    # 'Q'
card         # Card(rank='Q', suit='hearts')
```

## 💠 Özel Sınıf Metotlarını Kullanın

| 🆔 İsim | 📃 Açıklama |
| :--- | :--- |
| `__init__` | Sınıf oluşturulduğunda çağırılır \(`constructor`\) |
| `__str__` | Sınıf `str`, `f"{}"` veya `print` ile yazdırılmak istendiğinde çağırılır |
| `__repr__` | Debug işlemleri sırasında sınıf hakkında bilgileri verir \(VS Code Debug metinleri vs\) |
| `__eq__` | Sınıf arasında eşitlik kıyaslaması yapıldığında çalışır \(`a == b`\) |
| `__hash__` | Dict gibi işlemlerde key olarak sınıfın kullanılması için hashable olması gerekir `hash(str(self))` şeklinde kullanılabilir |

## 🏷️ Decorator Yapısı ile Tekrarlı Kodlardan Sakın

* ➕ Decorator yapısı fonksiyonların üstüne `@` ile eklenen fonksiyonlardır
* 🌊 Fonksiyon her çağırıldığında önce `@` ile eklenen fonksiyon çalışır sonra istenen çağırılır
* 👮‍♂️ API işlemlerinde yetki kontrolleri için kullanılması zaman kazandırır
* 💁‍♂️ `@functools.wraps(func)` decorator yapısı ile asıl fonksiyonun `__name__` gibi karakter özellikleri saklanır \(aksi halde `__name__` değeri `@` olan fonksiyonun ismini verir\)

```python
from typing import Tuple

def authentication_required(func):
    @functools.wraps(func)
    def wrapper_decorator(*args, **kwargs):
        if not args[0].authenticated:
            raise UnauthorizedError(response=None)
        value = func(*args, **kwargs)
        return value

    return wrapper_decorator

class DataBase:
    
    def __init__(auth: str):
        self.authenticated = True if auth else False

    @authentication_required
    def get_user(id: int) -> Tuple[str, str]:
        # fetch user from database
        # ....
        name = "YEmreAk"
        symbol = "🦅"
        return name, symbol # Tuple[str, str]

name, birthdate = DataBase("👮‍♂️").get_user(7)
```

## 📜 `print`'ten Vazgeç `logger` ile Raporlama Yap

* 🎨 Öncelikle `colorlog` ile renkli raporlama yapabilirsin
* 📦 import logging ile log paketini indirin

> Buraya detaylı bilgi sonradan eklenecek

{% page-ref page="../temel/raporlama.md" %}

## 🔗 Faydalı Bağlantılar

* [📃 Python Best Practice](https://data-flair.training/blogs/python-best-practices/)
* [📃 30 Python Best Practice Tips and Tricks](https://towardsdatascience.com/30-python-best-practices-tips-and-tricks-caefb9f8c5f5)
* [📃 Top Python Projects](https://data-flair.training/blogs/python-projects-with-source-code/)

