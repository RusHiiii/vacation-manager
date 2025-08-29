from django.db import models

class Year(models.TextChoices):
    CURRENT_YEAR = 'CURRENT', 'Année N'
    NEXT_YEAR = 'NEXT', 'Année N + 1'