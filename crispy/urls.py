from django.urls import path
from crispy.views import PatientListView, PatientDetailView, PatientCreateView, \
    PatientUpdateView, PatientDeleteView, test, HistoryDetailView, HistoryCreateView, \
    HistoryUpdateView, HistoryDeleteView, PrescriptionCreateView

urlpatterns = [
    path('', PatientListView.as_view(), name='patients'),
    path('patient/<int:pk>', PatientDetailView.as_view(), name='patient_detail'),
    path('history/<int:pk>', HistoryDetailView.as_view(), name='history_detail'),
    path('update/<int:pk>', PatientUpdateView.as_view(), name='patient_update'),
    path('delete/<int:pk>', PatientDeleteView.as_view(), name='patient_delete'),
    path('create/', PatientCreateView.as_view(), name='patient_create'),
    path('hiscreate/<int:ptid>', HistoryCreateView.as_view(), name='history_create'),
    path('hisupdate/<int:pk>', HistoryUpdateView.as_view(), name='history_update'),
    path('hisdelete/<int:pk>', HistoryDeleteView.as_view(), name='history_delete'),
    path('prescreate/<int:hisid>', PrescriptionCreateView.as_view(),
         name='prescription_create'),
    path('test/', test, name='test'),
]
