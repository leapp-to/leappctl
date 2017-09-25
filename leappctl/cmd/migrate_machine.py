import click

from leappctl.session import get, post
from leappctl.utils import port_spec


CMD = "migrate-machine"
CMD_SHORT_HELP = "Executes the migration of an OS into a macrocontainer"
CMD_LONG_HELP = """
This command migrates one or more application into containers by creating a macrocontainer.

This means that the entire system will be converted into a container, possibly bringing all the dirty with it.
"""


@click.command(CMD, help=CMD_LONG_HELP, short_help=CMD_SHORT_HELP)
@click.option('--source-host',
              '-s',
              required=True,
              prompt=True,
              help='Host to be migrated into a macrocontainer.')
@click.option('--source-user',
              '-u',
              required=True,
              default='root',
              help='User in source host to connect via SSH.')
@click.option('--target-host',
              '-t',
              required=True,
              prompt=True,
              default='localhost',
              help='Host in which macrocontainer will run.')
@click.option('--target-user',
              '-U',
              default='root',
              help='User in target host to connect via SSH.')
@click.option('--container-name',
              '-n',
              help='Container name to be created in the target host.')
@click.option('--disable-start',
              '-d',
              is_flag=True,
              default=False,
              help='Don\'t start the container')
@click.option('--force-create',
              '-f',
              is_flag=True,
              default=True,
              help='Force container creation in the target.')
@click.option('--excluded_paths',
              '-E',
              multiple=True,
              type=click.Path(),
              help='Define paths which will be excluded from the source')
@click.option('--tcp-port',
              '-p',
              default=None,
              type=port_spec,
              help='(Re)define target tcp ports to forward to macrocontainer - [target_port:source_port]')
@click.option('--excluded-port',
              '-e',
              default=None,
              type=port_spec,
              help='Define tcp ports which will be excluded from the mapped ports [[target_port]:source_port>]')
@click.option('--debug',
              '-D',
              is_flag=True,
              default=False,
              help='Turn on debug logging on stderr')
def cli(**kwargs):
    # Simple POST
    resp = post(CMD, kwargs)
    data = resp.json()
    click.echo('Response: {0}\n'.format(data['json']['target_host']))

    # Simple GET
    resp1 = get(CMD, kwargs)
    data = resp1.json()
    click.echo('Response: {0}\n'.format(data))
