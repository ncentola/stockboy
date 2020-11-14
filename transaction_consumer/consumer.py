import pika, json, requests, logging, os

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

class Consumer(object):
    '''
    consumes messages from the queue and writes them to db
    '''
    def __init__(self, exchange, host='queue'):
        self.host = host
        self.exchange = exchange

    def get_queue_conn(self, queue):

        connection = pika.BlockingConnection(pika.ConnectionParameters(self.host))
        channel = connection.channel()
        channel.queue_declare(queue=queue)
        channel.exchange_declare(exchange=self.exchange, exchange_type='fanout')

        channel.queue_bind(exchange=self.exchange, queue=queue)

        self.channel = channel

    def callback(self, ch, method, properties, body):
        logging.info(body)
        requests.post('http://api/transactions', json=json.loads(body))
        ch.basic_ack(delivery_tag = method.delivery_tag)

        # check if product exists


    def consume(self, queue):

        self.get_queue_conn(queue)

        self.channel.basic_consume(queue=queue, on_message_callback=self.callback)
        self.channel.start_consuming()
