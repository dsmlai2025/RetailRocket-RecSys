# models.py - SIMPLIFIED (no implicit - mock for demo)
import numpy as np
import joblib
from pathlib import Path

class RecSysPipeline:
    def __init__(self):
        # Mock models for live demo (real models optional)
        self.item_pop = np.random.rand(10000)
        print("✅ Mock production model loaded")
    
    def predict(self, session_items, k=5):
        """Real-time recommendations"""
        if len(session_items) < 3:
            # Cold start
            recs = np.random.choice(10000, k, replace=False, p=self.item_pop/np.sum(self.item_pop))
            scores = self.item_pop[recs]
        else:
            # Session-based (mock ALS + XGB)
            base_score = np.random.rand()
            recs = np.random.choice(10000, k*3, replace=False, p=self.item_pop/np.sum(self.item_pop))
            scores = base_score + np.random.rand(k*3)*0.3
            recs, scores = recs[:k], scores[:k]
        
        return recs, scores
    
    def cold_start_recs(self, last_item, k=5):
        return self.predict([], k)

