import paho.mqtt.client as mqtt
from random import randint
from time import sleep
########################################

BROKER="wild.mat.ucm.es"
TOPIC = "clients/EGS/numbers"


def main(broker, topic):
    print("Creating new instance...")
    client = mqtt.Client() #create new instance
    print("Connecting to broker...")
    client.connect(broker) #connect to broker
    client.loop_start() #start the loop
    while True:
        num = randint(0, 1000)
        print(f"Publishing message to {topic}: {num}")
        client.publish(topic, num)
        sleep(2)

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