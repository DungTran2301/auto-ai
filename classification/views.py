from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect, csrf_exempt
import time
import os
import pickle
from classification.model_training.utils.text_process import preprocess
from sklearn.preprocessing import LabelEncoder

MODEL_PATH = "classification/model_training/models"
msv_model = pickle.load(open(os.path.join(MODEL_PATH,"linear_classifier.pkl"), 'rb'))

with open('classification/model_training/labels/label.txt', encoding='utf-8') as file:
   lines = file.readlines()


labels = [line.strip() for line in lines]

@api_view(['GET', 'POST'])
@csrf_exempt
def classify(request):
  if request.method == 'POST':
    postdata = request.data
    command = postdata.get('command') 

    document = preprocess(command)

    label = msv_model.predict([document])
    # t = label_encoder.inverse_transform(label)

    return Response({
        'status': 200,
        'message': "",
        'data': {
            'type': label[0],
            'typeStr': labels[label[0]].split("__label__")[1].replace("_", " ")
        }
    }, status=status.HTTP_200_OK)

    