import json

import responder
from tortoise import Tortoise
from mediple.models import User

config_secret = json.loads(open('.secret/info.json').read())
api = responder.API()


@api.on_event("shutdown")
async def close_db_connection(self):
    await Tortoise.close_connections()


@api.route("/")
async def home(req, resp):
    await Tortoise.init(
        db_url=config_secret['mediple']['database']['url'], modules={"models": ["mediple.models"]}
    )

    await User.create(name="Test User")
    user = await User.first()

    resp.text = f"Hello, {user.name}"


@api.route("/id/{id}")
async def home(req, resp, id):
    await Tortoise.init(
        db_url=config_secret['mediple']['database']['url'], modules={"models": ["mediple.models"]}
    )

    await User.create(name="Test User")
    user = await User.first()

    resp.text = f"Hello, {user.name}"


api.run(address='0.0.0.0', port=6765, debug=True)
