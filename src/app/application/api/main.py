from fastapi import FastAPI

from app.application.api.users.handlers import router


def create_app() -> FastAPI:
    app = FastAPI(
        title="ddd-fastapi",
        description="main-app API",
        version="0.0.1",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        debug=True
    )

    app.include_router(router=router, prefix='/app')

    return app
