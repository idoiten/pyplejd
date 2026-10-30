class AuthenticationError(Exception):
    """Authentication failed."""


class ConnectionError(Exception):
    """Connection failed."""


class WriteError(Exception):
    """A command could not be written to the mesh."""
