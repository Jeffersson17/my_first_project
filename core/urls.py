from django.urls import path
from core.views import PessoaListView, PessoaCreateView, PessoaUpdateView, PessoaDeleteView

urlpatterns = [
    path('pessoa/', PessoaListView.as_view(), name="list"),
    path('create/', PessoaCreateView.as_view(), name="create"),
    path('editar/<int:pk>/', PessoaUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', PessoaDeleteView.as_view(), name='delete'),
]
