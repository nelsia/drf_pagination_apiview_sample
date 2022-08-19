from django.db import models


class DRFPaginationModel(models.Model):
    col1 = models.CharField(max_length=30)
    col2 = models.CharField(max_length=30)

    def __str__(self):
        return self.col1

