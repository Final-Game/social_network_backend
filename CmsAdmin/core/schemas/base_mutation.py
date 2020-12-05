import graphene
from core.app.bus import Bus


class BaseMutation(graphene.Mutation):
    @classmethod
    def get_bus(cls, bus: Bus = Bus()):
        return bus

    @classmethod
    def mutate(cls, *args, **kwargs):
        return cls()