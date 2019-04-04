Originally based on https://github.com/saabeilin/sanic-secure-session
It seems like Mr. Beilin doesn't have anytime to maintain it these days,
so I needed to create my own branch that
1. support aioredis instead of asyncio_redis
2. cater for sanic 19.3.1 which requires max-age to be integer, thus breaking the original sanic-secure-session

This is created solely for my own project / work, and it's not meant for general usage
But if you're interested in making it for more common usage, just inform me.
Probably gonna need to resolve licensing questions with saabeilin first.
