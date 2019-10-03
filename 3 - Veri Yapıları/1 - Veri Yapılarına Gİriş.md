---
description: Temel değişkenlerin birleştirilmesi ile oluşturulan yapılardır 🗃
---


# 🚪 Veri Yapılarına Giriş

## 🌟 List

Birden fazla veriyi saklamak için kullanılan değişkendir. (array)

- Birbirinden farklı değişkenleri tutabilir (_confused list_)
- Aynı değişken birden fazla tekrar edebilir
- Hızlıca göz atmak için [buraya][list] buraya bakabilirsin

| List Metodları               | Açıklama                                                    |
| ---------------------------- | ----------------------------------------------------------- |
| `len(list)`                  | Karakter sayısı                                             |
| `list.append(<value>)`       | Eleman ekleme                                               |
| `del list[i]`                | `i`. elemanı silem                                          |
| `list[i]` veya `list.get(i)` | `i`. karakter                                               |
| `list[-i]`                   | `len-i`. karakter                                           |
| `list[i:]`                   | `i`. eleman ve sonrasındakiler                              |
| `list[:i]`                   | `i`. elemana kadar (`i` dahil değil) olanlar                |
| `list[i:j]`                  | `i`. eleman ve `j`. elemana kadar (`j` dahil değil) olanlar |
| `[5] * i`                    | `i` tane 5 sayısı (`i=3` için `[5, 5, 5]`)                  |

- `[<değişken> for <değişken> in <dizi | liste | menzil> if <koşul>` İstenen koşullardaki elemanların listesini verir
  - Örn: `[x for x in range(0, 5) if x != 20]`

### 👮‍ İki Listenin Farkı (Sırası Önemli ve Güvenli Yöntem)

```py
a = [1, 2, 20, 6, 210]
b = set([6, 20, 1])
[x for x in a if x not in b]
```

> [Converting a list to a set changes element order](https://stackoverflow.com/a/9792680)

### 🏃‍ İki Listenin Farkı (Sırası Önemsiz ve Eşsiz Veriler)

```py
a = [1, 2, 20, 6, 210]
b = [1, 2, 210]
list3 = list(set(list1) - set(list2))
```

> [Remove all values within one list from another list?](https://stackoverflow.com/a/30353802)

## 🗂 Array

Matematiksel işlemler ve _Data Science_ için tercih edilen modüldür.

- İlk olarak `numpy` _package_ indirilmelidir
  - `pip install numpy`
  - `conda install numpy`
- `from numpy import array` şeklinde dahil edilir
- `list` gibidir ama sadece **aynı** tür objeyi barındırır
  - `["a", 1]` olmaz, ikisi de `string` ya da `int` olmalıdır

> [List vs Array](https://medium.com/backticks-tildes/list-vs-array-python-data-type-40ac4f294551)

## 👝 Tuple

List gibidir lakin verileri değiştirilemez. (_immutable_)

- List'ten daha **hızlıdır**
- _Immutable_ olduğu için değişken verileri barındıramaz
  - İçerisine list öğresi olmaz
- Verileri sıralıdır (_ordered_)

## 🛩 Set

Küme işlemleri için kullanılır.

- Temel küme özelliklerini taşır.
  - _Keşisim, birleşim ..._
- Veriler **sıralı değildir**
- Set'in kendine özgü bir yerleştirme yapısı (_hash_) vardır.
  - Bu yapı sayesinde veriler, en hızlı olacak şekilde, **karmaşık** olarak dizilir
  - List'ten daha **hızlıdır**
  - Kaynak için [buraya][set mi yoksa list mi daha hızlı] bakabilirsin
- Birbirinden farklı değişkenleri tutabilir
- Aynı değişken birden fazla **yazılamaz** (küme özelliği)
- Tüm değerlerin _inmutable_ (değiştirilemez) olması gerekmektedir
  - `myset = {[1, 2, 3]}` komutunda `[1, 2, 3]` list öğesi _mutable_ olduğundan değiştirilebilir (ekleme çıkarma olabilir)
- _Indexing_ (indekslenme) ve _slicing, subscription_ (kesme, parçalama) işlemlerini desteklemez
  - `myset[0]` çalışmaz

| Set Metodları                | Açıklama                  |
| ---------------------------- | ------------------------- |
| `add(<immutable>)`           | Eleman ekleme             |
| `for <isim> in <set>`        | Elemanları döngü ile alma |
| `<isim> = next(iter(<set>))` | Elemanları sıra ile alma  |

- `<immutable>` Herhangi değiştirilemez değer
  - Örn: `1`, `"yemreak"`, `tuple`, `str`, `int` vs
- `<isim>` Elemena verilecek isim
  - Örn: `i`, `e` vs

> **Ek bağlantılar:**
>
> - [Hızlıca set açıklaması][set]
> - [Detaylı set açıklaması][set detaylı]

## 📕 Dict

Verilerin anahtarlara (_key_) göre saklandığı `list` yapısıdır.

- Her _key_ değeri eşsiz (_unique_) olmalıdır
- _Key_ değerleri **ana değişkenleri** olabilir, `list`, `tuple` gibi listeler olamaz

> Alttaki işlemlerin her biri `dict` objesinin alt işlemidir.

| İşlem                          | Açıklama                                        |
| ------------------------------ | ----------------------------------------------- |
| `dict[<key>]` & `get(<key>)`   | Anahtar ile veri alma, veri yoksa hata fırlatır |
| `dict[<key>] = <değer>`        | Belirli anahtara değer atama                    |
| `<key> in dict`                | Anahtar `dict`'e var mı kontrolü                |
| `json.dumps(dict)`             | `dict`'i `str`'a çevirme                        |
| `dict( (a,1) for a in <list>)` | `<liste>`'nin her elamanı ile 1'i eşleyen dict  |


- [`Dict`'i `str`'a çevirme][dict'i str'a çevirme]
- [`Dict`'ten hızlı bir yöntem var mı][dict'ten hızlı var mı]

## 📚 Zip

Birden fazla list yada benzeri yapıları birleştirmek için kullanlır.

```python
key = ['name', 'age', 'height', 'weight', 'hair', 'eyes', 'has dog']
value = ['Dylan', 28, 167.5, 56.5, 'brown', 'brown', True]

zipped = zip(key_list, value_list) # <zip object at 0x7f2ae4e91508>
list(zipped) # [('name', 'Dylan'), ('age', 28), ('height', 167.5), ('weight', 56.5), ('hair', 'brown'), ('eyes', 'brown'), ('has dog', True)]
dict(zipped) # {'name': 'Dylan', 'age': 28, 'height': 167.5, 'weight': 56.5, 'hair': 'brown', 'eyes': 'brown', 'has dog': True}

# Zip işlemini geri alma
key_list, value_list = zip(*zipped)

```

## 💱 Veri Yapıları Arasında Dönüşüm

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

## 🔍 Arama İşlemleri (Searching)

- Arama işlemlerinin temeli `in` ile yapılmaktadır.
- Tekrarlama işlemleri `for <key> in <yapı>:` ile yapılmaktadır

> Arama işlemi `KeyError` (_tanımsız değişkenler ile işlem yapma_) sorunuu ortadan kaldırır.

```python
if 'has dog' in me_dict:
    pass
```

## 🥾 Sıralama İşlemleri (Sorting)

Sırala işlemleri `sorted` metodu ile yapılmaktadır.

- Eğer yapıda farklı elemanlar var ise `map(<type>, <yapı>)` ile `sorted` fonksiyonu kullanılır
- Eğer `dict` verilerinde anahtar-veri (_key-value_) olarak sıralamk istersek `dict.items()` yapısı kullanılır

```python
print(sorted(map(str, example_tuple)))
print(sorted(map(str, example_set)))
print(sorted(me_dict.items())) # Key-Value değerlerini
print(sorted(me_dict)) # Sadece değerleri sıralar

sort(list) # sadece sıralar veri döndürmez
```

## 🤸‍ Comprehensions

Tek satır ile yapı oluşturmadır.

- Daha anlaşılır
- Daha hızlı

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


[dict'i str'a çevirme]: https://stackoverflow.com/a/4547331/9770490
[dict'ten hızlı var mı]: https://stackoverflow.com/a/40694623/9770490
[dictionary]: https://www.programiz.com/python-programming/dictionary
[tuple]: https://www.programiz.com/python-programming/tuple
[list]: https://www.programiz.com/python-programming/list
[set]: https://www.programiz.com/python-programming/set
[set detaylı]: https://www.datacamp.com/community/tutorials/sets-in-python
[set mi yoksa list mi daha hızlı]: https://stackoverflow.com/a/7717046/9770490s
