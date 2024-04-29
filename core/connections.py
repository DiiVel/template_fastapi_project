# from databases import Database
# from starlette.requests import Request
# from fastapi import FastAPI
# from starlette.routing import Mount
# from redis import Redis
#
#
# def get_database(request: Request) -> Database:
#     return request.app.state.database
#
# def get_cache(request: Request) -> Redis:
#     return request.app.state.cache
#
# def inject_db(app: FastAPI, db: Database, cache: Redis):
#     app.state.database = db
#     app.state.cache = cache
#     for route in app.router.routes:
#         if isinstance(route, Mount):
#             route.app.state.database = db
#             route.app.state.cache = cache