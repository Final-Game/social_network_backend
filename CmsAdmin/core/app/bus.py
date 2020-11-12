import inspect

from abc import ABC, abstractmethod
from django.utils.translation import gettext as _


class HandlerNotFound(Exception):
    pass


class Resolver:
    def handler_for(self, command):
        """
        Retrieve the handler class for a command. If the command implements a
        ``handler`` method, it should return the class of the handler. Otherwise
        it will search for a class with the name {CommandName}Handler.
        """
        try:
            if command.handler() != None:
                return command.handler()
        except AttributeError:
            pass

        try:
            return getattr(
                self._getmodule(command), command.__class__.__name__ + "Handler"
            )
        except AttributeError:
            return None

    def _getmodule(self, command):
        return inspect.getmodule(command)


class Bus:
    """
    The actual command bus, when given a command, it finds an appropriate handler
    and fires it.
    """

    #: The command name resolver, used to figure out names for commands that
    #: don't have a `handler` method.
    resolver: Resolver

    def __init__(self, resolver: Resolver = None):
        self.resolver = resolver or Resolver()

    def dispatch(self, command):
        handler_cls = self.resolver.handler_for(command)

        if handler_cls is None:
            raise HandlerNotFound(
                _("Unable to find handler for %(name)s")
                % {"name": command.__class__.__name__}
            )
        return handler_cls().handle(command)


class Command(ABC):
    # assign handler to improve performance
    def handler(self):
        return None


class Query(ABC):
    # assign handler to improve performance
    def handler(self):
        return None


class CommandHandler(ABC):
    @abstractmethod
    def handle(self, command: Command):
        pass


class QueryHandler(ABC):
    @abstractmethod
    def handle(self, query: Query):
        pass


if __name__ == "__main__":

    class HelloCommand(Command):
        x: int

        def __init__(self, x: int):
            self.x = x

        def handler(self):
            return HelloCommandHandler

    class HelloCommandHandler(CommandHandler):
        def handle(self, command: HelloCommand):
            print("Handling for HelloCommand: {}".format(command.x))

    b = Bus()
    b.dispatch(HelloCommand(10))
    pass
