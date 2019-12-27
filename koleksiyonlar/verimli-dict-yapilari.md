# 📗 Verimli Dict Yapıları

## 🚅 OrderedDict

* 🍢 Sıralanmış `dict` olarak geçmektedir
* 🚀 Sıralandığı için $$O(1)$$ erişim hızına sahiptir.

## 🧃 DefaultDict

* 🚫 `dict` verilerinde en önemli sorun olmayan anahtar \(_key_\) verileridir. 
* ✨ Olmayan anahtarlar için varsayılan değer atanır
* 🧹 Kodda daha temiz yapı sunar
* 🏗️`defaultdict(<type>)` şeklinde tanımlanır  

### 💖 DefaultDict Avantajı

```python
from collections import defaultdict
def count_default(x):
    count_dict = defaultdict(int)
    for ele in x:
        count_dict[ele] += 1 # count_dict'te olmayanların değeri 0 olduğundan 1 arttırılabilir
    return count_dict
count_default(ele)
```

```python
def count(x):
    count_dict = {}
    for ele in x:
        if ele in count_dict.keys():
            count_dict[ele] += 1
        else: # count_dict'te olmayan veriler için 1 atanmalıdır
            count_dict[ele] = 1
    return count_dict
count(ele)
```

