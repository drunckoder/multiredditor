import logging

client_id = 'bnRM0jBIBu1PxQ'
client_secret = '1xk_xv2wdX5foVdzSOxKrTip9xA'
redirect_uri = 'http://127.0.0.1:5000/reddit/auth/callback'
scopes = ['mysubreddits', 'identity', 'read']
user_agent = 'Multiredditor'
cache_expire = 3600

logging_config = {
    'level': logging.INFO
}
