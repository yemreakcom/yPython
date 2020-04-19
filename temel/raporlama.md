---
description: Python ile raporlama (logging) işlemleri ve logging modülünün kullanımı
---

# 📜 Raporlama İşlemleri

## 🏂 Raporlamaya Giriş

* 📦 Raporlama işlemleri için `logging` modülü kullanır
* 🍱 Python içerisinde hazır olarak bulunan bir modüldür, indirmeye gerek yok
* 📜 `logging` modülü print yapısından daha kullanışlıdır
* 👨‍💼 Raporlama seviyeleri ile isteğe bağlı çıktılar verilir
* 🙄 `print` metodu olsaydı if koşulları ile yapmamız gerekirdi

## 🏗️ Oluşturma İşlemleri

* 🔨 Yapılandırma ayarları `logging.basicConfig` metodu ile düzenlenir
* 💎 `format` ile çıktıların yapısı, `level` ile çıktıların sınırı belirlenir
* 🚀 `logging.getLogger` metodu `__name__` ile kullanıldığında, dosya ismine ait bir raporlayıcı oluşturur
* 👨‍💼 Oluşturulan yeni raporlayıcılar `setLogger` metodu ile sınırlandırılabilir
* 💁‍♂️ Bu sınırlandırmalar diğer raporlayıcıları etkilemez

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

# Tüm raporlayıcıları tanımlama
logging.basicConfig(format=log_format , level=log_level)

logger = logging.getLogger(__name__)

# Belirli bir raporlayıcı sınırlama
logger.setLevel(logging.ERROR) 
```

{% hint style="warning" %}
📢 `logging` modülü globaldir, her dosya için ortak log yapısı kullanılır
{% endhint %}

## 🎌 Temel Kullanım

Raporlayıcı objenizin debug, info, warn, error, exception, fatal metotları ile raporlama yapabilirsiniz

* 👮‍♂️ Her metot karşılığı olan raporlama seviyesine göre raporlama yapar

| 💎 Metot | 📝 Açıklama |
| :--- | :--- |
| fatal | CRITICAL seviyesinde raporlama |
| exception | ERROR seviyesinde **hata mesajı ile** raporlama |
| error | ERROR seviyesinde raporlama |
| warn | WARN seviyesinde raporlama |
| info | INFO seviyesinde raporlama |
| debug | DEBUG seviyesinde raporlama |

## 👮‍♂️ Raporlama Seviyeleri

Raporlama seviyeli yukarıdan aşağıya doğru daha da sınırlı hale gelir.

* `DEBUG` işlemi `ERROR` çıktılarını da raporlar
* `ERROR` çıktıları kendinden daha düşük çıktıları raporlarmaz

| ⭐ Seviye | 📝 Açıklama |
| :--- | :--- |
| CRITICAL \(50\) | Exception veya en yüksek seviyeli durumları raporlayan seviyedir |
| ERROR \(40\) | Hata durumunda kullanılan raporlama seviyesidir |
| WARNING \(30\) | Uyarılar amaçlı kullanılan raporlama seviyesidir |
| INFO \(20\) | Ön planda çalışan işlemleri kontrol etmek için kullanılır. Dosya güncelleme, sunucuya bağlanma işlemleri raporlarmak için kullanılır |
| DEBUG \(10\) | Arkaplanda yapılan işlemleri kontrol etmek için kullanılır, objeleri oluşturma güncelleme gibi çıktılarınızı bunun ile raporlayabilirinisiz |
| NOTSET \(0\) | 🤷‍♂️ |

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

## 👨‍🎨 Detaylı Renkli Raporlama

* 🧐 Detaylarla ilgilenenler için `colorlog` modülü önerilir
* 🖌 Metinleri  `%(log_color)` ve `%(reset)s` değişkenleri arasına alarak renklendirebilirsin
* 🙄 İşlemin çalışması için `colorlog.ColorFormatter` objesini `logger` objesine alttaki gibi eklemen lazım

```python
import logging
LOG_LEVEL = logging.DEBUG
LOGFORMAT = (
    " %(log_color)s%(levelname)-8s%(reset)s |"
    " %(log_color)s%(message)s%(reset)s")
from colorlog import ColoredFormatter
logging.root.setLevel(LOG_LEVEL)
formatter = ColoredFormatter(LOGFORMAT)
stream = logging.StreamHandler()
stream.setLevel(LOG_LEVEL)
stream.setFormatter(formatter)
log = logging.getLogger('pythonConfig')
log.setLevel(LOG_LEVEL)
log.addHandler(stream)

log.debug("A quirky message only developers care about")
log.info("Curious users might want to know this")
log.warn("Something is wrong and any user should be informed")
log.error("Serious stuff, this is red for a reason")
log.critical("OH NO everything is on fire")
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [How can I color Python logging output?](https://stackoverflow.com/a/23964880/9770490)  alanına bakabilirsin.
{% endhint %}

## 🎨 Renkli Raporlama

* 📦 Renkli raporlama için `coloredlogs` modülü kullanılır
* ⏬ Yüklemek için `pip install coloredlogs` komutunu kullanın
* 💡 Renklendirme için standart konsol renk komutlarını kullanır
* 👨‍🔧 Renklendirme çalışmazsa`colorama` modülünü yükleyin
* ⏬ Yüklemek için `pip install colorama` komutunu kullanın

> 💁‍♂️ Alternatif olarak, en kolay kullanımı sağlayan [`zenglog`](https://github.com/ManufacturaInd/python-zenlog) modülüne bakmanda fayda var

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
‍🧙‍♂ Detaylı bilgi için [`coloredlogs`](https://coloredlogs.readthedocs.io/en/latest/readme.html) alanına bakabilirsin.
{% endhint %}

## 🔨 Yapılandırma Dosyası

```javascript
{
    "version": 1,
    "disable_existing_loggers": false,
    "formatters": {
        "simple": {
            "class": "colorlog.ColoredFormatter",
            "format": "%(asctime)s %(log_color)s%(message)s%(reset)s",
            "datefmt": "%H:%M:%S"
        },
        "detailed": {
            "class": "logging.Formatter",
            "format": "%(asctime)s.%(msecs)03d [%(threadName)s] %(levelname)-7s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S"
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "INFO",
            "formatter": "simple",
            "stream": "ext://sys.stdout"
        },
        "debug_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "DEBUG",
            "formatter": "detailed",
            "filename": "log/debug/{filename}.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "mode": "w",
            "encoding": "utf8"
        },
        "info_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "INFO",
            "formatter": "detailed",
            "filename": "log/info/{filename}.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "mode": "w",
            "encoding": "utf8"
        },
        "warn_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "WARNING",
            "formatter": "detailed",
            "filename": "log/warning/{filename}.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "mode": "w",
            "encoding": "utf8"
        },
        "error_file_handler": {
            "class": "logging.handlers.RotatingFileHandler",
            "level": "ERROR",
            "formatter": "detailed",
            "filename": "log/error/{filename}.log",
            "maxBytes": 10485760,
            "backupCount": 20,
            "mode": "w",
            "encoding": "utf8"
        }
    },
    "loggers": {
        "urllib3.connectionpool": {
            "level": "ERROR",
            "handlers": [
                "console"
            ],
            "propagate": false
        }
    },
    "root": {
        "level": "DEBUG",
        "handlers": [
            "console",
            "debug_file_handler",
            "info_file_handler",
            "warn_file_handler",
            "error_file_handler"
        ]
    }
}
```

## 🔗 Faydalı Bağlantılar

* [📖 Logging HowTo](https://docs.python.org/3/howto/logging.html)
* [📖 Logging facility for Python](https://docs.python.org/3/library/logging.html)
* [📖 coloredlogs: Colored terminal output for Python’s logging module](https://coloredlogs.readthedocs.io/en/latest/readme.html)
* [📖 Format of log message ~ coloredlogs](https://coloredlogs.readthedocs.io/en/latest/readme.html#format-of-log-messages)

{% hint style="success" %}
🚀 Bu alandaki bağlantılar [YEmoji ~Bağlantılar](https://emoji.yemreak.com/kullanim/baglantilar) yapısına uygundur
{% endhint %}

