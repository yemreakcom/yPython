# 💎 Namedtuple

## 🔰 NamedTuple'ı Tanıyalım

* ✨ Özel adlandırılmış tuple değerleridir
* 📋 `verbose=True` olursa üretilen kodu görürüz

{% hint style="success" %}
🚀 `namedtuple`, neredeyse hiç hafıza maliyeti olmadan kendi kendini belgeleyen kod oluşturmak için harika bir yoldur.
{% endhint %}

```python
from collections import namedtuple
Vector3 = namedtuple('Vector', ['x', 'y', 'z'], verbose=True)

vec = Vector3(1,2,3)
vec.x, vec.y, vec.z

vec.x = 5 # Çalışmaz, çünkü tuple idir. (Dict'ten varkı burada belli olur)


def tfunc(a,b,c):
    print(a,b,c)

tfunc(*vec)
```

## 👨‍💻 NamedTuple ile Üretilen Kod

```python
from builtins import property as _property, tuple as _tuple
from operator import itemgetter as _itemgetter
from collections import OrderedDict

class Vector(tuple):
    'Vector(x, y, z)'

    __slots__ = ()

    _fields = ('x', 'y', 'z')

    def __new__(_cls, x, y, z):
        'Create new instance of Vector(x, y, z)'
        return _tuple.__new__(_cls, (x, y, z))

    @classmethod
    def _make(cls, iterable, new=tuple.__new__, len=len):
        'Make a new Vector object from a sequence or iterable'
        result = new(cls, iterable)
        if len(result) != 3:
            raise TypeError('Expected 3 arguments, got %d' % len(result))
        return result

    def _replace(_self, **kwds):
        'Return a new Vector object replacing specified fields with new values'
        result = _self._make(map(kwds.pop, ('x', 'y', 'z'), _self))
        if kwds:
            raise ValueError('Got unexpected field names: %r' % list(kwds))
        return result

    def __repr__(self):
        'Return a nicely formatted representation string'
        return self.__class__.__name__ + '(x=%r, y=%r, z=%r)' % self

    def _asdict(self):
        'Return a new OrderedDict which maps field names to their values.'
        return OrderedDict(zip(self._fields, self))

    def __getnewargs__(self):
        'Return self as a plain tuple.  Used by copy and pickle.'
        return tuple(self)

    x = _property(_itemgetter(0), doc='Alias for field number 0')

    y = _property(_itemgetter(1), doc='Alias for field number 1')

    z = _property(_itemgetter(2), doc='Alias for field number 2')
```

## ⭐ Örnek Kullanım

```python
# -*- coding: utf-8 -*-
from collections import namedtuple

LEFT = 'left'
RIGHT = 'right'
MIDDLE = 'middle'
WHEEL = 'wheel'
X = 'x'
X2 = 'x2'

UP = 'up'
DOWN = 'down'
DOUBLE = 'double'
VERTICAL = 'vertical'
HORIZONTAL = 'horizontal'


ButtonEvent = namedtuple('ButtonEvent', ['event_type', 'button', 'time'])
WheelEvent = namedtuple('WheelEvent', ['delta', 'time'])
MoveEvent = namedtuple('MoveEvent', ['x', 'y', 'time'])
```
