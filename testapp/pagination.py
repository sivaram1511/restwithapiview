from rest_framework import pagination
class MyPagination(pagination.PageNumberPagination):
    page_size=1
    page_query_param='mypage'
    page_size_query_param='num'
    max_page_size=3
class MyPagination2(pagination.LimitOffsetPagination):
    default_limit=3
    limit_query_param="mylimit"
    offset_query_param="myoffset"
    max_limit=3
class MyPagination3(pagination.CursorPagination):
    Ordering='esal'
