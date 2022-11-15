# CarPricePrediction-Django

---
This is a Web Deployment of the Car Price Predictior, Random Forest Regressot Model. The model had an R^2 score of 0.93. 

This is also available on Kaggle : 
https://www.kaggle.com/code/utkarshsaxenadn/car-price-prediction-eda-ml-models-r-2-0-93

---
Download the folder in Zip format, unzip it and open the command prompt. Make sure that you have Django installed.
After opening the command prompt, run the below command:

```
python ./manage.py runserver
```

In case of any error, first run: 


```
python ./manage.py migrate
```

Then run :

```
python ./manage.py runserver
```

Imports Required : 
Make sure that you have downloaded the following modules : 

1. Django
2. Numpy
3. Sklearn
4. Joblib

If these modules are not installed you may get the respective errors,

Django : The backend will not run and you will not get the port link.

Numpy & Sklearn : The preprocessing will not take place. 

Joblib : This is used for loading the model, so without this model will not exist.

Hope You enjoyed. 
