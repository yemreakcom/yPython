---
description: Paratic sitesi üzerinden dolar fiyatını websocket işlemleri ile alma, çekme
---
# 💲 Anlık Dolar Fiyatı Alma

## 🔗 WS URL Bilgisini Alma

* 🕸 [https://piyasa.paratic.com/doviz/dolar/](https://piyasa.paratic.com/doviz/dolar/) sitesi üzerinden geliştirici seçenekleri açıyoruz
* 👨‍🔬 Geliştirici seçeneklerinden **Network** alanından **WS** filtresi ile ws isteğini buluyoruz
* 📋 Bulunan ws isteğinin url değerini sağ tıklayıp **Copy Link Adress **ile kopyalıyoruz

![](<../.gitbook/assets/Screen Shot 2021-08-05 at 14.33.53.png>)

## 🚧 WS Hiyerarşisini Taklit Etme

* ► WS networkünün üzerine basıp **Messages** alanını açıyoruz
* 📩 Kırmızı istekler gelen mesajlar, yeşil istekler ise gönderilen mesajlardır
* 🐾 Alttaki kod örneğinde olduğu gibi aynısını taklit ediyoruz

> 😥 Dolar 8.52 olmuş, bu işlemleri yaparken de 8.53 oldu

![](<../.gitbook/assets/Screen Shot 2021-08-05 at 14.38.23.png>)

![](<../.gitbook/assets/Screen Shot 2021-08-05 at 14.41.30.png>)

## 💻 Kaynak Kod

* 📦 komutu `pip install websockets` ile websockets kütüphanesini indiriyoruz

```python
import asyncio
from json import loads
from pprint import pprint

import websockets
from websockets.legacy.client import WebSocketClientProtocol

WS_ADRESS = "wss://socket2.paratic.com/socket.io/?EIO=4&transport=websocket"
WS_USD_TRY_MESSAGE = r'42["joinStream", {"codes": ["USD/TRL"]}]'


async def main():

    async with websockets.connect(WS_ADRESS) as ws:
        ws: WebSocketClientProtocol

        await ws.recv()
        await ws.send("40")

        await ws.recv()
        await ws.recv()
        await ws.recv()
        await ws.send(WS_USD_TRY_MESSAGE)

        while True:
            data = str(await ws.recv())
            if "spot_pariteler" in data:
                price = data.split("|")[2]
                print(price)
            await ws.send("3")


asyncio.get_event_loop().run_until_complete(main())
```
