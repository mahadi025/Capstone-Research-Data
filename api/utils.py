from rest_framework.response import Response
from core.models import CapstoneData
from .serializers import CapstoneDataSerializer


def getCapstoneDataList(request):
    capstoneData = CapstoneData.objects.all().order_by(
        "model_name", "dataset", "batch_size", "epochs", "learning_rate", "dropout"
    )
    serializer = CapstoneDataSerializer(capstoneData, many=True)
    return Response(serializer.data)


def getCapstoneDataDetail(request, pk):
    capstoneData = CapstoneData.objects.get(id=pk)
    serializer = CapstoneDataSerializer(capstoneData, many=False)
    return Response(serializer.data)
