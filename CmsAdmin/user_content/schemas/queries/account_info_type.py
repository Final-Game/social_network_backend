import graphene


class AccountInfoType(graphene.ObjectType):
    id = graphene.String(description="Id")
    verify_status = graphene.Int(description="Verify status")