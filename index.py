from fastapi import FastAPI

app = FastAPI(
    title="PayPulse",
    description="Feel the pulse of your payments with PayPulse. Monitor and manage your financial transactions in real-time for a healthy and thriving business.",
)


@app.get('/', tags=['health'], summary="Check server health")
def root():
    return {"message": 'healthy'}