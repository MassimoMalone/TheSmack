from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import hello

app = FastAPI()

# Add CORS
origins = [
    "http://localhost:5173",  # Your frontend URL (Vite)
    "http://localhost:3000",  # CRA default
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(hello.router, prefix="/api")

@app.get("/")
def root():
    return {"message": "API is running"}
