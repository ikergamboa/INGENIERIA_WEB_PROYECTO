from rest_framework import serializers
from .models import Cliente

from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['usuario', 'direccion', 'telefono', 'ciudad']
        read_only_fields = ['usuario']  # Make the 'usuario' field read-only

User = get_user_model()

class RegistroSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True, trim_whitespace=False)
    password_confirm = serializers.CharField(write_only=True, trim_whitespace=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'password_confirm']
        read_only_fields = ['id']

    def validate(self, data):
        if data['password'] != data['password_confirm']:
            raise serializers.ValidationError({
                'password_confirm': 'Las contraseñas no coinciden.'
            })

        usuario = User(
            username=data['username'],
            email=data['email']
        )

        try:
            validate_password(data['password'], usuario)
        except ValidationError as error:
            raise serializers.ValidationError({
                'password': error.messages
            })

        return data

    @transaction.atomic
    def create(self, validated_data):
        validated_data.pop('password_confirm')

        usuario = User.objects.create_user(**validated_data) # el ** convierte el diccionario en argumentos de palabra clave
        Cliente.objects.create(usuario=usuario)  # Crea un objeto Cliente asociado al usuario recién creado

        return usuario
