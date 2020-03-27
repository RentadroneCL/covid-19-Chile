from fastapi import APIRouter
from app.Total import Total
from app.DailyReport import DailyReport

router = APIRouter()


@router.get('/')
async def index():
    data = DailyReport.all()

    return data

@router.get('/total')
async def total():
    data = Total.all()

    return data.last()
