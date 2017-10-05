def to_port_spec(arg):
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


def to_port_map(items):
    """Converts a (host_port, container_port) tuple into a list of dicts"""
    port_map = []
    for target, source in items:
        port_map.append({
            'protocol': 'tcp',
            'exposed_port': int(target),
            'port': int(source)})
    return dict(ports=port_map)
