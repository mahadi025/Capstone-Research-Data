from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models


class ModelTests(TestCase):
    def test_create_transfer_learning_model(self):
        model = models.TransferLearningModel.objects.create(
            model_name="MobileNetV3Small",
            epochs="25",
            batch_size="32",
            learning_rate="0.001",
            optimizer="Adam",
            dataset="Smote",
            training_accuracy="80",
            validation_accuracy="80",
            testing_accuracy="80",
        )

        self.assertEqual(str(model), f"{model.model_name}-{model.dataset}")
