# 🔃 IPython I/O İşlemleri

Resmi [Google Colab dökümanına][i/0 ipython] bakmanda fayda var

## Dosya Upload Etme

```py
from google.colab import files

uploaded = files.upload()

for fn in uploaded.keys():
  print('User uploaded file "{name}" with length {length} bytes'.format(
      name=fn, length=len(uploaded[fn])))
```

## Dosya İndirme

```py
from google.colab import files

with open('example.txt', 'w') as f:
  f.write('some content')

files.download('example.txt')
```

## Dizin İndirme

```py
zipped_file = "/content/file.zip"
folder_to_zip = "/content/Folder_To_Zip"
!zip -r "{zipped_file}" "{folder_to_zip}"

from google.colab import files
files.download(zipped_file)
```

### Dizin İndirme Arayüzü

```py
#@title Dizin İndirme Arayüzü
INDIRILECEK_DIZININ_YOLU = "sample_data" #@param {type:"string"}

from google.colab import files

# Dizin adını alma
folder_name = INDIRILECEK_DIZININ_YOLU.split('/').pop()

# Gerekli dosyaları oluşturma
!cp -r "/{INDIRILECEK_DIZININ_YOLU}" "/content"
!zip -r '{folder_name}.zip'  "{folder_name}"

# İndirme işlemini başlatma
files.download(f'{folder_name}.zip')

# Geçici dosyaları temizleme
!rm -rf '{folder_name}.zip'
!rm -rf '{folder_name}'
```

## Bilgisayar Kamerasına Erişme

```py
from IPython.display import display, Javascript
from google.colab.output import eval_js
from base64 import b64decode

def take_photo(filename='photo.jpg', quality=0.8):
  js = Javascript('''
    async function takePhoto(quality) {
      const div = document.createElement('div');
      const capture = document.createElement('button');
      capture.textContent = 'Capture';
      div.appendChild(capture);

      const video = document.createElement('video');
      video.style.display = 'block';
      const stream = await navigator.mediaDevices.getUserMedia({video: true});

      document.body.appendChild(div);
      div.appendChild(video);
      video.srcObject = stream;
      await video.play();

      // Resize the output to fit the video element.
      google.colab.output.setIframeHeight(document.documentElement.scrollHeight, true);

      // Wait for Capture to be clicked.
      await new Promise((resolve) => capture.onclick = resolve);

      const canvas = document.createElement('canvas');
      canvas.width = video.videoWidth;
      canvas.height = video.videoHeight;
      canvas.getContext('2d').drawImage(video, 0, 0);
      stream.getVideoTracks()[0].stop();
      div.remove();
      return canvas.toDataURL('image/jpeg', quality);
    }
    ''')
  display(js)
  data = eval_js('takePhoto({})'.format(quality))
  binary = b64decode(data.split(',')[1])
  with open(filename, 'wb') as f:
    f.write(binary)
  return filename
```

---

```py
from IPython.display import Image
try:
filename = take_photo()
print('Saved to {}'.format(filename))

# Show the image which was just taken.
display(Image(filename))
except Exception as err:
# Errors will be thrown if the user does not have a webcam or if they do not
# grant the page permission to access it.
print(str(err))
```

[i/0 ipython]: https://colab.research.google.com/notebooks/io.ipynb
