from rest_framework import serializers
from .models import Master, Detail


class DetailSerializer(serializers.ModelSerializer):
    # master_id = serializers.PrimaryKeyRelatedField(many=False, queryset=Master.objects.all())
    master_url = serializers.HyperlinkedIdentityField(
        view_name="master-detail"
    )
    url = serializers.HyperlinkedIdentityField(
        view_name="detail-detail"
    )
    class Meta:
        model = Detail
        fields = ["id", "url", "description", "master", "master_url"]


class MasterSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name="master-detail"
    )
    details = DetailSerializer(many=True, read_only=True)

    class Meta:
        model = Master
        fields = ["id", "url", "name", "details"]
