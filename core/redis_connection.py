from redis.asyncio import ConnectionPool
from redis.asyncio.client import Redis

from core.config import settings

try:
    pool = ConnectionPool(
        host=settings.REDIS_HOST,
        port=settings.REDIS_PORT,
        password=settings.REDIS_PASSWORD,
        db=settings.REDIS_DB,
    )
    redis = Redis(
        connection_pool=pool,
    )
except Exception as exc:
    print(exc)