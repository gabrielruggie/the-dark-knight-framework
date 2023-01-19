from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from main.routes.admin_finance import finance

# env
from main.utilities.load_env_file import Environment

origins =['http://localhost:3000']

'''
Creates FastAPI instance and mounts all routes to it
Configures CORS middleware as well
'''
def setup ():
    app = FastAPI()
    # Mount Routers
    app.include_router(finance, prefix=f'/admin-stack/{Environment.API_VERSION}/finance-manager', tags=["finance-manager"])

    # Allowing communication between frontend and backend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app    

api = setup()