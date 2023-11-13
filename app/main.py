from fastapi import FastAPI
from fastapi import Depends
from sqlalchemy.orm import Session
from app.database import Base
import routers.crud as crud
from routers import user, auth, routes, crud

app = FastAPI()

# Menambahkan router yang telah dibuat sebelumnya

app.include_router(routes.router)
app.include_router(user.router)
app.include_router(auth.router)

# Inisialisasi database
Base.metadata.create_all(bind=crud.engine)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
