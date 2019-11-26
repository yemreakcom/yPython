# 💠 Argparse Action

## 🧱 Action Yapısı

| Parametre | Açıklama |
| :--- | :--- |
| `'store_true'` | Flag\* değeri olur ve komutta içerilirse `True` değeri alır \(`-h` gibi\) |
| `count` | Kaç kere yazıldığı bilgisini tutar \(-vvv için 3\) |

```python
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
```

## **📜 Komutun Çıktısı**

```bash
$ python3 prog.py --verbose
verbosity turned on

$ python3 prog.py --verbose 1
usage: prog.py [-h] [--verbose]
prog.py: error: unrecognized arguments: 1

$ python3 prog.py --help
usage: prog.py [-h] [--verbose]

optional arguments:
  -h, --help  show this help message and exit
  --verbose   increase output verbosity
```



