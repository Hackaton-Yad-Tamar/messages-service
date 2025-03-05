from twilio.rest import Client
from fastapi import HTTPException
from config import TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_PHONE_NUMBER

async def send_sms(to_number: str, body: str):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        message = client.messages.create(
            from_=TWILIO_PHONE_NUMBER,
            to=to_number,
            body=body
        )
        return {"status": "success", "message_sid": message.sid}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"SMS sending failed: {str(e)}")

