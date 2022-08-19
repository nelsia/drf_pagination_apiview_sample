from rest_framework import serializers

from myapp.models import DRFPaginationModel


class DRFPaginationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DRFPaginationModel
        fields = "__all__"


