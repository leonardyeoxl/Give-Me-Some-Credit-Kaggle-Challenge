from classifier import Classifer
from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
classifier = Classifer()

class Item(BaseModel):
    RevolvingUtilizationOfUnsecuredLines: float
    age: int
    NumberOfTime3059DaysPastDueNotWorse: int
    DebtRatio: float
    MonthlyIncome: int
    NumberOfOpenCreditLinesAndLoans: int
    NumberOfTimes90DaysLate: int
    NumberRealEstateLoansOrLines: int
    NumberOfTime6089DaysPastDueNotWorse: int
    NumberOfDependents: int

@app.get("/classify/")
def classify(item: Item):
    prediction = classifier.Classify(item.dict())
    return {"prediction":prediction}