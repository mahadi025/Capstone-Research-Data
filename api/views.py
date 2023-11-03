from .serializers import CapstoneDataSerializer
from core.models import CapstoneData
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .utils import getCapstoneDataList, getCapstoneDataDetail


@api_view(["GET"])
def getRoutes(request):
    routes = [
        {
            "Endpoint": "/capstone-data/",
            "method": "GET",
            "body": None,
            "description": "Returns all the list of recorded data",
        },
        {
            "Endpoint": "/capstone-data/id",
            "method": "GET",
            "body": None,
            "description": "Returns a single data",
        },
    ]
    return Response(routes)


@api_view(["GET"])
def getList(request):
    if request.method == "GET":
        return getCapstoneDataList(request)


@api_view(["GET"])
def getData(request, pk):
    if request.method == "GET":
        return getCapstoneDataDetail(request, pk)
