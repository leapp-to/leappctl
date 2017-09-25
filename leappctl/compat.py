try:
    from urllib.parse import urljoin  # noqa
except ImportError:
    from urlparse import urljoin  # noqa
