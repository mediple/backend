import json

from tortoise import Tortoise, run_async

config_secret = json.loads(open('.secret/info.json').read())


async def init():
    await Tortoise.init(
        db_url=config_secret['mediple']['database']['url'],
        modules={"models": ["mediple.models"]}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


run_async(init())
