import pika, json, requests, logging, os
from utils import look_up_upc

logging.basicConfig(level=os.environ.get("LOGLEVEL", "INFO"))

class Consumer(object):
    '''
    consumes messages from the queue
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

        body_json = json.loads(body)

        # get rid of the quantity entry if it exists
        body_json.pop('quantity', None)

        # check if item exists in DB, will 404 if not
        r = requests.post('http://api/upc_lookup', json=body_json)

        if r.status_code == 200:
            ch.basic_ack(delivery_tag = method.delivery_tag)
        else:
            upc = body_json['upc']
            try:

                # look up product info via API
                logging.info('Looking up info for product {}...'.format(upc))
                product_data = look_up_upc(upc)
                logging.info('Found info for product {}!'.format(upc))

                # insert product info into DB
                logging.info('Creating new record for product {}...'.format(upc))
                requests.post('http://api/products', json=product_data)
                logging.info('Succesfully created new record for product {}!'.format(upc))

            except:

                # something failed - log error and requeue the message
                logging.error('Error looking up info for product {}, requeueing message...'.format(upc))
                ch.basic_reject(delivery_tag = method.delivery_tag, requeue=True)


    def consume(self, queue):

        self.get_queue_conn(queue)

        self.channel.basic_consume(queue=queue, on_message_callback=self.callback)
        self.channel.start_consuming()
