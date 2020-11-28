import graphene


class TestMutation(graphene.Mutation):
    result = graphene.String(default_value="result test mutation.")

    class Arguments:
        pass

    def mutate(self, *args, **kwargs):
        return TestMutation(result="Nguyen Minh Tuan")
