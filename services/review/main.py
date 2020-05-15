from starlette.applications import Starlette
from starlette.responses import JSONResponse

app = Starlette()


@app.route("/")
async def review(request):
    return JSONResponse({"message": "review!"})
