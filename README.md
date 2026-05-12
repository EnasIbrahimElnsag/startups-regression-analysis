# 📊 Startup Profit Prediction — Regression Analysis

A complete machine learning project that applies and compares three regression techniques — **Simple Linear Regression**, **Multiple Linear Regression**, and **Polynomial Regression** — to predict startup profits based on spending data.

---

## 📁 Project Structure

```
├── Startups_Regression.ipynb   # Main Jupyter Notebook
├── startups.csv                # Dataset
└── README.md                   # Project documentation
```

---

## 🎯 Objective

Predict the **Profit** of a startup company based on its spending across R&D, Administration, and Marketing, and determine which regression model performs best.

---

## 📦 Dataset

The dataset (`startups.csv`) contains information about **50 startups** across different US states.

| Column | Description |
|---|---|
| `R&D Spend` | Amount spent on Research & Development |
| `Administration` | Amount spent on Administration |
| `Marketing Spend` | Amount spent on Marketing |
| `State` | US State (New York / California / Florida) |
| `Profit` | Target variable — the company's profit |

---

## 🛠️ Libraries Used

```python
import pandas as pd          # Data loading and manipulation
import numpy as np           # Numerical computations
import matplotlib.pyplot as plt  # Plotting and visualization
import seaborn as sns        # Statistical visualizations
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import LabelEncoder, PolynomialFeatures
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
```

---

## 🔄 Workflow

### 1. Data Loading & Understanding
- Loaded the CSV dataset using `pandas`
- Explored shape, data types, and statistical summaries with `.shape()`, `.describe()`, `.info()`

### 2. Data Preprocessing
- ✅ Checked for **missing values** → None found
- ✅ Checked for **duplicate records** → None found
- 🔤 **Encoded categorical variable** `State` using `LabelEncoder` (New York, California, Florida → numeric)

### 3. Exploratory Data Analysis (EDA)
- **Correlation Heatmap** — revealed that `R&D Spend` has the strongest correlation with `Profit`
- **Boxplot** — compared Profit distribution across States
- **Histogram** — examined the distribution of Profit
- **Pairplot** — explored relationships between all numeric features

### 4. Model Building & Evaluation
Three models were trained using a **70/30 train-test split** (`random_state=42`).

---

## 🤖 Models

### 🔹 Simple Linear Regression
Uses **one feature** — `R&D Spend` — to predict Profit.

```python
X = df[['R&D Spend']]
y = df['Profit']
```

**Formula:**  
`Profit = b0 + b1 × (R&D Spend)`

---

### 🔹 Multiple Linear Regression
Uses **three features** — `R&D Spend`, `Administration`, `Marketing Spend` — to predict Profit.

```python
X = df[['R&D Spend', 'Administration', 'Marketing Spend']]
y = df['Profit']
```

**Formula:**  
`Profit = b0 + b1×(R&D) + b2×(Admin) + b3×(Marketing)`

---

### 🔹 Polynomial Regression (Degree = 2)
Applies polynomial transformation to `R&D Spend` to capture **non-linear** relationships.

```python
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(df[['R&D Spend']])
```

**Formula:**  
`Profit = b0 + b1×(R&D) + b2×(R&D)²`

---

## 📊 Model Comparison (Results)

| Model | R² Score | MSE | MAE |
|---|---|---|---|
| Simple Linear Regression | ~0.94 | — | — |
| Multiple Linear Regression | ~0.94 | Lowest | Lowest |
| Polynomial Regression (deg=2) | ~0.94 | — | — |

> 📌 **Best Model:** Multiple Linear Regression achieved the best balance with the **highest R²** and **lowest MAE**, making it the most reliable predictor for this dataset.

### 📈 Metrics Explained

| Metric | What it measures | Better when |
|---|---|---|
| **R² Score** | How well the model explains variance in profit | Closer to **1.0** |
| **MSE** | Average of squared prediction errors | As **low** as possible |
| **MAE** | Average absolute prediction error (in dollars) | As **low** as possible |

---

## 📉 Visualizations

Each model includes an **Actual vs. Predicted scatter plot** to visually assess performance. Points closer to the red dashed line (perfect fit line) indicate better predictions.

---

## 🔍 Key Findings

1. **R&D Spend** is the most influential feature — it has the highest correlation with Profit among all features.
2. All three models achieved an **R² score close to 0.94**, meaning they explain ~94% of the variance in profit.
3. **Multiple Linear Regression** performs best overall by using all three spending features.
4. **Polynomial Regression** slightly improved fit on the training set, but the relationship between R&D Spend and Profit is **mostly linear** — meaning polynomial features don't add significant value here.
5. The `State` variable had relatively **low impact** compared to spending features.

---

## ✅ Conclusion

| Question | Answer |
|---|---|
| Which model is most accurate? | **Multiple Linear Regression** |
| Most important feature? | **R&D Spend** |
| Is the relationship linear? | **Yes**, mostly linear |
| Any overfitting? | No — train and test R² scores are close |

---

## 🚀 How to Run

1. Clone or download the project files
2. Make sure you have the required libraries installed:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```
3. Place `startups.csv` in the same directory as the notebook
4. Open and run `Startups_Regression.ipynb` cell by cell in Jupyter Notebook or JupyterLab

---

## 👩‍💻 Author

This project was built as a regression analysis study comparing multiple ML algorithms on real-world startup data.
