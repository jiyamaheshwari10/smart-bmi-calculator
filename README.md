
# Smart BMI Calculator

A simple, responsive web application that calculates Body Mass Index (BMI) from a user's height and weight. It displays the BMI value, the corresponding adult BMI category, and a brief interpretation of the result.

## Features

- Calculates BMI using height and weight.
- Classifies results into standard adult BMI categories.
- Displays a simple interpretation of the result.
- Validates user input and handles invalid values.
- Includes a BMI reference guide.
- Provides a clear button to reset the calculator.
- Uses a clean, responsive interface.

## Tech Stack

- **Python** — BMI calculation and application logic
- **Flask** — Web framework and request handling
- **HTML** — Page structure and input form
- **CSS** — Styling and responsive layout

## Project Structure

```text
smart-bmi-calculator/
├── app.py
├── README.md
├── requirements.txt
├── static/
│   └── style.css
└── templates/
    └── index.html
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
cd smart-bmi-calculator
```

Replace `YOUR_REPOSITORY_URL` with your actual GitHub repository URL.

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

**Windows Command Prompt:**

```bat
.venv\Scripts\activate
```

**Windows PowerShell:**

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open this address in your browser:

http://127.0.0.1:5000/

## BMI Formula

BMI is calculated using:

BMI = Weight (kg) / Height (m)²

For example, for a height of 1.70 metres and a weight of 65 kilograms:

BMI = 65 / (1.70 × 1.70) = 22.49

## Learning Outcomes

Through this project, I practised:

- Building a web application using Flask.
- Connecting HTML forms to Python backend logic.
- Using conditional statements for BMI classification.
- Handling invalid inputs and exceptions.
- Organising a Python project into separate files.
- Styling a web interface using CSS.

## Disclaimer

BMI is a screening measure, not a medical diagnosis. Standard adult BMI categories may not be appropriate for children, teenagers, pregnant individuals, or every clinical situation.
