from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from ordersapp.models import Order


class OrderList(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderCreate(CreateView):
    pass


class OrderDelete(DeleteView):
    pass


class OrderUpdate(UpdateView):
    pass


class OrderRead(DeleteView):
    pass


def forming_complete(request, pk):
    pass
