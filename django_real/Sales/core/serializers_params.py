from rest_framework import serializers


class ReadjustmentSalarySerializer(serializers.Serializer):
    percentage_readjustments = serializers.DecimalField(
        required=True,
        allow_null=False,
        max_digits=5,
        decimal_places=2,
    )
