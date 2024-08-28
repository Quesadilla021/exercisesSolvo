from rest_framework import serializers

from Holidays.models import Holiday



class HolidaySerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    actions = serializers.SerializerMethodField()
    def get_name(self, obj):
        return obj.name

    def get_actions(self, obj):
        return {
            "create": True,
            "update": True,
            "destroy": True,
            "detail": True,
        }

    class Meta:
        model = Holiday
        fields = ['name', 'actions', 'id', 'weekday', 'date', 'country', ]

class HolidayDataTableSerializer(serializers.Serializer):
    data = serializers.ListField(child=HolidaySerializer(), required=True)
    draw = serializers.IntegerField(required=True)
    recordsFiltered = serializers.IntegerField(required=True)
    recordsTotal = serializers.IntegerField(required=True)