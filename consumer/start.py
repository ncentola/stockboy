#!/usr/bin/python

from consumer import Consumer

def main():
    c = Consumer()
    c.consume(queue='scanner')

if __name__ == '__main__':
    main()
