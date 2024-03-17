from rest_framework import serializers

from app.models import Client, Domain


class DomainSerializer(serializers.Serializer):
    schema_name = serializers.CharField(max_length=100)
    name = serializers.CharField(max_length=100)
    domain = serializers.CharField(max_length=100)
    is_primary = serializers.BooleanField(default=False)

    def create(self, validated_data):
        client = Client(schema_name=validated_data['schema_name'], name=validated_data['name'])
        client.save()
        domain = Domain(domain=validated_data['domain'], is_primary=validated_data['is_primary'])
        domain.tenant = client
        domain.save()
        return domain
