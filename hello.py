import click

@click.command()
@click.option('--repeat', default=1, help='rude mode')
def hello(repeat):
	for _ in range(repeat):
		click.echo('Hello World')

@click.command()
@click.option('--rude', is_flag=True, default=False, help='rude mode')
@click.argument('name')
def greet(rude, name):
	if rude:
		click.echo('Yo %s' % name)
	else:
		click.echo('Hello %s' % name)

@click.group()
def command():
	pass

command.add_command(hello)
command.add_command(greet)
