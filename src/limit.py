import redis
from fastapi import HTTPException
from starlette.middleware.base import BaseHTTPMiddleware


class RedisRateLimiter(BaseHTTPMiddleware):
    def __init__(
        self, app, max_requests: int, time_window: int, redis_instance: redis.Redis
    ):
        """
        The __init__ function is called when the class is instantiated.
        It sets up the instance of the class, and it's where you define your attributes.


        :param self: Represent the instance of the class
        :param app: Pass the flask application object to the class
        :param max_requests: int: Set the maximum number of requests that can be made in a time window
        :param time_window: int: Set the time window in seconds
        :param redis_url: str: Connect to the redis database
        :return: None
        :doc-author: Trelent
        """
        super().__init__(app)
        self.max_requests = max_requests
        self.time_window = time_window
        self.redis = redis_instance

    async def dispatch(self, request, call_next):
        client_ip = request.client.host
        key = f"rate_limit:{client_ip}"

        current_requests = self.redis.get(key)
        if current_requests is None:
            self.redis.set(key, 1, ex=self.time_window)
        else:
            current_requests = int(current_requests)
            if current_requests >= self.max_requests:
                raise HTTPException(status_code=429, detail="Too Many Requests")
            else:
                self.redis.incr(key)

        response = await call_next(request)
        return response
