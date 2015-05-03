#!/usr/bin/env python
import pika
import threading
import sys
import time
def process_record(body):
    print "recived"
    time.sleep(2)

class RabbitWorker(object):
    def __init__(self):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        self.channel = self.connection.channel()
        self.channel.basic_qos(prefetch_count=1)
        self.channel.queue_declare(queue='create_record')

    def callback(self, ch, method, properties, body):
        response = process_record(body)
        if properties.reply_to:
            ch.basic_publish(exchange='',
                     routing_key=properties.reply_to,
                     properties=pika.BasicProperties(correlation_id = props.correlation_id),
                     body=response)

    def consume(self):
        self.channel.basic_consume(self.callback, queue='create_record', no_ack=True)
        self.channel.start_consuming()


if __name__ == "__main__":
    for i in range(100):
        rabbitworker = RabbitWorker()
        worker = threading.Thread(target=rabbitworker.consume)
        worker.start()
    a = raw_input()
    if a:
        sys.exit(0)
