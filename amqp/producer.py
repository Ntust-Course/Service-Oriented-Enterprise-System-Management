import pika


def build_param(
    host="soa-rabbitmq-server", **kwargs
) -> pika.ConnectionParameters:
    return pika.ConnectionParameters(host, **kwargs)


def produce():
    connection = pika.BlockingConnection(build_param())
    channel = connection.channel()
    channel.basic_publish(
        exchange="test", routing_key="test", body=b"Test message."
    )
    connection.close()


if __name__ == "__main__":
    produce()
