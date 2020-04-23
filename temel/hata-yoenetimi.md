---
description: 'Exception handling, try except (try / catch) yapısı'
---

# 🐛 Hata Yönetimi

## 🧱 Temel Yapı

Olası hatalarda programın kapanmasını engelleyerek hata kontrolü sağlar.

```python
try:
    a = float("Ben sayı değilim")
except ValueError as err:
    print("Bu sayı değil", err)
```

## 💞 Birden Fazla Hata Türü Yakalama

```python
except (IDontLikeYouException, YouAreBeingMeanException) as e:
    pass
```

## 📜 Hatayı Raporlama

* 📃 Hataları raporlamak için `logging.exception` metodu kullanılır
* 💁‍♂️ Detaylı bilgi için [📜 Raporlama İşlemleri](raporlama.md) yazısına bakınız

