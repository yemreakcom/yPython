---
description: Argparse kullanım örnekleri
---
# ⭐ Argparse Örnekleri

## 🌟 Genel Kullanım

```python
from argparse import ArgumentParser

parser = ArgumentParser(description='A simple CLI.')
# python <file> a b c için args.paths = ["a", "b", "c"]
parser.add_argument(
        'paths',
        nargs="+",
        metavar='paths',
        help='Projelerin yolları',
    )
parser.add_argument(
        '--log-file',
        '-o',
        default=os.path.join(os.getcwd(), 'output.log'),
        dest="logFile",
        help='Save the output in this file.',
        type=str,
        )
parser.add_argument(
        '--clean-file',
        action='store_true',
        default=False,
        help='Clear the log file on startup.Default is No',
        )
parser.add_argument(
        '--cancel-key',
        help='A single key that use as the cancel key, Default is ` (backtick)',
        )
parser.add_argument('--nargs', nargs='+')

args = parser.parse_args()
```
