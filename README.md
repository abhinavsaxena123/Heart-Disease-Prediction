# Heart-Disease-Prediction ❤️
### Cardio Health Risk Assessment

## 🪄 About
This project aims to predict the likelihood of heart disease in individuals based on various medical and demographic factors. Heart disease remains one of the leading causes of mortality globally, and early prediction can play a crucial role in preventing adverse outcomes. This machine learning model uses clinical data to assess the probability of heart disease, helping in early detection and personalized treatment.

## 📈 Data Source
The Datasource for this project was taken from Kaggle dataset Cardio Health Risk Assessment Dataset.
* Dataset Link: https://www.kaggle.com/datasets/kapoorprakhar/cardio-health-risk-assessment-dataset/data

## Dataset Features:
```
The prediction is based on the following 13 features:
* Age: Age of the individual
* Sex: Gender of the individual (1 = male, 0 = female).
* Chest pain type: Different types of chest pain experienced, classified into four categories.
* Resting Blood Pressure (BP): Blood pressure level when at rest.
* Cholesterol: Serum cholesterol in mg/dl.
* Fasting Blood Sugar (FBS) over 120: Whether fasting blood sugar is over 120 mg/dl (1 = true, 0 = false).
* Resting Electrocardiographic (EKG) Results: Results from the EKG test, represented in numerical categories (0,1,2).
* Maximum Heart Rate (Max HR): Maximum heart rate achieved during exercise.
* Exercise-Induced Angina: Angina induced by exercise (1 = yes, 0 = no).
* ST Depression: Depression in the ST segment of the EKG during exercise relative to rest.
* Slope of the ST Segment: Slope of the peak exercise ST segment (1, 2, 3)
* Number of Major Vessels (Fluoroscopy): Number of major vessels colored by fluoroscopy (range 0-3).
* Thallium Stress Test: Result of thallium stress test (3 = normal, 6 = fixed defect, 7 = reversible defect).
```

## Project Overview 
The Heart Disease Prediction project uses machine learning to classify individuals at risk of heart disease. The project includes data visualization, statistical analysis, model training with cross-validation, and a web app to facilitate user interaction with the model.

## Features 🌟
* Data Analysis and Visualization: EDA to understand feature distribution and correlations

* Statistical Tests: Validating feature significance and hypothesis testing.
* Model Building with CV and Grid Search: Cross-validated model selection with hyperparameter tuning.
* Streamlit Web Application: For user-friendly predictions.

## ⚙️ SetUp Instructions:
### 1. Clone the Repository
```
git clone https://github.com/abhinavsaxena123/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
```

### 2. Set Up a Virtual Environment
* Using venv (for Python):
```
python3 -m venv env                        # Use `python` on Windows instead of `python3`
source env/bin/activate                    # On Windows, use source env/Scripts/activate
```
OR
* To create a Conda environment:
```
conda create -n heart_disease_env python=3.8
conda activate heart_disease_env
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```

## Usage
### 1. Run the Jupyter Notebook:
```
jupyter notebook
```
OR 

### 2. Run the Streamlit App:
```
streamlit run app.py
```


## Exploratory Data Analysis (EDA)
The EDA process includes the following steps to better understand the data:
* Feature Distribution: Visualizing the distribution of continuous and categorical features
* Correlations: Heatmaps and scatter plots to observe relationships between features.
* Heart Disease Presence: Analyzing how features correlate with heart disease outcomes.

## Visualizations 
The following plots have been generated:
* Distribution plot for Heart Disease By gender: 
<img width="437" alt="image" src="https://github.com/user-attachments/assets/89becf9c-3fa9-40d0-b87a-6b5611747145">

* Distribution of Max Heart Rate by Heart Disease Status:
<img width="476" alt="image" src="https://github.com/user-attachments/assets/4aa458e5-6f5d-4d44-885b-d6c98c8f4834">


## Results From Statistical Tests
To ensure statistical relevance, I conducted tests such as:

* 1. Chi-Square Test : To examine associations between categorical variables
   > Variables Sex, Chest pain type, Exercise angina, Thallium, and Number of vessels fluro, EKG results
   show a statistically significant association with 'Heart Disease',  while FBS over 120 does not.

* 2. Independent t-test: For comparing mean values between groups.
   <img width="200" alt="image" src="https://github.com/user-attachments/assets/0dc21351-d236-4af4-9da9-ab37e48e4da1">
   
   > The results suggest that Age, BP, Max HR, and ST Depression are more strongly associated with heart disease status, and they may serve as valuable features for 
    predictive modeling.

* 3. ANOVA Test: To assess differences in feature distributions.
   > The ANOVA results indicate significant associations between various continuous variables (Max HR, ST Depression, BP) and categorical variables (Chest Pain Type, Slope 
    of ST, Thallium).

   > Particularly strong associations were found between the slope of the ST segment and both Max HR and ST depression, highlighting their potential importance in 
   cardiovascular assessment.

   > Significant differences in Max HR and ST depression based on chest pain type suggest that understanding chest pain characteristics can help predict heart disease 
    outcomes and tailor interventions.

* 4. Point-Biserial Correlation Coefficient: Correlation with Target Variable.
<img width="468" alt="image" src="https://github.com/user-attachments/assets/a1f40374-3be3-41f2-b983-7dea85909898">

  > Age, Max HR, and ST Depression appear to be important predictors of heart disease based on their strong correlations and significance levels.

  > While BP and Cholesterol show some level of correlation, they may not be as reliable as the other features in predicting heart disease, especially Cholesterol, which is 
  close to the significance threshold.

These tests provide insights into which features are statistically significant for predicting heart disease.

## Model Building ⌛
Model-building process includes:
1. 





## Results and Discussion
### Model Performance



## Discussion
The model provides insights into the impact of different features on heart disease prediction. Results from statistical tests and feature importance analysis confirm that factors like age, chest pain type, and cholesterol levels are significant predictors.







### Future Improvements 
* Enhanced Feature Engineering: Adding more medical data and extract more detailed features.
* Advanced Models: Experimenting with ensemble techniques and deep learning for potentially better accuracy.
* Advanced Visualizations: Interactive dashboards for data visualization and trend analysis.


