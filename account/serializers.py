from rest_framework import serializers
from account.models import Account

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ['picture']