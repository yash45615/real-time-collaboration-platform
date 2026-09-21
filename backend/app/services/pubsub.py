import json

from app.core.redis_client import redis_client


def publish_message(
    channel: str,
    message: dict,
):
    redis_client.publish(
        channel,
        json.dumps(message),
    )


def subscribe(channel: str):
    pubsub = redis_client.pubsub()

    pubsub.subscribe(channel)

    return pubsub