import graphene
import CouponWallet.schema

class Query(CouponWallet.schema.Query ,graphene.ObjectType):
    pass

schema = graphene.Schema(query = Query)