import click
import json
from leappctl.session import post


CMD = "check-target"
CMD_HELP = "This command checks services (like Docker, Rsync) on a target system"


@click.command(CMD, help=CMD_HELP)
@click.option('--target-host',
              '-t',
              required=True,
              prompt=True,
              default='localhost',
              help='Host where checks will be executed.')
@click.option('--target-user-name',
              '-u',
              default='root',
              help='User in target host to connect via SSH.')
@click.option('--check-target-service-status',
              '-s',
              is_flag=True,
              default=False,
              help='Check status of services')
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
