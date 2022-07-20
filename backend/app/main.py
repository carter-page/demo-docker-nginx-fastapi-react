from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/day", tags=["Dates"])
async def get_day_of_week(day_num: int = 0):
    """
    Get the current day of week
    """
    days = ['Sun', 'Mon', 'Tues', 'Wed', 'Thur', 'Fri', 'Sat']
    return days[day_num]