---
description: Python ile module ve package kodlama veya oluşturma
---

# 📦 Modül ve Paketler

## 🚶‍♂️ Dosyalar Arasında Gezinme

* 💡 Python ile dizinlerde bulunan kaynak kodları `__init__.py` dosyası ile belirtilir
* 📢 Eğer dizinde `__init__.py` **olmazsa** kaynak kod dosyaları arasında **import işlemi yapılmaz**&#x20;
* 👨‍💻 Kaynak kodlardan import işlemleri için `.` karakteri kullanılır
  * `.` ile aynı dizindeki dosyaya
  * `..` ile üst dizindeki dosyaya
  * `...` ile 2 üst dizindeki dosyaya erişilir

## 📂 Modüller

Her python dosyasına modül denir.

* `import` ile dahil edilirler
* `.` ile içindekilere erişilir
* Modül barındıran dizinler `__init__.py` dosyası içermelidir
* `__init__.py` dosyası . yapısının kullanılmasına ve `__all__=['']` yapısı ile hangi objelerin aktarılacağını belirler

{% code title="__init__.py" %}
```python
"""GitBook yönetim paketi
"""
# aynı dizinde core.py isimli dosyaya erişme
from .core import (check_summary, create_changelog,
                   generate_description_section, generate_filelink_string,
                   get_summary_url_from_repo_url, read_summary_from_url)
                   
# aynı dizinde entity.py isimli dosyaya erişme
from .entity import (ConfigOptions, IntegrationOptions, OptionParser, Options,
                     SubmoduleOptions)

# Sadece alttaki objeler dışarı aktarılır
__all__ = [
    'IntegrationOptions',
    'SubmoduleOptions',
    'ConfigOptions',
    'OptionParser',
    'Options',
    'generate_description_section',
    'generate_filelink_string',
    'get_summary_url_from_repo_url',
    'read_summary_from_url',
    'check_summary',
    'create_changelog'
]
```
{% endcode %}

### ⭐ Modül Kullanım Örnekleri

* Python aynı modülü birden fazla kez `import` etmez
  * Kullanıcı birden fazla `import` işlemi yaparsa tepki vermez
* Baştan `import` edilmek istenirse `imp.reload(modül)` şeklinde kullanılır

{% tabs %}
{% tab title="✨ Tanımlama" %}
```python
import math # Doğrudan öodülü alma
print("Pi: ", math.pi) # Pi: 3.141592653589793
```

```python
import math as m # Modülü özel isimlendirme
print("Pi: ", m.pi) # Pi: 3.141592653589793
```

```python
from math import pi # Modül içinden özel değeri alma
print("Pi: ", pi) # Pi: 3.141592653589793
```

```python
from math import * # Modül içindeki her şeyi alma
print("Pi: ", pi) # Pi: 3.141592653589793
```
{% endtab %}

{% tab title="🌟 Sık Kullanılanlar" %}
| Modül                                                                   | Odaklantığı İşlemler                            |
| ----------------------------------------------------------------------- | ----------------------------------------------- |
| math                                                                    | Matematiksel                                    |
| random                                                                  | Rastgele                                        |
| Numpy                                                                   | Vektör işlemleri ve üst seviye matematik        |
| Pandas                                                                  | Veri işlemleri                                  |
| Scipy                                                                   |                                                 |
| Scikit-Learn                                                            |                                                 |
| Matplotlib                                                              | Grafik, çizim ve tablo işlemleri                |
| Seaborn                                                                 |                                                 |
| TensorFlow                                                              | Makine Öğrenimi ve Deep Learning                |
| [tqdm](https://tqdm.github.io)                                          | Progress Bar (Yüklenyior vs gibi işlemler için) |
| [colorama](https://www.geeksforgeeks.org/print-colors-python-terminal/) | Terminal renklendirme                           |
{% endtab %}

{% tab title="🎲 Random" %}
| Fonksiyon                         | Açıklama                                    |
| --------------------------------- | ------------------------------------------- |
| `random()`                        | 0 <= sayı <= 1 kesirli sayı                 |
| `randrange(<max>)`                | sayı <= `max`                               |
| `randrange(<min>, <max>, <adım>)` | `min` <= sayı <= `max` (`adım` kadar artar) |
{% endtab %}
{% endtabs %}

### 📁 Modül Dosyaları

Modül dosyalarının aranma yerleri:

* Çalışılan dizin
* Ortam değişkenlerindeki `PYTHONPATH` değişkeni değeri
* Kuruluma bağlı varsayılan dizin

{% tabs %}
{% tab title="👁‍🗨 Sistemin Python Modüllerine Bakma" %}
```python
>>> import sys
>>> sys.path
['',
'C:\\Python33\\Lib\\idlelib',
'C:\\Windows\\system32\\python33.zip',
'C:\\Python33\\DLLs',
'C:\\Python33\\lib',
'C:\\Python33',
'C:\\Python33\\lib\\site-packages']

>>> import example
>>> example.__name__
'example'

>>> a = 1 # Modül değişkenlerine ekleniyor
>>> b = "hello" # Modül değişkenlerine ekleniyor
>>> import math # Modül değişkenlerine ekleniyor
>>> dir()
['__builtins__', '__doc__', '__name__', 'a', 'b', 'math', 'pyscripter']
```
{% endtab %}

{% tab title="👀 Modül İçinde Tanımlanan İsimlere Bakma" %}
```python
>>> dir(example)
['__builtins__',
'__cached__',
'__doc__',
'__file__',
'__initializing__',
'__loader__',
'__name__',
'__package__',
'add']
```
{% endtab %}
{% endtabs %}

## 📦 Paketler (Package)

* Birden fazla modülü içinde barındırır
* `.` ile modüllere erişilir
  * Tekrar `.` atılırsa modülün içindekilere erişilir

```python
import Game.Level.start
from Game.Level import start
from Game.Level.start import select_difficulty
```
