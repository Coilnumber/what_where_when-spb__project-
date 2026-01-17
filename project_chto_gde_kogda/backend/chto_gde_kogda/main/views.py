from rest_framework.decorators import action
from django.shortcuts import render
from rest_framework import serializers, viewsets, mixins
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from .serialaizers import ThingReadSerialaizer, ThingCreateSerialaizer
from .models import *




class ThingViewSet(viewsets.mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    queryset = Thing.objects.filter(is_published=True)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return ThingReadSerialaizer
        return ThingCreateSerialaizer


    @action(detail=True, methods=["post"])
    def take(self, request, pk=None):
        thing = self.get_object()
        thing.is_published = False
        thing.save()

        return Response({'status': 'Вы забрали свою вещь! Спасибо вам за использование сервиса, рады, что он помог вам!'})
