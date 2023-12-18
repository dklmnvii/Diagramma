import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from Server_cafe.database.db_manager import base_manager
from settings import SCRIPTS_TABLES_PATH, SCRIPTS_RIMARY_DATA_PATH
from routers import (menu_router, clients_router, personals_router, orders_router,
                     tables_router, expenses_router, suppliers_router,
                     reviews_router)

app = FastAPI(
    title='Cafe'
)

app.include_router(menu_router, prefix='/menu')
app.include_router(clients_router, prefix='/clients')
app.include_router(personals_router, prefix='/personals')
app.include_router(orders_router, prefix='/orders')
app.include_router(tables_router, prefix='/tables')
app.include_router(expenses_router, prefix='/expenses')
app.include_router(suppliers_router, prefix='/suppliers')
app.include_router(reviews_router, prefix='/reviews')



@app.get('/')
def root():
    return RedirectResponse('/docs')


if __name__ == '__main__':
    if not base_manager.check_base():
        base_manager.create_base(SCRIPTS_TABLES_PATH, SCRIPTS_RIMARY_DATA_PATH)
    uvicorn.run(app="start_server:app", host="127.0.0.1",  port=8000, reload=True)