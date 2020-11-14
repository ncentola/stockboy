#!/usr/bin/python

from consumer import Consumer

def main():
    c = Consumer(exchange='scans')
    c.consume(queue='upc_lookup')

if __name__ == '__main__':
    main()
