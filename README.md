# Boston House Price Prediction Using Linear Regression

This project is a simple Machine Learning Web Application that predicts housing prices in Boston based on various input features. It uses a Linear Regression model trained on the Boston Housing dataset and is built using Flask for the web interface.

# Dataset Description

The model is trained on the Boston Housing Dataset, which includes the following features:

CRIM: Per capita crime rate by town

ZN: Proportion of residential land zoned for large lots

INDUS: Proportion of non-retail business acres per town

CHAS: Charles River dummy variable (1 if tract bounds river; 0 otherwise)

NOX: Nitric oxides concentration (parts per 10 million)

RM: Average number of rooms per dwelling

AGE: Proportion of owner-occupied units built prior to 1940

DIS: Weighted distances to five Boston employment centers

RAD: Index of accessibility to radial highways

TAX: Full-value property-tax rate per $10,000

PTRATIO: Pupil-teacher ratio by town

B: 1000(Bk - 0.63)^2 where Bk is the proportion of Black residents

LSTAT: Percentage of lower status population

MEDV: Median value of owner-occupied homes in $1000s (target variable)


# Model training

The model was trained using Linear Regression from sklearn.linear_model on the scaled Boston Housing dataset.

model coefficients:-  
[-0.7049, 0.9103, -0.0210, 0.6984, -1.7005, 2.4840,
 0.4171, -2.4827, 2.4094, -1.7804, -2.1417, 0.8313,
 -3.9181]

Intercept: 22.54

# Evaluation Metrics

| Metric                    | Value     |
| ------------------------- | --------- |
| Mean Squared Error (MSE)  | **25.47** |
| Mean Absolute Error (MAE) | **3.54**  |
| Root Mean Squared Error   | **5.05**  |
| R² Score                  | **0.731** |
| Adjusted R² Score         | **0.706** |

These results suggest that the model explains around 73% of the variance in the target variable on the test data.

### Software and tools requirements

Github account
VS Code
Heroku account
Git CLI
numpy
pandas
scikit-learn
matplotlib
seaborn
pickle5
flask

Housing_Prediction_Linear_Reg_Project/
│
├── app.py                     # Flask app
├── model.pkl                  # Trained model file
├── templates/
│   └── index.html             # HTML form
├── static/
│   └── style.css              # Custom CSS
├── requirements.txt           # Python dependencies
├── README.md                  # Project readme
└── .gitignore

# Clone the repository
git clone https://github.com/Ajay-Kumar-Prasad/Housing_Prediction_Linear_Reg_Project.git
cd Housing_Prediction_Linear_Reg_Project

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # For macOS/Linux
venv\Scripts\activate     # For Windows

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
