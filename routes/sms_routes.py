from fastapi import APIRouter
from pydantic import BaseModel
from services.sms_service import send_sms

router = APIRouter()

class SMSRequest(BaseModel):
    to_number: str
    message: str

@router.post("/send-sms")
async def sms_endpoint(request: SMSRequest):
    return await send_sms(request.to_number, request.message)
