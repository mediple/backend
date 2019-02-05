import json
import time

import responder
from tortoise import Tortoise
from mediple.models import User

config_secret = json.loads(open('.secret/info.json').read())
api = responder.API()


@api.on_event("shutdown")
async def close_db_connection(self):
    await Tortoise.close_connections()


# x-www 방식
@api.route("/api/register/x-www")
async def home(req, res):
    # await Tortoise.init(
    #     db_url=config_secret['mediple']['database']['url'], modules={"models": ["mediple.models"]}
    # )

    @api.background.task
    def progress_data(data):
        print(data)
        time.sleep(3)

    data = await req.media()

    progress_data(data)

    res.media = {'success': True}


@api.route("/api/login")
async def home(req, res):
    await Tortoise.init(
        db_url=config_secret['mediple']['database']['url'], modules={"models": ["mediple.models"]}
    )


api.run(address='0.0.0.0', port=6765, debug=True)
