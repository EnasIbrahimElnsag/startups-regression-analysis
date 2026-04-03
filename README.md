# 📈 Startup Profit Prediction — Regression Analysis

A machine learning project that predicts startup profit using three regression techniques: **Simple Linear Regression**, **Multiple Linear Regression**, and **Polynomial Regression**, applied to a real-world startup dataset.

---

## 📌 Project Overview

This notebook walks through a full data science pipeline — from loading and exploring the data, to building and evaluating three different regression models — to determine which approach best predicts a startup's profit based on its spending behavior.

---

## 📂 Dataset

**File:** `startups.csv`

| Column | Description |
|---|---|
| R&D Spend | Amount spent on Research & Development |
| Administration | Administrative expenses |
| Marketing Spend | Amount spent on Marketing |
| State | State where the startup operates |
| Profit | Target variable — the startup's profit |

---

## 🔄 Project Workflow

```
Load Data → Explore & Understand → Handle Missing/Duplicates
    → Encode Categorical Variables → Visualize → Build Models → Evaluate
```

### Steps:
1. **Import Libraries** — pandas, numpy, matplotlib, seaborn, sklearn
2. **Load Dataset** — Read `startups.csv`
3. **Data Understanding** — Shape, types, statistics
4. **Data Cleaning** — Check for nulls and duplicates
5. **Encoding** — Label Encoding for the `State` column
6. **Visualization** — Heatmap, boxplots, histograms, pairplot
7. **Modeling** — Three regression models
8. **Evaluation** — R² Score, MSE, RMSE, MAE

---

## 🤖 Models Built

### 1. Simple Linear Regression
- **Feature:** R&D Spend only
- **Target:** Profit
- Evaluated using R² Score and MSE

### 2. Multiple Linear Regression
- **Features:** R&D Spend, Administration, Marketing Spend
- **Target:** Profit
- Evaluated using R², MSE, RMSE, MAE

### 3. Polynomial Regression (degree=2)
- **Feature:** R&D Spend (transformed to polynomial features)
- **Target:** Profit
- Compared train vs. test R² to check for overfitting

---

## 📊 Evaluation Metrics

| Metric | Description |
|---|---|
| **R² Score** | How well the model explains variance in profit |
| **MSE** | Mean Squared Error |
| **RMSE** | Root Mean Squared Error |
| **MAE** | Mean Absolute Error |

---

## 🛠️ Requirements

Install dependencies with:

```bash
pip install pandas numpy matplotlib seaborn scikit-learn jupyter
```

---

## 🚀 How to Run

```bash
# Clone the repository
git clone https://github.com/username/repo-name.git

# Navigate to the project folder
cd repo-name

# Launch Jupyter Notebook
jupyter notebook
```

Then open the `.ipynb` file and run all cells from top to bottom.

> ⚠️ Make sure `startups.csv` is in the **same folder** as the notebook.

---

## 📁 Project Structure

```
📦 repo-name/
 ┣ 📓 Startups_Regression_Analysis.ipynb
 ┣ 📊 startups.csv
 ┗ 📄 README.md
```

---

## 💡 Key Findings

- **R&D Spend** is the strongest predictor of profit across all models
- **Multiple Linear Regression** provides a more comprehensive view by combining all spending features
- **Polynomial Regression** captures non-linear patterns with competitive accuracy

---

## 🙋 Author

Made with ❤️ as part of a Machine Learning course project.
