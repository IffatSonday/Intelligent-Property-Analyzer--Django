
from django.contrib import admin
from django.urls import path, include


#django admon header customization

admin.site.site_header="IntelliPropAnalyser Admin Dashboard"
admin.site.site_title="IPA"
admin.site.index_title="Welcome to IPA Admin Dashboard"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('IPA.urls'))
]
