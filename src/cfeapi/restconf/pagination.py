from rest_framework import pagination

class CFEAPIPagination(pagination.LimitOffsetPagination):
    # page_size = 5
    default_limit   = 5
    max_limit       = 20
    # max_limit = 1
    # limit_query_param = 'lim'
