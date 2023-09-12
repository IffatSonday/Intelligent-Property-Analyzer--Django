from django.http import HttpResponse
from django.shortcuts import render
import pickle
import pandas as pd
import sys
from .models import price_prediction

def index(request):
    return render(request, 'index.html')

def getPredictions(input_data):
    # Load the machine learning model
    model = pickle.load(open('./static/model.pkl', 'rb'))

    # Ensure that the input_data columns match the features used during training
    prediction = model.predict(input_data)

    return prediction

def prediction(request):
    # Initialize predicted_price with a default value (None)
    predicted_price = None

    # Load the external dataset 
    df = pd.read_csv('C:/Users/Effat/Desktop/TCS RIO Internship/IPA_Dataset.csv')

    if request.method == 'POST':
        # Sample input data as a dictionary
        LotArea = request.POST['LotArea']
        MSZoning = request.POST['MSZoning']
        BldgType = request.POST['BldgType']
        ExterQual = request.POST['ExterQual']
        OverallQual = request.POST['OverallQual']
        GarageType = request.POST['GarageType']
        CentralAir = request.POST['CentralAir']
        Heating = request.POST['Heating']

        matching_records = []

        # Iterate through the external dataset
        for index, row in df.iterrows():
            # Convert 'LotArea' to a float
            lot_area = float(row['LotArea'])
            
            # Convert 'feature1' to a float
            feature1_float = float(LotArea)

            # Check for matching 'LotArea' and 'ExterQual' values with tolerance
            if abs(lot_area - feature1_float) < 1e-6 and row['ExterQual'] == ExterQual:
                matching_records.append(row)

        if matching_records:
            predicted_price = matching_records[0]['SalePrice']

        # Create a new Prediction instance and save it to the database
        if predicted_price is not None:
            prediction_instance = price_prediction(                
                LotArea=LotArea,
                MSZoning=MSZoning,
                BldgType=BldgType,
                ExterQual=ExterQual,
                OverallQual=OverallQual,
                GarageType=GarageType,
                CentralAir=CentralAir,
                Heating=Heating,
                predicted_price=predicted_price
            )
            prediction_instance.save()

    print("Debugging: Prediction value =", predicted_price, file=sys.stderr)
    # Assuming result is a single prediction, pass it to the template
    return render(request, 'prediction.html', {'predicted_price': predicted_price})

    return render(request, 'prediction.html')  # Render the initial form
