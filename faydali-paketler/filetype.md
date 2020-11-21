---
description: >-
  Dosyaların MIME tiplerini belirleyerek hangi dosyanın ne olduğunu python ile
  anlamanızı sağlar
---

# 🧐 FileType

## 👀 Hızlı Kullanım

```python
import filetype

def main():
    kind = filetype.guess('tests/fixtures/sample.jpg')
    if kind is None:
        print('Cannot guess file type!')
        return

    print('File extension: %s' % kind.extension)
    print('File MIME type: %s' % kind.mime)

if __name__ == '__main__':
    main()
```

{% hint style="info" %}
[👨‍💻 FileType](https://github.com/h2non/filetype.py)
{% endhint %}

