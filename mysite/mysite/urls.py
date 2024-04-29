from django.contrib import admin
from django.urls import path
from myapp.views import comment_text, start_middle_end, comment_with_date, comment_update_sme, \
    comment_without_k_with_c, filter_date_comm_blog

urlpatterns = [
    path('admin/', admin.site.urls),
    path('filter-date-comm-blog/', filter_date_comm_blog),
    path('comments-text/', comment_text),
    path('start-middle-end/', start_middle_end),
    path('comments-with-date/', comment_with_date),
    path('comments-update-sme/', comment_update_sme),
    path('comments-without-k-with-c/', comment_without_k_with_c),
]
