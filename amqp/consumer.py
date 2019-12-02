import pika


credentials = pika.PlainCredentials("test", "test")


def build_param(
    host="soa-rabbitmq-server", **kwargs
) -> pika.ConnectionParameters:
    return pika.ConnectionParameters(host, credentials=credentials, **kwargs)


def consume():
    # Logic of consume message
    connection = pika.BlockingConnection(build_param())
    channel = connection.channel()

    for method_frame, properties, body in channel.consume("test"):
        # Display the message parts and acknowledge the message
        print(
            f"method_frame={repr(method_frame)}, properties={repr(properties)}, body={repr(body)}"
        )
        channel.basic_ack(method_frame.delivery_tag)

        # Escape out of the loop after 10 messages
        if method_frame.delivery_tag == 10:
            break

    # Cancel the consumer and return any pending messages
    requeued_messages = channel.cancel()
    print(f"Requeued {requeued_messages} messages")
    connection.close()


if __name__ == "__main__":
    consume()
