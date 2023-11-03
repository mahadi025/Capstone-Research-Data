from django.db import models
from django.conf import settings
import os
import uuid


def graph_accuracy_image_file_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid.uuid4()}{ext}"

    return os.path.join("uploads", "graph", "accuracy", filename)


def graph_loss_image_file_path(instance, filename):
    ext = os.path.splitext(filename)[1]
    filename = f"{uuid.uuid4()}{ext}"

    return os.path.join("uploads", "graph", "loss", filename)


class CapstoneData(models.Model):
    model_name = models.CharField(
        max_length=255,
        choices=(
            ("MobileNetV3Small", "MobileNetV3Small"),
            ("ResNet50", "ResNet50"),
            ("EffecientNetB3", "EffecientNetB3"),
            ("VGG19", "VGG19"),
            ("XceptionNet", "XceptionNet"),
        ),
    )
    batch_size = models.CharField(
        max_length=4,
        choices=(("16", "16"), ("32", "32"), ("64", "64"), ("128", "128")),
        default="16",
    )
    epochs = models.CharField(
        max_length=4, choices=(("25", 25), ("50", 50)), default="25"
    )
    learning_rate = models.CharField(
        max_length=6, choices=(("0.001", "0.001"), ("0.005", "0.005")), default="0.001"
    )
    optimizer = models.CharField(
        max_length=10,
        choices=(("Adam", "Adam"), ("Adamax", "Adamax"), ("RMSprop", "RMSprop")),
        default="Adam",
    )
    dropout = models.CharField(
        max_length=5,
        choices=(("0.2", "0.2"), ("0.3", "0.3"), ("0.4", "0.4"), ("0.5", "0.5")),
        blank=True,
    )
    dataset = models.CharField(
        max_length=255,
        choices=(
            ("Original+Smote+Image Processing", "Original+Smote+Image Processing"),
            ("Original+Image Processing", "Original+Image Processing"),
            (
                "Original+Augmentation+Image Processing",
                "Original+Augmentation+Image Processing",
            ),
        ),
        default="Original+Image Processing",
    )
    training_accuracy = models.CharField(max_length=3, blank=True)
    validation_accuracy = models.CharField(max_length=3, blank=True)
    testing_accuracy = models.CharField(max_length=3, blank=True)
    accuracy_graph = models.ImageField(
        null=True, blank=True, upload_to=graph_accuracy_image_file_path
    )
    loss_graph = models.ImageField(
        null=True, blank=True, upload_to=graph_loss_image_file_path
    )

    class Meta:
        verbose_name_plural = "CapstoneData"

    def __str__(self):
        return (
            self.model_name
            + "-"
            + f"({self.dataset})"
            + "-"
            + f"({self.batch_size},{self.epochs},{self.learning_rate},{self.dropout},{self.optimizer})-({self.training_accuracy},{self.validation_accuracy},{self.testing_accuracy})"
        )
