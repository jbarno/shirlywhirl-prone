""" Wrapper for the facebook graph sdk
"""

import facebook
import os

ACCESS_TOKEN=os.environ["fb_access_token"]


def graph_from_config():
    g = facebook.GraphAPI(ACCESS_TOKEN, version="3.0")
