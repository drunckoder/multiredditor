import logging

import falcon

from multiredditor.resources.common import BaseResource

log = logging.getLogger(__name__)


class Root(BaseResource):

    # noinspection PyMethodMayBeStatic
    def on_get(self, req: falcon.Request, resp: falcon.Response):
        resp.body = 'Hello!'
        raise falcon.HTTPTemporaryRedirect('/reddit/auth/initiate')
