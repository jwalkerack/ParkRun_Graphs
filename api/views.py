from rest_framework.views import APIView
from rest_framework.response import Response
from run.models import timings
from .serializers import TimingsSerializer
from rest_framework.pagination import PageNumberPagination


class LocationView(APIView):
    def get(self, request):
        locations = timings.objects.all()
        paginator = PageNumberPagination()
        page = request.query_params.get('page', 1)
        page_size = request.query_params.get('page_size', 100)
        paginator.page_size = page_size
        result_page = paginator.paginate_queryset(locations, request)
        serializer = TimingsSerializer(result_page, many=True)
        response_data = {
            "current_page": paginator.page.number,
            "count": locations.count(),
            "total_pages": paginator.page.paginator.num_pages,
            "results": serializer.data
        }
        return Response(response_data)
