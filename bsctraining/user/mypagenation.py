from rest_framework.pagination import LimitOffsetPagination

class mylimitoffsetpagination(LimitOffsetPagination):
    default_limit = 5
