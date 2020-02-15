---
description: Python ile raporlama (logging) işlemleri ve logging modülünün kullanımı
---

# 📜 Raporlama İşlemleri

## 🏂 Raporlamaya Giriş

* 📦 Raporlama işlemleri için `logging` modülü kullanır
* 🍱 Python içerisinde hazır olarak bulunan bir modüldür, indirmeye gerek yok
* 📜 `logging` modülü print yapısından daha kullanışlıdır
* 👮‍♂️ Raporlama seviyeleri ile isteğe bağlı çıktılar verilir
* 🙄 `print` metodu olsaydı if koşulları ile yapmamız gerekirdi

## 🎌 Temel Kullanım

* 🔨 Yapılandırma ayarları `logging.basicConfig` metodu ile düzenlenir
* 💎 `format` ile çıktıların yapısı, `level` ile çıktıların sınırı belirlenir
* 🚀 `logging.getLogger` metodu `__name__` ile kullanıldığında, dosya ismine ait bir raporlayıcı oluşturur

```python
import logging

logformat = r"%(levelname)s:%(filename)s %(message)s"
loglevel = logging.DEBUG

logging.basicConfig(format=logformat, level=loglevel)

logger = logging.getLogger(__name__)
```

{% hint style="warning" %}
📢 `logging` modülü globaldir, her dosya için ortak login yapısı kullanılır
{% endhint %}

## 🔗 Faydalı Bağlantılar

* [📖 Logging HowTo](https://docs.python.org/3/howto/logging.html)
* [📖 Logging facility for Python](https://docs.python.org/3/library/logging.html)

{% hint style="success" %}
🚀 Bu alandaki bağlantılar [YEmoji ~Bağlantılar](https://emoji.yemreak.com/kullanim/baglantilar) yapısına uygundur
{% endhint %}

