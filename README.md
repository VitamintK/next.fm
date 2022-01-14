# next.fm

Last.fm is a great service, but its services only show you your most-listened to albums/artists/tracks by number of scrobbles (i.e. plays), NOT by amount of time listened.

I was interested in seeing which albums I spent the most time listening to, so I wrote this script using the last.fm API. The API doesn't make this data straightforward to find, as one endpoint (getrecenttracks) returns all the tracks you listen to, but the track information doesn't contain the duration. Conversely, another enpoint (gettoptracks) DOES return the duration, but doesn't include the album associated with the track. Because of this issue, previous approaches [[0]](https://github.com/LenaMartens/lastfm-duration-sort)[[1]](https://www.reddit.com/r/lastfm/comments/fpmvmb/check_your_artists_by_minute_scrobbled/)[[2]](https://timewhizzs.net/)[[3]](https://github.com/pmcdonough8133/last.timer) have only shown your most-listened-to artists or most-listened-to tracks by time. My script joins the two endpoints to show the results for albums as well.

And here are my results :)

```
Random Access Memories [Limited Box Set Edition] - 25h54m3s
Kind Of Blue (2013 HDtracks) - 20h19m23s
The Life of Pablo - 20h1m9s
Persona4 Original Soundtrack - 18h34m15s
Bitches Brew - 14h1m47s
Now He Sings, Now He Sobs - 10h49m4s
Red - 10h32m15s
Duet - 10h3m40s
Emotion - 9h36m19s
Samba in Seattle : Live at the Penthouse 1966-1968 - 9h16m11s
Since I Left You - 9h7m45s
Fearless - 9h7m10s
Candy Claws (2013) - Ceres & Calypso in the Deep Time [mp3] - 8h49m54s
Graduation - 8h40m54s
A Love Supreme - 8h31m1s
My Beautiful Dark Twisted Fantasy - 8h16m26s
Late Registration - 8h15m51s
folklore - 7h21m38s
My Favorite Things - 7h6m8s
1989 (Deluxe) - 6h55m40s
Year of the Snitch - 6h51m30s
The Incredible True Story - 6h48m32s
808s & Heartbreak - 6h44m48s
Atrocity Exhibition - 6h34m19s
Ceres & Calypso Instrumentals in DUAL MONO - 6h25m53s
Tetsuo & Youth - 6h20m48s
The Rip Tide - 6h7m36s
25 - 6h0m27s
```

(I accidentally left Random Access Memories playing overnight so it's a bit skewed but it would be somewhere at the top anyways)

![my top 25 albums](my_results.png)