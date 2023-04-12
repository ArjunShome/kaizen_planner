import json

from redis import Redis


class AppCache:
    def __init__(self, **kwargs):
        self._redis_client = None
        self.kwargs = kwargs

    def init_app(self, redis_url='', **kwargs):
        self.kwargs.update(kwargs)
        redis_url = redis_url if redis_url else 'redis://localhost:6379/0'

        self._redis_client = Redis.from_url(redis_url, **self.kwargs)

    def set(self, key, value, expiration=None, only_if_not_exist=False, only_if_exist=False):
        value = json.dumps(value)
        self._redis_client.set(name=key, ex=expiration, value=value, nx=only_if_not_exist, xx=only_if_exist)
        return True

    def get(self, key):
        value = self._redis_client.get(key)
        return json.loads(value) if value else None

    def delete(self, *keys):
        self._redis_client.delete(*keys)


app_cache = AppCache()
