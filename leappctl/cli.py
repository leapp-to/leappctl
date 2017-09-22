import os
import pkgutil

import click

from leappctl import cmd, __version__


SHORT_HELP = "leappctl is a control interface for leapp-daemon"
LONG_HELP = """
This tool is designed to help the administrator control the functioning of leapp-daemon.
"""


@click.group('leappctl', help=LONG_HELP, short_help=SHORT_HELP)
@click.version_option(__version__)
def cli():
    pass


def load_commands():
    pkg_path = os.path.dirname(cmd.__file__)
    for importer, name, is_pkg in pkgutil.iter_modules([pkg_path]):
        if is_pkg:
            continue
        mod = importer.find_module(name).load_module(name)
        cli.add_command(mod.cli)


def main():
    load_commands()
    cli()


if __name__ == '__main__':
    main()
