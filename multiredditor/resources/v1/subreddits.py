import logging
import json

import falcon

from multiredditor.middleware import reddit_loader
from multiredditor.resources.common import BaseResource

log = logging.getLogger(__name__)


class Subreddits(BaseResource):
    @falcon.before(reddit_loader.get_reddit)
    def on_get(self, req: falcon.Request, resp: falcon.Response):
        reddit = req.context['reddit']
        subreddits = reddit.get_subreddits()
        resp.body = json.dumps(subreddits)
