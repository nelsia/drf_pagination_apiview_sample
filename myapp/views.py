from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination # ページネーションのクラス

from myapp.models import DRFPaginationModel
from myapp.serializers import DRFPaginationSerializer


class DRFPaginationSampleView(APIView, LimitOffsetPagination):
    def get(self, request):
        # モデルから全データを取得
        q = DRFPaginationModel.objects.all()

        results = self.paginate_queryset(q, request, view=self)
        t = DRFPaginationSerializer(results, many=True)

        # t.dataでpaginationされたデータにアクセスできる
        res = {
            "data": t.data,
            "test": "このように好きな値とかもセットできる"
        }

        return self.get_paginated_response(res)

