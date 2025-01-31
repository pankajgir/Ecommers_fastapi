from fastapi import FastAPI
from prodect import api as prodectrouter
from tortoise.contrib.fastapi import register_tortoise

app=FastAPI()
app.include_router(prodectrouter.app)

register_tortoise(
    app,
    db_url="postgres://postgres:12345@127.0.0.1/ecomfastapi",
    modules={'models':['prodect.models',]},
    generate_schemas=True,
    add_exception_handlers=True
)

