Flask Healthcare Application

## Project Overview
This Python script demonstrate the use of collecting and analyzing user expense data for a data analysis company in Washington, DC, the objective is to analyze their income spending in preparation for a new product launch in the healthcare industry.

## Features
- Flask Web App: User interface for data collection.
- MongoDB Integration: Stores user data in a NoSQL database.
- Python Class: Processes user data and saves it to a CSV file.
- Data Analysis: Jupyter notebook for visualizing user expenses.
- Hosting: Can be deployed on AWS EC2 for broader access.

## Requirement
- Python 3.x
- MongoDB
- Flask
- Jupyter Notebook
- Amazon web service (AWS)

## Usage
1. Ensure you have all required libraries installed:
pip install -r requirements.txt
Flask
pymongo
pandas
matplotlib
seaborn

2. Ensure MongoDB is installed and running. You can start MongoDB using:
sudo systemctl start mongodb

3. Run the Flask Application
python app.py

4. Data Analysis in Jupyter Notebook. To analyze and visualize the collected data, open the Jupyter notebook:
jupyter notebook

5. Exporting the Analysis
The Jupyter notebook automatically saves visualizations as PNG files in the folder:
expenses_by_category.png
expenses_by_age.png


## File instruction
- Flask healthcare app.py: Python Script for developing a survey tool for collecting participants' data. 
- README.txt: Instructions on how to access and utilize the code.

