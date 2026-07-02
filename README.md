# 🏠 Bangalore House Price Prediction

🚀 **Live Demo:** https://housepriceanalysis.streamlit.app

A Machine Learning project that predicts Bangalore house prices using Linear Regression and Streamlit.

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
<img width="1917" height="1018" alt="image" src="https://github.com/user-attachments/assets/670633ac-7cc2-48de-8767-76b624f9b45b" />
<img width="1917" height="1017" alt="image" src="https://github.com/user-attachments/assets/437d1c1f-a245-41d7-b3c7-fe3dbb6c99d2" />
<img width="1917" height="1021" alt="image" src="https://github.com/user-attachments/assets/ad26d6f2-98c7-4b23-b179-16a3105d830a" />
<img width="717" height="546" alt="image" src="https://github.com/user-attachments/assets/7ef9973d-e06c-44d2-ad79-155c9506ccfb" />
<img width="237" height="172" alt="image" src="https://github.com/user-attachments/assets/41b0fbad-2bec-41fd-84bd-813420107960" />



## 🎯 Future Improvements

- Support **additional machine learning** models
- Include **location-based** price prediction
- **Hyperparameter tuning**
- Model comparison dashboard
- **Cloud deploymen**t

---

## 👨‍💻 Author

**Karthikeyan M**

M.Tech in Data Science  
Presidency University, Bengaluru

GitHub: https://github.com/krth-007

---
