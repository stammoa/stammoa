import graphene
from graphene_django import DjangoObjectType
from .models import CouponList

class CouponListType(DjangoObjectType):
    class Meta:
        model = CouponList

class Query(graphene.ObjectType):
    couponList = graphene.List(CouponListType)

    def resolve_couponList(self, args):
        return CouponList.objects.all()