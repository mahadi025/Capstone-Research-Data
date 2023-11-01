from .serializers import TransferLearningModelSerializer
from core.models import TransferLearningModel
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters


class GetMethod(viewsets.ModelViewSet):
    queryset = TransferLearningModel.objects.all().order_by(
        "model_name",
        "dataset",
        "epochs",
        "batch_size",
        "learning_rate",
        "dropout",
        "optimizer",
    )
    serializer_class = TransferLearningModelSerializer
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = [
        "model_name",
        "batch_size",
        "learning_rate",
        "epochs",
        "dropout",
        "optimizer",
        "dataset",
    ]
