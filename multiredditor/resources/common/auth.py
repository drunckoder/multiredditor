from multiredditor.cache import redis
from multiredditor.middleware import reddit_loader
from multiredditor.reddit import Reddit
from multiredditor.resources.common import BaseResource
import falcon


class AuthInitiate(BaseResource):

    # noinspection PyMethodMayBeStatic
    def on_get(self, req: falcon.Request, resp: falcon.Response):
        reddit = Reddit()
        redirect_url, session_id = reddit.get_auth_url_and_session_id()
        redis.set_reddit(session_id=session_id, reddit=reddit)
        raise falcon.HTTPTemporaryRedirect(location=redirect_url)


class AuthCallback(BaseResource):

    @falcon.before(reddit_loader.get_reddit)
    @falcon.after(reddit_loader.set_reddit)
    def on_get(self, req: falcon.Request, resp: falcon.Response):
        reddit = req.context['reddit']
        access_token = req.params['code']
        reddit.auth.authorize(access_token)
        status = reddit.user.me()
        resp.body = str(status)
        # TODO: redirect to frontend
