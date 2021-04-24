import graphene
from graphene_django import DjangoObjectType

from myapp.models import UserModel
class UserType(DjangoObjectType):
    class Meta:
        model = UserModel


        
class Query(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        return UserModel.objects.all()


schema = graphene.Schema(query=Query)