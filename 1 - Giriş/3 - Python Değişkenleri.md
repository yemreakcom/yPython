# 💫 Python Değişkenleri 

<!-- TODO: Immutabble mutable kavramını açıkla -->

## Temel Değişkenler

| Tip     | Açıklama         | Örnek                                           |
| ------- | ---------------- | ----------------------------------------------- |
| bool    | 2'li değer, bit  | `True`                                          |
| int     | Sayı             | `1`                                             |
| float   | Virgüllü sayı    | `1.2`, `round(3.12312, 2) # 3.12`               |
| complex | Karmaşık sayılar | `2+3j`, `x = complex(5, 3)`, `x.real`, `x.imag` |
| str     | String, metin    | `"Hello"` / `'Hello'`                           |

> Değişkenin daha önceden tanımlandığını kontrol etme için [buraya][değişkenin daha önceden tanımlandığını kontrol etme] bakabilirsin.

## Veri Yapıları

| Tip          | Açıklama                           | Örnek          |
| ------------ | ---------------------------------- | -------------- |
| [List]       | `liste = [1, 2]`                   | `liste[index]` |
| [Set]        | `kume = {1.0, "Hello", (1, 2, 3)}` | `kume.add(1)`  |
| [Dictionary] | `site = {"adi":"yemreak"}`         | `site['adi']`  |
| [Tuple]      | `konum = (1, 2)`                   | `x, y = konum` |

> Veri yapıları konusu altında işlenmektedir.

## Değişkenlerin Özellikleri

- Bellekte ayrıdıkları alanda, üzerine atanan değerleri tutan objelerdir
- Temel değişkenlerde atama `=` işlemlerinde değer (_"value"_) aktarımı yapılır
- Diğer değişkenlerde adres (_"referance"_) aktarımı yapılır
  - `list` için `b = list(a)` ya da `b = a[:]` yapısı ile değer kopyalanır
  - `b = a` yapısı adresi kopyalar, `a.append(1)` yapıldığında `b`'ye de eklenir

## Değersiz Değişken Tanımlama

```python
degersiz = None
```

## Sabit Değerler (Constants)

Python'da _constant_'lar yoktur. Sabit değerler büyük harfler ile belirtilir.

> Aynı dosya içerisinde büyük harflerle yazılsa bile değiştirilebilir.

**`sabitler.py` dosyası**

```python
PI = 3.14
YER_CEKIMI = 9.8
```

**`main.py` dosyası**

```python
import sabitler

print(sabitler.PI) # 3.14
print(sabitler.GRAVITY) # 9.8
```

## Değişkenler Arası Dönüşüm (Casting)

Değişkenin tipi öğrenmek için `type(<değişken>)` komutu kullanılır.

```python
ondalikli = 5.8
type(ondalikli) #  <class 'float'>
tam = int(5.8) # 5 atanır
type(tam) # <class 'int'>

sonuc = int(7/3.5) # 2 atanır
sonuc = int(7/3) # 2 atanır
sonuc = float(7 / 3.5) # 2.0 atanır
sonuc = 7 / 3 # 2.33 atanır

value = "False"
print(bool(value)) # True verir, bool'a takılama string içeriğine bakmaz.
print(bool("")) # False
```

## Taban ve Tavan İşlemleri

```python
import math

tam = math.ceil(5.8) # 6 atanır
tam = math.floor(5.8) # 5 atanır
```

### Eval Fonksiyonu ile Dönüştürme

```python
value = "5"
print(type(value)) # <class 'str'>
print(type(eval(value))) # <class 'int'>
print(type(value)) # <class 'str'>
```

### İleri Seviye Değişken Dönüştürme

```python
value1 = "5"
value2 = 3

print(type(value1)) # <class 'str'>
print(type(value2)) # <class 'int'>

value3 = type(value2)(value1) # Value1'i value2'nin tipine dönüştürme

print(value3) # 5
print(type(value3)) # <class 'int'>
```

## Değişken Tipleri için Ek Kaynak

- [Basic Data Types in Python](https://realpython.com/python-data-types/)

## Değişken ve Sabitlerde Gizlilik

- `__` ile gizli anlamında gelmektedir.
  - Dışarıdan sadece `_<class>.__<değişken>` şeklinde erişilebilir

> Detaylar için [buraya](https://www.bogotobogo.com/python/python_private_attributes_methods.php) bakabilirsin.

## Değişkenin Tanımlı Olduğunu Kontrol Etme

```python
if 'myVar' in locals():
  # myVar exists.
if 'myVar' in globals():
  # myVar exists.
if hasattr(obj, 'attr_name'):
  # obj.attr_name exists.
```

> Kaynak için [buraya](https://stackoverflow.com/a/843293) bakabilirsin.

## Programı Sonlandırma

Alttaki metodlarla programı sonlandırabilirsin.

- `exit(<mesaj>)`
- `quit(<mesaj>)`
- `sys.exit(<mesaj>)`

## Sayılar, Sayılar Arası Dönüşüm ve Matematik

### Tabanlı Sayılar

| Taban  | Ön ek           | Örnek                | Çıktı         |
| ------ | --------------- | -------------------- | ------------- |
| 2'lik  | `0b` ya da `0B` | `print(0b1101011)`   | 107           |
| 8'lik  | `0o` ya da `0O` | `print(0xFB + 0b10)` | 253 (251 + 2) |
| 16'lık | `0x` ya da `0X` | `print(0o15)`        | 13            |

### Ondalıklı Sayılar (Decimals / Floats)

```python
>>> (1.1 + 2.2) == 3.3
False
>>> 1.1 + 2.2
3.3000000000000003
```

```python
import decimal

print(0.1) # 0.1
print(decimal.Decimal(0.1)) # Decimal('0.1000000000000000055511151231257827021181583404541015625')
```

```python
from decimal import Decimal as D

print(D('1.1') + D('2.2')) #  Decimal('3.3')
print(D('1.2') * D('2.50')) # Decimal('3.000')
```

#### Decimal Float Kullanımları ve Farkı

- Decimal daha fazla bellek kaplar
- Finansal işlemlerde decimal tercih edilir

#### Kesirli Sayılar (Fractions)

```python
import fractions

print(fractions.Fraction(1.5)) # 3/2
print(fractions.Fraction(5)) # 5
print(fractions.Fraction(1,3)) # 1/3
```

```python
import fractions

# Floatlar virgülden sonra da sayı barındırdığından dolayı farklı sonuç verir
print(fractions.Fraction(1.1)) # 2476979795053773/2251799813685248
print(fractions.Fraction('1.1')) # 11/10
```

#### Kesirli Sayılarla İşlemler

```python
from fractions import Fraction as F

print(F(1,3) + F(1,3)) # 2/3
print(1 / F(5,6)) # 6/5
print(F(-3,10) > 0) # False
print(F(-3,10) < 0) # True
```

### Matematik İşlemleri

```python
import math

print(math.pi) # 3.141592653589793
print(math.cos(math.pi)) # -1.0
print(math.exp(10)) # 22026.465794806718
print(math.log10(1000)) # .0
print(math.sinh(1)) # 1.1752011936438014
print(math.factorial(6)) # 720
```

#### Matematikte Rastgelelik

```python
import random

x = ['a', 'b', 'c', 'd', 'e']

print(random.randrange(10,20)) # Rastgele 10, 20 arasında sayı yazdırma
print(random.choice(x)) # Rastgele seçim yapma
random.shuffle(x) # Karıştrma
print(x) # Karışım sonucunu yazma
print(random.random()) # Rastgele eleman yazma
```

<!-- ## Harici Bağlantılar -->

[list]: https://www.programiz.com/python-programming/list
[set]: https://www.programiz.com/python-programming/set
[tuple]: https://www.programiz.com/python-programming/tuple
[dictionary]: https://www.programiz.com/python-programming/dictionary
[değişkenin daha önceden tanımlandığını kontrol etme]: https://stackoverflow.com/questions/843277/how-do-i-check-if-a-variable-exists
