from .. import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views import generic

from braces.views import SetHeadlineMixin

class Create(LoginRequiredMixin, SetHeadlineMixin, generic.CreateView):
    form_class = forms.CompanyForm
    headline = 'Create Company'
    template_name = 'companies/form.html'
    success_url = reverse_lazy('users:dashboard')

    def form_valid(self, form):
        form.instance.create_by = self.request.user
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response


class Update(LoginRequiredMixin, SetHeadlineMixin, generic.UpdateView):
    form_class = forms.CompanyForm
    template_name = 'companies/form.html'

    def get_queryset(self):
        return self.request.user.companies.all()

    def get_headline(self):
        return 'Edit ' + str(self.object.name)

    def get_success_url(self):
        return reverse('groups:companies:detail', kwargs={'slug': self.object.slug})


class Detail(LoginRequiredMixin, generic.DetailView):
    template_name = 'companies/detail.html'

    def get_queryset(self):
        return self.request.user.companies.all()
