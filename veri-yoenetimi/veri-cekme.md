---
description: "Verilerin yuvası \U0001F492 olan internet'ten verinin nasıl çekileceği"
---

# 🧲 İnternet'ten Veri Çekme

## 🔰 Veri Çekmeye Giriş

Web siteleri üzerindeki tabloları çekmek için `pd.read_html` kullanılır

## 🧱 Verilerin Sağlaması Gereken Özellikler

Günlük hayatta veriler istediğimiz kadar basit olmaz, bunlar üzerinde işlemler yaparak uygun hale getiririz

* Tek tablodan oluşan basit veya bağlantılı bir kaç tablodan oluşan
  * Farklı veriler için _mapping_ ile veri tipleri birbirine benzetilir
* Kolay analiz edilebilir formatta olan
* Makine öğrenimine sokulabilecek veriler
* Düşük karmaşıklığa sahip
* Yüksek boyutlu veriler için optimizasyon

## 💨 Hızlıca URL'den Veri Alma

Veri almanın en hızlı ve basit yolu

```python
import urllib.request
contents = urllib.request.urlopen("http://example.com/foo/bar").read()

# Encoding işlemi için (https://stackoverflow.com/a/17615424/9770490)
encoding = "utf-8"
contents = contents.decode(encoding)
```

## 🆔 Veri Çekme Sorunları Engellemek için `UserAgent` Ayarlama

Bazı web siteleri, isteklerin nereden geldiğini bilmeden hareket edemezler. Bu sebeple isteği detaylandırmamız gerekmektedir.

> `HTML` alanına bağlantıyı yazın, `pd.read_html(html)` şeklinde kullanın

```python
from urllib.request import urlopen, Request

HTML = "" # Örn: https://en.wikipedia.org/

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
reg_url = HTML
req = Request(url=reg_url, headers=headers) 
html = urlopen(req).read() # Pandas için kullanılacak html objesi
```

> ["\[Python\]\[Crawler\]“HTTP Error 403: Forbidden”](https://medium.com/@speedforcerun/python-crawler-http-error-403-forbidden-1623ae9ba0f)

## 🌍 Internet'ten Tablo Çekme Örneği

Tüm tablo verileri arasında `0`, `1` ... değerleri ile gezinebiliriz.

```python
import pandas as pd
import json
df = pd.read_html('https://en.wikipedia.org/w/index.php?title=Fortune_Global_500&oldid=855890446', header=0)[1]
fortune_500 = json.loads(df.to_json(orient="records"))
df
```

![](../.gitbook/assets/image%20%285%29.png)

```python
df_list = pd.read_html("https://en.wikipedia.org/w/index.php?title=Automotive_industry&oldid=875776152", header=0)
car_totals = json.loads(df_list[1].to_json(orient="records"))
car_by_man = json.loads(df_list[3].to_json(orient='records'))
```

![](../.gitbook/assets/image%20%281%29.png)

