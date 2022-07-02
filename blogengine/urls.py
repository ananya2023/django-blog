
from django.contrib import admin
from django.urls import path
from django.urls import include
from .views import redirect_blog

from django.views.static import serve
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('', redirect_blog),

]
