import responder
from tortoise import Tortoise
from mediple.models import User


api = responder.API()


@api.on_event("shutdown")
async def close_db_connection(self):
    await Tortoise.close_connections()


@api.route("/")
async def home(req, resp):

    await Tortoise.init(
        db_url="sqlite://mediple.db", modules={"models": ["mediple.models"]}
    )

    await User.create(name="Test User")
    user = await User.first()

    resp.text = f"Hello, {user.name}"


api.run(address='0.0.0.0', port=6765, debug=True)
