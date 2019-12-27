# ⏳ Counter

## 🔰 Counter Yapısını Tanıyalım 

* 💕`list` objelerini sayar `dict` yapısında Anahtar-Miktar ikilisi döndürür. 
* 🚫 Olmayan anahtarlar için `0` değeri döndürülür

## ⭐ Örnek Kod

```python
from collections import Counter
ele = ['a','b','a','c','b','b','d']
c = Counter(ele)

# Counter({'b': 3, 'a': 2, 'c': 1, 'd': 1})

c['a'], c['z'] # (2, 0)
c.most_common(5) # [('b', 3), ('a', 2), ('c', 1), ('d', 1)]
```

{% hint style="info" %}
‍🧙‍♂ En fazla tekrar eden anahtarlar için `most_common(<gösterilecek_anahtar_sayısı>)` fonksiyonu kullanılır
{% endhint %}

