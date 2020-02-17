# 🏗️ Decorator

## 👀 Hızlı Bakış

* 🍱 Metotları başka bir metotları tetikleyerek kullanmayı sağlar
* 💠 Fonksiyonların üstlerinde kullanılır
* 🏷️ Etiketleme \(annotations\) olarak da bilinir

```python
def background(func):

    def inner(*args, **kwargs):
        threading.Thread(target=func, args=args, kwargs=kwargs).start()

    return inner

@background
def test(val1, val2):
    for i in range(val1, val2):
        print(i)


if __name__ == "__main__":
    test(10, 20)
    test(20, 30)

# 10 20 21 22 23 24 25 26 27 28 11 12 13 29 14 15 16 17 18 19
```

## 💎 Parameter ile Kullanım

```python
def delayed(duration):
    def background(func):

        def inner(*args, **kwargs):
            threading.Timer(duration, func, args, kwargs).start()

        return inner
    return background


@delayed(1)
def test(val1, val2):
    for i in range(val1, val2):
        print(i)


if __name__ == "__main__":
    test(10, 20)
    test(20, 30)
    
# 10 11 12 13 14 20 21 22 15 16 17 18 19 23 24 25 26 27 28 29
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [👨‍💻 Decorators with Parameters](https://stackoverflow.com/a/25827070/9770490) alanına bakabilirsin.
{% endhint %}

## 🔗 Faydalı Bağlantılar

* [👨‍💻 Decorators with Parameters](https://stackoverflow.com/a/25827070/9770490)

