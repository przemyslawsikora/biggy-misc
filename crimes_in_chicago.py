from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer
import pandas as pd
from dateutil import parser

input_file = 'Crimes in Chicago/Crimes_-_2001_to_present.csv'
kafka_address = 'localhost:9093'
schema_registry_url = 'http://localhost:8085'
event_model_path = 'event-model.avsc'
kafka_topic = 'events'

event_schema = avro.load(event_model_path)
producer = AvroProducer({
    'bootstrap.servers': kafka_address,
    'schema.registry.url': schema_registry_url
}, default_value_schema=event_schema)

chunk_size = 10 ** 4
for chunk in pd.read_csv(input_file, chunksize=chunk_size):
    for index, row in chunk.iterrows():
        if index % 10000 == 0:
            print('sent {:,} events to kafka'.format(index))
        event = {
            'object': 'Crime in Chicago',
            'time': {
                'type': 'moment',
                'startDate': int(parser.parse(timestr=row['Date'],
                                              default=parser.parse("00:00-05:00")).timestamp() * 1000),
                'startDateOffset': '-05:00'
            },
            'attributes': {
                'crime_type': str(row['Primary Type']).lower(),
                'crime_description': str(row['Description']).lower(),
                'crime_location': str(row['Location Description']).lower(),
                'crime_arrest': row['Arrest'],
                'crime_domestic': row['Domestic'],
                'crime_beat': str(row['Beat']),
                'crime_district': str(row['District']),
                'crime_ward': str(row['Ward']),
                'crime_community_area': str(row['Community Area'])
            }
        }
        producer.produce(topic=kafka_topic, value=event)
        if index % 500 == 0:
            producer.flush()
    producer.flush()
print(f'sent all events')
