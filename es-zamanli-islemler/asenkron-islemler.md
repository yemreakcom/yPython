---
description: Python ile asenkron programlama
---

# 💫 Asenkron İşlemler

## 🔰 Ne Amaçla Kullanılır

* Paralel işleme gibi seri olarak kodları çalıştırmayı sağlar
* Asenkron işlemlerin tamamlanması beklenirken diğer işlemleri derler
* `await` komutu ile asenkron işlemin tamamlanması beklenir

## 👪 Birden Fazla Task Çalıştırma

```python
import asyncio

async def first_task():
    print("İlk işlem yapılıyor")
    await asyncio.sleep(1)
    print("İlk işlem tamamlandı")

async def second_task():
    print("İkinci işlem yapılıyor")
    await asyncio.sleep(1)
    print("İkinci işlem tamamlandı")

async def run_tasks():
    tasks = []
    tasks.append(first_task())
    tasks.append(second_task())
    await asyncio.gather(*tasks)

asyncio.get_event_loop().run_until_complete(run_tasks())
```

## ⌛ Sırayla Çalışan İşlemler Tanımlama

* `wrapper` ile her yeni `connect` işleminden önce `delay` kadar bekleme işlemi yapılır
* Bu sayede ilk işlem `A` sürede olursa ikinci işlem `A + delay` sürede yapılacaktır

```python
import asyncio

async def connect():
	pass

async def wrapper(delay, coro):
    await asyncio.sleep(delay)
    return await coro

async def multiconnect():
    for i in range(5):
        asyncio.create_task(wrapper(0.4 * i , connect()))

asyncio.get_event_loop().run_until_complete(multiconnect)
```

## 🕳️ Async ile Websocket

```python
import asyncio

import websockets
from websockets.exceptions import ConnectionClosedError

SocketListener = Callable[[dict], None]


async def _connect(self, address: str, callback: SocketListener):
    while True:
        async with websockets.connect(address, ssl=True, ping_interval=0.) as ws:
            while True:
                try:
                    callback(loads(await ws.recv()))
                except (asyncio.TimeoutError, websockets.exceptions.ConnectionClosed):
                    try:
                        pong = await ws.ping()
                        await asyncio.wait_for(pong, timeout=self.PING_TIMEOUT)
                        continue
                    except:
                        await asyncio.sleep(self.SLEEP_TIME)
                        break
                except socket.gaierror:
                    await asyncio.sleep(self.SLEEP_TIME)
                    continue
                except (ConnectionRefusedError, ConnectionClosedError):
                    await asyncio.sleep(self.SLEEP_TIME)
                    continue

def _create_task(self, address: str, callback: SocketListener) -> asyncio.Future:
    return asyncio.ensure_future(self._connect(adress, callback))


def callback_func(json_data: dict):
    pass

ADRESS = ""
task = _create_task(ADRESS, callback_func)
asyncio.get_event_loop().run_until_complete(asyncio.gather(task))
```

