from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, ListView, DetailView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from BookingApp.models import Property, Booking, Review
from BookingApp.serializers import PropertySerializer, BookingSerializer, ReviewSerializer
from BookingApp.forms import BookingForm


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'Profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user_name'] = self.request.user.username
        context['user_properties'] = Property.objects.filter(creator=self.request.user)
        return context


class PropertyListView(ListView):
    model = Property
    template_name = 'property_list.html'
    context_object_name = 'properties'


class PropertyCreateView(CreateView):
    model = Property
    template_name = 'property_create.html'
    fields = ['name', 'address', 'description', 'price_per_night', 'image']
    success_url = reverse_lazy('property_list')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class PropertyDetailView(DetailView):
    model = Property
    template_name = 'property_detail.html'
    context_object_name = 'property'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


class PropertyDeleteView(DeleteView):
    model = Property
    success_url = reverse_lazy('property_list')
    template_name = 'property_delete.html'


from django.utils import timezone

class BookingCreateView(CreateView):
    model = Booking
    form_class = BookingForm
    template_name = 'booking_form.html'

    def dispatch(self, request, *args, **kwargs):
        property_obj = get_object_or_404(Property, pk=self.kwargs['property_id'])
        if property_obj.creator == request.user:
            return redirect('property_detail', pk=property_obj.pk)
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        property_obj = get_object_or_404(Property, pk=self.kwargs['property_id'])
        form.instance.user = self.request.user
        form.instance.property = property_obj
        form.instance.check_in_date = timezone.now().date()

        
        form.instance.total_price = property_obj.price_per_night * form.instance.num_days

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('property_detail', kwargs={'pk': self.kwargs['property_id']})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['property_id'] = self.kwargs['property_id']
        return context






class PropertyViewSet(ModelViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAdminUser]


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Booking.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        return Review.objects.filter(author=self.request.user)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)