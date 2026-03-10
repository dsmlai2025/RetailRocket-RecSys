## 🚀 Setup & Usage

### **Quick Start (5 mins)**
```bash
git clone https://github.com/YOUR_USERNAME/RetailRocket-Production-RecSys
cd RetailRocket-Production-RecSys
```

# 1. Download dataset
```python
kaggle datasets download -d retailrocket/ecommerce-dataset
unzip ecommerce-dataset.zip -d data/RetailRocket/
```

# 2. Install
```python
pip install -r requirements.txt```

# 3. Run Stages
```python
jupyter notebook notebooks/01_data_preprocessing.ipynb
jupyter notebook notebooks/02_model_pipeline.ipynb
```

# 4. Live Demo
```bash
uvicorn app/api:app --reload --port 8000  # Terminal 1
streamlit run app/app.py                 # Terminal 2
```

Production (Docker)
```bash
docker-compose up --build
```

## **4. Architecture Diagram (architecture.mmd)**

5. How to Run - Setup Instructions

```bash
#!/bin/bash
echo "🚀 RetailRocket Production RecSys Setup"
```

# 1. Download dataset
```python
echo "📥 Downloading RetailRocket dataset..."
kaggle datasets download -d retailrocket/ecommerce-dataset
unzip -q ecommerce-dataset.zip -d data/RetailRocket/
```

# 2. Install dependencies
```python
pip install -r requirements.txt
```

# 3. Create directories
```bash
mkdir -p models feature_store docs app
```

# 4. Run Stage 0 & 1
```bash
echo "📓 Run notebooks/01_data_preprocessing.ipynb"
echo "📓 Run notebooks/02_model_pipeline.ipynb"
```

# 5. Start production
```python
echo "🌐 Terminal 1: uvicorn app/api:app --reload --port 8000"
echo "🌐 Terminal 2: streamlit run app/app.py"
echo "🌐 Live: http://localhost:8501"
```

Docker Setup
# Production deployment
docker-compose up --build
