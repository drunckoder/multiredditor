import praw
import redis

from multiredditor import config
from multiredditor.cache import pickle


class Redis(redis.Redis):

    def get_reddit(self, session_id: str) -> praw.Reddit:
        unpickled_reddit = pickle.unpickle_reddit(self[session_id])
        return unpickled_reddit

    def set_reddit(self, session_id, reddit: praw.Reddit) -> None:
        pickled_reddit = pickle.pickle_reddit(reddit)
        self.set(name=session_id, value=pickled_reddit, ex=config.cache_expire)


redis = Redis()
