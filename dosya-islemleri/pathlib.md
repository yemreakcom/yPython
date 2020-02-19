---
description: Nesneye yönelik dosya sistemi yolları işlemleri
---

# 🛍️ Pathlib \| Dosya

## 🎈 Neden Tercih Edilmeli

* 🍱 Nesne tabanlı dosya sistemi yolları yönetimidir
* ✨ Yeni dosya sistemi yönetimidir
* 🧃 Dosya yolu objede ve ona özgü metotlarda saklanır
* 📦 `Glob` modülü içine dahildir
* 💎 Özel operatörleri ile hızlı çalışmayı sağlar
  * 🚶‍♂️ `os.path.join` yerine `/` kullanmanız yeterlidir

{% hint style="info" %}
‍🧙‍♂ Detaylı bilgi için [Basic Usage](https://docs.python.org/3/library/pathlib.html#basic-use) alanına bakabilirsin.
{% endhint %}

## 🆚 Os ile Farkı

| os and os.path | pathlib |
| :--- | :--- |
| [`os.path.abspath()`](https://docs.python.org/3/library/os.path.html#os.path.abspath) | [`Path.resolve()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.resolve) |
| [`os.chmod()`](https://docs.python.org/3/library/os.html#os.chmod) | [`Path.chmod()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.chmod) |
| [`os.mkdir()`](https://docs.python.org/3/library/os.html#os.mkdir) | [`Path.mkdir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.mkdir) |
| [`os.rename()`](https://docs.python.org/3/library/os.html#os.rename) | [`Path.rename()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rename) |
| [`os.replace()`](https://docs.python.org/3/library/os.html#os.replace) | [`Path.replace()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.replace) |
| [`os.rmdir()`](https://docs.python.org/3/library/os.html#os.rmdir) | [`Path.rmdir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.rmdir) |
| [`os.remove()`](https://docs.python.org/3/library/os.html#os.remove), [`os.unlink()`](https://docs.python.org/3/library/os.html#os.unlink) | [`Path.unlink()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.unlink) |
| [`os.getcwd()`](https://docs.python.org/3/library/os.html#os.getcwd) | [`Path.cwd()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.cwd) |
| [`os.path.exists()`](https://docs.python.org/3/library/os.path.html#os.path.exists) | [`Path.exists()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.exists) |
| [`os.path.expanduser()`](https://docs.python.org/3/library/os.path.html#os.path.expanduser) | [`Path.expanduser()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.expanduser) and [`Path.home()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.home) |
| [`os.path.isdir()`](https://docs.python.org/3/library/os.path.html#os.path.isdir) | [`Path.is_dir()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_dir) |
| [`os.path.isfile()`](https://docs.python.org/3/library/os.path.html#os.path.isfile) | [`Path.is_file()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_file) |
| [`os.path.islink()`](https://docs.python.org/3/library/os.path.html#os.path.islink) | [`Path.is_symlink()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.is_symlink) |
| [`os.stat()`](https://docs.python.org/3/library/os.html#os.stat) | [`Path.stat()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.stat), [`Path.owner()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.owner), [`Path.group()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.group) |
| [`os.path.isabs()`](https://docs.python.org/3/library/os.path.html#os.path.isabs) | [`PurePath.is_absolute()`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.is_absolute) |
| [`os.path.join()`](https://docs.python.org/3/library/os.path.html#os.path.join) | [`PurePath.joinpath()`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.joinpath) |
| [`os.path.basename()`](https://docs.python.org/3/library/os.path.html#os.path.basename) | [`PurePath.name`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.name) |
| [`os.path.dirname()`](https://docs.python.org/3/library/os.path.html#os.path.dirname) | [`PurePath.parent`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.parent) |
| [`os.path.samefile()`](https://docs.python.org/3/library/os.path.html#os.path.samefile) | [`Path.samefile()`](https://docs.python.org/3/library/pathlib.html#pathlib.Path.samefile) |
| [`os.path.splitext()`](https://docs.python.org/3/library/os.path.html#os.path.splitext) | [`PurePath.suffix`](https://docs.python.org/3/library/pathlib.html#pathlib.PurePath.suffix) |

## 🚶‍♂️ Dosya Yollarında İlerleme

```python
from pathlib import Path

p = Path('/etc')
q = p / 'init.d' / 'reboot'
q # PosixPath('/etc/init.d/reboot')
q.resolve() # PosixPath('/etc/rc.d/init.d/halt')
```

## 🔗 Faydalı Bağlantılar

{% embed url="https://docs.python.org/3/library/pathlib.html" %}

