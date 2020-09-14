---
description: Python ile alakalı hata çözümlerim
---

# 👨‍🔧 Hata Çözümleri

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

## 🧰 Pip error: Microsoft Visual C++ 14.0 is required

* Eğer aşağıdaki gibi bir hata mesajı alıyorsanız
*  [Visual C++ 2015 Build Tools](http://go.microsoft.com/fwlink/?LinkId=691126&fixForIE=.exe.) bağlantısından Microsoft Visual C++ 14.0'ı Visual Studio indirmeden kurabilirsiniz
* Ardından yüklemek istediğiniz paketi `pip install -U <paket_adi>` şeklinde baştan yükleyin
  * `-U` bayrağı,  `--upgrade` anlamına gelmektedir

```python
error: Microsoft Visual C++ 14.0 is required. Get it with "Microsoft Visual
C++ Build Tools": http://landinghub.visualstudio.com/visual-cpp-build-tools
```

{% hint style="warning" %}
😩 Her ne kadar Visual Studio kurulmadan kurulsa da, dosya boyutu hala çok yüksektir
{% endhint %}

