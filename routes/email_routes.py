from fastapi import APIRouter
from pydantic import BaseModel
from services.email_service import send_email

router = APIRouter()

class EmailRequest(BaseModel):
    to_email: str
    subject: str
    body: str

@router.post("/send-email")
async def email_endpoint(request: EmailRequest):
    return await send_email(request.to_email, request.subject, request.body)
