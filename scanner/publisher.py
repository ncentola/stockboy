import pika

class Publisher(object):
    def __init__(self, host='queue'):
        self.host = host

    def get_queue_conn(self, queue):

        connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
        channel = connection.channel()
        channel.queue_declare(queue=queue)

        self.channel = channel

    def publish(self, routing_key, message):

        self.channel.basic_publish(
            exchange='',
            routing_key=routing_key,
            body=message
        )
