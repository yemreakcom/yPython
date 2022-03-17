---
description: Python'a hoş geldin, kuralları ve gelenekleri tanıyalım
---

# 🙋‍♂️ Hoş Geldin

## 🚧 Python ile Programlamaya Hazırlanma

Python ve JavaScript en popüler diller arasındadır.

* Python kodlarının uzantıları `.py` şeklindedir.
* Windows için `.pyw` uzantılı python dosyaları `start` (veya `pythonw`) komutu ile çalıştırılabilmekte
* Python komutunu ve pip ile indirdiklerinizi terminal üzerinden görebilmek için aşağıdakileri ortam değişkenlerine kaydetmeniz gerekmekte
  * `python.exe`'nin yolunu
  * `pip` ile indirilen terminal üzerinden derlenebilir komutlar için de _Scripts_ yolunu
  * `pip install` komutu ile indirilen script'ler scripts dizinine gider
  * `pip3 freeze --local | xargs pip3 uninstall -y` komutu ile tüm pip ile kurulanları silebilirsin
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
* Girintiler (`\t` karakteri) `{}` işlevi görür
* `:` karakteri ile yeni bir scope (alt alan) açılır
  * `for`, `def` gibi döngü veya metot işlemlerinde kullanırlar
* Metotlar arasında 2 satır bırakılır
* Metotların en son satırları boş olmalıdır (return için)
* Kodun en son satırı boş olmalıdır (End of File)
* _Private_ metotlar `_` ile başlar
  * `_add`, `_is_ prime`
* Özel metotlar _"dunder"_ `__` ile başlar ve biter
  * `__init__`, `__add__`

{% hint style="info" %}
Daha fazla bilgi için harici bağlantılardaki [Should I use underscores or camel case for Python?](https://www.quora.com/Should-I-use-underscores-or-camel-case-for-Python) bağlantısına tıklayabilirsin.
{% endhint %}

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

## 📢 UTF-8 ve Script Bildirimleri

Her python scriptinin en üstüne alttaki metni (**shebang**) yazın

```bash
##!/usr/bin/python3
# -*- coding: utf-8 -*-
```
