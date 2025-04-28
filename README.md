In this project, a music recommendation system is developed to find similar songs and recommend new songs based on a user's preferences, i.e., how they have `rated` a song or if they have `liked` a song.

It features `2` different models: `ratings-based` and the `hybrid` model.

- The `ratings` model utilises only the `ratings` feature to develop the recommendation system, while
- The `hybrid` model utilises the `ratings`, `likes` & `genre` features to develop the recommendation system with each feature contributing different weights; `ratings = [0.5]`, `likes = [0.3]` & `genre = [0.2]`.


`Assumptions:`
- The `ratings` feature has a scale of `1 - 5` with a half-step count, i.e, `1.5`, `2.5`.
- A `like` is worth a `4` point score and assigned to `ratings >= 3.5` with a `.45` probability of being assigned.

`Data:`
- The song `name` and `genre` were downloaded from [Kaggle](https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019?resource=download).
- The `ratings` feature is a dummy dataset generated using deepseek, with higher `ratings` having more weightage, while
- The `likes` feature was populated in Google Sheets.


`Data Information:`
- `userId` - the id of a user.
- `musicId` - the id of a song.
- `rating` - the score representing a user's preference.
- `likes` - indicating whether a user likes a song or not.
- `title` - the title of a song, the artist & year it was released.
- `genre` - the genre of the song.

`Data Stat:`
- Total number of `ratings` - `249,975`.
- Unique `MusicId's` - `23,493`.
- Unique `Users` - `1512`.
-----------------

**Youtube Data**

Considering the data used in the initial system was dummy (ratings), I decided test the system with real data.

`Data Information:`
- `userId` - the id of a user.
- `musicId` - the id of a song.
- `views` - the number of views on Youtube.
- `rating` - the score representing a user's preference.
- `likes` - indicating whether a user likes a song or not.
- `title` - the title of a song.
- `artist` - the artist/artists of the song.
- `year` - the year it was posted on Youtube.
- `genre` - the genre of the song.

`Assumptions:`
- The `ratings` feature has a scale of `1 - 5` with a half-step count, i.e, `1.5`, `2.5`. The half-step count is assigned to `55%` of each scale bin, i.e. if the bin of scale `1.0` has `4000` records, `2200` will be `1.5`, while `1800` will be `1.0`. `This does not apply for scale 5.0`
- A `like` is worth a `3` point score and assigned to `ratings >= 3.5` with a `.45` probability of being assigned.

`Data:`
- The song `title`, `artist`, `views` and `year` were scraped from [kworb](https://kworb.net/youtube/topvideos_published_2023.html), while the genre was scraped from [Spotify](https://developer.spotify.com/dashboard/) and [MusicBrainz](https://musicbrainz.org/artist/f4fdbb4c-e4b7-47a0-b83b-d91bbfcfa387) 
- The `ratings` feature is derived by splitting the `views` into 5 equal bins, and
- The `likes` feature was populated in Google Sheets.

`Data Stat:`
- Total number of `ratings` - `51,472`.
- Unique `MusicId's` - `4,830`.
- Unique `Users` - `325`.

`Run Script:`
- To run the `scrape_music.py` file, copy and paste this into your terminal or bash `python3 scrape_music.py` and run. Depending on the `Python` you have installed, you may use `python scrape_music.py`.

-----------------

A brief article of the project can be found [here](https://medium.com/@aoluf/music-recommendation-system-a-shallow-dive-fca7b699f4a4)
