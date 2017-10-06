import os
from contextlib import contextmanager

import requests

from leappctl import __version__
from leappctl.compat import urljoin


def make_endpoint(cmd):
    BASE_ENDPOINT = os.getenv('LEAPP_DAEMON_ENDPOINT', 'http://127.0.0.1:8000/v1/')
    return urljoin(BASE_ENDPOINT, cmd)


@contextmanager
def get_daemon_session():
    """Set default HTTP parameters to communicate with daemon"""
    headers = {
        'User-Agent': 'leappctl/{version}'.format(version=__version__),
    }

    with requests.Session() as session:
        session.headers.update(headers)
        yield session


def get(cmd, params):
    """Send a GET request to the daemon"""
    with get_daemon_session() as s:
        return s.get(make_endpoint(cmd), json=params)


def post(cmd, params):
    """Send a POST request to the daemon"""
    with get_daemon_session() as s:
        return s.post(make_endpoint(cmd), json=params)
