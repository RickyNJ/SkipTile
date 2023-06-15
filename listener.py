import time
from kafka import KafkaConsumer

bootstrap_servers = 'localhost:29092'
topic_name = 'PressureValues'

consumer = KafkaConsumer(topic_name, bootstrap_servers=bootstrap_servers)

total_messages = 0
start_time = time.time()
messages_last_second = 0

for message in consumer:
    total_messages += 1
    print(f"Total messages: {total_messages}")
    messages_last_second += 1
    
    current_time = time.time()
    elapsed_time = current_time - start_time
    
    if elapsed_time >= 1:
        print(f"Total messages: {total_messages}")
        print(f"Messages per second: {messages_last_second / elapsed_time}")
        
        start_time = current_time
        messages_last_second = 0