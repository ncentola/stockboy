#!/usr/bin/python

from consumer import Consumer

def main():
    c = Consumer(exchange='scans')
    c.consume(queue='transactions')

if __name__ == '__main__':
    main()
