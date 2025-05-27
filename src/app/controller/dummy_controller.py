from fastapi import APIRouter

router = APIRouter(prefix="/dummy", tags=["Dummy"])

@router.get("/ping")
def ping():
    print("Received request at /dummy/ping")
    return {"status": "ok", "message": "Ping successful!"}

@router.post("/echo")
async def echo(data: dict):
    print(f"Received request at /dummy/echo with data: {data}")
    return {"received_data": data}