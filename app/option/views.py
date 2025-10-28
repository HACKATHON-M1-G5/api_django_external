from django.shortcuts import redirect, render
from rest_framework import viewsets

from .form.option_form import OptionForm
from .models import Option
from .serializers import OptionSerializer


class OptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer

def add_option(request):
    if request.method == 'POST':
        form = OptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('option_list')
    else:
        form = OptionForm()
    return render(request, 'option/add_option.html', {'form': form})