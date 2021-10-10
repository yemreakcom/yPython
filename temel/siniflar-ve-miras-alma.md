---
description: Python ile class, interface, meta class, property, static ve class metotları, override vs gibi yapılar
---
# 🍎 Sınıflar ve Miras Alma

## 🏰 Class

* Nesneye yönelik programlama (OOP) temelini oluşturur
* Veri ve metotları gruplandırmamızı ve verimli kodlamamızı sağlar

```python
class Foo(object):

    # you couldn't use self. or cls. out here, they wouldn't mean anything

    # this is a class attribute
    thing = 'athing'

    def __init__(self, bar):
        # I want other methods called on this instance of Foo
        # to have access to bar, so I create an attribute of self
        # pointing to it
        self.bar = bar

    @staticmethod
    def default_foo():
        # static methods are often used as alternate constructors,
        # since they don't need access to any part of the class
        # if the method doesn't have anything at all to do with the class
        # just use a module level function
        return Foo('baz')

    @classmethod
    def two_things(cls):
        # can access class attributes, like thing
        # but not instance attribut
```

## 🍎 Class Anahtar Kelimeleri

* Tip işlemleri yapmak için `print(dir(<tip>))` yazıp çıkan metotlardan kullanacaklarımızı tanımlamamız gerekir
  * Örn: `int` işlemlerini yapmak için `print(dir(int))`
  * `__add__`, `__sub__` ...
* Çoklu işlemler için `if isinstance(number, int):` yapısı kullanılır

> [Python Operator Overloading](https://www.programiz.com/python-programming/operator-overloading)

| Anahtar                | Açıklama                                   |
| ---------------------- | ------------------------------------------ |
| `self`                 | Diğer dillerdeki `this` anlamına gelir     |
| `__init__`             | Constructor fonksiyonudur                  |
| `__repr__`             | Ekrana ne yazılacağı (`print`)             |
| `__str__`              | `str()` içerisine alındığında yapılacaklar |
| `__rmul__`             | Ters `*` işlemi                            |
| `__contains__`         | Dahiliye işlemi                            |
| `def function(param):` | Fonksiyon tanımlama                        |
| `del p1.age`, `del p1` | Obje ya da class silme                     |

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için 

* 📖 [Emulating container types](https://docs.python.org/3/reference/datamodel.html#emulating-container-types)

alanlarına bakabilirsin.
{% endhint %}

### :star2: Equal Metot Örneği

* `isinstance` metodu ile aynı sınıftan olup olmadığı kontrol edilir
* `vars(self)` kodu ile sınıfın sahip olduğu tüm değişkenler `dict` olarak alınır
* `dict` verisi `key` `value` çiftlerine dönüştürülerek otomatik kontrole hazırlanır
* `getattr` metodu ile verilen `key` ile değişken temsil edilir ve `value` değerine eşitliği kontrol edilir
* Her koşulun sağlanması durumunda `True` aksi halde `False` döndürülür

```python
def __eq__(self, o: object) -> bool:
	if isinstance(o, Account):
	    for key, value in vars(self).items():
	        if not getattr(o, key) == value:
	            return False
	    return True
	return False
```

### 💎 Properties

```python
class Window(object):
    @property
    def always_on_top(self):
        script = self._render_template('window/win_is_always_on_top.ahk')
        resp = self.engine.run_script(script)
        return bool(ast.literal_eval(resp))

    @always_on_top.setter
    def always_on_top(self, value):
        if value in ('on', 'On', True, 1):
            self.win_set('AlwaysOnTop', 'On')
        elif value in ('off', 'Off', False, 0):
            self.win_set('AlwaysOnTop', 'Off')
        elif value in ('toggle', 'Toggle', -1):
            self.win_set('AlwaysOnTop', 'Toggle')
        else:
            raise ValueError(
                f'"{value}" not a valid option')

window = Window()
window.always_on_top = "on"
print(window.always_on_top) # "on"
```

### ❔ Class Metotları

* 🔳 Class metotları sadece class objesine erişir
* 👮‍♂️ Obje özelliklerine erişemez (`self` ile erişilir)
* ⚡ Class objesi de kullanılmayacaksa Static metotları tercih ediniz

```python
class Window(object):
    @classmethod
    def from_mouse_position(cls, engine: ScriptEngine, **kwargs):
        script = engine.render_template('window/from_mouse.ahk')
        ahk_id = engine.run_script(script)
        return cls(engine=engine, ahk_id=ahk_id, **kwargs)
        
Window.from_mouse_position(...)
```

### ⚡ Static Metotlar

* 📢 Static metotlarda `self` veya `cls` parametresi olmaz
* 🕊️ Class içeriklerinden bağımsızdır

```python
class Laptop:

	@staticmethod
	def details():
		print('Hello! I am a laptop.')

laptop1 = Laptop()
laptop1.details()
```

### 🍏 Inheritance (Miras)

Miras işlemlerinde `object` yerine miras alınacak **class** adı yazılır.

* Üst sınıfın metotlarını ve değişkenlerini barındırır (_yani özelliklerine sahip_)
* Karmaşık programlama mimarilerinde oldukça faydalıdır, düzenli olmayı sağlar

```python
class Rectangle(object):
    def __init__(self, height, length):
        self.height = height
        self.length = length

    def area(self): # Alan
        return self.height * self.length

    def perimeter(self): # Çevre
        return 2 * (self.height + self.length)

class Square(Rectangle):
    def __init__(self, length):
        super(Square, self).__init__(length, length)

s = Square(5)
s.area(), s.perimeter() # (25, 20)

type(s) == Square # False
type(s) == Rectangle # True
isinstance(s, Rectangle) # True
```

```python
class InputData:
    def read(self):
        raise NotImplementedError

class PathInputData(InputData):
    def __init__(self, path):
        super().__init__()
        self.path = path
        
    # read tanımlanmazsa hata verir
    def read(self):
        with open(self.path) as f:
        return f.read()
```

```python
# Miras kontrolü

class BaseClass: pass
class SubClass(BaseClass): pass

issubclass(SubClass, BaseClass)
True
issubclass(SubClass, object)
True
issubclass(BaseClass, SubClass)
False
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Use @classmethod Polymorphism to Construct Objects Generically](https://thepythonguru.com/python-classes-and-interfaces/#item-39-use-classmethod-polymorphism-to-construct-objects-generically) alanına bakabilirsin.
{% endhint %}

### 🍍 Meta Class

```python
class DirectiveMeta(type):
    """
    Overrides __str__ so directives with no arguments can be used without instantiation
    Overrides __hash__ to make objects 'unique' based upon a hash of the str representation
    """
    def __str__(cls):
        return f"#{cls.__name__}"

    def __hash__(self):
        return hash(str(self))

    def __eq__(cls, other):
        return str(cls) == other


class Directive(SimpleNamespace, metaclass=DirectiveMeta):
    """
    Simple directive class
    They are designed to be hashable and comparable with string equivalent of AHK directive.
    Directives that don't require arguments do not need to be instantiated.
    """
    def __init__(self, **kwargs):
        super().__init__(name=self.name, **kwargs)
        self._kwargs = kwargs

    @property
    def name(self):
        return self.__class__.__name__

    def __str__(self):
        if self._kwargs:
            arguments = ' '.join(str(value) for key, value in self._kwargs.items())
        else:
            arguments = ''
        return f"#{self.name} {arguments}".rstrip()

    def __eq__(self, other):
        return str(self) == other

    def __hash__(self):
        return hash(str(self))
```

### ⭐ Class Örnekleri

{% tabs %}
{% tab title="👶 Basit" %}
```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

p1 = Person("John", 36)

print(p1.name) # John
print(p1.age) # 36
```
{% endtab %}

{% tab title="📜 Yazdırılabilir" %}
```python
class Rational(object):

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return '%d/%d' % (self.numerator, self.denominator)

fraction = Rational(4, 3)
print(fraction) # 4/3
```
{% endtab %}

{% tab title="➕ Toplama Çıkarma Destekli" %}
```python
class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y)

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y)
```
{% endtab %}

{% tab title="🤝 Çokça Operatörü Destekleyen" %}
```python
class Rational(object):

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __repr__(self):
        return '%d/%d' % (self.numerator, self.denominator)

    def __mul__(self, number):
        if isinstance(number, int): # Int destekler
            return Rational(self.numerator * number, self.denominator)
        elif isinstance(number, Rational): # Rational destekler
            return Rational(self.numerator * number.numerator, self.denominator * number.denominator)
        else:
            raise TypeError('Expected number to be int or Rational. Got %s' % type(number))

    def _gcd(self):
        smaller = min(self.numerator, self.denominator)
        small_divisors = {i for i in range(1, smaller + 1) if smaller % i == 0}
        larger = max(self.numerator, self.denominator)
        common_divisors = {i for i in small_divisors if larger % i == 0}
        return max(common_divisors)

    def reduce(self):
        gcd = self._gcd()
        self.numerator = self.numerator / gcd
        self.denominator = self.denominator / gcd
        return self
```
{% endtab %}

{% tab title="💠 Metotlu" %}
```python
class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc() # Hello my name is John
```
{% endtab %}

{% tab title="💎 Metotlu Operatörlü" %}
```python
from math import sqrt

class Point(object):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point(%d, %d)" % (self.x, self.y)

    def __add__(self, point):
        return Point(self.x + point.x, self.y + point.y)

    def __sub__(self, point):
        return Point(self.x - point.x, self.y - point.y)

    def distance(self, point):
        return sqrt((self.x - point.x) ** 2 + (self.y - point.y) ** 2)
```
{% endtab %}

{% tab title="🤯 Üst Seviye" %}
```python
class DataFrame(NDFrame):

    def __init__(self, data=None, index=None, columns=None, dtype=None,
                 copy=False):
        if data is None:
            data = {}
        if dtype is not None:
            dtype = self._validate_dtype(dtype)

        if isinstance(data, DataFrame):
            data = data._data

        if isinstance(data, BlockManager):
            mgr = self._init_mgr(data, axes=dict(index=index, columns=columns),
                                 dtype=dtype, copy=copy)
        elif isinstance(data, dict):
            mgr = self._init_dict(data, index, columns, dtype=dtype)
        elif isinstance(data, ma.MaskedArray):
            import numpy.ma.mrecords as mrecords
            # masked recarray
            if isinstance(data, mrecords.MaskedRecords):
                mgr = _masked_rec_array_to_mgr(data, index, columns, dtype,
                                               copy)

            # a masked array
            else:
                mask = ma.getmaskarray(data)
                if mask.any():
                    data, fill_value = maybe_upcast(data, copy=True)
                    data[mask] = fill_value
                else:
                    data = data.copy()
                mgr = self._init_ndarray(data, index, columns, dtype=dtype,
                                         copy=copy)

        elif isinstance(data, (np.ndarray, Series, Index)):
            if data.dtype.names:
                data_columns = list(data.dtype.names)
                data = dict((k, data[k]) for k in data_columns)
                if columns is None:
                    columns = data_columns
                mgr = self._init_dict(data, index, columns, dtype=dtype)
            elif getattr(data, 'name', None) is not None:
                mgr = self._init_dict({data.name: data}, index, columns,
                                      dtype=dtype)
            else:
                mgr = self._init_ndarray(data, index, columns, dtype=dtype,
                                         copy=copy)
        elif isinstance(data, (list, types.GeneratorType)):
            if isinstance(data, types.GeneratorType):
                data = list(data)
            if len(data) > 0:
                if is_list_like(data[0]) and getattr(data[0], 'ndim', 1) == 1:
                    if is_named_tuple(data[0]) and columns is None:
                        columns = data[0]._fields
                    arrays, columns = _to_arrays(data, columns, dtype=dtype)
                    columns = _ensure_index(columns)

                    # set the index
                    if index is None:
                        if isinstance(data[0], Series):
                            index = _get_names_from_index(data)
                        elif isinstance(data[0], Categorical):
                            index = _default_index(len(data[0]))
                        else:
                            index = _default_index(len(data))

                    mgr = _arrays_to_mgr(arrays, columns, index, columns,
                                         dtype=dtype)
                else:
                    mgr = self._init_ndarray(data, index, columns, dtype=dtype,
                                             copy=copy)
            else:
                mgr = self._init_dict({}, index, columns, dtype=dtype)
        elif isinstance(data, collections.Iterator):
            raise TypeError("data argument can't be an iterator")
        else:
            try:
                arr = np.array(data, dtype=dtype, copy=copy)
            except (ValueError, TypeError) as e:
                exc = TypeError('DataFrame constructor called with '
                                'incompatible data and dtype: %s' % e)
                raise_with_traceback(exc)

            if arr.ndim == 0 and index is not None and columns is not None:
                values = cast_scalar_to_array((len(index), len(columns)),
                                              data, dtype=dtype)
                mgr = self._init_ndarray(values, index, columns,
                                         dtype=values.dtype, copy=False)
            else:
                raise ValueError('DataFrame constructor not properly called!')

        NDFrame.__init__(self, mgr, fastpath=True)
```
{% endtab %}
{% endtabs %}

## 💎 Enumeration

Resmi dokümantasyon için [buraya](https://docs.python.org/3/library/enum.html) bakabilirsin.

* Sıralı ve sabit veriler oluşturmak için kullanılır
* `from enum import Enum` ile projeye dahil edilir
* Enumlarda değer eşitliği için `<enum>.value == <value>` kullanın
* Enumları değerler ile oluşturmak için `<Enum>(<value>)` yapısını kullanın
  * Enum ile enum oluşturabilirsiniz `<Enum>(<enum>)`
  * Değişkenin enum veya değer tuttuğundan emin olmadığınız durumlarda üstteki yapıyı kullanın

{% tabs %}
{% tab title="🧱 Temel Kullanım" %}
```python
from enum import Enum
from typing import Union  # Tip belirtme amaçlı eklenmiştir

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

# Temel erişimler
Color              # <enum 'Color'>
Color.RED.value    # 1
Color.RED.name     # RED
type(Color.RED)    # <enum 'Color'>
Color(1)           # <Color.RED: 1>
Color(Color.BLUE)  # <Color.BLUE: 3>

# Enum tanımlama
color_var: Union[str, Color]     # str veya Color tipinde bir obje
color: Color = Color(color_var)  # Enum ile enum objesi oluşturabilirz
color: Color = Color.RED         # Direkt olarak enum atama

# Enum değerlerine erişme
color = Color.RED
color.value == 1  # True
color == 1        # False
color.name == "RED"  # True
color == "RED"       # False

isinstance(Color.GREEN, Color) # True
```
{% endtab %}

{% tab title="💠 Fonksiyon API" %}
```python
ornek = Enum('Color', 'ANT BEE CAT DOG')
print(ornek) # <enum 'Color'>
```
{% endtab %}

{% tab title="💎 Eşsiz Enum" %}
```python
from enum import Enum, unique
@unique
class Mistake(Enum):
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 3

# Traceback (most recent call last):
# ValueError: duplicate values found in <enum 'Mistake'>: FOUR -> THREE
```
{% endtab %}
{% endtabs %}

## 🔶 Multi Value Enum

* Birden fazla değere sahip enum sınıfı tanımlamaya olanak sağlar
* `pip install aenum` ile gerekli paket yüklenmelidir

```python
from aenum import MultiValueEnum

class DType(MultiValueEnum):
    float32 = "f", 8
    double64 = "d", 9

>>> DType("f")
<DType.float32: 'f'>

>>> DType(9)
<DType.double64: 'd'>
```

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [YEmoji](https://emoji.yemreak.com/kullanim/baglantilar) yapısına uygun oluşturulmuş:

* 👪 [Get Enum name from multiple values python](https://stackoverflow.com/a/43210118/9770490)

alanlarına bakabilirsin.
{% endhint %}
