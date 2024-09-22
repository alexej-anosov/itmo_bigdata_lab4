# import sqlalchemy as sa
# from sqlalchemy.ext.asyncio import AsyncSession
# from db import Prediction

    
# async def add_prediction(db: AsyncSession, x: dict, y: float):
#     new_prediction = dict(
#     season = x['season'].value,
#     holiday = x['holiday'].value,
#     workingday = x['workingday'].value,
#     weather = x['weather'].value,
#     temp =  x['temp'],
#     atemp =  x['atemp'],
#     humidity =  x['humidity'],
#     windspeed =  x['windspeed'],
#     year =  x['year'],
#     month =  x['month'],
#     day =  x['day'],
#     hour =  x['hour'],
#     prediction = x['result']
#     )
#     new_prediction = Prediction(**new_prediction)
#     db.add(new_prediction)
#     await db.commit()

