from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, EmailStr, Field

router = APIRouter()


class ContactMessage(BaseModel):
    """Schema for contact form submissions"""
    name: str = Field(..., min_length=1, max_length=255)
    email: EmailStr
    subject: str = Field(..., min_length=1, max_length=500)
    message: str = Field(..., min_length=1, max_length=5000)


@router.post("/contact")
async def send_contact_message(contact: ContactMessage):
    """
    Handle contact form submissions.

    Future implementation:
    - Send email to abathar.k987@gmail.com
    - Store message in database
    - Send confirmation email to sender

    For now, this is a placeholder endpoint.
    """
    # TODO: Implement email sending (e.g., using SendGrid, Mailgun, or SMTP)
    # TODO: Store message in database for record keeping
    # TODO: Send confirmation email to sender

    # Placeholder response
    return {
        "status": "success",
        "message": "Thank you for your message. We will get back to you soon!",
        "note": "Contact form functionality will be implemented in future updates."
    }


@router.get("/contact-info")
def get_contact_info():
    """
    Get contact information for display.
    """
    return {
        "name": "Abathar Kmash",
        "email": "abathar.k987@gmail.com",
        "phone": "+49 176 20360789",
        "address": "Haimhauser 15\n80802 München\nGermany",
        "ensemble_email": "ogaro.ensemble@gmail.com"
    }
