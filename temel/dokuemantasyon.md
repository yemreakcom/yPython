---
description: Python ile dokümantasyon oluşturma kuralları ve bilgileri
---

# 📑 Dokümantasyon

## 📜 Dokümantasyon PyDoc

* `'''` ile fonksiyonların üstüne dokümantasyon \(açıklama\) eklenir
* `#` ile koda yorum eklenir
* 🖨 Dokümantasyonlar [sphinx](https://www.sphinx-doc.org/en/master/) aracılığıyla dışarı aktarılabilir
* [📖 Getting started with sphinx](https://docs.readthedocs.io/en/latest/intro/getting-started-with-sphinx.html)

```python
def func(a):
  """ 1 Değeri döndürür """
  return 1 # Döndürme keywordu
```

{% hint style="info" %}
Detaylar için [How To Use PyDoc To Document Python Code](https://www.youtube.com/watch?v=Y6TgbyfKCNM) videosuna bakabilirsin
{% endhint %}

## 📃 Modül Dokümantasyon Örneği

```python
'''
Xenotix Python Keylogger for Windows
====================================
Coded By: Ajin Abraham <ajin25@gmail.com>
Website: http://opensecurity.in/xenotix-python-keylogger-for-windows/
GitHub: https://github.com/ajinabraham/Xenotix-Python-Keylogger

FEATURES
========
1.STORE LOGS LOCALLY
2.SEND LOGS TO GOOGLE FORMS
3.SEND LOGS TO EMAIL
4.SEND LOGS TO FTP

MINIMUM REQUIREMENTS
===================
Python 2.7: http://www.python.org/getit/
pyHook Module: http://sourceforge.net/projects/pyhook/
pyrhoncom Module: http://sourceforge.net/projects/pywin32/
pyHook Module -
Unofficial Windows Binaries for Python Extension Packages: http://www.lfd.uci.edu/~gohlke/pythonlibs/

NOTE: YOU ARE FREE TO COPY,MODIFY,REUSE THE SOURCE CODE FOR EDUCATIONAL PURPOSE ONLY.
'''
```

