---
description: Python ile websocket işlemleri (okuma yazma vs)
---
# 🕳️ Web Socket

## 👀 Hızlıca Tanıyalım

* 🔌 Ağ programlama kullanılan Socket yapısının web uygulamalarına uygulanmış halidir
* 🕊️ Düşük gecikme ve hızlı işlemler için tercih edilen HTTP protokolüne kıyasla hafif bir yapıdır
* 🔁 İki yönlü bağlantı yapısıyla sadece istemci değil, sunucu da istekte bulunabilir
* 🌊 İki bağlantı yapısı sayesinden sürekli olarak veri beslemesi yapılabilmektedir
* 💁‍♂️ Verileri güncellemek için isteğin yenilenmesine gerek yoktur, sürekli olarak güncel veriler aktarılır, veri değişikliklerine bağlıdır
* 🦄 Güncel veriler aktarıldığı için tek seferlik HTTP isteği ile bağlantı işlemi yapılır
* ❌ HTTP protokolünü kullanmadığı için URL yapısı `ws` veya `wss` ile başlar

> 👮‍♂️ HTTP protokolü tek yönlü bağlantı olduğundan sadece istemci istekte bulunur, sunucu istekte bulunamaz

## 🚧 Nasıl Çalışır

* ✨ İstemcinin bize erişebileceği bir IP ve port adresi tanımlanır
* 🏗️ İstemci ile bağlantı kurmak için `ws` veya güvenli olan `wss` ile başlayan url ile istek atılır
* 👀 Bağlantı kurulduğunda; hata, bilgi veya bağlantının kapanması durumunda sunucu istemciye mesajlar göndermeye başlar

## 💁‍♂️ Hangi Alanlarda Tercih Edilir

* 🕹️ Oyunlar gibi istemci ile sunucunun haberleşmesinin çok yüksek miktarda olduğu uygulamalarda
* 🗨️ Mesajlaşma uygulamaları gibi her mesaj gelme durumunda güncellenmesi gereken servislerde
* 💨 Bankacılık ve döviz işlemlerinde olduğu gibi düşük gecikme ile tamamlanması gereken işlemlerde

## ⭐ Python ile Websocket Örneği

```python
# pip install websocket_client

import websocket

try:
    import thread
except ImportError:
    import _thread as thread

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")


def on_open(ws):
    def run(*args):
       for i in range(3):
            time.sleep(1)
            ws.send("Hello %d" % i)
        time.sleep(1)
        ws.close()
        print("thread terminating...")
    thread.start_new_thread(run, ())


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "ws://echo.websocket.org/",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close)
    ws.on_open = on_open
    ws.run_forever()
```

## 🔗 Faydalı Bağlantılar

* [👪 Difference between a web-service and web-socket](https://stackoverflow.com/questions/25024685/difference-between-a-web-service-and-web-socket)
* [📺 WebSockets vs HTTP (REST)](https://www.youtube.com/watch?v=NJn9QW1t6pI)
* [📝 WebSocket vs REST](https://www.educba.com/websocket-vs-rest/s)
* [📦 Python - Websocket Client](https://pypi.org/project/websocket_client/)
