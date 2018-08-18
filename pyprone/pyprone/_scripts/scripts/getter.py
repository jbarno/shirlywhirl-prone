""" A file for getting stuff
"""

import click
import facebook
import os
import requests


page_id = 266760960405597


@click.command()
@click.argument("source", default="facebook")
def get_from(source):
    print source
    if "facebook" in source:
        return get_facebook(source)
    raise NotImplementedError("soon")


def get_facebook(page_id=page_id, token=os.environ.get("FB_ACCESS_TOKEN")):
    if not token:
        raise EnvironmentError("Missing FB_ACCESS_TOKEN")
    g = facebook.GraphAPI(access_token=token)
    click.echo(request.get("https://{src}/266760960405597?fields=about,photos{webp_images,images}".format(src=src)))