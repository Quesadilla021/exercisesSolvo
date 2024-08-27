from rest_framework import serializers

from Holidays.models import Holiday



class HolidaySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.name

    def get_action(self):
        return {
            "create": True,
            "update": True,
            "destroy": True,
            "detail": True,
        }

    class Meta:
        model = Holiday
        fields = '__all__'

class HolidayDataTableSerializer(serializers.Serializer):
    data = serializers.ListField(child=HolidaySerializer(), required=True)
    draw = serializers.IntegerField(required=True)
    recordFiltered = serializers.IntegerField(required=True)
    recordsTotal = serializers.IntegerField(required=True)