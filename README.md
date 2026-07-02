# 🏠 Bangalore House Price Prediction

An end-to-end Machine Learning project that predicts residential property prices in Bangalore using a Linear Regression model. The project includes data preprocessing, exploratory data analysis, model evaluation, and an interactive Streamlit web application for real-time price prediction.

---

## 📖 About the Project

The objective of this project is to build a simple and interpretable house price prediction model using real estate data from Bangalore.

The project covers the complete machine learning workflow—from cleaning raw data to deploying an interactive web application—making it suitable as a beginner-friendly data science portfolio project.

---

## 🚀 Key Features

- Cleaned and preprocessed housing dataset
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Linear Regression model training
- Model performance evaluation
- Interactive Streamlit dashboard
- Real-time house price prediction

---

## 📂 Project Structure

```
HousePriceAnalysis/
│
├── dashboard/
│   └── dashboard.py
├── data/
│   └── cleaned_house_data.csv
├── images/
│   ├── actual_vs_predicted.png
│   └── residual_plot.png
├── model/
│   └── house_price_model.pkl
├── notebook/
│   ├── EDA.ipynb
│   └── Model_Evaluation.ipynb
├── requirements.txt
└── README.md
```

---

## 📊 Features Used for Prediction

- Total Square Feet
- Number of Bedrooms (BHK)
- Number of Bathrooms
- Number of Balconies

---

## 🧠 Machine Learning Model

**Algorithm:** Linear Regression

The model was trained using Scikit-learn and evaluated using standard regression metrics.

### Evaluation Metrics

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Residual Analysis

---

## 💻 Streamlit Dashboard

The dashboard allows users to:

- Enter property details
- Predict estimated house prices instantly
- View model information
- Experience an interactive interface without writing code

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Streamlit
- Joblib
- Jupyter Notebook

---

## ▶️ How to Run the Project

Clone the repository:

```bash
git clone https://github.com/krth-007/HousePriceAnalysis.git
```

Move into the project directory:

```bash
cd HousePriceAnalysis
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

Launch the Streamlit application:

```bash
streamlit run dashboard/dashboard.py
```

---

## 📸 Project Screenshots

You can place screenshots of the dashboard and evaluation plots inside the **images/** folder and display them here.

Example:

```
images/
├── dashboard.png
├── actual_vs_predicted.png
└── residual_plot.png
```

---

## 🎯 Future Improvements

- Support additional machine learning models
- Include location-based price prediction
- Hyperparameter tuning
- Model comparison dashboard
- Cloud deployment

---

## 👨‍💻 Author

**Karthikeyan M**

M.Tech in Data Science  
Presidency University, Bengaluru

GitHub: https://github.com/krth-007

---

⭐ If you found this project useful, consider giving it a star.
