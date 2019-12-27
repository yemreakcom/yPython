# 👨‍🔧 Sistem Yönetimi

## 🎌 Komut veya Program Çalıştırma

Komutlar ve programların yönetimi `subprocess` paketi ile gerçekleşmektedir.

{% tabs %}
{% tab title="🧆 Komutların çalıştırılması" %}
```python
import subprocess, os

os.chdir(os.path.dirname(__file__)) # İstenilen dizine girme

# Orjinal komut: git descript --always
print(subprocess.check_output(["git", "describe", "--always"]).strip().decode()) 
```
{% endtab %}

{% tab title="🎪 Programların Çalıştırılması ve Çıktılarının Okunması" %}
```python
#!/usr/bin/env python3
from subprocess import Popen, PIPE

with Popen(r'C:\path\to\program.exe "arg 1" "arg 2"',
           stdout=PIPE, stderr=PIPE) as p:
    output, errors = p.communicate()
lines = output.decode('utf-8').splitlines()
```
{% endtab %}
{% endtabs %}

> * [Get the current git hash in a Python script](https://stackoverflow.com/a/57683700/9770490)
> * [Python popen\(\) - communicate\( str.encode\(encoding=“utf-8”, errors=“ignore”\) \) crashes](https://stackoverflow.com/a/33291200/9770490)

## 👀 İşletim Sistemini Tespit Etme

```python
import platform as _platform
if _platform.system() == 'Windows':
    from. import _winmouse as _os_mouse
elif _platform.system() == 'Linux':
    from. import _nixmouse as _os_mouse
elif _platform.system() == 'Darwin':
    from. import _darwinmouse as _os_mouse
else:
    raise OSError("Unsupported platform '{}'".format(_platform.system()))
```

## 🚩 Python Modül Dizinlerini Ayarlama

Python modüllerinin dizinleri `PYTHONPATH` ile belirlenir edilir.

```python
# Tek başına çalışmak isterse
if __name__ == "__main__":
    import os
    import sys
    sys.path.append(os.getcwd())
```

