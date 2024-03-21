from rest_framework import viewsets, mixins, status
from rest_framework.viewsets import GenericViewSet
from planetarium.permissions import IsAdminOrIfAuthenticatedReadOnly

from planetarium.models import (
    ShowTheme,
    PlanetariumDome,
    Reservation,
    AstronomyShow,
    ShowSession,
    Ticket,
)

from planetarium.serializers import (
    ShowThemeSerializer,
    PlanetariumDomeSerializer,
    ReservationSerializer,
    AstronomyShowSerializer,
    ShowSessionSerializer,
    TicketSerializer,
)


class ShowThemeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = ShowTheme.objects.all()
    serializer_class = ShowThemeSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly, )


class PlanetariumDomeViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    GenericViewSet,
):
    queryset = PlanetariumDome.objects.all()
    serializer_class = PlanetariumDomeSerializer
    permission_classes = (IsAdminOrIfAuthenticatedReadOnly, )

