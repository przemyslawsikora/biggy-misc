from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

kafka_address = 'localhost:9093'
schema_registry_url = 'http://localhost:8085'
event_model_path = 'event-model.avsc'

event_schema = avro.load(event_model_path)
producer = AvroProducer({
    'bootstrap.servers': kafka_address,
    'schema.registry.url': schema_registry_url
}, default_value_schema=event_schema)
event = {
    'object': 'example of event',
    'time': {
        'type': 'moment',
        'startDate': 1560520346000,
        'startDateOffset': '+02:00'
    },
    'attributes': {
        'string_field': 'sample text',
        'boolean_field': True,
        'int_field': 123,
        'long_field': 3756387563874563785683756,
        'float_field': 0.25,
        'double_field': 0.79385739857298284,
        'bytes_field': b'\x00\x01\x02',
        'array_string_field': ['aaa', 'bbb'],
        'array_boolean_field': [True, False],
        'array_int_field': [1, 2],
        'array_long_field': [9387563953875463856, 7893457398457398457],
        'array_float_field': [0.1, 0.2],
        'array_double_field': [0.387456387456, 1.374563745673],
        'array_bytes_field': [b'\x00\x01\x02', b'\x03\x04\x05']
    }
}
producer.produce(topic='events', value=event)
producer.flush()
