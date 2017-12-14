import json

import click

from leappctl.session import post


CMD = "check-system"
CMD_HELP = "Run a group of checks on the system"
HTML_OUT_CMD = "check-html-output"


@click.command(CMD, help=CMD_HELP)
@click.option('--checks',
              '-c',
              required=True,
              prompt=True,
              help='Checks to be executed on system.')
@click.option('--html',
              is_flag=True,
              default=False,
              help='Display check result as HTML')
@click.option('--out',
              '-o',
              type=click.File('w+'),
              help='File where result should be stored')
def cli(**kwargs):
    req_body = kwargs

    display_html = req_body.pop('html')
    output_file = req_body.pop('out')

    # POST collected data to the appropriate endpoint in leapp-daemon
    resp = post(CMD, req_body)
    resp_body = resp.json()

    if display_html:
        resp_html = post(HTML_OUT_CMD, resp_body['data'])
        resp_html_body = resp_html.json()
        try:
            content = resp_html_body['data']['html_output'][0]['value']
        except LookupError:
            content = ""
    else:
        content = json.dumps(resp_body)

    if output_file:
        output_file.write(content)
    else:
        print(content)
