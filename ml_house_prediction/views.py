from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
import pickle

model = pickle.load(open("ml_house_prediction/regmodel.pkl","rb"))
scaler = pickle.load(open("ml_house_prediction/scaling.pkl","rb"))
# Create your views here.

@api_view(["GET",])
def home(request):
    return render(request, 'home.html')

@api_view(["POST",])
def predict(request):
    import numpy as np
    data = request.data
    data=[float(x) for x in request.data.values()]
    final_input=scaler.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output=model.predict(final_input)[0]
    data = {
        "prediction_text":"The House price prediction is {}".format(output)
    }
    return render(request,"home.html",data)