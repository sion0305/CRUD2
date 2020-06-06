from django.contrib import admin
from django.urls import path, include
import funccrud.urls
import funccrud.views
import portfolio.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', funccrud.views.welcome, name='welcome'),
    path('funccrud/', include(funccrud.urls)),
    #funccrud에 해당하는 애들이 많아서 funccrud.urls에 만들어 놓고 포함시키기
    path('portfolio/', portfolio.views.portfolio, name='portfolio'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#media 모을 위치 ??
