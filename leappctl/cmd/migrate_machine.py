import click


SHORT_HELP = """Executes the migration of an OS into a macrocontainer"""
LONG_HELP = """
This command migrates one or more application into containers by creating a macrocontainer.

This means that the entire system will be converted into a container, possibly bringing all the dirty with it.
"""


@click.command('migrate-machine', help=LONG_HELP, short_help=SHORT_HELP)
def cli():
    for x in range(5):
        click.echo('Number %d!' % x)
