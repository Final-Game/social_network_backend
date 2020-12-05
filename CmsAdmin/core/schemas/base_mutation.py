import graphene
from core.app.bus import Bus

bus: Bus = Bus()


class BaseMutation(graphene.Mutation):
    @classmethod
    def get_bus(cls):
        global bus
        return bus

    @classmethod
    @property
    def bus(cls) -> Bus:
        return cls.get_bus()

    @classmethod
    def mutate(cls, *args, **kwargs):
        return cls()