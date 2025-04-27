
from config import Config
from redis import StrictRedis


# # Setup our redis connection for storing the blocklisted tokens. You will probably
# # want your redis instance configured to persist data to disk, so that a restart
# # does not cause your application to forget that a JWT was revoked.
jwt_redis_blocklist = StrictRedis(
    host=Config.REDIS_HOST,
    port=Config.REDIS_PORT,
    db=Config.REDIS_TOKEN_DB,
    decode_responses=True
)