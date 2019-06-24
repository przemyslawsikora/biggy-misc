from confluent_kafka.avro import AvroConsumer
from confluent_kafka.avro.serializer import SerializerError

kafka_address = 'localhost:9093'
schema_registry_url = 'http://localhost:8085'
event_model_path = 'event-model.avsc'
topic_name = 'events'

consumer = AvroConsumer({
    'bootstrap.servers': kafka_address,
    'schema.registry.url': schema_registry_url,
    'group.id': 'python-consumer',
    'auto.offset.reset': 'earliest'})
consumer.subscribe([topic_name])
while True:
    msg = None
    try:
        msg = consumer.poll(10)
    except SerializerError as e:
        print("Message deserialization failed for {}: {}".format(msg, e))
        break
    if msg is None:
        continue
    if msg.error():
        print("PythonConsumer error: {}".format(msg.error()))
        continue
    print(msg.value())
consumer.close()
