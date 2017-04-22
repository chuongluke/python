from django.shortcuts import render
from feelings.groups import forms
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.urlresolvers import reverse_lazy
from django.views import generic

class CompanyCreate(LoginRequiredMixin, generic.CreateView):
    form_class = forms.CompanyForm
    template_name = 'companies/company_form.html'
    success_url = reverse_lazy('users:dashboard')

    def form_valid(self, form):
        form.instance.create_by = self.request.user
        response = super().form_valid(form)
        self.object.members.add(self.request.user)
        return response