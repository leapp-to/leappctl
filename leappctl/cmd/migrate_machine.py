import click
import requests
from requests.exceptions import ConnectionError

from leappctl import __version__
from leappctl.utils import port_spec


CMD_SHORT_HELP = """Executes the migration of an OS into a macrocontainer"""
CMD_LONG_HELP = """
This command migrates one or more application into containers by creating a macrocontainer.

This means that the entire system will be converted into a container, possibly bringing all the dirty with it.
"""


@click.command('migrate-machine', help=CMD_LONG_HELP, short_help=CMD_SHORT_HELP)
@click.option('--source-host', '-s', required=True, prompt=True, help='Migrated container will not be started immediately.')
@click.option('--source-user', '-u', required=True, default='root', help='User in source host to connect via SSH.')
@click.option('--target-host', '-t', required=True, default='localhost', help='Target host in which macrocontainer will run.')
@click.option('--target-user', '-U', default='root', help='User in target host to connect via SSH.')
@click.option('--container-name', '-n', help='Container name to be created in the target host.')
@click.option('--disable-start', '-d', is_flag=True, default=False, help='Don\'t start the container')
@click.option('--force-create', '-f', is_flag=True, default=True, help='Force container creation in the target.')
@click.option('--excluded_paths', '-E', multiple=True, type=click.Path(), help='Define paths which will be excluded from the source')
@click.option('--tcp-port', '-p', default=None, type=port_spec, help='(Re)define target tcp ports to forward to macrocontainer - [target_port:source_port]')
@click.option('--excluded-port', '-e', default=None, type=port_spec, help='Define tcp ports which will be excluded from the mapped ports [[target_port]:source_port>]')
@click.option('--debug', '-D', is_flag=True, default=False, help='Turn on debug logging on stderr')
def cli(**kwargs):
    with requests.Session() as session:
        headers = {
            'User-Agent': 'leappctl/{version}'.format(version=__version__),
        }
        try:
            resp = session.get('http://localhost:8000', headers=headers, json=kwargs)
        except ConnectionError:
            click.secho('Connection error', fg='red', bold=True)
        else:
            click.secho('Response: {}\n'.format(resp.text.encode('utf8')), fg='green', bold=True)
