from fastapi import FastAPI
from uvicorn import run


description = """
FinTracker
### Description

* FinTracker API is an open-source web API to help you take control of your personal finances. Track your income, expenses, budgets, and investments with this flexible and customizable tool.

"""

app = FastAPI(
    title="FinTracker API",
    description=description,
    version="0.1.0",
)


@app.get("/")
def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    run("main:app", host="localhost", port=8000, reload=True)
