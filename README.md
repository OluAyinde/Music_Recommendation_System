In this project, a music recommendation system was developed to find similar songs and recommend new songs based on a user's preferences, i.e., how they have `rated` a song or if they have `liked` a song.

It features 2 different models: `ratings` only and the `hybrid` model.

- The `ratings` model utilises only the `ratings` feature to develop the recommendation system, while
- The `hybrid` model utilises the `ratings`, `likes` & `genre` features to develop the recommendation system with each feature contributing different weights; `ratings = [0.5]`, `likes = [0.3]` & `genre = [0.2]`.


`Assumptions:`
- The `ratings` feature has a scale of `1 - 5` with a half-step count, i.e, `1.5`, `2.5`.
- A `like` is worth a `4` point score and assigned to `ratings >= 3.5` with a `.45` probability of being assigned.

`Data:`
- The song `name` and `genre` were downloaded from [Kaggle](https://www.kaggle.com/datasets/saurabhshahane/music-dataset-1950-to-2019?resource=download).
- The `ratings` feature is a dummy dataset generated using deepseek, with higher `ratings` having more weightage, while
- The `likes` feature was populated in Google Sheets.
