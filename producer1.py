import paho.mqtt.client as mqtt
import random
import time
import matplotlib.pyplot as plt

framesPerSecond = 120
pointsPerFrame = 500
testRuns = 50

# Define the MQTT broker hostname and port number
broker_hostname = "localhost"
broker_port = 1883

# Define the topic to publish the message to
topic = "matten/1"

# Create a new MQTT client instance
client = mqtt.Client()

# Connect to the broker
client.connect(broker_hostname, broker_port)
times =[]

randomMessages = []
for i in range(120):
    mes = ""
    for i in range(1600):
        mes += (str(random.randint(0,500))+",")
    mes+="filler"
    randomMessages.append(mes)

for i in range(200):
    start_time = time.time()
    for ii in range(len(randomMessages)):
        client.publish(topic, randomMessages[ii])
        time.sleep(0.006)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(str(elapsed_time))
    times.append(elapsed_time)

# Disconnect from the broker
client.disconnect()

fig, ax = plt.subplots()
line = ax.plot(times)
ax.axhline(y=1, color='r')
ax.set_ylim(0,2)
plt.show()

