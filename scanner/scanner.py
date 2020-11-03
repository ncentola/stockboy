from datetime import datetime as dt
from publisher import Publisher
from constants import TEST_UPC_CODES
import pika, random, json

class Scanner(Publisher):

    def __init__(self, queue='scanner'):

        super(Scanner, self).__init__()

        self.queue = queue
        self.set_mode()

    def get_mode(self):
        # TODO GPIO switch input
        if True:
            return 1
        else:
            return -1

    def set_mode(self):

        self.mode = self.get_mode()

    def read(self):

        while True:
            r = random.randint(1, 1000000)
            # print(r)
            if r == 42:
                r_upc = random.randint(0, len(TEST_UPC_CODES)-1)
                message = {
                    'upc': TEST_UPC_CODES[r_upc],
                    'quantity': self.mode
                }
                return json.dumps(message)

    def run(self):

        super(Scanner, self).get_queue_conn(queue=self.queue)

        while True:

            if self.mode != self.get_mode():
                self.set_mode()
                super(Scanner, self).get_queue_conn(queue=self.queue)

            super(Scanner, self).publish(routing_key=self.queue, message=self.read())
