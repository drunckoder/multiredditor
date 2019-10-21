import logging

import falcon

from multiredditor import config
from multiredditor.resources import (
    Root, AuthInitiate, AuthCallback, Subreddits, Multis
)

logging.basicConfig(**config.logging_config)
log = logging.getLogger(__name__)


class MultiRedditor(falcon.API):
    def __init__(self, *args, **kwargs):
        super(MultiRedditor, self).__init__(*args, **kwargs)

        self.add_route('/', Root())
        self.add_route('/reddit/auth/initiate', AuthInitiate())
        self.add_route('/reddit/auth/callback', AuthCallback())
        self.add_route('/api/v1/user/subreddits', Subreddits())
        self.add_route('/api/v1/user/multireddits', Multis())


app = MultiRedditor()
