from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError

c = AvroConsumer({
    'bootstrap.servers': 'localhost:9093',
    'schema.registry.url': 'http://localhost:8085',
    'group.id': 'python-consumer',
    'auto.offset.reset': 'earliest'})
c.subscribe(['events'])
while True:
    msg = None
    try:
        msg = c.poll(10)
    except SerializerError as e:
        print("Message deserialization failed for {}: {}".format(msg, e))
        break
    if msg is None:
        continue
    if msg.error():
        print("PythonConsumer error: {}".format(msg.error()))
        continue
    print(msg.value())
c.close()
