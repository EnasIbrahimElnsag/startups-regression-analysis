# 📊 Startup Profit Prediction — Regression Analysis

> A complete Machine Learning project that predicts startup profit based on different spending factors using Regression models.
> Developed as part of the Machine Learning course, where different regression algorithms were implemented and compared to select the best performing model.

\---

## 🎯 Objective

Predict the expected profit of a startup based on its spending across three key dimensions:

* 💰 **R\&D Spend** — Investment in research and development
* 🏢 **Administration Spend** — Administrative and operational expenses
* 📣 **Marketing Spend** — Marketing and advertising expenditure

The project also identifies the **best-performing regression model** through systematic comparison and evaluation.

\---

## 📂 Dataset

The dataset contains information about **50 startups** with the following features:

|Feature|Description|
|-|-|
|R\&D Spend|Investment in research and development|
|Administration Spend|Administrative expenses|
|Marketing Spend|Marketing and advertising expenses|
|State|Location of the startup|
|**Profit**|🎯 Target variable — the value to predict|

\---

## 🔄 Project Workflow

### 1\. Data Preprocessing

* ✅ Checked for missing values
* ✅ Checked for duplicate records
* ✅ Encoded categorical features (State column)
* ✅ Split data into training and test sets

### 2\. Exploratory Data Analysis

* 📊 Correlation analysis between features and target variable
* 📈 Distribution analysis of spending features
* 🔍 Feature relationship visualization (scatter plots \& heatmaps)

\---

## 🤖 Machine Learning Models

The following regression models were implemented, trained, and compared:

|#|Model|
|-|-|
|1|Simple Linear Regression|
|2|Multiple Linear Regression|
|3|Polynomial Regression|

\---

## 📈 Model Evaluation

Models were evaluated using three standard regression metrics:

* **R² Score** — Proportion of variance explained by the model
* **MSE** — Mean Squared Error
* **MAE** — Mean Absolute Error

### Results

|Model|R² Score|MSE|MAE|
|-|-|-|-|
|Simple Linear Regression|0.9407|\~$4.2M|\~$2.8M|
|**Multiple Linear Regression** ✅|**0.9453**|**\~$4.1M**|**\~$2.7M**|
|Polynomial Regression|0.9410|\~$5.8M|\~$3.9M|

> 🏆 \*\*Best Model: Multiple Linear Regression\*\* — achieved the best overall performance with balanced R² Score and lowest prediction error.

\---

## 🚀 Interactive Application

A **Gradio-powered** web application was developed to make the model accessible:

* 🖊️ Users input spending values for R\&D, Administration, and Marketing
* ⚡ The trained Multiple Linear Regression model processes inputs in real time
* 💡 Expected profit is instantly displayed as output
* 🌐 Deployed on Hugging Face Spaces for public access

### 🔗 Live Demo

👉 *https://huggingface.co/spaces/Enasibrahim/startup-profit-prediction*

\---

## 🛠️ Technologies Used

|Library|Purpose|
|-|-|
|Python|Core programming language|
|Pandas|Data loading, cleaning, and manipulation|
|NumPy|Numerical computations|
|Scikit-learn|Model implementation and evaluation|
|Matplotlib|Data visualization|
|Seaborn|Statistical data visualization|
|Gradio|Interactive web application interface|

\---

## 👥 Team Members

|#|Name|
|-|-|
|1|Enas Ibrahim Ali Elnsag|
|2|Malak Tamer Mohamed Ali|
|3|Salma Amer Ahmed Abdel Fattah|
|4|Fatma Mohamed Helmy Mohamed|
|5|Mariem Medhat Afifi|

\---

