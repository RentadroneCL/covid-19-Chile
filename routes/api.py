from fastapi import APIRouter
from app.DailyReport import DailyReport

router = APIRouter()


@router.get('/')
async def index():
    data = DailyReport.all()

    return data

