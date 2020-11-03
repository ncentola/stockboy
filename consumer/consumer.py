import pika, json, requests

class Consumer(object):
    '''
    consumes messages from the queue and writes them to db
    '''
    def __init__(self, host='queue'):
        self.host = host
        self.handler = DBHandler()

    def get_queue_conn(self, queue):

        connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
        channel = connection.channel()
        channel.queue_declare(queue=queue)

        self.channel = channel

    def callback(self, ch, method, properties, body):

        requests.post('http://api/transactions', json=json.loads(body))
        ch.basic_ack(delivery_tag = method.delivery_tag)

        # check if product exists
        

    def consume(self, queue):

        self.get_queue_conn(queue)

        self.channel.basic_consume(queue=queue, on_message_callback=self.callback)
        self.channel.start_consuming()
