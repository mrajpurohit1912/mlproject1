# 🎓 ScorePredictor-End-to-End-Project

This is an **end-to-end Machine Learning project** that predicts **student scores** based on given features.  
The project covers everything from **EDA and model training** to **deployment** with a complete ML pipeline.  

---

## 🚀 Project Workflow  

1. **Data Collection & Preprocessing**  
   - Load dataset  
   - Handle missing values, outliers, and categorical features  
   - Perform feature scaling  

2. **Exploratory Data Analysis (EDA)**  
   - Visualize distributions  
   - Correlation heatmaps  
   - Feature importance  

3. **Model Training**  
   - Train multiple regression models  
   - Hyperparameter tuning  
   - Model evaluation using metrics  

4. **Pipeline Creation**  
   - End-to-end pipeline with preprocessing + model  
   - Save trained models and artifacts  

5. **Deployment**  
   - Flask application (`application.py`)  
   - Web templates (`templates/`)  
   - Predict student scores via user input  

---


## 📂 Repository Structure
```bash
├── artifacts/ # Saved models, scalers, logs
├── notebook/ # Jupyter notebooks for EDA & model training
├── src/ # Source code (pipeline, utils, etc.)
├── templates/ # HTML templates for Flask app
├── application.py # Flask app entry point
├── requirements.txt # Required dependencies
├── setup.py # Setup for packaging
├── README.md # Documentation
└── .gitignore
```


## 🛠 Setup Instructions

1. Clone the repository:
```bash
git clone https://github.com/<your-username>/ScorePredictor-End-to-End-Project.git
cd sScorePredictor-End-to-End-Project
```

2. Create a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows

```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python application.py
```

5. Open in browser:
```bash
http://127.0.0.1:5000/
```

🛠 Tech Stack

Python

Jupyter Notebook – EDA & experimentation

Scikit-learn – ML models & pipeline

Flask – Web deployment

HTML/CSS (templates/) – Simple UI



📈 Model Evaluation

RMSE, MAE, R² Score

Cross-validation performance
