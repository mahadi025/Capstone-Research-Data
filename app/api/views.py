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

    # def get_queryset(self):
    #     queryset = TransferLearningModel.objects.all()
    #     model_name = self.request.query_params.get("model_name")
    #     batch_size = self.request.query_params.get("batch_size")
    #     learning_rate = self.request.query_params.get("learning_rate")
    #     epochs = self.request.query_params.get("epochs")
    #     dropout = self.request.query_params.get("dropout")
    #     optimizer = self.request.query_params.get("optimizer")
    #     dataset = self.request.query_params.get("dataset")

    #     if model_name:
    #         queryset = queryset.filter(model_name=model_name)
    #     if batch_size:
    #         queryset = queryset.filter(batch_size=batch_size)
    #     if learning_rate:
    #         queryset = queryset.filter(learning_rate=learning_rate)
    #     if epochs:
    #         queryset = queryset.filter(epochs=epochs)
    #     if dropout:
    #         queryset = queryset.filter(dropout=dropout)
    #     if dataset:
    #         queryset = queryset.filter(dataset=dataset)
    #     if optimizer:
    #         queryset = queryset.filter(optimizer=optimizer)

    #     return queryset
