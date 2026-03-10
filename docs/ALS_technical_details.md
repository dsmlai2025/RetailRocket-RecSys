### ALS Matrix Factorization - Production Implementation

#### Loss Function
```python
L(U,V) = Σ c_ui(r_ui - uᵀv_i)² + λ(‖U‖² + ‖V‖²)
```
```python
c_ui = 1 + 15 × event_weight
```
```python
λ = 0.1, factors=64, iterations=20
```
#### Cold Start Handling

1. <3 interactions → Popular by category
2. New items → Content-based TF-IDF
3. Session-only → Real-time sequence model
4. Coverage: 98.2% ✓
