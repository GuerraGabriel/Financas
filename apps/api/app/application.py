from .routers import conta_router, receita_router
from fastapi import FastAPI
import uvicorn

app = FastAPI(
    debug=True,
    root_path=''
    )

app.include_router(conta_router)
app.include_router(receita_router)

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8000)
