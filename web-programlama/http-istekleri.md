---
description: 'Python ile HTTP istekleri, get, push request'
---

# 💌 HTTP İstekleri

## 🔸 HTTP Durum Kodları

* 🚦 HTTP durum kodları **status code** olarak adlandırılır
* 💡 Sunucunun durumu hakkında bilgi verir
  * 👍 20\* başarılı
  * 🔗 30\* sayfa yönlendirmesi
  * 🚫 40\* bulunamadı
  * 🐞 50\* sunucu hataları

```python
import requests

# İlk URL'in durum kodunu alma
status_code = requests.head(url).status_code

# Son URL'in durum kodunu alma
status_code = requests.head(url, allow_redirects=True).status_code

print(status_code)
```

## 🔗 Faydalı Bağlantılar

* [Python Requests library redirect new url](https://stackoverflow.com/questions/20475552/python-requests-library-redirect-new-url)

