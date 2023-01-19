from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# Routers
from main.routes.ymbl_query_routes import router

'''
Creates FastAPI instance and mounts all routes to it
Configures CORS middleware as well
'''
def setup ():
    app = FastAPI()
    # Mount Routers
    app.include_router(router=router, prefix=f'', tags=['standings, stats, schedule'])

    # Allowing communication between frontend and backend
    app.add_middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return app    

api = setup()