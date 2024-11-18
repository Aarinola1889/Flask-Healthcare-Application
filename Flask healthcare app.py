#Step 1: Create the Flask Web Application
from flask import Flask
from flask_pymongo import PyMongo
from config import Config

mongo = PyMongo()

def create_app(config_class=Config):
    app = Flask(_name_)
    app.config.from_object(config_class)

    mongo.init_app(app)

    from app import routes
    app.register_blueprint(routes.main)

    return app

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from user import User
from pymongo import MongoClient
import numpy as np

# Connect to MongoDB
client = MongoClient('mongodb://127.0.0.1:27017/')
db = client['database']
collection = db['survey_data']

# Fetch data from MongoDB and create User objects
users = []
for data in collection.find():
    user = User(
        name=data['name'],
        email=data['email'],
        age=data['age'],
        gender=data['gender'],
        marital_status=data['marital_status'],
        education=data['education'],
        employment_status=data['employment_status'],
        occupation=data['occupation'],
        income=data['income'],
        expenses=data['expenses']
    )
    users.append(user)
    
# Convert User objects to a list of dictionaries
user_dicts = [user.to_dict() for user in users]

# Create a DataFrame and save to CSV
df = pd.DataFrame(user_dicts)
df.to_csv('data.csv', index=False)
print("Data saved to data.csv")

images_folder = 'charts'
os.makedirs(images_folder, exist_ok=True)

# 1. Income Distribution by Age
plt.figure(figsize=(12, 6))
plt.scatter(df['age'], df['income'])
plt.title('Income Distribution by Age')
plt.xlabel('Age')
plt.ylabel('Income')
plt.savefig(os.path.join(images_folder, 'income_by_age.png'))
plt.show()

# 2. Gender distribution across spending categories
plt.figure(figsize=(12, 6))
for category in expense_categories:
    male_avg = df[df['gender'] == 'male'][category].mean()
    female_avg = df[df['gender'] == 'female'][category].mean()
    
    plt.bar(category + '_male', male_avg, label='Male' if category == expense_categories[0] else '')
    plt.bar(category + '_female', female_avg, label='Female' if category == expense_categories[0] else '')

plt.title('Average Spending by Gender and Category')
plt.xlabel('Expense Category')
plt.ylabel('Average Spending')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout
plt.savefig(os.path.join(images_folder, 'spending_by_gender.png'))
plt.show()

# 3. Income Distribution by Education Level
plt.figure(figsize=(12, 6))
sns.boxplot(x='education', y='income', data=df)
plt.title('Income Distribution by Education Level')
plt.xlabel('Education Level')
plt.ylabel('Income')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(images_folder, 'income_by_education.png'))
plt.show()

# 4. Employment Status and Income
plt.figure(figsize=(10, 6))
sns.boxplot(x='employment_status', y='income', data=df)
plt.title('Income Distribution by Employment Status')
plt.xlabel('Employment Status')
plt.ylabel('Income')
plt.savefig(os.path.join(images_folder, 'income_by_employment_status.png'))
plt.show()

# 5. Marital Status and Expenses
plt.figure(figsize=(12, 6))
df.groupby('marital_status')[expense_categories].mean().plot(kind='bar', stacked=True)
plt.title('Average Expenses by Marital Status')
plt.xlabel('Marital Status')
plt.ylabel('Average Expenses')
plt.legend(title='Expense Category', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.savefig(os.path.join(images_folder, 'expenses_by_marital_status.png'))
plt.show()

# 6. Occupation and Income
plt.figure(figsize=(12, 6))
occupation_income = df.groupby('occupation')['income'].mean().sort_values(ascending=False)
occupation_income.plot(kind='bar')
plt.title('Average Income by Occupation')
plt.xlabel('Occupation')
plt.ylabel('Average Income')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(os.path.join(images_folder, 'income_by_occupation.png'))
plt.show()

# 7. Age Distribution by Employment Status
plt.figure(figsize=(10, 6))
sns.boxplot(x='employment_status', y='age', data=df)
plt.title('Age Distribution by Employment Status')
plt.xlabel('Employment Status')
plt.ylabel('Age')
plt.savefig(os.path.join(images_folder, 'age_by_employment_status.png'))
plt.show()

print("All visualizations saved as PNG files in the 'images' folder.")

class User:
    def _init_(self, name, email, age, gender, marital_status, education, employment_status, occupation, income, expenses):
        self.name = name
        self.email = email
        self.age = age
        self.gender = gender
        self.marital_status = marital_status
        self.education = education
        self.employment_status = employment_status
        self.occupation = occupation
        self.income = income
        self.expenses = expenses

    def to_dict(self):
        return {
            'name': self.name,
            'email': self.email,
            'age': self.age,
            'gender': self.gender,
            'marital_status': self.marital_status,
            'education': self.education,
            'employment_status': self.employment_status,
            'occupation': self.occupation,
            'income': self.income,
            **self.expenses
        }