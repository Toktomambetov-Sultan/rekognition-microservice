from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.services import aws 


@api_view(['GET', 'POST'])
def recognition(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        print(request.data)   
        res = aws.match(request.data["file"])
        return Response(res, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        aws.upload([request.data])
        return Response("", status=status.HTTP_200_OK)