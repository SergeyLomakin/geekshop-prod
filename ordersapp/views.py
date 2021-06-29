from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView


class OrderList(ListView):
    pass


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
