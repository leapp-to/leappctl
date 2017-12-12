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
              help='File where result should be stored')
def cli(**kwargs):
    req_body = kwargs

    display_html = req_body.pop('html')
    output_file = req_body.pop('out')

    # POST collected data to the appropriate endpoint in leapp-daemon
    resp = post(CMD, req_body)

    # Pretty-print response
    resp_body = resp.json()

    if display_html:
        html_content = ""
        resp_html = post(HTML_OUT_CMD, resp_body['data'])
        resp_html_body = resp_html.json()
        if 'html_output' in resp_html_body['data']:
            html_output = resp_html_body['data']['html_output']
            if html_output:
                html_content = html_output[0]['value']

        if output_file:
            with open(output_file, 'w+') as f:
                f.write(html_content)
        else:
            print(html_content)

    else:
        if output_file:
            with open(output_file, 'w+') as f:
                f.write(json.dumps(resp_body))
        else:
            print(json.dumps(resp_body))
