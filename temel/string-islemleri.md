---
description: Python'da string (metin) işlemleri
---

# 🔤 String İşlemleri

## 👀 Hızlı Bakış

* 🌟 Programlama dillerindeki en önemli konulardandır
* 📈 Verimliliği artırma adına bu konunun bilinmesi mühimdir

> 💁‍♂️ Diğer önemli konu **Arama İşlemleri** olarak söylenir

## 🧱 Temel İşlemler

String'ler karakter listesi olarak geçtiğinden `list` özelliklerini taşır.

| İşlem | Açıklama |
| :--- | :--- |
| `+`, `=-` ... | Aritmetik operatörleri destekler |
| `len(string)` | Karakter sayısı |
| `string[i]` | `i`. karakter |
| `string[-i]` | `len-i`. karakter \(Sondan `i` kadar önceki\) |
| `string[i:]` | `i`. eleman ve sonrasındakiler |
| `string[:i]` | `i`. elemana kadar \(`i` dahil değil\) olanlar |
| `string[i:j]` | `i`. eleman ve `j`. elemana kadar \(`j` dahil değil\) olanlar |
| `string[-j:-i]` | `len-j`. eleman ve `len-i`. elemana kadar \(`len-i` dahil değil\) olanlar |
| `'{:>i}'.format('test')` | `i` karakter ayırır metni sağa yaslar |
| `'{:i}'.format('test')` | `i` karakter ayırır metni sola sağlar |

{% hint style="info" %}
🧙‍♂️ Detaylar için [string formatlama](https://pyformat.info/) sayfasına bakabilirsin.
{% endhint %}

## 🔌 String Ön Ekleri

| 💠 Metot | 📝 Açıklama |
| :--- | :--- |
| `f` | Format string ön eki |
| `r` | Raw String ön eki |
| `u` | Unicode string ön eki |
| `"""` | Çok satırlı string |

```python
x = 10
f"{x} = 10"  # "x = 10"
f"{x=}"      # "x = 10"  (F-String)

"Hello\tWorld"  # "Hello    World"
r"Hello\tWorld" # "Hello\tWorld"

u"🦅" # "🦅"

"""Hello
World
"""
# Hello
# World

"""
    Hello
    World
"""
# 
#     Hello
#     World

"""
    Hello
    World
""".strip()

# Hello
# World
```

## 👨‍🔧 String Düzenleme

### 📈 Verimlilik Notları

* `r` ök eki ile yazılan string daha hızlı işlenir
* `replace` metodu en hızlı string değiştirme metodudur.
  * `replace(...).replace(...)` ile çoklu değişim yapılması daha hızlıdır

> Ek kaynaklar:
>
> * Daha fazla bilgi için [buraya](https://www.programiz.com/python-programming/methods/string) ve [buraya](https://stackoverflow.com/questions/10660435/pythonic-way-to-create-a-long-multi-line-string) bakabilirsin

> * String değiştirme hızları kıyaslaması için [buraya](https://stackoverflow.com/a/27086669/9770490) bakabilirsin



### 💠 Metotlar ile

| 💠 Metot | 📝 Açıklama |
| :--- | :--- |
| `len` | Uzunluk |
| `strip` | Temizleme, düzeltme |
| `ltrip` | Metnin solunu temizleme, düzeltme |
| `rtrip` | Metnin sağını temizleme, düzeltme |
| `format` | Formatlama |
| `lower`, `upper` | Küçük / büyük harf |
| `split` | Parçalama |
| `[<başlangıç>:<bitiş>]` | Kesme |
| `join` | Birleştirme |
| `find` | Karakter indeksini bulma |
| `replace` | Metin değiştirme |
| `count` | Metin sayma |
| `sort` | Metni sıralama |

```python
len("yemreak") # 7

' abc '.strip() # 'abc'
' abc '.ltrip() # 'abc '
' abc '.rtrip() # ' abc'

"X: {}, Y: {}".format(1, 2) # 'X: 1, Y: 2'
"As".lower(), "As".upper()  # "as", "AS"
"yemreak".replace("ak", "") # 'yemre'

['n', 'a', 'i'].sort()      # ['a', 'i', 'n']

"ye mre ak".split(" ")             # ['ye', 'mre', 'ak']
"yemreak".[2:5], "yemreak".[-3:-1] # "mre", "ea"

','.join(['do', 're', 'mi']) # 'do,re,mi'

"yemreak".find('e') # 1 (yoksa -1)
"yeymey".count("y") # 3

```

### 💎 Özel karakterler ile

* ⌨️ print gibi yazdırma metotlarında kullanılır

| 🦄 Karakter | 📝 Açıklama |
| :--- | :--- |
| `\n` | Yeni satır |
| `\r` | Satır başı |
| `\t` | Tab \(4 boşluk |
| `\` | Escape chars |

### 💯 Operatörler ile

| 💎 Operatör | 📝 Açıklama |
| :--- | :--- |
| `: <10` | 10 karakterlik alana sola dayalı yazma |
| `: >10` | 10 karakterlik alana sağ dayalı yazma |
| `=` | F-string |
| `%` | Operatör ile formatlama |

```python
var = "YEmreAk"
f"{var=}"     # "var='YEmreAk'"
f"{var: <10}" # 'YEmreAk   '
f"{var: >10}" # '   YEmreAk'
f"{var: ^10}" # ' YEmreAk '

num = 1234.56789
f"{num=}"      # 'num=1234.56789'
f"{str(num)=}" # "str(num)='1234.56789'"
f"{num:.7f}"   # '1234.5678900'
f"{num:.7g}"   # '1234.568'

num = 1234.5672
f"{num:.7g}"   # '1234.567'

'new(%s %d)' % ('help', 5) # 'new(help 5)'
```

## 👨‍💻 Kod Parçaları

### 🔂 Karakter Değiştirme

Stringler `string[i] = char` yapısını desteklemez, alttaki yöntem gibi işlemler kullanılır

```python
def change_char(string, i, char):
    if i != -1:
        return string[:i]+char+string[i+1:]
    else:
        return string[:i]+char
```

### 🙃 Karakterleri Ters Çevirme

```python
def reverse_char(sentence):
    rev = ""
    for i in range(1, len(sentence) + 1):
        rev += sentence[-i]

    return rev

```

### 🙃 Kelimeleri Ters Çevirme

```python
def reverse_word(sentence):
    words = sentence.split(' ')
    for i in range(1, len(words) + 1):
        sentence += words[-i] + " "

    return sentence[:-1] # Sondaki, fazladan ' ' karakteri kaldırılıyor
```

### 🔍 Metin Arama

Alttaki yöntem ile tek bir karakteri string içerisinde bulabilirsiniz.

```python
string = "yemreak"
tek_metin = "yemre"
metinler = ['emre', 'ak']

# Tek metin işlemi
if tek_metin in string:
  print("Metin bulundu")

# Çok fazla metin işlemleri
if all(metin in string for metin in metinler):
  print("Hepsi bulundu")

if any(metin in string for metin in metinler):
  print("Herhangi biri bulundu)
```

> Kaynak için [buraya](https://stackoverflow.com/a/3389611/9770490) bakabilirsin.

### ️‍🕵️‍♂️ Metinlerin Konumunu Bulma

```python
import re
[m.start() for m in re.finditer('test', 'test test test test')]
#[0, 5, 10, 15]
```

> [How to find all occurrences of a substring?](https://stackoverflow.com/a/4664889/9770490)

### 🅰️ Karakter Sayma

```python
string = "Yemreak"
for i, char in enumerate(string):
  print(i, char)

# 0 Y
# 1 e
# 2 m
# ...
```

