from drf_yasg.views import get_schema_view
from rest_framework.permissions import AllowAny
from drf_yasg import openapi

schema_view_v1 = get_schema_view(
    openapi.Info(
        title="Triplus API",
        default_version='v1',
        description="This is the triplus API",
        contact=openapi.Contact(email="utae@yeou.us"),
        license=openapi.License(name="Globe"),
    ),
    validators=['flex'],
    public=True,
    permission_classes=(AllowAny,),
)
