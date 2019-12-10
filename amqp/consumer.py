from time import sleep

import pika
from pika.adapters.blocking_connection import BlockingChannel

credentials = pika.PlainCredentials("test", "test")


def build_param(host="soa-rabbitmq-server", **kwargs) -> pika.ConnectionParameters:
    return pika.ConnectionParameters(host, credentials=credentials, **kwargs)


def callback(ch: BlockingChannel, method, properties, body):
    print(f" [x] Recived {repr(body)}")
    sleep(5)
    ch.basic_ack(delivery_tag=method.delivery_tag)


def consume():
    connection = pika.BlockingConnection(build_param())
    channel = connection.channel()
    channel.queue_declare(queue="test")
    channel.basic_consume(queue="test", on_message_callback=callback)
    print(" [*] Waiting for messages. Press Ctrl+C to exit.")
    channel.start_consuming()


if __name__ == "__main__":
    consume()
