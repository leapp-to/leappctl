import click
import json
from leappctl.session import post


CMD = "destroy-container"
CMD_HELP = "This command destroy a container by name on a target system"


@click.command(CMD, help=CMD_HELP)
@click.option('--container-name',
              '-n',
              required=True,
              prompt=True,
              help='Name of a container that will be destroyed')
@click.option('--target-host',
              '-t',
              required=True,
              prompt=True,
              default='localhost',
              help='Hostname of the remote system')
@click.option('--target-user',
              '-u',
              default='root',
              help='Username for the remote system')
def cli(**kwargs):
    req_body = kwargs

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
