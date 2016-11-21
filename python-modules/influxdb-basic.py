import logging
from time import sleep
from influxdb import InfluxDBClient as I

logging.basicConfig(
    level=logging.INFO
)
logger = logging.getLogger('haha')
logger.setLevel(logging.INFO)


c = I('localhost', 8086, None, None, 'test')

data1 = [
    {
        "measurement": 'ttt',
        "tags": {},
        "fields": {
            'value': 13
        }
    }
]

data2 = [
    {
        "measurement": 'ttt',
        "tags": {},
        "fields": {
            'value': 14
        }
    }
]


c.create_database('test')
r1 = c.write_points(data1)
logger.info(r1)

sleep(10)

c.create_database('test')
r2 = c.write_points(data2)
logger.info(r2)
