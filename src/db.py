import redis


def test_connection(redis_instance: redis.Redis):
    try:
        redis_instance.ping()
        return True
    except redis.exceptions.ConnectionError:
        return False


async def track_total_tokens(redis_instance: redis.Redis, new_tokens: int):
    # Get the current total tokens then add the new tokens
    curr_tokens = int(redis_instance.get("cumulative_tokens") or 0)
    redis_instance.set("cumulative_tokens", curr_tokens + new_tokens)
