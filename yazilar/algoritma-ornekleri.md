# 🔢 Algoritma Örnekleri

## 🎈 Asal Sayı Hesaplama (Prime)

{% tabs %}
{% tab title="📜 Açıklama" %}
The first optimization takes advantage of the fact that two is the only even prime. Thus we can check if a number is even and as long as its greater than 2, we know that it is not prime.

Our second optimization takes advantage of the fact that when checking factors, we only need to check odd factors up to the square root of a number. Consider a number $$n$$ decomposed into factors $$n=ab$$ . There are two cases, either $$n$$ is prime and without loss of generality, $$a=n, b=1$$ or $$n$$ is not prime and $$a,b \neq n,1$$ . In this case, if $$a > \sqrt{n}$$ , then $$b<\sqrt{n}$$ . So we only need to check all possible values of $$b$$ and we get the values of $$a$$ for free! This means that even the simple method of checking factors will increase in complexity as a square root compared to the size of the number instead of linearly.
{% endtab %}

{% tab title="👶 Basit" %}
```python
def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True
```
{% endtab %}

{% tab title="✨ Optimize" %}
```python
import math
def is_prime_fast(number):
    if number < 2:
        return False

    root = round(math.sqrt(number))
    for i in range(2, root + 1):
        if number % i == 0:
            return False

    return True
```
{% endtab %}

{% tab title="✅ Test" %}
```python
# Doğruluğu test etme
for n in range(10000):
    assert is_prime(n) == is_prime_fast(n)

# Hız testleri
# %%timeit ile hesaplanmıştır (jupyter notebook)
is_prime(67867967) # 4.85 s ± 94.8 ms per loop (mean ± std. dev. of 7 runs, 1 loop each)
is_prime_fast(67867967) # 578 µs ± 12.4 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
```
{% endtab %}
{% endtabs %}

## 🔢 Mersenne Number

{% tabs %}
{% tab title="📜 Açıklama" %}
A Mersenne number is any number that can be written as $$2^p - 1$$ for some $$p$$ . For example, 3 is a Mersenne number ( $$2^2 - 1$$ ) as is 31 ( $$2^5 - 1$$ ). We will see later on that it is easy to test if Mersenne numbers are prime.
{% endtab %}

{% tab title="👨‍💻 Kod" %}
```python
def mersenne_number(p):
    return 2 ** p - 1

def is_prime(number):
    if number < 2:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

def get_primes(n_start, n_end):
    return [x for x in range(n_start, n_end + 1) if is_prime(x)]

mersennes = [mersenne_number(x) for x in get_primes(3, 65)]
```
{% endtab %}
{% endtabs %}

## 🪁 Lucas Lehmer

{% tabs %}
{% tab title="📜 Açıklama" %}
We can test if a Mersenne number is prime using the [Lucas-Lehmer test](https://en.wikipedia.org/wiki/Lucas%E2%80%93Lehmer_primality_test). First let's write a function that generates the sequence used in the test. Given a Mersenne number with exponent $$p$$ , the sequence can be defined as

$$n_0 = 4$$ $$n_i = (n_{i-1}^2 - 2) mod (2^p - 1)$$ 
{% endtab %}

{% tab title="👨‍💻 Kod" %}
```python
def lucas_lehmer(p):
    n = [4]

    limit = p - 2
    mersenne = mersenne_number(p)

    for i in range(1, limit + 1):
        n.append((n[i - 1] ** 2 - 2) % mersenne)


    return n

ll_result = lucas_lehmer(17)
```
{% endtab %}
{% endtabs %}

## 🔢 Mersenne Prime

{% tabs %}
{% tab title="📜 Açıklama" %}
 For a given Mersenne number with exponent $$p$$ , the number is prime if the Lucas-Lehmer series is 0 at position $$p-2$$ . Write a function that tests if a Mersenne number with exponent $$p$$ is prime. Test if the Mersenne numbers with prime $$p$$ between 3 and 65 (i.e. 3, 5, 7, ..., 61) are prime. Your final answer should be a list of tuples consisting of `(Mersenne exponent, 0)` (or `1`) for each Mersenne number you test, where `0` and `1` are replacements for `False` and `True` respectively.
{% endtab %}

{% tab title="👨‍💻 Kod" %}
```python
def ll_prime(p):
    ll = lucas_lehmer(p)
    return not bool(ll[-1])

mersenne_primes = [(x, int(ll_prime(x))) for x in get_primes(3, 65)]
```
{% endtab %}
{% endtabs %}

## 💯 Sieve of Eratosthenes

{% tabs %}
{% tab title="📜 Açıklama" %}
The method works as follows (see [here](https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes) for more details)

1. Generate a list of all numbers between 0 and N; mark the numbers 0 and 1 to be not prime
2. Starting with $p=2$ (the first prime) mark all numbers of the form $np$ where $n>1$ and $np <= N$ to be not prime (they can't be prime since they are multiples of 2!)
3. Find the smallest number greater than $p$ which is not marked and set that equal to $p$, then go back to step 2. Stop if there is no unmarked number greater than $p$ and less than $N+1$

We will break this up into a few functions, our general strategy will be to use a Python `list` as our container although we could use other data structures. The index of this list will represent numbers.

We have implemented a `sieve` function which will find all the prime numbers up to $n$. You will need to implement the functions which it calls. They are as follows

* `list_true` Make a list of true values of length $n+1$ where the first two values are false (this corresponds with step 1 of the algorithm above)
* `mark_false` takes a list of booleans and a number $p$. Mark all elements $2p,3p,...n$ false (this corresponds with step 2 of the algorithm above)
* `find_next` Find the smallest `True` element in a list which is greater than some $p$ (has index greater than $p$ (this corresponds with step 3 of the algorithm above)
* `prime_from_list` Return indices of True values

Remember that python lists are zero indexed. We have provided assertions below to help you assess whether your functions are functioning properly.
{% endtab %}

{% tab title="👨‍💻 Kod" %}
```python
def list_true(n):
    return [False] * (2) + [True] * (n - 1)

# Test
# assert len(list_true(20)) == 21
# assert list_true(20)[0] is False
# assert list_true(20)[1] is False

def mark_false(bool_list, p):
    limit = ((len(bool_list) -1)  // p) + 1
    for i in range(2, limit):
        bool_list[i*p] = False
    return bool_list

# Test
# assert mark_false(list_true(6), 2) == [False, False, True, 
# True, False, True, False]

def find_next(bool_list, p):
    for i in range(p + 1, len(bool_list)):
        if bool_list[i]:
            return i
# Test
# assert find_next([True, True, True, True], 2) == 3
# assert find_next([True, True, True, False], 2) is None

def prime_from_list(bool_list):
    return [i for i, x in enumerate(bool_list) if x]

# Test
# assert prime_from_list([False, False, True, True, False]) ==  [2, 3]

def sieve(n):
    bool_list = list_true(n)
    p = 2
    while p is not None:
        bool_list = mark_false(bool_list, p)
        p = find_next(bool_list, p)
    return prime_from_list(bool_list)

assert sieve(1000) == get_primes(0, 1000)

# Hız testleri
# %%timeit ile hesaplanmıştır (jupyter notebook)
sieve(1000) 
get_primes(0, 1000)

# 402 µs ± 7.47 µs per loop (mean ± std. dev. of 7 runs, 1000 loops each)
# 4.9 ms ± 93.2 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
```
{% endtab %}
{% endtabs %}

## 👨‍💻 Code Snippets

{% tabs %}
{% tab title="📋 List İşlemleri" %}
```python
[x for x in iter if x = 1]
```

```python
sum([obj["items"] for obj in groups[name]]
```

```python
[(name, sum([obj["items"] for obj in groups[name]])) for name in groups]
```

```python
lis = [("a",1) ...]
max(lis, key=lambda x:x[1]) # 2. elemana göre hesaplama
```
{% endtab %}

{% tab title="🍒 Verileri Sınıflara Göre Gruplama" %}
```python
def group_by_field(data, fields):

    def generate_keys(data, field):
        yield set([x[field] for x in data])

    groups = {}
    for field in fields:
        group = {name: [] for name in generate_keys(data, field)}
        groups[field] = group

    for x in data:
        groups[field][x[field]].append(data)

    return groups
```
{% endtab %}

{% tab title="📊 İstatistik" %}
```python
import math
import statistics

def grap_data(scripts, key):
    return [script[key] for script in scripts]

def standart_deviation(datas, avg):
    nominator = 0
    for data in datas:
        nominator += (data - avg) ** 2

    return math.sqrt(nominator / len(datas))

def median(datas, quartile = 2):
    center = len(datas) // 2

    if quartile == 1:
        center = center // 2
    if quartile == 3:
        center += center // 2

    datas = sorted(datas)

    if len(datas) % 2 == 0:
        med = (datas[center - 1] + datas[center]) / 2
    else:
        med = datas[center]

    return med

def describe(key):

    datas = grap_data(scripts, key)

    total = sum(datas)
    avg = total / len(datas)
    s = standart_deviation(datas, avg)

    med = median(datas)
    q25 = median(datas, 1)
    q75 = median(datas, 3)

    return (total, avg, s, q25, med, q75)
```
{% endtab %}

{% tab title="📙 Dict" %}
```python
for field in groups:
    # print(field)
    for name in groups[field]:
        # print(name)
        for data in groups[field][name]:
            print(data)
            break
        break
    break
```
{% endtab %}
{% endtabs %}

## 📂 Yüksek Miktarda Veriyi Ele Alma

{% tabs %}
{% tab title="🧩 Format" %}
```python
{
    field: {
        name : [ # Be careful it's list (not dict)
            data: {
                "items": 5 # some value
            },
            ...
        ],
        ...
    },
    ...
}
```
{% endtab %}

{% tab title="✨ Verilerin İşlenmesi" %}
```python
def group_by_field(data, fields):

    def create_keys(data, field):
        return set([x[field] for x in data])

    groups = {}
    for field in fields:
        group = {name: [] for name in create_keys(data, field)}
        groups[field] = group

    for x in data:
        groups[field][x[field]].append(x)

    return groups

def get_max_item(groups, attribute):
    max_items = []
    for group in groups:
        field = groups[group]

        sums = []
        for name in field:
            sums.append((name, sum([data[attribute] for data in field[name]])))

        max_items.append(max(sums, key=lambda x:x[1]))

    return max_items
```
{% endtab %}
{% endtabs %}
