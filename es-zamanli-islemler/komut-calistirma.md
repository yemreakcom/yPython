---
description: Python üzerinde işletim sistemi komutlarını çalıştırma
---
# 🎌 Komut Çalıştırma

## 🧆 Komutların çalıştırılması

Komutlar ve programların yönetimi `subprocess` paketi ile gerçekleşmektedir.

```python
import subprocess, os

os.chdir(os.path.dirname(__file__)) # İstenilen dizine girme

# Orjinal komut: git descript --always
print(subprocess.check_output(["git", "describe", "--always"]).strip().decode()) 
```

## 🎪 Programların Çalıştırılması ve Çıktılarının Okunması

```python
#!/usr/bin/env python3
from subprocess import Popen, PIPE

with Popen(r'C:\path\to\program.exe "arg 1" "arg 2"',
           stdout=PIPE, stderr=PIPE) as p:
    output, errors = p.communicate()
lines = output.decode('utf-8').splitlines()
```

## 🔗 Faydalı Bağlantılar

* [Get the current git hash in a Python script](https://stackoverflow.com/a/57683700/9770490)
* [Python popen() - communicate( str.encode(encoding=“utf-8”, errors=“ignore”) ) crashes](https://stackoverflow.com/a/33291200/9770490)
