
import math

from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def home():
    bmi = None
    category = None
    error = None
    interpretation = None

    if request.method == "POST":
        try:
            height = float(request.form["height"])
            weight = float(request.form["weight"])

            if not math.isfinite(height) or not math.isfinite(weight):
                error = "Please enter finite numeric values."

            elif not (0.5 <= height <= 2.8):
                error = "Please enter a height between 0.5 and 2.8 metres."

            elif not (2 <= weight <= 500):
                error = "Please enter a weight between 2 and 500 kilograms."

            else:
                bmi = round(weight / (height ** 2), 2)

                if bmi < 18.5:
                    category = "Underweight"
                    interpretation = (
                        "Your BMI is below the standard adult "
                        "healthy-weight range."
                    )

                elif bmi < 25:
                    category = "Healthy weight"
                    interpretation = (
                        "Your BMI falls within the standard adult "
                        "healthy-weight range."
                    )

                elif bmi < 30:
                    category = "Overweight"
                    interpretation = (
                        "Your BMI is above the standard adult "
                        "healthy-weight range."
                    )

                else:
                    category = "Obesity"
                    interpretation = (
                        "Your BMI is in the obesity range under "
                        "standard adult BMI categories."
                    )

        except (ValueError, KeyError):
            error = "Please enter valid height and weight."

    return render_template(
        "index.html",
        bmi=bmi,
        category=category,
        error=error,
        interpretation=interpretation
    )


if __name__ == "__main__":
    app.run(debug=True)
