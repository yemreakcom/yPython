---
description: Python üzerinde paraleli eş zamanlı ve çok çekirdekli işlemler
---

# 🎎 Multiprocessing

## 🆚 Multiprocessing vs Multithreading

* 🕐 Thread eski bir yapıdır
* 👮‍♂️ Thread işlemlerinde aynı alana erişim sırasında verilerde sorun olabilir
  * Func1 ile Fun2 A dosyasına erişsin
  * Func1 A'dan 5 değerini çeker
  * Func2 de A'dan 5 değerini çeker \(çünkü func1 A dosyasını erişime kapatmaz\)
  * Func1 değeri 1 artırır, A'ya 6 yazar
  * Func2 de değeri 1 artırır, A'ya 6 yazar
  * Sonuç olarak A değerinin 7 olması beklenirken, 6 olduğu görülür
  * 👨‍🔧 Çözüm: `Multiprocessing`
* 🎳 Multiprocessing, threading'e nazaran daha maliyetlidir, basit işlerde tercih edilmez \([overhead](http://bilgisayarkavramlari.sadievrenseker.com/2011/01/03/overhead-ek-yuk/)\)
* 📈 IO işlemleri için 🧵 Multi-Threading, CPU işlemleri için 🎎 Multi-Processing daha verimlidir
* 💡 Multiprocessing IO işlemleri için de hızlı olsa da maliyetli olduğundan thread daha uygun seçimdir

> 🔸 Multithreading, **çoklu kullanım** anlamına gelirken; multiprocessing, **çoklu işleme** anlamına gelmektedir

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için kaynaklar:

* [Multiprocessing vs. Threading in Python](https://timber.io/blog/multiprocessing-vs-multithreading-in-python-what-you-need-to-know/)
* [The Why, When, and How of Using Python Multi-threading and Multi-Processing](https://medium.com/towards-artificial-intelligence/the-why-when-and-how-of-using-python-multi-threading-and-multi-processing-afd1b8a8ecca)
{% endhint %}

## ⭐ Multiprocessing Örneği

```python
from multiprocessing import Process


def func1():
    print('func1: starting')
    for i in range(10000000):
        pass
    print('func1: finishing')


def func2():
    print ('func2: starting')
    for i in range(10000000):
        pass
    print ('func2: finishing')


if __name__ == '__main__':
    p1 = Process(target=func1)
    p1.start()
    p2 = Process(target=func2)
    p2.start()
    p1.join() # Process1'in tamamlanmasını beklemek için kullanılır
    p2.join()

# func1: starting
# func2: starting
# func2: finishing
# func1: finishing
```

## 🔗 Faydalı Kaynaklar

* [Multiprocessing basic](https://pymotw.com/2/multiprocessing/basics.html)

