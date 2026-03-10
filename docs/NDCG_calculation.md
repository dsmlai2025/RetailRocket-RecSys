# Access:
# Streamlit: http://localhost:8501
# FastAPI Docs: http://localhost:8000/docs

6. Detailed Technical Docs
docs/NDCG_calculation.md

# NDCG@5 Calculation - Complete Example
NDCG@K = DCG@K / IDCG@K
DCG@K = Σ (rel_i / log₂(i+1))

## Your RetailRocket Example
Ground Truth: [Prime Drink(7231), Lululemon(1956)]
Prediction: [7231, 1956, Adidas, RXBAR, On Shorts]
Relevance:​

DCG@5 = 1.0 + 0.63 + 0 + 0 + 0 = 1.63
IDCG@5 = 1.0 + 0.63 + 0.5 = 2.13
NDCG@5 = 1.63/2.13 = 0.766 ✓

docs/ALS_technical_details.md
# ALS Matrix Factorization - Production Implementation

## Loss Function
L(U,V) = Σ c_ui(r_ui - uᵀv_i)² + λ(‖U‖² + ‖V‖²)
c_ui = 1 + 15 × event_weight
λ = 0.1, factors=64, iterations=20

## Cold Start Handling


<3 interactions → Popular by category

New items → Content-based TF-IDF

Session-only → Real-time sequence model
Coverage: 98.2% ✓
