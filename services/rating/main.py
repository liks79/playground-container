from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette()


@app.route("/")
async def rating(request):
    return JSONResponse({"rating": "5.0"})
