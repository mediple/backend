from tortoise import Tortoise,  run_async


async def init():
    await Tortoise.init(
        db_url="sqlite://mediple.db", modules={"models": ["mediple.models"]}
    )
    # Generate the schema
    await Tortoise.generate_schemas()


run_async(init())