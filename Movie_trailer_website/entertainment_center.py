import fresh_tomatoes
import media

# Logan movie: movie title, storyline, poster image and movie trailer
logan = media.Movie("Logan",
                    "A story about Wolverine's cloned daughter",
                    ("https://upload.wikimedia.org/wikipedia/en/3/37/"
                     "Logan_2017_poster.jpg"),
                    "https://www.youtube.com/watch?v=Div0iP65aZo",
                    "Audience Score: 91%"" liked it")

# 300 movie: movie title, storyline, poster image and movie trailer
three_hundred = media.Movie("300",
                            "A story about the Battle of Themopylae",
                            ("https://ae01.alicdn.com/kf/HTB1PPf5NFXXXXaJXFXXq"
                             "6xXFXXXR/-font-b-Spartan-b-font-font-b-300-b-"
                             "font-2007-font-b-Movie-b.jpg"),
                            "https://www.youtube.com/watch?v=UrIbxk7idYA",
                            "Audience Score: 89%"" liked it")

# Gladiator movie: movie title, storyline, poster image and movie trailer
gladiator = media.Movie("Gladiator",
                        "Maximus is forced to be a gladiator",
                        ("https://www.movieposter.com/posters/archive/main"
                         "/22/A70-11370"),
                        "https://www.youtube.com/watch?v=Q-b7B8tOAQU",
                        "Audience Score: 87%"" liked it")

# Braveheart movie: movie title, storyline, poster image and movie trailer
braveheart = media.Movie("Braveheart",
                         ("William Wallace fights for independence against the"
                          " evil King Edward I of England"),
                         ("https://upload.wikimedia.org/wikipedia/en/thumb/5/"
                          "55/Braveheart_imp.jpg/220px-Braveheart_imp.jpg"),
                         "https://www.youtube.com/watch?v=rXYCBBJBj6Y",
                         "Audience Score: 85%"" liked it")

# Rounders movie: movie title, storyline, poster image and movie trailer
rounders = media.Movie("Rounders",
                       ("Mike McDermott loses big to the Russian mob and has "
                        "to settle his debts"),
                       ("https://upload.wikimedia.org/wikipedia/en/thumb/6/67/"
                        "RoundersPoster.jpg/220px-RoundersPoster.jpg"),
                       "https://www.youtube.com/watch?v=cjUgHE3hxyg",
                       "Audience Score: 87%"" liked it")

# The Hangover movie: movie title, storyline, poster image and movie trailer
the_hangover = media.Movie("The Hangover",
                           ("Three buddies wake up from a crazy bachelor party"
                            " in Las Vegas"),
                           ("https://upload.wikimedia.org/wikipedia/en/thumb/b"
                            "/b9/Hangoverposter09.jpg/220px-Hangoverposter09."
                            "jpg"),
                           "https://www.youtube.com/watch?v=dB2jElYbTIo",
                           "Audience Score: 84%"" liked it")

movies = [logan, three_hundred, gladiator, braveheart, rounders, the_hangover]
fresh_tomatoes.open_movies_page(movies)
