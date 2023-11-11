from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt

@api_view(['POST'])
@csrf_exempt
def userCommand(request):
  if request.method == 'POST':
    postdata = request.data
    command = postdata.get('command') 
    
    print(command)

    return Response({
        'status': 200,
        'message': "success"
    }, status=status.HTTP_200_OK)
