import streamlit as st
import joblib
from pathlib import Path

# ---------- Load Model ----------
ROOT = Path(__file__).resolve().parent.parent
MODEL_PATH = ROOT / "model" / "house_price_model.pkl"

try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    st.error("Model file not found. Please ensure 'house_price_model.pkl' exists in the model directory.")
    st.stop()

# ---------- Page Config ----------
st.set_page_config(
    page_title="Bangalore House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Header ----------
st.title("🏠 Bangalore House Price Prediction")
st.markdown("""
    **Premium Real Estate Intelligence**  
    Predict property values in Bangalore's most sought-after locations using a trained Linear Regression model.
""")

st.divider()

# ---------- Sidebar Info ----------
with st.sidebar:
    st.header("About the Model")
    st.info("""
        This application uses a **Linear Regression** model trained on Bangalore housing data.
        - **Features**: Total Sqft, Bathrooms, Balconies, BHK
        - Best suited for mid to high-end residential properties.
    """)
    st.caption("Developed by Karthikeyan M • M.Tech Data Science • Presidency University")

# ---------- Main Inputs ----------
col1, col2 = st.columns([2, 1.5])

with col1:
    st.subheader("🏠 House Details")
    
    total_sqft = st.number_input(
        "Total Square Feet",
        min_value=300.0,
        max_value=15000.0,
        value=1500.0,
        step=50.0,
        help="Super built-up area in square feet"
    )
    
    bhk = st.number_input(
        "Bedrooms (BHK)",
        min_value=1,
        max_value=10,
        value=3,
        step=1,
        help="Number of bedrooms, hall & kitchen"
    )
    
    bath = st.number_input(
        "Bathrooms",
        min_value=1,
        max_value=10,
        value=3,
        step=1
    )
    
    balcony = st.number_input(
        "Balconies",
        min_value=0,
        max_value=5,
        value=2,
        step=1
    )

# ---------- Prediction Section ----------
with col2:
    st.subheader("📊 Prediction Result")
    
    predict_button = st.button("🚀 Predict Price", type="primary", use_container_width=True)
    
    if predict_button:
        with st.spinner("Analyzing market data..."):
            features = [[total_sqft, bath, balcony, bhk]]
            prediction = model.predict(features)
            
            # Format price nicely
            price_lakhs = prediction[0]
            
            st.success("✅ Prediction Complete!")
            
            st.metric(
                label="Estimated House Price",
                value=f"₹ {price_lakhs:,.2f} Lakhs",
                delta=None
            )
            
            # Additional insights
            if price_lakhs > 300:
                st.info("🌟 This falls in the **premium/high-end** segment of Bangalore real estate.")
            elif price_lakhs > 150:
                st.info("⭐ This is a strong mid-premium property valuation.")
            else:
                st.info("🏡 This is positioned in the affordable to mid-range segment.")

    else:
        st.info("👆 Click **Predict Price** to get valuation")

# ---------- Footer ----------
st.divider()

st.markdown("""
    ### Model Information
    - **Algorithm**: Linear Regression  
    - **Features**: Total Sqft, Bathrooms, Balconies, BHK  
    - **Use Case**: Quick valuation for modern apartments & villas in Bangalore
""")

st.caption(
    "Developed by Karthikeyan M | M.Tech Data Science | Presidency University | Linear Regression Model"
)