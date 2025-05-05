from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi
from app.routes import user_routes

app = FastAPI()

# Add JWT Bearer Auth support in Swagger UI
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="Smart Queue User Service API",
        version="1.0",
        description="Handles user registration, login, and profile",
        routes=app.routes,
    )
    openapi_schema["components"]["securitySchemes"] = {
        "JWT": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT"
        }
    }
    for path in openapi_schema["paths"].values():
        for method in path.values():
            method["security"] = [{"JWT": []}]
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi

# Register the user routes
app.include_router(user_routes.router, prefix="/api/v1/users")