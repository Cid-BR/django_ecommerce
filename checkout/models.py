from django.db import models

class CarItemManager(models.Manager):
    def add_item(self, cart_key, product):
        if self.filter(cart_key=cart_key, product=product).exists():
            created = False
            cart_item = self.get_or_create(cart_key=cart_key, product=product)
            cart_item.quantity = cart_item.quantity+1
            cart_item.save()
        else:
            created = True
            cart_item = CarItem.objects.created(cart_key=cart_key, product=product, price = product.price)
        return cart_item, created

class CarItem(models.Model):
    cart_key = models.CharField(
        'Chave do Carrinho', max_length=40, db_index=True
    )
    product = models.ForeignKey('catalog.Product', verbose_name='Produto', on_delete = models.CASCADE)
    quantity = models.PositiveIntegerField('Quantidade', default=1)
    price = models.DecimalField('Preço', decimal_places=2, max_digits= 8)

    class Meta:
        verbose_name    ='Item do Carrinho'
        verbose_name_plural = 'Itens do Carrinho'
        unique_together = (('cart_key', 'product'),)

    def __str__(self):
        return '{} [{}]'.format(self.product, self.quantity)
