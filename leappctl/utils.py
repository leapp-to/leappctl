import os


def port_spec(arg):
    """Converts a port forwarding specifier to a (host_port, container_port) tuple
    Specifiers can be either a simple integer, where the host and container port are
    the same, or else a string in the form "host_port:container_port".
    """
    host_port, sep, container_port = arg.partition(":")
    host_port = int(host_port)
    if not sep:
        container_port = host_port
    else:
        container_port = int(container_port)
    return str(host_port), container_port


def path_spec(ctx, param, arg):
    path = os.path.normpath(arg)
    if not os.path.isabs(path):
        raise ValueError("Path '{}' is not absolute or valid.".format(str(arg)))
    return path
