from .models import Pessoa
from rest_framework import serializers


class PessoaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Pessoa
        fields = ['id', 'nome', 'idade']
