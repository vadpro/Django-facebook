from django.dispatch import Signal


# Sent right after user is created
facebook_user_registered = Signal('user', 'facebook_data')

# Sent after user is created, before profile is updated with data from Facebook
facebook_pre_update = Signal('user', 'profile', 'facebook_data')
facebook_post_update = Signal('user', 'profile', 'facebook_data')

# Sent after storing the friends from graph to db
facebook_post_store_friends = Signal('user', 'friends', 'current_friends', 'inserted_friends')

# Sent after storing the likes from graph to db
facebook_post_store_likes = Signal('user', 'likes', 'current_likes', 'inserted_likes')

# Some signals for compatibility with Django Registration
# A new user has registered.
user_registered = Signal('user', 'request')

# A user has activated his or her account.
user_activated = Signal('user', 'request')

# Run when the token extend finished
facebook_token_extend_finished = Signal('user', 'profile', 'token_changed', 'old_token')
