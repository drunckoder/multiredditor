import os
import hashlib

import praw
from multiredditor import config
from .multireddit import parse_multireddits


class Reddit(praw.Reddit):
    def __init__(self, *args, **kwargs):
        reddit_config = {
            'client_id': config.client_id,
            'client_secret': config.client_secret,
            'redirect_uri': config.redirect_uri,
            'user_agent': config.user_agent
        }
        reddit_config.update(kwargs)
        super(Reddit, self).__init__(*args, **reddit_config)

    def get_auth_url_and_session_id(self):
        session_id = hashlib.sha256(os.urandom(1024)).hexdigest()
        url = self.auth.url(scopes=config.scopes, state=session_id, duration='temporary')
        return url, session_id

    def get_subreddits(self):
        subreddits = [str(x) for x in self.user.subreddits(limit=5)]
        return subreddits

    def get_multireddits(self):
        multireddits = parse_multireddits(self.user.multireddits())
        return multireddits



