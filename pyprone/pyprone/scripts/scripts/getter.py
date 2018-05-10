""" A file for getting stuff
"""

import requests
import click


page_id=266760960405597
@click.argument(source)
def get_from(source):
    if "facebook.com" in source:
        return get_facebook(source)
    except NotImplemented("soon")


def get_facebook(src):
    token = os.environ["fb_access_token"]
    return request.get("https://{src}/266760960405597?fields=about,photos{webp_images,images}".format(src=src),
