# Twitch API

import time
import twitch

helix = twitch.Helix('client-id')

# Users
while True:
    print("Grabbing room list")
    for user in helix.users(['username']):
        print(user.display_name)
    time.sleep(1)
