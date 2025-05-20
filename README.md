Boston House Price Prediction Using Linear Regression
This project is a simple Machine Learning Web Application that predicts housing prices in Boston based on various input features. It uses a Linear Regression model trained on the Boston Housing dataset and is built using Flask for the web interface.

Predicts median house prices in Boston.
The project uses the Boston Housing Dataset, which includes the following features:

CRIM: Per capita crime rate by town

ZN: Proportion of residential land zoned for large lots

INDUS: Proportion of non-retail business acres per town

CHAS: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)

NOX: Nitric oxides concentration (parts per 10 million)

RM: Average number of rooms per dwelling

AGE: Proportion of owner-occupied units built before 1940

DIS: Weighted distances to employment centers

RAD: Index of accessibility to radial highways

TAX: Property-tax rate

PTRATIO: Pupil–teacher ratio

B: Proportion of Black residents

LSTAT: % lower status of the population

MEDV: Median value of owner-occupied homes (target)



### Software and tools requirements

1.Github account
2.VS Code
3.Heroku account
4.Git CLI

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
