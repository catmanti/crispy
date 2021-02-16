from django.urls import path
from crispy.views import PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView, test, HistoryDetailView

urlpatterns = [
    path('', PatientListView.as_view(), name='patients'),
    path('patient/<int:pk>', PatientDetailView.as_view(), name='patient_detail'),
    path('history/<int:pk>', HistoryDetailView.as_view(), name='hitory_detail'),
    path('update/<int:pk>', PatientUpdateView.as_view(), name='patient_update'),
    path('delete/<int:pk>', PatientDeleteView.as_view(), name='patient_delete'),
    path('create/', PatientCreateView.as_view(), name='patient_create'),
    path('test/', test, name='test'),
]
