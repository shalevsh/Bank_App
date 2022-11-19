from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from server_utils.routers import category_routs, transaction_routs


app = FastAPI()

app.include_router(transaction_routs.transaction_router)
app.include_router(category_routs.category_router)


origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return "server is running"


if __name__ == "__main__":
    uvicorn.run("server:app", host="localhost", port=8000, reload=True)
