from django.db import connection
from rest_framework import viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import Note
from .serializers import NoteSerializer


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer


@api_view(["GET"])
@permission_classes([AllowAny])
def health(request):
    """Touch the database, so a deployment that cannot reach Postgres reports
    unhealthy instead of looking fine and failing on the first real request."""
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return Response({"status": "ok", "database": "ok"})
    except Exception:
        return Response({"status": "degraded", "database": "unreachable"}, status=503)
