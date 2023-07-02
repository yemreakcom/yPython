---
description: >-
  Bu blog yazısında, Python ile bir fonksiyonun süresini ve çağırıldığı yeri
  nasıl raporlayacağımızı anlatacağım. Örnekte self içeren bir fonksiyonu ve
  logger objesini kullanacağız.
---

# 🧾 Fonksiyon Süresini ve Çağırıldığı Yeri Dekoratör ile Raporlama

```python
# 📦 İhtiyaç duyulan paketlerin yüklenmesi
from functools import wraps
from time import time
from traceback import extract_stack
from typing import Any
```

📚 Yukarıdaki paketler Python'ın standard kütüphanesinden geliyor.

* `functools` modülünün `wraps` fonksiyonu, dekoratörlerde kullanılır ve orijinal fonksiyonun adını, docstring'ini vb. korur.
* `time` modülünün `time` fonksiyonu, çağrıldığı anın zamanını verir.
* `traceback` modülünün `extract_stack` fonksiyonu, fonksiyon çağrılarının izini çıkarır.
* `typing` modülünün `Any` türü, herhangi bir türü temsil eder ve dinamik tiplendirme esnekliği sağlar.

```python
# 👷 Dekoratör fonksiyonunun tanımlanması
async def self_logging(func):
```

🛠️ `self_logging` adında bir dekoratör fonksiyon tanımlıyoruz. Bu dekoratör, hedef fonksiyonu parametre olarak alır.

```python
    # 🎁 Orijinal fonksiyonun özelliklerini koruma
    @wraps(func)
```

📦 `wraps` fonksiyonu dekoratörlere eklenir ve hedef fonksiyonun meta verilerini (örneğin: ismi, docstring'i) korur.

```python
    # 🧤 Dekoratörün gerçekleştirdiği işlemleri tanımlama
    async def wrapper(*args: Any, **kwargs: Any):
```

🧩 `wrapper` adında bir iç fonksiyon tanımlıyoruz. Bu fonksiyon, hedef fonksiyonun parametrelerini dinamik bir şekilde kabul edebilir.

```python
        # ⏱️ İşlem başlamadan önceki zamanı kaydetme
        begin = time()
```

⌚ İşlemin başlangıç zamanını kaydediyoruz. Bunu daha sonra işlemin ne kadar sürdüğünü hesaplamak için kullanacağız.

```python
        # 🖨️ Hedef fonksiyonun çağrıldığı yer ve parametrelerin loglanması
        args[0].logger(
            "debug",
            f"Calling {func.__name__} from {extract_stack()[-2].name}",
            (f"Args: {args}", f"Kwargs: {kwargs}"),
        )
```

📜 `logger` objesini kullanarak hedef fonksiyonun çağrıldığı y

eri ve kullanılan parametreleri logluyoruz. Burada `extract_stack()[-2].name` ifadesi ile fonksiyonun çağrıldığı yerin ismini alıyoruz.

```python
        # 🏁 Hedef fonksiyonun çalıştırılması ve sonucunun kaydedilmesi
        result = await func(*args, **kwargs)
```

🎯 Hedef fonksiyonu çağırıyoruz ve dönen sonucu `result` değişkeninde saklıyoruz.

```python
        # 🖨️ Hedef fonksiyonun ne kadar sürede tamamlandığının ve parametrelerin loglanması
        args[0].logger(
            "debug",
            f"Done {func.__name__} in {time() - begin} seconds",
            (f"Args: {args}", f"Kwargs: {kwargs}"),
        )
```

⏲️ İşlemin tamamlanma süresini hesaplayıp logluyoruz. Hesaplamak için başlangıç zamanını şimdiki zamandan çıkarıyoruz.

```python
        # 📤 Hedef fonksiyonun sonucunun dönülmesi
        return result
```

🔄 Hedef fonksiyonun sonucunu dönüyoruz. Dekoratör, hedef fonksiyonun sonucunu etkilememeli.

```python
    # 🎁 Dekoratör fonksiyonun sonucunun dönülmesi
    return wrapper
```

🎁 `self_logging` fonksiyonu olarak `wrapper` fonksiyonunu dönüyoruz. Böylece dekoratör, hedef fonksiyon yerine `wrapper` fonksiyonunu çağıracak.

Bu kod örneği, Python'daki dekoratörlerin, asenkron işlemlerin ve loglamanın nasıl kullanılabileceğini gösterir. Aynı zamanda fonksiyonun çağrıldığı yerin izini sürme ve geçen zamanı ölçme yeteneği de sağlar. Bu yetenekler, özellikle büyük ve karmaşık yazılım projelerinde çok değerlidir. Bu tür projelerde hataların nereden kaynaklandığını belirlemek ve performans darboğazlarını tespit etmek için bu tür bilgiler hayati öneme sahiptir.
