import logging
import json

import falcon

from multiredditor.middleware import reddit_loader
from multiredditor.resources.common import BaseResource

log = logging.getLogger(__name__)


class Multis(BaseResource):
    @falcon.before(reddit_loader.get_reddit)
    def on_get(self, req: falcon.Request, resp: falcon.Response):
        reddit = req.context['reddit']
        multireddits = reddit.get_multireddits()
        resp.body = json.dumps([multireddit.to_json() for multireddit in multireddits])

    @falcon.before(reddit_loader.get_reddit)
    def on_post(self, req: falcon.Request, resp: falcon.Response):
        resp.body = 'Not implemented'
