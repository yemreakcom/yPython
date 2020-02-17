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

log_format = (
        '%(asctime)s - '
        '%(name)s - '
        '%(funcName)s - '
        '%(levelname)s - '
        '%(message)s'
)
log_level = logging.DEBUG

logging.basicConfig(format=log_format , level=log_level )

logger = logging.getLogger(__name__)
```

{% hint style="warning" %}
📢 `logging` modülü globaldir, her dosya için ortak login yapısı kullanılır
{% endhint %}

## 📂 Dosyaya Raporlama

```python
import logging

message = "Raporlanacak"
LOG_DIR = "dosya/dizini"
LOG_FILE = "dosya.log"
FLAG = "w" # a+, r
ENCODING = "utf-8"

# Rapolamayı tanımlama
logging.basicConfig(
    handlers=[logging.FileHandler(LOG_DIR + LOG_FILE, FLAG, ENCODING)], 
    level=logging.DEBUG,
    format='%(asctime)s: %(message)s'
)

logging.info("mesaj") # Raporu yazma
```

## 🎨 Renkli Raporlama

* 📦 Renkli raporlama için `coloredlogs` modülü kullanılır
* ⏬ Yüklemek için `pip install coloredlogs` komutunu kullanın
* 💡 Renklendirme için standart konsol renk komutlarını kullanır
* 👨‍🔧 Renklendirme çalışmazsa`colorama` modülünü yükleyin
* ⏬ Yüklemek için `pip install colorama` komutunu kullanın3

```python
import coloredlogs
import logging

# Logger objesi oluşturma
logger = logging.getLogger(__name__)

# Tüm raporlama işlemlerinin renkli olmasını sağlar
coloredlogs.install(level='DEBUG')

# Sadece verilen logger'ın renkli olmasını sağlar
coloredlogs.install(level='DEBUG', logger=logger)

# Formatı değiştirme
log_format = ""
    + "%(asctime)s,%(msecs)03d %(hostname)s %(name)s[%(process)d] "
    + "%(levelname)s %(message)s"
coloredlogs.install(level='DEBUG', fmt=log_format)

# Örnekler
logger.debug("this is a debugging message")
logger.info("this is an informational message")
logger.warning("this is a warning message")
logger.error("this is an error message")
logger.critical("this is a critical message")

```

![](../.gitbook/assets/coloredlogs_example.png)

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [coloredlogs](https://coloredlogs.readthedocs.io/en/latest/readme.html) alanına bakabilirsin.
{% endhint %}

## 🔗 Faydalı Bağlantılar

* [📖 Logging HowTo](https://docs.python.org/3/howto/logging.html)
* [📖 Logging facility for Python](https://docs.python.org/3/library/logging.html)
* [📖 coloredlogs: Colored terminal output for Python’s logging module](https://coloredlogs.readthedocs.io/en/latest/readme.html)
* [📖 Format of log message ~ coloredlogs](https://coloredlogs.readthedocs.io/en/latest/readme.html#format-of-log-messages)

{% hint style="success" %}
🚀 Bu alandaki bağlantılar [YEmoji ~Bağlantılar](https://emoji.yemreak.com/kullanim/baglantilar) yapısına uygundur
{% endhint %}

