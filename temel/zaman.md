# 🕐 Zaman İşlemleri

## ⏱ Zaman İşlemleri \(Time, Datetime\)

```python
import time
from datetime import datetime

time.time() # Anlık süreyi saniye cinsinden verir
datetime.utcnow() # UTC formatında tarihi verir
datetime.now() # Yerel formatta tarihi verir (Türkiye)
datetime.now().strftime('%d-%b-%Y-%H:%M:%S') # Formatlı zaman bilgisi 26-Jun-2019-16:00:07
```

## 🙇‍ Program Kapandığında İşlem Yapma \(on Exit\)

```python
import atexit

def exit_handler():
    print 'My application is ending!'

atexit.register(exit_handler)
```

> [Doing something before program exit](https://stackoverflow.com/a/3850271/9770490)

