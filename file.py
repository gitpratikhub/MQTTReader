import asyncio
import signal
import time
import uvloop
from gmqtt import Client as MQTTClient

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

STOP = asyncio.Event()

def on_connect(client, flags, rc, properties):
    print('Connected')
    client.subscribe('/event', qos=0)

def on_message(client, topic, payload, qos, properties):
    print('RECV MSG:',  payload)
    return payload

def on_disconnect(client, packet, exc=None):
    print('Disconnected')

def on_subscribe(client, mid, qos, properties):
    print('SUBSCRIBED')

def ask_exit(*args):
    STOP.set()

async def main(broker_host,broker_port):
    client = MQTTClient('pratik-doc')

    client.on_connect = on_connect
    client.on_message = on_message
    client.on_disconnect = on_disconnect
    client.on_subscribe = on_subscribe


    await client.connect(broker_host, broker_port)

    await STOP.wait()
    await client.disconnect()


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    host = '172.21.0.2'
    port = '9001'

    loop.add_signal_handler(signal.SIGINT, ask_exit)
    loop.add_signal_handler(signal.SIGTERM, ask_exit)

    loop.run_until_complete(main(host,port))