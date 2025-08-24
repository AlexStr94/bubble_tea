from django.apps import AppConfig
import os


class BubbleTeaConfig(AppConfig):
    name = "bubble_tea"
    verbose_name = "Bubble Tea"

    path = os.path.dirname(__file__)