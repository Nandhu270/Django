from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

class CustomPagination(PageNumberPagination):
    page_query_param = 'page_emp'
    page_size_query_param = 'page_size'
    page_size = 3
    max_page_size = 10

    def get_paginated_response(self, data):
        return Response({
            "next" : self.get_next_link(),
            "prev" : self.get_previous_link(),
            "count" : self.page.paginator.count,
            'page_size' : self.page_size,
            'result' : data
        })