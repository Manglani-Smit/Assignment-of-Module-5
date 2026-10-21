from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination

# Question 2: PageNumberPagination (3 restaurants per page)
class RestaurantPageNumberPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 10


# Question 3: LimitOffsetPagination
class RestaurantLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2
    max_limit = 10