""" A file for getting stuff
"""

import click
import facebook
import requests


page_id = 266760960405597


@click.command()
@click.argument("source", default="facebook")
def get_from(source):
    print source
    if "facebook" in source:
        return get_facebook(source)
    raise NotImplementedError("soon")

@click.command()
@click.argument("page_id", default=page_id)
@click.argument("token", envvar="FB_ACCESS_TOKEN")
def get_facebook(page_id, token):
    g = facebook.GraphAPI(access_token=token)
    click.echo(request.get("https://{src}/266760960405597?fields=about,photos{webp_images,images}".format(src=src)))