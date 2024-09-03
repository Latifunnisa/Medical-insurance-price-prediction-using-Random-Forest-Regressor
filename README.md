# Medical Insurance Price Prediction using Random Forest Regressor

## Overview

This project reports delves into the development of a predictive model for medical insurance pricing. The primary objective is to leverage data science techniques to create a model that can accurately forecast insurance price based on various factors such as age, gender, body mass index (BMI), smoking status, and location. By analyzing historical data and identifying key trends, the model aims to provide a robust tool for price prediction that can be used by insurance companies to enhance their pricing strategies and improve customer satisfaction. Using the Random Forest Regressor, the model has achieved an R² Score of 86.73%, indicating a strong ability to predict insurance prices accurately.

## Project Structure

### Data Collection

The dataset includes various factors that influence medical insurance costs. These factors include demographic data (age, gender), lifestyle choices (smoking status), and health indicators (BMI).

### Data Preprocessing

Before feeding the data into the model, several preprocessing steps were performed:

- **Handling Missing Data**: Missing values were addressed using appropriate imputation techniques.
- **Outlier Detection and Removal**: Outliers in features like BMI and smoking status were identified and treated to prevent skewed model predictions.
- **Feature Scaling**: Continuous variables were scaled to ensure uniformity across features, improving model performance.

### Exploratory Data Analysis (EDA)

Visualizations and statistical analyses were conducted to understand the distribution of data and relationships between features. Key insights were derived, such as the impact of smoking on insurance costs and the correlation between age and BMI.

### Model Training

A Random Forest Regressor was chosen due to its robustness and ability to handle complex datasets with multiple features. The model was trained on the preprocessed dataset, with hyperparameter tuning performed to optimize performance.

### Model Evaluation

The model’s accuracy was measured using metrics like the R² score, which reached 86.73%. Predictions were compared against actual values, and error metrics were calculated to assess model reliability.

### User Interface

A web-based interface was developed to allow users to input their personal details and receive an estimated insurance price. The interface is user-friendly and designed to make predictions accessible to non-technical users.

## Tools Used

- **PyCharm**: Used as the primary Integrated Development Environment (IDE) for developing the Python scripts.
- **Jupyter Notebook**: Employed for exploratory data analysis (EDA) and model training, offering an interactive environment for data exploration.

To run this project locally, follow these steps:
## Installation and Setup

1. **Install Dependencies**: 
   Ensure that you have Python installed. Install the required packages using:
   ```bash
   pip install -r requirements.txt
2. **Run the Application**: Start the web application by running:
   ```bash
   python app.py

## Usage 
1. **Model Training**
Run the training script to train the Random Forest Regressor on the provided dataset. This step will generate the model, which can be saved for later use.

2. **Web Interface**
Use the web interface to interact with the trained model. Enter details like age, gender, BMI, smoking status, and location to get a predicted insurance price.

## Results
The Random Forest model performs well, achieving an R² score of 86.73%. The predictions align closely with actual insurance prices, making this model a reliable tool for estimating insurance costs based on user inputs.

## Future Work
1. **Model Improvement**
Explore other machine learning algorithms like Gradient Boosting or Neural Networks to potentially enhance prediction accuracy.

2. **Feature Expansion**
Incorporate additional features such as medical history, exercise frequency, or diet to refine the prediction model.

3. **Deployment**
Consider deploying the application to a cloud platform like AWS or Heroku for broader accessibility.

## Acknowledgments
Special thanks to Kaggle - Medical Insurance Cost Prediction Dataset for providing the dataset used in this project.
