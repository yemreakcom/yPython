---
description: Argparse ile çoklu argüman (list) ekleme
---

# 🌊 Argparse Nargs

## 🔰 Nargs Genel Kullanımı

`nargs='<operatör>+'` şeklinde kullanılır

| Operatör | Açıklama |
| :--- | :--- |
| `+` | 1 or more |
| `*` | 0 or more |
| `?` | 0 or 1 |

## 🌊 Argparse ile `nargs` Detayları

Kaynak için [Argparse option for passing a list as option](https://stackoverflow.com/a/15753721/9770490) alanına bakabilirsin

```python
import argparse

parser = argparse.ArgumentParser()

# By default it will fail with multiple arguments.
parser.add_argument('--default')

# Telling the type to be a list will also fail for multiple arguments,
# but give incorrect results for a single argument.
parser.add_argument('--list-type', type=list)

# This will allow you to provide multiple arguments, but you will get
# a list of lists which is not desired.
parser.add_argument('--list-type-nargs', type=list, nargs='+')

# This is the correct way to handle accepting multiple arguments.
# '+' == 1 or more.
# '*' == 0 or more.
# '?' == 0 or 1.
# An int is an explicit number of arguments to accept.
parser.add_argument('--nargs', nargs='+')

# To make the input integers
parser.add_argument('--nargs-int-type', nargs='+', type=int)

# An alternate way to accept multiple inputs, but you must
# provide the flag once per input. Of course, you can use
# type=int here if you want.
parser.add_argument('--append-action', action='append')

# To show the results of the given option to screen.
for _, value in parser.parse_args()._get_kwargs():
    if value is not None:
        print(value)
```

```python
$ python arg.py --default 1234 2345 3456 4567
...
arg.py: error: unrecognized arguments: 2345 3456 4567

$ python arg.py --list-type 1234 2345 3456 4567
...
arg.py: error: unrecognized arguments: 2345 3456 4567

$ # Quotes won't help here... 
$ python arg.py --list-type "1234 2345 3456 4567"
['1', '2', '3', '4', ' ', '2', '3', '4', '5', ' ', '3', '4', '5', '6', ' ', '4', '5', '6', '7']

$ python arg.py --list-type-nargs 1234 2345 3456 4567
[['1', '2', '3', '4'], ['2', '3', '4', '5'], ['3', '4', '5', '6'], ['4', '5', '6', '7']]

$ python arg.py --nargs 1234 2345 3456 4567
['1234', '2345', '3456', '4567']

$ python arg.py --nargs-int-type 1234 2345 3456 4567
[1234, 2345, 3456, 4567]

$ # Negative numbers are handled perfectly fine out of the box.
$ python arg.py --nargs-int-type -1234 2345 -3456 4567
[-1234, 2345, -3456, 4567]

$ python arg.py --append-action 1234 --append-action 2345 --append-action 3456 --append-action 4567
['1234', '2345', '3456', '4567']
```



