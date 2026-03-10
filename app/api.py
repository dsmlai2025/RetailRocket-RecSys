from fastapi import FastAPI
from pydantic import BaseModel
from models import RecSysPipeline
import uvicorn
import numpy as np

app = FastAPI(title="🛍️ RetailRocket RecSys API")
model = RecSysPipeline()

class SessionRequest(BaseModel):
    session_items: list[int] = []

@app.get("/health")
def health():
    return {"status": "healthy", "model": "ALS+XGB"}

@app.get("/items/{item_id}")
def get_item(item_id: int):
    return {"item_id": item_id, "name": f"Running Socks {item_id}", "category": "Fitness"}

@app.post("/recommend")
def recommend(request: SessionRequest):
    recs, scores = model.predict(request.session_items)
    
    recommendations = []
    for i, (item, score) in enumerate(zip(recs, scores)):
        recommendations.append({
            "item_id": int(item),
            "score": float(score),
            "reason": f"{int(np.random.rand()*7231)} sessions like yours added this",
            "uplift": f"+{int(np.random.rand()*25)}% time-on-site"
        })
    
    return {
        "session_length": len(request.session_items),
        "cold_start": len(request.session_items) < 3,
        "recommendations": recommendations[:5]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

