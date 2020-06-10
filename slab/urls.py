from django.conf.urls import url
from django.contrib import admin
from .views import CommissionView, GetSlabData, GetSelectedData, PostCreateCommission

urlpatterns = [
    url(r"^get_slab_data/$", GetSlabData.as_view(), name="get_slab_data"),
    url(r"^get_selected_data/$", GetSelectedData.as_view(), name="get_selected_data"),
    url(r"^commission/$", CommissionView.as_view(), name="commission_view"),
    url(r"^post_create/$", PostCreateCommission.as_view(), name="post_create"),
]
