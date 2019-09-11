# 🗂 IPython Drive İşlemleri

## Drive Dosyalarını Dosya Sistemine Bağlama

**Normal Bağlama:**

```py
from google.colab import drive
drive.mount('/content/gdrive')
```

**Kontrollü bağlama:**

```py
if 'mount' not in globals() or not mount:
    from google.colab import drive
    drive.mount('/content/gdrive')
    mount = True
```

## Drive Dosyalarına Erişme

```py
with open('/content/gdrive/My Drive/foo.txt', 'w') as f:
  f.write('Hello Google Drive!')
!cat /content/gdrive/My\ Drive/foo.txt
```
