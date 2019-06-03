from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

event_schema = avro.load('event-model.avsc')
event = {
    'date': 1557671938745
}
producer = AvroProducer({
    'bootstrap.servers': 'localhost:9093',
    'schema.registry.url': 'http://localhost:8085'
}, default_value_schema=event_schema)
producer.produce(topic='events', value=event)
producer.flush()
