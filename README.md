project/
├── app.py
├── model.pkl               # trained model file
├── utils.py                # function to load model and predict
├── sample_data.csv         # sample training data
├── train_model.py          # script to train the ML model
├── requirements.txt        # dependencies
└── README.md               # project overview and setup instructions



# Re-run the code to generate the README.md file after the state reset
readme_content = """
# 🌾 Nigeria Agricultural Market Price Predictor

An intelligent machine learning web application that predicts the price of common crops across different Nigerian states based on user inputs (crop, location, month). Built with Flask and deployed using Azure Web Apps.

---

## 📌 Overview

This app allows users (farmers, marketers, and consumers) to get estimated prices for crops based on historical market data. It’s trained on real datasets and serves as a demonstration for AI-driven solutions in agriculture.

---

## ✨ Features

- ✅ Predicts crop prices by state and month
- ✅ Handles unknown inputs with smart suggestions
- ✅ Simple and responsive UI
- ✅ Built with Python (Flask + Scikit-learn)
- ✅ Trained on personal research of some of the Nigeria food prices

---

## 🛠️ Technologies Used

- Python 3.9+
- Flask
- Scikit-learn
- Pandas
- Bootstrap 5
- Azure App Service (for deployment)

---

## 📁 Project Structure

── app.py # Main Flask application
├── utils.py # Prediction logic
├── train_model.py # Script to train and save model
├── model.pkl # Saved machine learning model
├── sample_data.csv # Cleaned data used for training
├── README.md # Project documentation


---

## 🚀 How It Works

1. User selects a crop, state, and month from the UI.
2. The app sends the inputs to `utils.py`.
3. The model predicts based on trained patterns from `sample_data.csv`.
4. If input is slightly incorrect, it will suggest closest match.

---

## 🖼️ Screenshots

![App Screenshot](https://via.placeholder.com/600x400.png?text=Market+Price+Predictor+App)

---

## 🧪 How to Run Locally

1. Clone this repository:
```bash
git clone https://github.com/your-username/agric-price-predictor.git
cd agric-price-predictor

```

2. Create a virtual environment:


```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run the app:

```bash
python app.py
``` 


##### 📝 Sample Inputs
- Crops: Maize, Rice, Yam, Sorghum

- Locations: Kano, Kaduna, Lagos, Bauchi

- Months: 1 to 12 (for Jan–Dec, precisely for 2025 which is the current year)

###### ⚠️ Limitations
- Predictions are based on historical data and may not reflect current market shocks.

- Some crops or locations might have sparse data.

- Not all months may have strong prediction signals.

###### 🙏 Acknowledgements

3MTT Nigeria & NITDA


📬 Contact
Built by Abdulsomad Abdulwahab for the 3MTT Knowledge Showcase
Email: abdulsomad005@gmail.com
GitHub: github.com/Roslaan001


## Author
Abdulwahab Abdulsomad Olayiwola – 3MTT Cloud Computing Cohort 3
