from django.shortcuts import render
from joblib import load
import numpy as np
from sklearn.preprocessing import StandardScaler

# Create your views here.
def predict(request):

    # Mappings
    if request.method == 'POST':

        # Collect All Data
        wheelbase = float(request.POST['wheelbase'])
        carlength = float(request.POST['carlength'])
        carwidth = float(request.POST['carwidth'])
        carheight = float(request.POST['carheight'])
        curbweight = float(request.POST['curbweight'])
        enginesize = float(request.POST['enginesize'])
        boreratio = float(request.POST['boreratio'])
        stroke = float(request.POST['stroke'])
        compressionratio = float(request.POST['compressionratio'])
        horsepower = float(request.POST['horsepower'])
        peakrpm = float(request.POST['peakrpm'])
        citympg = float(request.POST['citympg'])
        highwaympg = float(request.POST['highwaympg'])

        
        # Process The Data
        scaler = StandardScaler()
        inputs = np.array([wheelbase,carlength,carwidth,carheight,curbweight,enginesize,boreratio,stroke,compressionratio,horsepower,peakrpm,citympg,highwaympg])
        X = scaler.fit_transform(inputs.reshape(-1,1)).reshape(1,-1)

        # Make Prediciton
        model = load('model\car-price-rfr.joblib')
        price = str(np.round(model.predict(X), 2)[0])


        # Display Prediction
        return render(request, "index.html", {'price':price})

    return render(request, "index.html")