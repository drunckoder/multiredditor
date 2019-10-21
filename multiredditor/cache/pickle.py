import pickle

import praw


def pickle_reddit(reddit: praw.Reddit) -> bytes:
    return pickle.dumps(reddit)


def unpickle_reddit(pickled_reddit: bytes) -> praw.Reddit:
    return pickle.loads(pickled_reddit)
