# 🕐 Zaman İşlemleri

## ⏱ Zaman İşlemleri \(Time, Datetime\)

```python
import time
from datetime import datetime

time.time() # Anlık süreyi saniye cinsinden verir
datetime.utcnow() # UTC formatında tarihi verir
datetime.now() # Yerel formatta tarihi verir (Türkiye)
datetime.datetime.now().time() # Yerel formatta saati verir (Türkiye)

# Formatlı zaman bilgisi 26-Jun-2019-16:00:07
datetime.now().strftime('%d-%b-%Y-%H:%M:%S') 
```

## ➖ Zaman Farkı Hesaplama

```python
a = datetime.datetime.now() # datetime.datetime(2013, 8, 25, 2, 5, 1, 879000)
b = datetime.datetime.now() # datetime.datetime(2013, 8, 25, 2, 5, 8, 984000)

a - b # datetime.timedelta(-1, 86392, 895000)
b - a # datetime.timedelta(0, 7, 105000)

(b - a).microseconds # 105000
(b - a).seconds # 7
(b - a).microseconds / 1000 # 105
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Python - time difference in milliseconds not working for me](https://stackoverflow.com/questions/18426882/python-time-difference-in-milliseconds-not-working-for-me) alanına bakabilirsin.
{% endhint %}

## ⭐ Fark Metotlarım

```python
def get_time_remain(time: datetime.time) -> datetime.timedelta:
	"""Yerel saat ile verilen time arasındaki farkı bulma

	Arguments:
		time {time} -- Saat bilgisi

	Returns:
		timedelta -- Zaman farkı
	"""
	return time - datetime.strptime(str(datetime.now().time()), FORMAT_TIME)


def is_before(time: datetime.time) -> bool:
	"""Verilen süre geçildi mi

	Arguments:
		time {dtime} -- Saat bilgisi

	Returns:
		bool -- Geçildiyse evet
	"""
	return get_time_remain(time).days < 0
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [How to get the difference between two 24 hour times?](https://stackoverflow.com/questions/39787787/how-to-get-the-difference-between-two-24-hour-times) alanına bakabilirsin.
{% endhint %}

## 🙇‍ Program Kapandığında İşlem Yapma \(on Exit\)

```python
import atexit

def exit_handler():
    print 'My application is ending!'

atexit.register(exit_handler)
```

> [Doing something before program exit](https://stackoverflow.com/a/3850271/9770490)

