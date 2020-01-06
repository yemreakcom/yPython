---
description: 'Dosya işlemlerinde okuma yöntemleri, çeşitleri'
---

# 👀 Dosyayı Okuma

## 📦 Obje

```python
f = open('./data/sample.txt', 'r', encoding="utf-8")
data = f.read()
f.close()

print(data)
print(f)
```

## 👨‍💼 Context Manager

```python
with open('./data/sample.txt', 'r', encoding="utf-8") as f:
    print(f.read())

print(f)
```

## 📋 Ortak Çıktı

```python
Hello!
Congratulations!
You've read in data from a file.
<_io.TextIOWrapper name='./data/sample.txt' mode='r' encoding='UTF-8'>
```

## 

