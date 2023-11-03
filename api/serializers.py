from rest_framework import serializers
from core.models import CapstoneData


class CapstoneDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CapstoneData
        fields = [
            "id",
            "model_name",
            "batch_size",
            "epochs",
            "learning_rate",
            "optimizer",
            "dataset",
            "dropout",
            "training_accuracy",
            "validation_accuracy",
            "testing_accuracy",
            "accuracy_graph",
            "loss_graph",
        ]
