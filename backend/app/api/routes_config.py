from app.api.routes.chat import router as chat_router
from app.api.routes.items import router as items_router
from app.api.routes.healthcheck import router as healthcheck_router

def include_routes(app):
    app.include_router(chat_router, prefix="/api")
    app.include_router(items_router, prefix="/api")
    app.include_router(healthcheck_router)