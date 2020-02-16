---
description: Yol (path) işlemleri
---

# 🚩 Yol İşlemleri \| Dosya

## 💡 Önemli Hususlar

Yol işlemleri için `os.path` modülü kullanılır.

* İşletim sistemlerindeki farklılıkları engellemek için `os.path.normpath` metodunu kullan
* Yolları birleştirmek için `\` veya `/` **kullanma**, işletim sistemlerine göre değişen `os.path.join` metodunu kullan
* Yolun doğruluğu `os.path.exists` ile kontrol etmeden işlem yapma

{% hint style="success" %}
[Pathlib](https://treyhunner.com/2018/12/why-you-should-be-using-pathlib/)'in daha iyi olduğu söylenmekte
{% endhint %}

## 🌟 Sık Kullanılan Metodlar

> Metodların kulalnımı `os.path.<metod>` şeklindedir

| Metod | Açıklama |
| :--- | :--- |
| `exists(<yol>)` | Yolun doğruluğu kontrol etme |
| `isfile(<yol>)` | Dosya mı kontrolü |
| `isdir(<yol>)` | Dizin mi kontrolü |
| `join(<yol1>, <dosya_adı>)` | Yolları birleştirme |
| `normpath<yol>` | Yoldaki fazladan `\` `/` gibi karakterleri kaldırma |
| `basename(<yol>)` | Dosyanın adını ve uzantısını bulma |
| `splitext(<dosya_adı>)` | Dosyanın yolunu ve uzantısını döndürür \(path, ext\) |

* `<yol>` Path, dosya yolu
  * _Örn: C:\Users\Username\help.txt_
* `<dosya_adı>` Dosyanın uzantısıyla birlikteki adı
  * _Örn: help.txt_

## ‍👀 Dizin veya Dosya Yolunu Bulma

{% tabs %}
{% tab title="👁‍🗨 Dosyanın Gerçek Yolu" %}
```python
filepath = os.path.realpath(__file__)
```
{% endtab %}

{% tab title="📜 Script Dosyasının Dizini" %}
```python
import os
dir_path = os.path.dirname(os.path.realpath(__file__))
```
{% endtab %}

{% tab title="📂 Çalışma Dizini" %}
```python
import os
cwd = os.getcwd()
```
{% endtab %}
{% endtabs %}

