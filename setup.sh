#!/bin/bash
echo "🚀 RetailRocket Production RecSys Setup"

# 1. Download dataset
echo "📥 Downloading RetailRocket dataset..."
kaggle datasets download -d retailrocket/ecommerce-dataset
unzip -q ecommerce-dataset.zip -d data/RetailRocket/

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create directories
mkdir -p models feature_store docs app

# 4. Run Stage 0 & 1
echo "📓 Run notebooks/01_data_preprocessing.ipynb"
echo "📓 Run notebooks/02_model_pipeline.ipynb"

# 5. Start production
echo "🌐 Terminal 1: uvicorn app/api:app --reload --port 8000"
echo "🌐 Terminal 2: streamlit run app/app.py"
echo "🌐 Live: http://localhost:8501"
