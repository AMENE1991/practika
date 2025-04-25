from django.shortcuts import render
from django.views.generic.edit import FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from rest_framework import viewsets
from rest_framework.permissions import IsAdminUser
from django.views.generic.detail import DetailView

from BookingApp.models import Property, Rating
from BookingApp.forms import RatingForm
from BookingApp.serializers import PropertySerializer

class PropertyDetailView(DetailView):
    model = Property
    template_name = 'property_detail.html'
    context_object_name = 'property'

class PropertyViewSet(viewsets.ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAdminUser]
