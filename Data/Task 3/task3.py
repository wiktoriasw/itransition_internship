import math

from fastapi import FastAPI

from fastapi.responses import PlainTextResponse

app = FastAPI()


@app.get("/wiktoriaswiech_ws_gmail_com",  response_class=PlainTextResponse,)
def find_lowest_common_multiple(x, y):
    try:
        x = int(x)
        y = int(y)
    except Exception:
        return "NaN"
    
    if x < 0 or y < 0:
        return "NaN"
    
    if x == 0 or y == 0:
        return "0"
    
    ret = abs(x * y) // math.gcd(x, y)
    return str(ret)
