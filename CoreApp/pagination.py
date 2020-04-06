from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class StandardPagination(PageNumberPagination):
    page_size = 6
    page_query_param = 'size'
    max_page_size = 10

    def get_paginated_response(self, data):
        context ={
            'next' : self.get_next_link(),
            'previous' : self.get_previous_link(),
            'count' : self.page.paginator.count,
            'results' : data
        }

        return Response(context)
