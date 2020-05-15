from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette()


@app.route("/")
async def detail(request):
    return JSONResponse({"detail": "Good story!"})
