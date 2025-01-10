from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Event
from .forms import EventForm

# Create your views here.

class AddEvent(CreateView):
    model = Event
    fields = ['title', 'description', 'location', 'ticket_link', 'image', 'slug', 'status', 'event_date', 'start_time', 'end_time',]
    template_name = 'events/add-event.html'
    success_url = reverse_lazy('events')

    def form_valid(self, form):
        form.instance.author = self.request.user
        messages.success(self.request, "Event added successfully!")
        return super().form_valid(form)


class EventList(generic.ListView):
    model = Event
    template_name = 'events/events.html'
    context_object_name = 'event_list'
    paginate_by = 12

    def get_queryset(self):
        return Event.objects.all().order_by('-event_date')



# def review_detail(request, pk):
#     """
#     Display an individual :model:`review.Review`.

#     **Context**

#     ``review``
#         An instance of :model:`review.Review`.

#     **Template:**

#     :template:`reviews/review_detail.html`
#     """
#     review = get_object_or_404(Review, pk=pk)
#     return render(request, 'reviews/review_detail.html', {'review': review})


# def review_edit(request, pk):
#     """
#     view to edit review
#     """
#     review = get_object_or_404(Review, pk=pk)

#     if request.method == "POST":
#         form = ReviewForm(request.POST, request.FILES, instance=review)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Review updated!")
#             return redirect('review_detail', pk=pk)
#         else:
#             messages.error(request, "Error updating review!")
#     else:
#         form = ReviewForm(instance=review)

#     return render(
#         request,
#         'reviews/review_edit.html',
#         {'form': form, 'review': review, })


# def review_delete(request, pk):
#     """
#     view to delete review
#     """
#     review = get_object_or_404(Review, pk=pk)

#     if review.author == request.user:
#         review.delete()
#         messages.add_message(request, messages.SUCCESS, 'Review deleted!')
#     else:
#         messages.add_message(
#             request,
#             messages.ERROR,
#             'You can only delete your own comments!')

#     return redirect('reviews')
