---
description: Dosya işlemlerine (file operation) yakından bakış
---

# 📂 Dosya İşlemleri

## 👮‍♂️ Dosyaya Erişim

Python üzerinde dosya işlemleri oldukça kolaydır.

{% tabs %}
{% tab title="✨ Kullanım" %}
* Temel okuma metodu `open(<dosya_ismi>, <erişim_modu>, encoding=<kodlama>)` şeklindedir
  * `<dosya_ismi>` Dosya yolu veya ismi
    * _Örn: "text.txt"_
  * `<erişim_modu>` Okuma, yazma veya ekleme
    * _Örn: 'a', 'w', 'r', 'r+' ..._
  * `<kodlama>` Dosya kodlama formatı
    * _Örn: 'utf-8'_
* Dosya bulunamazsa `IOError` hatası verir
{% endtab %}

{% tab title=" 💎 Erişim Modları" %}
| Mod | Anlamı | Açıklama |
| :--- | :--- | :--- |
| `r` | Read \(Okuma\) | Dosya varsa okumak için açar yoksa hata verir |
| `w` | Write \(Yazma\) | Dosyayı sıfırdan yazmak için oluşturma \(verileri siler\) |
| `a` | Append \(Ekleme\) | Dosyayı üzerine eklemek için açar, yoksa oluşturur |
| `wb, rb, ab` | Binary işlemleri | Sıkıştırılmış dosyada işlemler |

> Ek bilgiler için [buraya](https://stackoverflow.com/a/1466036/9770490) bakabilirsin.
{% endtab %}

{% tab title="💠 İşlem Metodları" %}
| Mod | Açıklama |
| :--- | :--- |
| `read()` | Dosyayı komple okuma |
| `readline()` | Dosyadaki 1 satırı okuma |
| `readlines()` | Dosyadaki tüm satırları `list` objesine alma |
| `write(<metin>)` | Dosyaya metin yazma |
| `close()` | Dosyayı kapatma \(context manager için gerekli değil\) |
{% endtab %}

{% tab title="⭐ Erişim Örnekleri" %}
```python
file_str = ""
with open("README.md", "r", encoding="utf-8") as file:
    file_str = "".join(file.readlines())
```

```python
file_str = ""
with open("README.md", "r", encoding="utf-8") as file:
    for line in file:
        file_str += line
```

```python
with open(xml_path) as fp:
        for row, line in enumerate(fp):
            pass
```

```python
with open("README.md", "r", encoding="utf-8") as file:
    lines = list(file) # Tüm satırları liste olarak döndürür
    line = file.readline() # Tek bir satırı string olarak döndürür
    lines = file.readlines() # Tüm satırları liste olarak döndürür
```
{% endtab %}
{% endtabs %}

## 👀 Dosya Okuma Yöntemleri

{% tabs %}
{% tab title="📦 Obje" %}
```python
f = open('./data/sample.txt', 'r', encoding="utf-8")
data = f.read()
f.close()

print(data)
print(f)
```
{% endtab %}

{% tab title="👨‍💼 Context Manager" %}
```python
with open('./data/sample.txt', 'r', encoding="utf-8") as f:
    print(f.read())

print(f)
```
{% endtab %}

{% tab title="📋 Ortak Çıktı" %}
```python
Hello!
Congratulations!
You've read in data from a file.
<_io.TextIOWrapper name='./data/sample.txt' mode='r' encoding='UTF-8'>
```
{% endtab %}
{% endtabs %}

## 💠 Dosya İşlemleri

{% tabs %}
{% tab title="🎈 Tek Satır Okuma" %}
```python
with open('./data/sample.txt', 'r') as f:
    print(f.readline())
```
{% endtab %}

{% tab title="👁‍🗨 Tüm Satırları Okuma" %}
```python
with open('./data/sample.txt', 'r') as f:
    print(f.readlines())
```
{% endtab %}

{% tab title="🤸‍♂️ Dosyayı Kapatmadan Yazma" %}
Sürekli açık olan bir dosya için:

* `flush()` metodu ile değişikliklerinizi kaydetmelisiniz
* Dosyayı kapatmak için `close()` metodunu kullanın

```python
DOSYA_YOLU = "README.md"
DOSYA_MODU = "w+" # w, a, r, w+ ...
ENCODING = "utf-8" # Özel karakterleri aktif etmek için

file = open(DOSYA_YOLU, DOSYA_MODU, encoding=ENCODING)
file.flush() # Dosyaya yapılan işlemleri kaydetme
file.close() # Dosyayı kapatır
```
{% endtab %}

{% tab title="👨‍💻 Encoding" %}
| Komut | Açıklama |
| :--- | :--- |
| `sys.stdout.reconfigure(encoding='utf-8')` | 🚀 Emoji gibi farklı formattaki metinler üzerinde çalışırken kullanılır \(Terminal bunları algılayamaz\) |

> [How to set sys.stdout encoding in Python 3?](https://stackoverflow.com/a/52372390/9770490)
{% endtab %}
{% endtabs %}

## 🚩 Dosya Okuma Formatları

### 🔨 Properties Dosya Formatını Okuma

* Modül olarak [configparser](https://docs.python.org/3/library/configparser.html) kullanılır
* `.gitsubmodules`, `config.ini` gibi dosyaların yapısında kullanılabilir

{% tabs %}
{% tab title="📑 Dosya Formatı" %}
```elixir
[DEFAULT]
ServerAliveInterval = 45
Compression = yes
CompressionLevel = 9
ForwardX11 = yes

[bitbucket.org]
User = hg

[topsecret.server.com]
Port = 50022
ForwardX11 = no
```
{% endtab %}

{% tab title="✍ Yazma" %}
```python
import configparser

config = configparser.ConfigParser()
# Yorum satırlarını okumadan
# config = configparser.ConfigParser(inline_comment_prefixes="#")

config['DEFAULT'] = {'ServerAliveInterval': '45',
                     'Compression': 'yes',
                     'CompressionLevel': '9'}
config['bitbucket.org'] = {}
config['bitbucket.org']['User'] = 'hg'
config['topsecret.server.com'] = {}
topsecret = config['topsecret.server.com']
topsecret['Port'] = '50022'     # mutates the parser
topsecret['ForwardX11'] = 'no'  # same here
config['DEFAULT']['ForwardX11'] = 'yes'
with open('example.ini', 'w') as configfile:
  config.write(configfile)
```
{% endtab %}

{% tab title="👀 Okuma" %}
```python
>>> config = configparser.ConfigParser()
>>> config.sections()
[]
>>> config.read('example.ini')
['example.ini']
>>> config.sections()
['bitbucket.org', 'topsecret.server.com']
>>> 'bitbucket.org' in config
True
>>> 'bytebong.com' in config
False
>>> config['bitbucket.org']['User']
'hg'
>>> config['DEFAULT']['Compression']
'yes'
>>> topsecret = config['topsecret.server.com']
>>> topsecret['ForwardX11']
'no'
>>> topsecret['Port']
'50022'
>>> for key in config['bitbucket.org']:  
...     print(key)
user
compressionlevel
serveraliveinterval
compression
forwardx11
>>> config['bitbucket.org']['ForwardX11']
'yes'
```
{% endtab %}
{% endtabs %}

