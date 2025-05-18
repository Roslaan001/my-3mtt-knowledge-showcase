from flask import Flask, request, render_template_string
from utils import predict_price
import pandas as pd

app = Flask(__name__)

# Load valid options
data = pd.read_csv("sample_data.csv")
CROPS = sorted(data['crop'].unique())
LOCATIONS = sorted(data['location'].unique())
MONTHS = list(range(1, 13))

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>🌾 Market Price Predictor</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <style>
        body {
            background: #f6f8fa;
            font-family: 'Segoe UI', sans-serif;
            padding-top: 50px;
        }
        .container {
            max-width: 500px;
            background: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.1);
        }
        .result {
            font-size: 1.3rem;
            margin-top: 20px;
        }
    </style>
</head>
<body>
<div class="container">
    <h2 class="mb-4 text-center">🌾AI Agriculture Price Predictor</h2>
    <form method="post">
        <div class="mb-3">
            <label for="crop" class="form-label">Select Crop</label>
            <select class="form-select" name="crop" required>
                {% for crop in crops %}
                    <option value="{{ crop }}">{{ crop }}</option>
                {% endfor %}
            </select>
        </div>

        <div class="mb-3">
            <label for="location" class="form-label">Select Location</label>
            <select class="form-select" name="location" required>
                {% for location in locations %}
                    <option value="{{ location }}">{{ location }}</option>
                {% endfor %}
            </select>
        </div>

        <div class="mb-3">
            <label for="month" class="form-label">Select Month</label>
            <select class="form-select" name="month" required>
                {% for month in months %}
                    <option value="{{ month }}">{{ month }}</option>
                {% endfor %}
            </select>
        </div>

        <button type="submit" class="btn btn-success w-100">Predict Price</button>
    </form>

    {% if prediction %}
        <div class="alert alert-info result text-center">
            <strong>Predicted Price:</strong> ₦{{ prediction }}
        </div>
    {% endif %}

    {% if error %}
        <div class="alert alert-danger mt-3 text-center">
            {{ error }}
        </div>
    {% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    error = None

    if request.method == "POST":
        crop = request.form["crop"]
        location = request.form["location"]
        month = int(request.form["month"])

        try:
            prediction = predict_price(crop, location, month)
        except Exception as e:
            error = "Something went wrong. Please try again."

    return render_template_string(
        HTML_TEMPLATE,
        crops=CROPS,
        locations=LOCATIONS,
        months=MONTHS,
        prediction=prediction,
        error=error
    )

if __name__ == "__main__":
    app.run(debug=False)
