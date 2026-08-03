from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()

profile={
    'This is the try to creat api using frame.'
    'THis is the proof that I also nedd to learn more things.'
}
class AnalyzeRequest(BaseModel):
    text:str
@app.get("/api/profile/")
def get_profile():
    return profile
@app.get("/api/hi/")
def get_profile():
    return 'hi,hello,你好'

@app.post("/app/analyze/")
def analyze(req:AnalyzeRequest):
     return {
        "text": req.text,
        "score": 0.5,
        "label": "偏平静",
        "pinyin": "（模块 6 再说）",
    }
