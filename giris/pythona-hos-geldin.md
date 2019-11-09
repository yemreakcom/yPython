---
description: Python kuralları ve geleneklerini tanıyalım
---

# 🙋‍♂️ Python'a Hoş Geldin

## 🚧 Python ile Programlamaya Hazırlanma

Python ve JavaScript en popüler diller arasındadır.

* Python kodlarının uzantıları `.py` şeklindedir.
* Windows için `.pyw` uzantılı python dosyaları `start` \(veya `pythonw`\) komutu ile çalıştırılabilmekte
* Python komutunu ve pip ile indirdiklerinizi terminal üzerinden görebilmek için aşağıdakileri ortam değişkenlerine kaydetmeniz gerekmekte
  * `python.exe`'nin yolunu
  * `pip` ile indirilen terminal üzerinden derlenebilir komutlar için de _Scripts_ yolunu
  * `pip install` komutu ile indirilen script'ler scripts dizinine gider
  * Python'ı `exe` yapmak için [auto-py-exe](https://github.com/brentvollebregt/auto-py-to-exe) aracını kullanabilirsin

{% hint style="info" %}
Aralarındaki kıyaslama için [buraya](https://www.educba.com/python-vs-javascript/) bakabilirsin.
{% endhint %}

## 👮‍♂️ Yazım Kuralları

Orijinal dokümantasyon için [buraya](https://www.python.org/dev/peps/pep-0008/) bakabilirsin.

* Her python dosyasına **modül** denir
  * `import` ile dahil edilirler
  * `.` ile içlerine erişilir
* Class isimleri için **camel case** yazım kuralı geçerlidir
  * Boşluk karakteri **harfi büyüterek** temsil edilir
  * `camelCase`
* Geri kalanlar için **snake case** yazım kuralı geçerlidir
  * Boşluk karakteri `_` ile temsil edilir
  * `snake_case`
* Girintiler \(`\t` karakteri\) `{}` işlevi görür
* `:` karakteri ile yeni bir scope \(alt alan\) açılır
  * `for`, `def` gibi döngü veya metot işlemlerinde kullanırlar
* Metotlar arasında 2 satır bırakılır
* Metotların en son satırları boş olmalıdır \(return için\)
* Kodun en son satırı boş olmalıdır \(End of File\)
* _Private_ metotlar `_` ile başlar
  * `_add`, `_is_ prime`
* Özel metotlar _"dunder"_ `__` ile başlar ve biter
  * `__init__`, `__add__`

{% hint style="info" %}
Daha fazla bilgi için harici bağlantılardaki [Should I use underscores or camel case for Python?](https://www.quora.com/Should-I-use-underscores-or-camel-case-for-Python) bağlantısına tıklayabilirsin.
{% endhint %}

## 📃 Modül Dokümantasyon Örneği

```python
'''
Xenotix Python Keylogger for Windows
====================================
Coded By: Ajin Abraham <ajin25@gmail.com>
Website: http://opensecurity.in/xenotix-python-keylogger-for-windows/
GitHub: https://github.com/ajinabraham/Xenotix-Python-Keylogger

FEATURES
========
1.STORE LOGS LOCALLY
2.SEND LOGS TO GOOGLE FORMS
3.SEND LOGS TO EMAIL
4.SEND LOGS TO FTP

MINIMUM REQUIREMENTS
===================
Python 2.7: http://www.python.org/getit/
pyHook Module: http://sourceforge.net/projects/pyhook/
pyrhoncom Module: http://sourceforge.net/projects/pywin32/
pyHook Module -
Unofficial Windows Binaries for Python Extension Packages: http://www.lfd.uci.edu/~gohlke/pythonlibs/

NOTE: YOU ARE FREE TO COPY,MODIFY,REUSE THE SOURCE CODE FOR EDUCATIONAL PURPOSE ONLY.
'''
```

## 👨‍💻 Çok Satırlı Kod Yazma

Çok satırlı kod yazmak için `\` karakterini koyup ENTER'a basarak alt satırdan devam edebilirsin

```python
python 'train.py' \
      --train_dir="/{MODELIN_CIKTI_DIZINI_YOLU}" \
      --pipeline_config_path="/{YAPILANDIRMA_DOSYASI_YOLU}" \
      {'--logtostderr' if logdir else ''}

python 'train.py' --train_dir="/{MODELIN_CIKTI_DIZINI_YOLU}" --pipeline_config_path="/{YAPILANDIRMA_DOSYASI_YOLU}" {'--logtostderr' if logdir else ''}
```

{% hint style="success" %}
Üstteki iki komut birbirine eşdeğerdir
{% endhint %}

## 📜 Dokümantasyon PyDoc

* `'''` ile fonksiyonların üstüne dokümantasyon \(açıklama\) eklenir
* `#` ile koda yorum eklenir

```python
def func(a):
  """ 1 Değeri döndürür """
  return 1 # Döndürme keywordu
```

{% hint style="info" %}
Detaylar için [How To Use PyDoc To Document Python Code](https://www.youtube.com/watch?v=Y6TgbyfKCNM) videosuna bakabilirsin
{% endhint %}

## 📢 UTF-8 ve Script Bildirimleri

Her python scriptinin en üstüne alttaki metni \(**shebang**\) yazın

```bash
##!/usr/bin/python3
# -*- coding: utf-8 -*-
```

## 🧪 Python Terminalinde Kod Tamamlama

Pyreadline modülünü kurarak `pip install pyreadline` bu işlemi yapabilirsin.

### 🐞 AttributeError: module 'readline' has no attribute 'redisplay' Hatası

* 📋 Hata metninde en sonda verilen dosya yolunu kopyala 
  * Örnek dosya yolu: `...\Python\3.6.1\Lib\rlcompleter.py`
* Dosyayı herhangi bir metin düzenleyicisi ile aç 📑
  * VsCode kullanıyorsan alttaki komutu \(**kendi dosya yolunla**\) cmd'ye kopyalayabilirsin 👇 
  * `code ...\Python\3.6.1\Lib\rlcompleter.py`
* 👀 Açılan dosyada hata notunda yer alan `line 80`'e, yani 80. satıra bak 
* Oradaki satırları \(`79`'dan başlıyor\) alttaki gibi değiştirdikten sonra sorunsuz çalışacak 🚀

```python
...
if _readline_available:                     ## Eski kodlar ##
    if hasattr(readline, 'redisplay'):      # if _readline_available:
        readline.insert_text('\t')          #     readline.insert_text('\t')
        readline.redisplay()                #     readline.redisplay()
    return ''                               # return ''
...
```

{% hint style="warning" %}
Bu işlemden sonra python terminalini baştan açmayı unutma
{% endhint %}

