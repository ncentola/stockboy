import pika

class Publisher(object):
    def __init__(self, host='queue', exchange='scans'):
        self.host = host
        self.exchange = exchange
        self.get_queue_conn(queue='scanner')

    def get_queue_conn(self, queue):

        connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
        channel = connection.channel()
        channel.exchange_declare(exchange=self.exchange, exchange_type='fanout')
        channel.queue_declare(queue=queue)

        self.channel = channel

    def publish(self, routing_key, message):

        self.channel.basic_publish(
            exchange=self.exchange,
            routing_key=routing_key,
            body=message
        )
