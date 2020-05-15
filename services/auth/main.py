from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette()


@app.route("/")
async def auth(request):
    return JSONResponse({"message": "authorized!"})
