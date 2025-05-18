import joblib
import pandas as pd

# Load model once
model = joblib.load("model.pkl")

def predict_price(crop, location, month):
    try:
        # Clean inputs
        crop = crop.strip().title()
        location = location.strip().title()
        month = int(month)

        # Construct DataFrame with correct column names
        input_df = pd.DataFrame([{
            "crop": crop,
            "location": location,
            "month": month
        }])

        prediction = model.predict(input_df)
        return f"{prediction[0]:,.2f}"

    except Exception as e:
        return "Invalid input format for prediction."
