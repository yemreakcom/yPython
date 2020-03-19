---
description: Python ile alakalı hata çözümlerim
---

# 👨‍🔧 Hata Notları

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

{% embed url="https://stackoverflow.com/a/57834015/9770490" %}

