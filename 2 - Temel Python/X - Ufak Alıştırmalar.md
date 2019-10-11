# 👨‍💻 Ufak Alıştırmalar

## ➗ İki Sayının Tam Bölünüp Bölünmemesini Tespit Etmek

```py
#!/usr/bin/python3
# -*- coding: utf-8 -*-

# “a”, “b”, “c” tanımlanması (python dilinde c'nin önceden tanımlanmasına gerek yoktur)
a = input("a=")
b = input("b=")

# Büyük sayının a'ya alınması.
if a < b:
    c = a  # “a”nın değerinin “c”de saklanması (python dilinde c'nin önceden tanımlanmasına gerek yoktur)
    a = b  # “b”nin değeri “a”ya atanması
    b = c  # “c”de Saklanan değerinin “b”ye aktarılması

if (a % b) == 0:
    print("Tam bölünebilir")
else:
    print("Tam bölünemez")
```
