# ⭐ Örnekler

## 📋 Dizin ve Dosya Yolları Listesi Döndürme

```python
def listfolderpaths(path=os.getcwd()):
        folderlist = []
        for name in os.listdir(path):
            pathname = os.path.join(path, name)
            if not is_private(name) and os.path.isdir(pathname):
                folderlist.append(pathname)
        return folderlist

def listfolderpaths(path=os.getcwd()):
    return [os.path.join(path, name) for name in os.listdir(path) if (not is_private(name) and os.path.isdir(os.path.join(path, name)))]

def listfilepaths(path=os.getcwd()):
    return [os.path.join(path, name) for name in os.listdir(path) if (not is_private(name) and os.path.isfile(os.path.join(path, name)))]

def list_files(image_dir, pattern):
    return [image for image in glob.glob(osp.join(image_dir, pattern))]

list_images(r"C\Users\Picture", ".jpg")
```

## 🌳 Dizinleri Ağaç Yapısında Listeleme

```python
def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
            
# Gizli dosaları atlayarak listeleme
for root, dirs, files in os.walk(path):
    # İşletim sistemleri göre farklı sırada hareket etmesini engelleme
    dirs.sort()
    files.sort()
    
    print root

    dirs[:] = [d for d in dirs if not d.startswith('.')]

    for dir in dirs:
        print os.path.join(root, dir)
    for file in files:
        print os.path.join(root, file)
    
# İstenen dizinleri atlayarak listeleme
for root, dirs, files in os.walk(path):
    if root in ignore_list:
        dirs[:] = []
        files[:] = []
```

## 👮‍♂️ Özel Dizinlere Erişim

### ⭐ Sistem Dizinlerine Erişme \(System Environment\)

```python
import os, sys, site
ENVIROMENT_VAR = "WINDIR" # Sistem değişkeni isimleri

pythonpath = os.path.dirname(sys.executable) # Python.exe yolu
pythondir = os.path.dirname(sys.exec_prefix) # python.exe dizini
varname = os.environ[ENVIROMENT_VAR] # Sistem değişkenini değeri
userpath = site.getuserbase() # Kullanıcı seviyesindeki python yolu
modul_init_path = os.__file__ # Os modülünün init dosyasının yolu
```

### 📦 Paket Dizinlerine Erişme

```python
import module # Herhangi bir pip ile indirilen modülü temsil eder, örn: pynput

path = module.__file__
site_packages_path = os.path.join(path, "..", "..")
```

