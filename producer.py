import pika


def produce(host="soa-rabbitmq-server"):
    connection = pika.BlockingConnection(host=host)
    channel = connection.channel()
    channel.basic_publish(
        exchange="test", routing_key="test", body=b"Test message."
    )
    connection.close()
