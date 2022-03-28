from rest_framework.routers import DefaultRouter
from core import viewsets

router = DefaultRouter()
router.register('zone', viewsets.ZoneViewSet)
router.register('department', viewsets.DepartmentViewset)
router.register('state', viewsets.StateViewset)

urlpatterns = router.urls
