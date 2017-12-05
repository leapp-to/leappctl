import json

import click

from leappctl.session import post


CMD = "check-system"
CMD_HELP = "Run a group of checks on the system"


@click.command(CMD, help=CMD_HELP)
@click.option('--checks',
              '-c',
              required=True,
              prompt=True,
              help='Checks to be executed on system.')
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
