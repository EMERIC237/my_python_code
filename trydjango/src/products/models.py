from django.db import models
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120) #math_length is required
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=100000, decimal_places=2)
    summary = models.TextField(blank=False, null=False)
    featured = models.BooleanField(default=True) #null=true, default=True

    #def get_absolute_url(self):
    #    return f"/product/{self.id}"

    def get_absolute_url(self):
        return reverse("products:product-detail", kwargs={"my_id": self.id}) #(to resolve the id problem of the url)