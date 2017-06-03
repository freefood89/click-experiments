import click

@click.command()
@click.option('--repeat', default=1, help='rude mode')
def hello(repeat):
	for _ in range(repeat):
		click.echo('Hello World')

@click.command()
@click.option('--rude', is_flag=True, default=False, help='rude mode')
@click.option('--blue', is_flag=True, default=False, help='blue mode')
@click.argument('name')
def greet(rude, blue, name):
	if blue:
		style = 'blue'
	else:
		style = 'white'

	if rude:
		click.echo(click.style('Yo %s' % name, fg=style))
	else:
		click.echo(click.style('Hello %s' % name, fg=style))

@click.group()
def command():
	pass

command.add_command(hello)
command.add_command(greet)
