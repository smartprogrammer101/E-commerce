from django.db.models.signals import pre_save, post_save, pre_delete
from django.dispatch import receiver
# from .models import Detail, Material, JobOrder
from .models import Review, Product
from django.db.models import Avg

# def approximate(num):
#     last2 = int(str(num)[2:])
#     if last2 != (50 or 00):
#         if last2 < 50 and last2 > 19:

#             appr_num = (num + 50 - last2)
#         else:
#             appr_num = (num - last2)

#         if last2 > 50 and last2 < 60:
#             appr_num = (num - last2 + 50)
            
#         if last2 >= 60:
#             appr_num = (num + 100 - last2)

#         return appr_num
#     else:
#         return num
# @receiver
def update_product_num_reviews_when_user_makes_review(sender, instance, created, **kwargs):
    # import pdb
    # pdb.set_trace()
    if created:
        product = instance.product
        product.num_reviews += 1
        product.rating = product.reviews.aggregate(avg=Avg('rating'))['avg']
        product.save()

post_save.connect(update_product_num_reviews_when_user_makes_review, sender=Review)

# def update_joborder_on_detail_save(sender, instance, **kwargs):
#     joborderTotal = instance.job_order.total
#     amount = int(instance.amount)
#     joborderTotal = joborderTotal - amount
#     instance.material_price = Material.objects.get(name=str(instance.material)).price
#     if str(instance.material) == 'SAV':
#         value = int((instance.width * instance.height * instance.quantity * instance.material_price) / 144)
#         instance.amount = approximate(value)
#     elif str(instance.material) == 'Flex':
#         value = int(instance.width * instance.height * instance.quantity * instance.material_price)
#         instance.amount = approximate(value)
#     elif str(instance.material) == 'WINDOW GRAPHICS':
#         value = int(instance.width * instance.height * instance.quantity * instance.material_price)
#         instance.amount = approximate(value)
#     elif str(instance.material) == 'CLEAR STICKER':
#         value = int(instance.width * instance.height * instance.quantity * instance.material_price)
#         instance.amount = approximate(value)
#     amount = int(instance.amount)
#     # import pdb
#     # pdb.set_trace()
#     tsum = joborderTotal + amount

#     instance.job_order.total = tsum
#     instance.job_order.save()
    
# def update_joborder_on_detail_delete(sender, instance, **kwargs):
#     joborderTotal = instance.job_order.total
#     amount = int(instance.amount)

#     tsum = joborderTotal - amount

#     instance.job_order.total = tsum
#     instance.job_order.save()

# # pre_save.connect(update_detail, sender=Detail)
# pre_save.connect(update_joborder_on_detail_save, sender=Detail)
# pre_delete.connect(update_joborder_on_detail_delete, sender=Detail)
