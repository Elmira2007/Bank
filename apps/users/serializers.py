from rest_framework import serializers

from apps.users.models import User, HistoryTransfer

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'phone', 'age', 'balance', 'wallet_address')
        extra_kwargs = {
            'wallet_address' : {'read_only': True},
            'balance' : {'read_only': True},
        }


class HistoryTransferSerializer(serializers.ModelSerializer):
    class Meta:
        model = HistoryTransfer
        fields = ('from_user', 'to_user', 'is_comleted', 'amount', 'created_at')