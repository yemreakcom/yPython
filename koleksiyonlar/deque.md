# 🌠 Deque

## 🔰 Deque'yi Tanıyalım

* 🍢 List objelerinin uç noktaları ile ilgilenen bir yapıdır.
* ✨ List'e göre optimize edilmiştir
  * `list` için $$O(N)$$ `dque` için $$O(1)$$
  * $${Verim}{O(1)} > {Verim}{O(N)}$$

```python
from collections import deque

d = deque([2,3,4,5]) # deque([2, 3, 4, 5])
d.append(10) # deque([2, 3, 4, 5, 10])
d.appendleft(20) # deque([20, 2, 3, 4, 5, 10])
```

## 🧮 Verimlilik Hesabı

```python
# %%timeit
d = deque()
for i in range(40000):
    d.appendleft(i)

# 3.76 ms ± 35.6 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```

```python
# %%timeit
l_ = list()
for i in range(40000):
    l_.insert(0, i)

# 410 ms ± 5.94 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
```

```python
list(d) == l_ # True
```

{% hint style="warning" %}
📢 Süreleri **IPython** üzerinde`%%timeit` kodu ile hesaplayabilirsiniz.
{% endhint %}

