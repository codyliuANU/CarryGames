from pip._vendor.distlib.compat import raw_input
from requests_oauthlib import OAuth2Session

__author__ = 'la0rg'

client_id = 'pkbcgy8h99jyhmwvwq9rt9ysqvg5mze7'
client_secret = '7EqzYtxB427Yb4AAfB3PR2bjMT4vxTwd'
redirect_uri = 'https://127.0.0.1:8000/authcode/'

code = '3rxwaya2nhdrd9kgw45fb5xh'
access_token = 'u9d6f3ttpa4d8dc9mnjeuax4'

oauth = OAuth2Session(client_id, redirect_uri=redirect_uri)

auth_url, state = oauth.authorization_url('https://eu.battle.net/oauth/authorize')
print('Please go to %s and authorize access.' % auth_url)
code = raw_input('Enter the code from URL:')

token = oauth.fetch_token('https://eu.battle.net/oauth/token',
                          client_secret=client_secret,
                          code=code)

print(token)


saved_token = {'token_type': 'bearer', 'accountId': 402584189, 'expires_in': 2591999, 'access_token': 'uk4cw4rp34kq828ky8frq66e', 'expires_at': 1435677230.9450767}

#new_oauth = OAuth2Session(client_id, redirect_uri=redirect_uri, state='', token=saved_token)

#result = new_oauth.get('https://eu.api.battle.net/account/user')

#print(result.content)