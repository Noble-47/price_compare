from django.contrib.auth import get_user_model
from django.db import models

from products.models import Product

User = get_user_model()

#
# class Wishlist(models.Model):
#     product_id = models.ManyToManyField(Product)
#     user = models.ForeignKey(User, related_name="wishlist", on_delete=models.CASCADE)
#     # price_history = models.ArrayField(
#     #     base=models.IntegerField(), size=5
#     # )  # use HstoreField
#
#     def get_price_changes():
#         pass
#
#     def __str__(self):
#         return f"{user.username} Wishlist"
