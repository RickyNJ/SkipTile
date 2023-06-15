import time
import paho.mqtt.client as mqtt

# Define variables for the MQTT broker and topic
MQTT_BROKER = "localhost"
MQTT_TOPIC = "matten/1"

# Define variables for tracking message rate
num_messages = 0
start_time = time.time()

# Define callback function for MQTT client
def on_message(client, userdata, message):
    global num_messages
    num_messages += 1

# Create MQTT client instance and connect to broker
client = mqtt.Client()
client.connect(MQTT_BROKER, 1883)

# Set callback function for message reception
client.on_message = on_message

# Subscribe to MQTT topic
client.subscribe(MQTT_TOPIC)

# Start loop to listen for MQTT messages
client.loop_start()

# Main loop to print message rate every second
while True:
    time.sleep(1)
    elapsed_time = time.time() - start_time
    message_rate = num_messages / elapsed_time
    print(f"Received {num_messages} messages at a rate of {message_rate:.2f} messages/second")
