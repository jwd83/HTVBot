# Twitch API

import time
import twitch
import htvsettings

helix = twitch.Helix(htvsettings.HELIX_CLIENT_ID )

# Users
while True:
    print("Grabbing room list")
    for user in helix.users(['username']):
        print(user.display_name)
    time.sleep(1)
