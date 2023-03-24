# SpotifyPlaylistGenerator

The point of this project was to take all my personal liked songs on spotify and cluster them into playlists using a kmeans approach, while learning about interacting with the spotify api in the process.  I used the api to build up a small set of song feature data (~85,000 songs), which I could use to train a kmeans model on.  I then used this model to predict clusters for my own music.

Referenced work:

-https://towardsdatascience.com/midnight-hack-5-using-machine-learning-to-categorize-spotify-playlists-57dc492fc3e6
-http://ben-tanen.com/notebooks/kmeans-music.html
