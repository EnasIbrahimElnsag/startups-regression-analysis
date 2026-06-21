# 📊 Startup Profit Prediction — Regression Analysis & ML Application

A complete machine learning project that applies and compares three regression techniques — **Simple Linear Regression**, **Multiple Linear Regression**, and **Polynomial Regression** — to predict startup profits based on spending data.

The project also includes an interactive **Gradio web application** that allows users to enter startup expenses and get an instant profit prediction using the best-performing regression model.

---

## 📁 Project Structure

```
├── Startups_Regression.ipynb   # Main Jupyter Notebook
├── startups.csv                # Dataset
├── model.pkl                   # Trained Multiple Linear Regression Model
├── app.py                      # Gradio Application
└── README.md                   # Project Documentation
```

---

## 🎯 Objective

The main goal of this project is to predict the **Profit** of a startup company based on its spending in:

- Research and Development
- Administration
- Marketing

Different regression algorithms were trained and compared to find the best model for profit prediction.

---

## 📦 Dataset

The dataset (`startups.csv`) contains information about **50 startup companies** across different US states.

| Column | Description |
|---|---|
| `R&D Spend` | Amount spent on Research and Development |
| `Administration` | Amount spent on Administration |
| `Marketing Spend` | Amount spent on Marketing |
| `State` | US State (New York / California / Florida) |
| `Profit` | Target variable — startup profit |

---

## 🛠️ Libraries Used

```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

import gradio as gr
import joblib
```

---

## 🔄 Workflow

### 1. Data Loading & Understanding
- Loaded the dataset using pandas
- Checked dataset shape
- Explored data types and statistical information using `.info()` and `.describe()`

### 2. Data Preprocessing

✅ Missing values checking  
✅ Duplicate records checking  
✅ Encoding categorical variable `State` using `LabelEncoder`

### 3. Exploratory Data Analysis (EDA)

The following visualizations were created:

- Correlation Heatmap
- Boxplot
- Histogram
- Pairplot

> **Key observation:** R&D Spend showed the strongest correlation with Profit.

---

## 🤖 Machine Learning Models

Three regression models were trained:

### 🔹 Simple Linear Regression

Uses only **R&D Spend** to predict Profit.

```
Profit = b0 + b1 × R&D Spend
```

### 🔹 Multiple Linear Regression

Uses **R&D Spend**, **Administration**, and **Marketing Spend** to predict Profit.

```
Profit = b0 + b1(R&D) + b2(Admin) + b3(Marketing)
```

### 🔹 Polynomial Regression

Polynomial transformation applied with degree = 2 to capture possible non-linear relationships.

```
Profit = b0 + b1(R&D) + b2(R&D)²
```

---

## 📊 Model Comparison

| Model | Performance |
|---|---|
| Simple Linear Regression | Good performance |
| Multiple Linear Regression | ⭐ Best overall model |
| Polynomial Regression | Similar performance |

### 🏆 Best Model

The **Multiple Linear Regression** model achieved the best results because it uses all important spending features (R&D Spend, Administration, Marketing Spend) and achieved the best balance between prediction accuracy and error values.

---

## 📈 Evaluation Metrics

| Metric | Description | Goal |
|---|---|---|
| **R² Score** | Measures how well the model explains profit variation | Higher is better |
| **MSE** | Measures average squared prediction errors | Lower is better |
| **MAE** | Measures average prediction error in dollars | Lower is better |

---

## 🖥️ Gradio Web Application

An interactive web interface was created using Gradio.

**Users can enter:**
- 💰 Research and Development Spend
- 🏢 Administration Expenditure
- 📢 Marketing Expenditure

Then the application predicts the expected startup profit.

**Features:**
- ✅ Simple user interface
- ✅ Real-time prediction
- ✅ Uses trained ML model
- ✅ Easy interaction without coding

---

## 🚀 How to Run

### 1. Install required libraries

```bash
pip install pandas numpy matplotlib seaborn scikit-learn gradio joblib
```

### 2. Run Notebook

Open `Startups_Regression.ipynb` and run all cells.

### 3. Run Application

```bash
python app.py
```

A Gradio link will appear. Open it in your browser.

---

## 🔍 Key Findings

- R&D Spend is the most influential feature affecting Profit.
- The regression models achieved strong performance.
- Multiple Linear Regression provided the best overall prediction.
- Spending features have more impact than the State feature.
- The relationship between spending and profit is mostly linear.

---

## ✅ Conclusion

| Question | Answer |
|---|---|
| Best Model? | Multiple Linear Regression |
| Most Important Feature? | R&D Spend |
| Relationship Type? | Mostly Linear |
| Deployment? | Gradio Application |

---

## 👩‍💻 Developed by

- Enas Ibrahim Ali Elnsag
- Malak Tamer Mohamed Ali
- Salma Amer Ahmed Abdel Fattah
- Fatma Mohamed Helmy Mohamed
- Mariem Medhet Afifi
