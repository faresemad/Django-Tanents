from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import Client, Domain

from .serializers import DomainSerializer


@api_view(['POST'])
def create_domain(request):
    """Create a new domain for a client.
    {
        "schema_name" : "any",
        "name" : "any",
        "domain" : "any.localhost",
        "is_primary" : True
    }
    """
    if request.method == 'POST':
        serializer = DomainSerializer(data=request.data)
        if serializer.is_valid():
            schema_name = serializer.validated_data['schema_name']
            name = serializer.validated_data['name']
            domain_name = serializer.validated_data['domain']
            is_primary = serializer.validated_data.get('is_primary', False)

            # Create or retrieve the client
            client, created = Client.objects.get_or_create(schema_name=schema_name, name=name)

            # Create the domain
            domain = Domain.objects.create(domain=domain_name, is_primary=is_primary, tenant=client)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
