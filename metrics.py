import random
from json import dumps
from kafka import KafkaProducer
import configparser
from time import sleep
try:
    parser = configparser.ConfigParser()
    parser.read('config.ini')
except configparser.ParsingError as e:
    print("Config Not found {}".format_map(e))
broker = parser.get('kafka', 'broker')
topic = parser.get('kafka', 'topic')
port = parser.get('kafka', 'port')


def random_numbers():
    while True:
        numbers = {}

        numbers = {
            "foo": random.randint(0, 100000000),
            "bar": round(random.random(), 2),
            "baz": random.randint(0, 10000),
            "boo": random.uniform(1.0, 300.5),
            "Citrus": random.randint(0, 100000000),
            "Autumn": round(random.random(), 2),
            "Tiger": random.uniform(1.0, 300.5),
            "Peaches": random.randint(0, 10000),
            "Alyson": random.randint(0, 50000),
            "Tangerine": random.uniform(1.0, 3000.5)
        }
        #json_data = json.dumps(numbers)
        print(numbers)
        producer = KafkaProducer(bootstrap_servers=broker,
                                 value_serializer=lambda x:
                                 dumps(x).encode('utf-8'))
        producer.send(topic=topic, value=numbers)



if __name__ == "__main__":
    random_numbers()
