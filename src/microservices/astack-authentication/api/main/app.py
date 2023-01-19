from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from main.routes.add_admin import admin
from main.routes.admin_token import token

# env
from main.utilities.load_env_file import Environment


'''
Creates FastAPI instance and mounts all routes to it
Configures CORS middleware as well
'''
def setup ():
    app = FastAPI()
    # Mount Routers
    app.include_router(admin, prefix=f'/admin-stack/{Environment.API_VERSION}/new-admin/add', tags=["new-admin-route"])
    app.include_router(token, prefix=f'/admin-stack/{Environment.API_VERSION}/oauth/authenticator', tags=["create-token-route"])
    # Allowing communication between frontend and backend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app    

api = setup()