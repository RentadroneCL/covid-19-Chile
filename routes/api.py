import pendulum
from fastapi import APIRouter
from app.Total import Total
from app.DailyReport import DailyReport
from fastapi.encoders import jsonable_encoder

router = APIRouter()


@router.get('/')
async def index():
    data = DailyReport.all()

    return data


@router.get('/total')
async def total():
    data = Total.all()

    return data.last()


@router.get('/totals')
async def totals():
    data = Total.all()

    # data[0]._original['new_cases']
    # data[0].new_cases

    collect = {
        'new_cases': data.map(lambda item: item.new_cases),
        'total_cases': data.map(lambda item: item.total_cases),
        'deceased': data.map(lambda item: item.deceased),
        'recovered': data.map(lambda item: item.recovered),
        'last_update': data.map(lambda item: pendulum.parse(item.last_update).to_date_string())
    }

    return collect

