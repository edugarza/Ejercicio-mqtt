from paho.mqtt.client import Client
from time import sleep
import paho.mqtt.publish as publish
import random

BROKER = "wild.mat.ucm.es"
TOPIC = 'clients/EGS/numbers'

def on_message(mqttc, data, msg):
    value = int(msg.payload)
    print("MESSAGE:", data, msg.topic, value)
    if value%2 == 0:
        print("El valor es par")
    else:
        print("El valor es impar")


def main(broker, topic):
    data = {'client' : None,
            'broker': broker}
    mqttc = Client(client_id="numbers", userdata=data)
    # data['client'] = mqttc
    mqttc.on_message = on_message
    mqttc.connect(broker)
    mqttc.subscribe(topic)
    mqttc.loop_forever()


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} broker topic")
        print(f"Using default values:\n\t- Broker: {BROKER}\n\t- Topic: {TOPIC}")
        broker = BROKER
        topic = TOPIC
    else:
        broker = sys.argv[1]
        topic = sys.argv[2]
    
    main(broker, topic)