#### NDCG@5 Calculation - Complete Example
NDCG@K = DCG@K / IDCG@K
DCG@K = Σ (rel_i / log₂(i+1))

#### Your RetailRocket Example
Ground Truth: [Prime Drink(7231), Lululemon(1956)]
Prediction: [7231, 1956, Adidas, RXBAR, On Shorts]
Relevance:​

DCG@5 = 1.0 + 0.63 + 0 + 0 + 0 = 1.63
IDCG@5 = 1.0 + 0.63 + 0.5 = 2.13
NDCG@5 = 1.63/2.13 = 0.766 ✓
