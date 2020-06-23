---
description: Python Flask ile web için microservice yazılımı
---

# 🌶️ Flask

## 👀 Hızlı Bakış

* 🐍 Python dili kullanan back-end microframework'tür
* 🕊️ Hafif yapısı ile gibi ufak yapıdaki projeler için tercih edilir
* 🤝 Jinja2 kalıplarını, secure cookies, unit testing ve RESTful istek yönetimlerini destekler
* 💁‍♂️ Django gibi framework'ler tarafından sunulan istenmeyen modüllerden kurtulmak isteyenler için birebirdir

## 💖 Avantajları

* 🧩 Esnek bir yapı olduğundan dolayı, geliştirilebilir
* 🕊️ Django ile karşılaştırıldığında daha hafif bir yapıda olduğundan ufak projeler için idealdir
* 🗃️ ORM yapısı olmadığından dolayı veri tabanı bağlaması oldukça kolaydır \(SQLAlchemy ile yapı kurulabilir\)
* 📖 Dokümantasyonu ve kaynakları oldukça iyidir
* 🏗️ Hızlıca prototip oluşturma imkanı sağlar

## 💔 Dezavantajları

* 🎳 Büyük çaplı projeler için uygun değildir \(django tercih edilmeli\)
* 👪 Topluluğu yetersizdir
* 👨‍💻 Full-stack programlama bilgisi gerektirir
* 🤵 Admin sayfası ve kimlik doğrulama gibi işlemler yoktur
* 🗃️ ORM \(object relational mapping\) yapısı yoktur \(SQLAlchemy ile yapı kurulabilir\)
* 🚛 Veri tabanını aktarma işlemi zordur, `flask-migrate` kütüphanesinin indirilmesi gerekir

### ⭐ Nerelerde Kullanılmalı

* 🕊️ Ufak çaplı, hafif projelerde ya da IoT cihazlarda
* 🎯 Proje odaklı hızlı ilerleyecek çalışmalarda
* 🏗️ Prototip oluşturma işlemlerinde

## 👨‍💻 Kod Örneği

```python
from flask import Flask 

app = Flask(__name__) 

@app.route("/") 
def hello():
     return "Hello World!"  

if __name__ == "__main__":
     app.run()
```

## 🔗 Faydalı Bağlantılar

* [👪 Python \(programming language\): What are the cons and pros of Django and Flask? What are some of the best sources to learn these Python frameworks?](https://www.quora.com/Python-programming-language-What-are-the-cons-and-pros-of-Django-and-Flask-What-are-some-of-the-best-sources-to-learn-these-Python-frameworks)
* [👨‍💻 Flask ~ GitHub](https://github.com/pallets/flask)
* [📃 Flask vs Django: How to Choose the Right Web Framework for Your Web App](https://blog.resellerclub.com/flask-vs-django-how-to-choose-the-right-web-framework-for-your-web-app/)
* [📃 Best back-end frameworks](https://www.keycdn.com/blog/best-backend-frameworks)
* [📃 Disadvantages of Flask](https://medium.com/@allwindicaprio/disadvantages-of-flask-33dd8b8726ab)

