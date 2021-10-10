# 👨‍🔧 Sistem Yönetimi

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
