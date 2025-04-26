from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI(
    title="Ogathon Challenges API",
    description="API para resolución de retos Ogathon (Patrones de Propagación Viral)",
    version="1.0.0"
)

def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return 1
    a, b = 1, 1
    for _ in range(2, n+1):
        a, b = b, a + b
    return b

@app.get("/challenges/solution-1")
async def solution_1(n: int):
    result = fibonacci(n)
    return JSONResponse(content={"result": result})
