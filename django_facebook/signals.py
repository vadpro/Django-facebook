from django.dispatch import Signal


# Sent right after user is created
facebook_user_registered = Signal()

# Sent after user is created, before profile is updated with data from Facebook
facebook_pre_update = Signal()
facebook_post_update = Signal()

# Sent after storing the friends from graph to db
facebook_post_store_friends = Signal()

# Sent after storing the likes from graph to db
facebook_post_store_likes = Signal()

# Some signals for compatibility with Django Registration
# A new user has registered.
user_registered = Signal()

# A user has activated his or her account.
user_activated = Signal()

# Run when the token extend finished
facebook_token_extend_finished = Signal()
