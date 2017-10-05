import json

import click

from leappctl.session import post
from leappctl.utils import to_port_spec, to_port_map


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
              multiple=True,
              type=to_port_spec,
              help='(Re)define target tcp ports to forward to macrocontainer - [target_port:source_port]')
@click.option('--excluded-port',
              '-e',
              default=None,
              multiple=True,
              type=to_port_spec,
              help='Define tcp ports which will be excluded from the mapped ports [[target_port]:source_port>]')
@click.option('--debug',
              '-D',
              is_flag=True,
              default=False,
              help='Turn on debug logging on stderr')
def cli(**kwargs):
    req_body = kwargs

    # Transformations
    req_body['tcp_ports_user_mapping'] = to_port_map(req_body.pop('tcp_port'))
    req_body['excluded_tcp_ports'] = {"tcp": {str(x[0]): {"name": ""} for x in req_body['excluded_port'] or ()}}
    req_body['default_port_map'] = True

    # POST collected data to the appropriate endpoint in leapp-daemon
    resp = post(CMD, req_body)

    # Pretty-print response
    resp_body = resp.json()
    json_pprint = json.dumps(resp_body, sort_keys=True, indent=4, separators=(',', ': '))
    click.secho(
        'Response:\n{0}\n'.format(json_pprint),
        bold=True,
        fg='green' if resp.status_code == 200 else 'red'
    )
