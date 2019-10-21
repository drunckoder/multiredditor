import falcon
from multiredditor.cache import redis


def get_reddit(req, resp, resource, params):
    try:
        session_id = req.params['state']
        reddit = redis.get_reddit(session_id)
        req.context['reddit'] = reddit
    except KeyError:
        raise falcon.HTTPUnauthorized('User not found')


def set_reddit(req, resp, resource):
    session_id = req.params['state']
    reddit = req.context['reddit']
    redis.set_reddit(session_id, reddit)
