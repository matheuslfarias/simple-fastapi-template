from fastapi import FastAPI, APIRouter

# 1
app = FastAPI(
    title="Recipe API", openapi_url="/openapi.json"
)

# 2
api_router = APIRouter()

# 3


@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root Get
    """
    return {"msg": "Hello, World!"}


# 4
app.include_router(api_router)
