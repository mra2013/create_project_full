from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"]  # Allows all headers
)

# Routers for different modules
from routers import cases, forms, milestones, uploads

app.include_router(cases.router)
app.include_router(forms.router)
app.include_router(milestones.router)
app.include_router(uploads.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI DMS application!"}