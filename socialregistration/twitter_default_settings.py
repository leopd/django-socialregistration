from django.conf import settings


settings.TWITTER_REQUEST_TOKEN_URL=getattr(settings,'TWITTER_REQUEST_TOKEN_URL', 'https://api.twitter.com/oauth/request_token')
settings.TWITTER_ACCESS_TOKEN_URL=getattr(settings,'TWITTER_ACCESS_TOKEN_URL','https://api.twitter.com/oauth/access_token')
settings.TWITTER_AUTHORIZATION_URL=getattr(settings,'TWITTER_AUTHORIZATION_URL','https://api.twitter.com/oauth/authorize')
