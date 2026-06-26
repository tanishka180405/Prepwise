# Redis is optional for local development
# If Redis is not running, the app will still work fine
try:
    import redis.asyncio as aioredis
    from config import settings
    redis_client = aioredis.from_url(
        settings.REDIS_URL,
        encoding="utf-8",
        decode_responses=True,
    )
except Exception:
    redis_client = None


async def get_redis():
    """FastAPI dependency — returns None if Redis not available."""
    return redis_client
