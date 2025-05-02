from .routes.chat import router as chat_router
from .routes.items import router as items_router

def include_routes(app):
    app.include_router(chat_router)
    app.include_router(items_router)