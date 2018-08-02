from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import RedirectView, TemplateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from catalog.models import Product
from django.forms import modelformset_factory
from . models import CartItem, Order
from accounts.models import User
from django.contrib import messages


class CreateCartItemView(RedirectView):

    pattern_name = 'carrinho'
    
    def get_redirect_url(self, *args, **kwargs):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        if self.request.session.session_key is None:
            self.request.session.save()
        
        cart_item, created = CartItem.objects.add_item(
            self.request.session.session_key, product
        )
        if created:
            messages.success(self.request, 'Produto adicionado com sucesso')
        else:
            messages.success(self.request, 'Produto atualizado com sucesso')
        return super().get_redirect_url(*args)

class CartItemView(TemplateView):
     
     template_name = 'checkout/cart.html'

     def get_formset(self, clear=False):
        CartItemFormSet = modelformset_factory(
            CartItem, fields=('quantity',), can_delete=True, extra=0
        )
        session_key =self.request.session.session_key
        if session_key:
            if clear:
                formset = CartItemFormSet(
                    queryset = CartItem.objects.filter(cart_key=session_key)
                )
            else:
                formset = CartItemFormSet(
                    queryset = CartItem.objects.filter(cart_key=session_key), 
                    data=self.request.POST or None
                )
        else:
            formset = CartItemFormSet(queryset=CartItem.objects.none())
        return formset

     def get_context_data(self, **kwargs):
        context = super(CartItemView, self).get_context_data(**kwargs)
        context['formset'] = self.get_formset()
        return context

     def post(self, request, *args, **kwargs):
        formset = self.get_formset()
        context = self.get_context_data(**kwargs)
        if formset.is_valid():
            formset.save()
            messages.success(request, 'Carrinho atualizado com sucesso')
            context['formset'] = self.get_formset(clear=True)
        return self.render_to_response(context)



class CheckoutView(LoginRequiredMixin, TemplateView):
    template_name = 'checkout/checkout.html'

    def get(self, request, *args, **kwargs):
        session_key = request.session.session_key
        if session_key and CartItem.objects.filter(cart_key = session_key).exists():
            cart_items = CartItem.objects.filter(cart_key=session_key)
            order = Order.objects.create_order(
                user=request.user, cart_items=cart_items
            )
        else:
            messages.info(request, 'Não há itens no carrinho de compras')
            return redirect('carrinho')
        response = super(CheckoutView, self).get(request, *args, **kwargs)
        response.context['order'] = order
        return super(CheckoutView, self).get(self, *args, **kwargs)

class RedirectCheckoutView(LoginRequiredMixin, UpdateView):
    model = User
    template_name = 'checkout/confirm_address.html'
    fields = ['logradouro', 'bairro', 'cidade', 'estado', 'pais', 'cep']
    success_url = reverse_lazy('finalizar')

    def get_object(self):
        return self.request.user