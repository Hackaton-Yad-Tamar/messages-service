from fastapi import FastAPI
import uvicorn
from routes.email_routes import router as email_router
from routes.sms_routes import router as sms_router
from fastapi.middleware.cors import CORSMiddleware  # Import CORS middleware

app = FastAPI(title="Alert Service")

app.include_router(email_router)
app.include_router(sms_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins (you can restrict this in production)
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PATCH, etc.)
    allow_headers=["*"],  # Allows all headers
)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
