from pykafka import KafkaClient
import pyarrow.parquet as pq
import pyarrow as pa
import pandas as pd
import time

client = KafkaClient(hosts="localhost:29092")
topic = client.topics[b'PressureValues']    

schema = pa.schema([('timestamp', pa.timestamp('s')), ('message', pa.string())])
writer = pq.ParquetWriter('data.parquet', schema)

start_time = time.time()
consumer = topic.get_simple_consumer()

## * Continuously read messages from the topic
for message in consumer:
    if message is not None:
        timestamp = time.time() - start_time
        mess = message.value.decode()
        # mess = mess.split(',')
        # mess.pop()
        mess = mess[:-1]
