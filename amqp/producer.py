import pika


credentials = pika.PlainCredentials("test", "test")


def build_param(
    host="soa-rabbitmq-server", **kwargs
) -> pika.ConnectionParameters:
    return pika.ConnectionParameters(host, credentials=credentials, **kwargs)


def produce():
    connection = pika.BlockingConnection(build_param())
    channel = connection.channel()
    channel.basic_publish(
        exchange="test", routing_key="test", body=b"Test message."
    )
    connection.close()


def produce_test():
    connection = pika.BlockingConnection(build_param())
    channel = connection.channel()
    channel.queue_declare(queue="test")
    channel.basic_publish(exchange="", routing_key="test", body="1")
    channel.basic_publish(exchange="", routing_key="test", body="2")
    channel.basic_publish(exchange="", routing_key="test", body="3")
    print("send msg to rabbitmq successful.")
    connection.close()


if __name__ == "__main__":
    # while True:
    produce_test()
