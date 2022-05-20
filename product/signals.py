from django.db.models.signals import pre_save, post_save, pre_delete, post_delete
from django.dispatch import receiver
# from .models import Detail, Material, JobOrder
from .models import Review, Product
from django.db.models import Avg



# @receiver
def delete_product_num_reviews_when_user_deletes_review(sender, instance, **kwargs):
    # import pdb
    # pdb.set_trace()
    product = instance.product
    product.num_reviews = product.reviews.count()
    product.rating = product.reviews.aggregate(avg=Avg('rating'))['avg']
    if product.rating is None:
        product.rating = 0
    product.save()
    print('>>>>>>>> DELETED <<<<<<')

post_delete.connect(delete_product_num_reviews_when_user_deletes_review, sender=Review)


def update_product_num_reviews_when_user_makes_review(sender, instance, created, **kwargs):
    # import pdb
    # pdb.set_trace()
    if created:
        product = instance.product
        product.num_reviews = product.reviews.count()
        product.rating = product.reviews.aggregate(avg=Avg('rating'))['avg']
        product.save()
        print('>>>>>>>> CREATED <<<<<<')

post_save.connect(update_product_num_reviews_when_user_makes_review, sender=Review)

