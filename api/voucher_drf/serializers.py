from rest_framework import serializers

from .models import Voucher

class VoucherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Voucher
        fields = ['voucher_code', 'discount', 'no_of_use']