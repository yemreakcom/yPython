---
description: Temel değişkenlerin birleştirilmesi ile oluşturulan yapılardır.
---

# 💽 Veri Yapıları

## ‍👀 Veri Yapılarına Hızlı Bakış

| Tip | Açıklama | Örnek |
| :--- | :--- | :--- |
| [List](https://www.programiz.com/python-programming/list) | `liste = [1, 2]` | `liste[index]` |
| [Set](https://www.programiz.com/python-programming/set) | `kume = {1.0, "Hello", (1, 2, 3)}` | `kume.add(1)` |
| [Dictionary](https://www.programiz.com/python-programming/dictionary) | `site = {"adi":"yemreak"}` | `site['adi']` |
| [Tuple](https://www.programiz.com/python-programming/tuple) | `konum = (1, 2)` | `x, y = konum` |

## 🧱 Temel Veri Yapıları

{% tabs %}
{% tab title="📋 List" %}
Birden fazla veriyi saklamak için kullanılan değişkendir. \(array\)

* Birbirinden farklı değişkenleri tutabilir \(_confused list_\)
* Aynı değişken birden fazla tekrar edebilir
* Hızlıca göz atmak için [buraya](https://www.programiz.com/python-programming/list) buraya bakabilirsin

| List Metodları | Açıklama |
| :--- | :--- |
| `len(list)` | Karakter sayısı |
| `list.append(<value>)` | Eleman ekleme |
| `del list[i]` | `i`. elemanı silme |
| `list[i]` veya `list.get(i)` | `i`. karakter |
| `list[-i]` | `len-i`. karakter |
| `list[i:]` | `i`. eleman ve sonrasındakiler |
| `list[:i]` | `i`. elemana kadar \(`i` dahil değil\) olanlar |
| `list[i:j]` | `i`. eleman ve `j`. elemana kadar \(`j` dahil değil\) olanlar |
| `[5] * i` | `i` tane 5 sayısı \(`i=3` için `[5, 5, 5]`\) |

* `[<değişken> for <değişken> in <dizi | liste | menzil> if <koşul>` İstenen koşullardaki elemanların listesini verir
  * Örn: `[x for x in range(0, 5) if x != 20]`

### 👮‍ İki Listenin Farkı \(Sırası Önemli ve Güvenli Yöntem\)

```python
a = [1, 2, 20, 6, 210]
b = set([6, 20, 1])
[x for x in a if x not in b]
```

> [Converting a list to a set changes element order](https://stackoverflow.com/a/9792680)

### 🏃‍ İki Listenin Farkı \(Sırası Önemsiz ve Eşsiz Veriler\)

```python
a = [1, 2, 20, 6, 210]
b = [1, 2, 210]
list3 = list(set(list1) - set(list2))
```

> [Remove all values within one list from another list?](https://stackoverflow.com/a/30353802)
{% endtab %}

{% tab title="📁 Array" %}
Matematiksel işlemler ve _Data Science_ için tercih edilen modüldür.

* İlk olarak `numpy` _package_ indirilmelidir
  * `pip install numpy`
  * `conda install numpy`
* `from numpy import array` şeklinde dahil edilir
* `list` gibidir ama sadece **aynı** tür objeyi barındırır
  * `["a", 1]` olmaz, ikisi de `string` ya da `int` olmalıdır

> [List vs Array](https://medium.com/backticks-tildes/list-vs-array-python-data-type-40ac4f294551)
{% endtab %}

{% tab title=" 👝 Tuple" %}
List gibidir lakin verileri değiştirilemez. \(_immutable_\)

* List'ten daha **hızlıdır**
* _Immutable_ olduğu için değişken verileri barındıramaz
  * İçerisine list öğresi olmaz
* Verileri sıralıdır \(_ordered_\)
{% endtab %}

{% tab title="⭕ Set" %}
Küme işlemleri için kullanılır.

* Temel küme özelliklerini taşır.
  * _Keşisim, birleşim ..._
* Veriler **sıralı değildir**
* Set'in kendine özgü bir yerleştirme yapısı \(_hash_\) vardır.
  * Bu yapı sayesinde veriler, en hızlı olacak şekilde, **karmaşık** olarak dizilir
  * List'ten daha **hızlıdır**
  * Kaynak için [buraya](https://stackoverflow.com/a/7717046/9770490s) bakabilirsin
* Birbirinden farklı değişkenleri tutabilir
* Aynı değişken birden fazla **yazılamaz** \(küme özelliği\)
* Tüm değerlerin _inmutable_ \(değiştirilemez\) olması gerekmektedir
  * `myset = {[1, 2, 3]}` komutunda `[1, 2, 3]` list öğesi _mutable_ olduğundan değiştirilebilir \(ekleme çıkarma olabilir\)
* _Indexing_ \(indekslenme\) ve _slicing, subscription_ \(kesme, parçalama\) işlemlerini desteklemez
  * `myset[0]` çalışmaz

| Set Metodları | Açıklama |
| :--- | :--- |
| `add(<immutable>)` | Eleman ekleme |
| `for <isim> in <set>` | Elemanları döngü ile alma |
| `<isim> = next(iter(<set>))` | Elemanları sıra ile alma |

* `<immutable>` Herhangi değiştirilemez değer
  * Örn: `1`, `"yemreak"`, `tuple`, `str`, `int` vs
* `<isim>` Elemena verilecek isim
  * Örn: `i`, `e` vs

> **Ek bağlantılar:**
>
> * [Hızlıca set açıklaması](https://www.programiz.com/python-programming/set)
> * [Detaylı set açıklaması](https://www.datacamp.com/community/tutorials/sets-in-python)
{% endtab %}

{% tab title="📙 Dict" %}
Verilerin anahtarlara \(_key_\) göre saklandığı `list` yapısıdır.

* Her _key_ değeri eşsiz \(_unique_\) olmalıdır
* _Key_ değerleri **ana değişkenleri** olabilir, `list`, `tuple` gibi listeler olamaz

> Alttaki işlemlerin her biri `dict` objesinin alt işlemidir.

| İşlem | Açıklama |
| :--- | :--- |
| `dict[<key>]` & `get(<key>)` | Anahtar ile veri alma, veri yoksa hata fırlatır |
| `dict[<key>] = <değer>` | Belirli anahtara değer atama |
| `<key> in dict` | Anahtar `dict`'e var mı kontrolü |
| `json.dumps(dict)` | `dict`'i `str`'a çevirme |
| `dict( (a,1) for a in <list>)` | `<liste>`'nin her elamanı ile 1'i eşleyen dict |

* [`Dict`'i `str`'a çevirme](https://stackoverflow.com/a/4547331/9770490)
* [`Dict`'ten hızlı bir yöntem var mı](https://stackoverflow.com/a/40694623/9770490)
{% endtab %}

{% tab title="📚 Zip" %}
Birden fazla list yada benzeri yapıları birleştirmek için kullanılır.

```python
key = ['name', 'age', 'height', 'weight', 'hair', 'eyes', 'has dog']
value = ['Dylan', 28, 167.5, 56.5, 'brown', 'brown', True]

zipped = zip(key_list, value_list) # <zip object at 0x7f2ae4e91508>
list(zipped) # [('name', 'Dylan'), ('age', 28), ('height', 167.5), ('weight', 56.5), ('hair', 'brown'), ('eyes', 'brown'), ('has dog', True)]
dict(zipped) # {'name': 'Dylan', 'age': 28, 'height': 167.5, 'weight': 56.5, 'hair': 'brown', 'eyes': 'brown', 'has dog': True}

# Zip işlemini geri alma
key_list, value_list = zip(*zipped)
```
{% endtab %}
{% endtabs %}

## ✨ Veri Yapıları İşlemleri

{% tabs %}
{% tab title="💱 Veri Yapıları Arasında Dönüşüm" %}
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
{% endtab %}

{% tab title="🔍 Arama İşlemleri \(Searching\)" %}
* Arama işlemlerinin temeli `in` ile yapılmaktadır.
* Tekrarlama işlemleri `for <key> in <yapı>:` ile yapılmaktadır

{% hint style="success" %}
Arama işlemi `KeyError` \(_tanımsız değişkenler ile işlem yapma_\) sorunu ortadan kaldırır.
{% endhint %}

```python
if 'has dog' in me_dict:
    pass
```
{% endtab %}

{% tab title="🥾 Sıralama İşlemleri \(Sorting\)" %}
Sırala işlemleri `sorted` metodu ile yapılmaktadır.

* Eğer yapıda farklı elemanlar var ise `map(<type>, <yapı>)` ile `sorted` fonksiyonu kullanılır
* Eğer `dict` verilerinde anahtar-veri \(_key-value_\) olarak sıralamk istersek `dict.items()` yapısı kullanılır

```python
print(sorted(map(str, example_tuple)))
print(sorted(map(str, example_set)))
print(sorted(me_dict.items())) # Key-Value değerlerini
print(sorted(me_dict)) # Sadece değerleri sıralar

sort(list) # sadece sıralar veri döndürmez
```
{% endtab %}

{% tab title="🤸‍ Comprehensions" %}
Tek satır ile yapı oluşturmadır.

* Daha anlaşılır
* Daha hızlı

**Verimli Yapı:**

```python
squares = [x**2 for x in range(10)] # Liste tanımlama
square_lut = {x: x**2 for x in range(10)} # Dict tanımlama
```

**Eski yapı:**

```python
squares = []
square_lut = {}
for x in range(10):
    squares.append(x**2)
    square_lut[x] = x**2
```

**Çoklu anahtar ile tekrarlama**

```python
me_dict_dtypes = {k: type(v) for k, v in me_dict.items()}
print(me_dict_dtypes)

# {'name': <class 'str'>, 'age': <class 'int'>, 'height': <class 'float'>, 'weight': <class 'float'>, 'hair': <class 'str'>, 'eyes': <class 'str'>, 'has dog': <class 'bool'>, 'favorite color': <class 'str'>, 'nieces/nephews': <class 'int'>}
```
{% endtab %}
{% endtabs %}

## 📰 Koleksiyonlar

{% tabs %}
{% tab title="📋 Namedtuple" %}
* Özel adlandırılmış tuple değerleridir
* `verbose=True` olursa üretilen kodu görürüz

> `namedtuple`, neredeyse hiç hafıza maliyeti olmadan kendi kendini belgeleyen kod oluşturmak için harika bir yoldur.

```python
from collections import namedtuple
Vector3 = namedtuple('Vector', ['x', 'y', 'z'], verbose=True)

vec = Vector3(1,2,3)
vec.x, vec.y, vec.z

vec.x = 5 # Çalışmaz, çünkü tuple idir. (Dict'ten varkı burada belli olur)


def tfunc(a,b,c):
    print(a,b,c)

tfunc(*vec)
```

### NamedTuple ile Üretilen Kod

```python
from builtins import property as _property, tuple as _tuple
from operator import itemgetter as _itemgetter
from collections import OrderedDict

class Vector(tuple):
    'Vector(x, y, z)'

    __slots__ = ()

    _fields = ('x', 'y', 'z')

    def __new__(_cls, x, y, z):
        'Create new instance of Vector(x, y, z)'
        return _tuple.__new__(_cls, (x, y, z))

    @classmethod
    def _make(cls, iterable, new=tuple.__new__, len=len):
        'Make a new Vector object from a sequence or iterable'
        result = new(cls, iterable)
        if len(result) != 3:
            raise TypeError('Expected 3 arguments, got %d' % len(result))
        return result

    def _replace(_self, **kwds):
        'Return a new Vector object replacing specified fields with new values'
        result = _self._make(map(kwds.pop, ('x', 'y', 'z'), _self))
        if kwds:
            raise ValueError('Got unexpected field names: %r' % list(kwds))
        return result

    def __repr__(self):
        'Return a nicely formatted representation string'
        return self.__class__.__name__ + '(x=%r, y=%r, z=%r)' % self

    def _asdict(self):
        'Return a new OrderedDict which maps field names to their values.'
        return OrderedDict(zip(self._fields, self))

    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return tuple(self)

    x = _property(_itemgetter(0), doc='Alias for field number 0')

    y = _property(_itemgetter(1), doc='Alias for field number 1')

    z = _property(_itemgetter(2), doc='Alias for field number 2')
```
{% endtab %}

{% tab title="🌠 Deque" %}
List objelerinin uç noktaları ile ilgilenen bir yapıdır.

* List'e göre optimize edilmiştir
  * List için $O\(N\)$ Dque için $O\(1\)$
  * ${Verim}_{O\(1\)} &gt; {Verim}_{O\(N\)}$

```python
from collections import deque

d = deque([2,3,4,5]) # deque([2, 3, 4, 5])
d.append(10) # deque([2, 3, 4, 5, 10])
d.appendleft(20) # deque([20, 2, 3, 4, 5, 10])
```

### Deque için Verimlilik Hesapbı

> Süreleri **IPython**'da `%%timeit` kodu ile hesaplayabilirsin

```python
# %%timeit
d = deque()
for i in range(40000):
    d.appendleft(i)

# 3.76 ms ± 35.6 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

```python
# %%timeit
l_ = list()
for i in range(40000):
    l_.insert(0, i)

# 410 ms ± 5.94 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

```python
list(d) == l_ # True
```
{% endtab %}

{% tab title="⏳ Counter" %}
`list` objelerini sayar `dict` yapısında Anahtar-Miktar ikilisi döndürür.

* Olmayan anahtarlar için `0` değeri döndürülür
* En fazla tekrar eden anahtarlar için `most_common(<gösterilecek_anahtar_sayısı>)` fonksiyonu kullanılır

```python
from collections import Counter
ele = ['a','b','a','c','b','b','d']
c = Counter(ele)

# Counter({'b': 3, 'a': 2, 'c': 1, 'd': 1})

c['a'], c['z'] # (2, 0)
c.most_common(5) # [('b', 3), ('a', 2), ('c', 1), ('d', 1)]
```
{% endtab %}

{% tab title="📗 Verimli Dict Yapıları" %}
## OrderedDict

Sıralanmış `dict` olarak geçmektedir

> Sıralandığı için $O\(1\)$ erişim hızına sahiptir.

## DefaultDict

`dict` verilerinde en önemli sorun olmayan anahtar \(_key_\) verileridir.

* Olmayan anahtarlar için varsayılan değer atanır
* Kodda daha temiz yapı sunar
* `defaultdict(<type>)` şeklinde tanımlanır

### DefaultDict Avantajı

```python
from collections import defaultdict
def count_default(x):
    count_dict = defaultdict(int)
    for ele in x:
        count_dict[ele] += 1 # count_dict'te olmayanların değeri 0 olduğundan 1 arttırılabilir
    return count_dict
count_default(ele)
```

```python
def count(x):
    count_dict = {}
    for ele in x:
        if ele in count_dict.keys():
            count_dict[ele] += 1
        else: # count_dict'te olmayan veriler için 1 atanmalıdır
            count_dict[ele] = 1
    return count_dict
count(ele)
```
{% endtab %}
{% endtabs %}

