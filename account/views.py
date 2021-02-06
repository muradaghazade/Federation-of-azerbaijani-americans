
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, get_object_or_404
from paypal.standard.forms import PayPalPaymentsForm
from django.utils.html import format_html
from django.views.generic import (
    CreateView,
    TemplateView,
    ListView,
    FormView,
)
from django.views.generic.edit import FormView
from django.views.generic.detail import DetailView
from .models import DonationUser
from .forms import RegisterForm, SignUpForm


class RegisterCreateView(CreateView):
    model = DonationUser
    form_class = RegisterForm
    template_name = "registration.html"
    success_url = reverse_lazy('account:register_done')


class RegisterDoneView(TemplateView):
    template_name = 'congratulation.html'


class DonateView(TemplateView):
    form_class = SignUpForm
    template_name = 'donate.html'

    def get(self, request):
        form = SignUpForm()

        context = {'form': form}
        return render(request, self.template_name, context)

    def post(self, request):
        form = SignUpForm(request.POST)
        if form.is_valid():
            # form.save()
            membership_id = request.POST.get('membership_id')
            user = DonationUser.objects.filter(
                membership_id=membership_id).first()
            if not user:
                return redirect('account:donate')
            return redirect(user.get_absolute_url())
        context = {'form': form}
        return render(request, self.template_name, context)


def payment_process(request, membership_id):
    user_object = DonationUser.objects.get(membership_id=membership_id)
    # amount = request.POST.get('amoun')
    paypal_dict = {
        "business": "husubayli@gmail.com",
        "amount": "",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('core:index')),
        "return": request.build_absolute_uri(reverse('core:index')),
        "cancel_return": request.build_absolute_uri(reverse('core:index')),
        # Custom command to correlate to some function later (optional)
        "custom": "premium_plan",
    }
    # Create the instance.
    form = ExtPayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form, "user_object": user_object}
    return render(request, "profile.html", context)


class ExtPayPalPaymentsForm(PayPalPaymentsForm):
    def render(self):
        form_open = u'''<form action="%s" id="PayPalForm" method="post">''' % (
            self.get_endpoint())
        form_close = u'</form>'
        # format html as you need
        submit_elm = u'''<input type="submit" value="Donate" class="btn my-custom-class" id="simple" style="bacground-color: ;">'''
        return format_html(form_open+self.as_p()+submit_elm+form_close)


def anonym_payment_process(request):
    # user_object = DonationUser.objects.get(membership_id=membership_id)
    # amount = request.POST.get('amoun')
    paypal_dict = {
        "business": "husubayli@gmail.com",
        "amount": "",
        "item_name": "name of the item",
        "invoice": "unique-invoice-id",
        "notify_url": request.build_absolute_uri(reverse('core:index')),
        "return": request.build_absolute_uri(reverse('core:index')),
        "cancel_return": request.build_absolute_uri(reverse('core:index')),
        # Custom command to correlate to some function later (optional)
        "custom": "premium_plan",
    }
    # Create the instance.
    form = ExtPayPalPaymentsForm(initial=paypal_dict)
    context = {"form": form}
    return render(request, "anonym.html", context)