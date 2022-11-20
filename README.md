# MQTTReader
## Installation

The mosquitto server run on 9001 port so you might face issue with connection to publish message so follow following commands to allow it


```bash
sudo apt install ufw
```
```bash
sudo ufw allow 9001
```

#### Publish Message
To Publish message to server use bellow command 
```bash
mosquitto_pub -h 172.21.0.2 -p 9001 -I 'pratik' -t /event -m '{"sensor_value":20.2}'
```
