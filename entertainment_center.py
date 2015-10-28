import media
import fresh_tomatoes

donnie_darko = media.Movie("Donnie Darko",
                           "A distrubed boy and his good friend Frank",
                           "http://yify-movie.com/images/bposter/donnie-darko-directors-cut-2001-movie-poster.jpg",
                           "https://www.youtube.com/watch?v=ZZyBaFYFySk")

black_swan = media.Movie("Black Swan",
                         "Dark vs light vs dance",
                         "https://upload.wikimedia.org/wikipedia/en/6/68/Black_Swan_poster.jpg",
                         "https://www.youtube.com/watch?v=5jaI1XOB-bs")

dune = media.Movie("Dune",
                   "Spice wars lead to death",
                   "https://upload.wikimedia.org/wikipedia/en/5/51/Dune_1984_Poster.jpg",
                   "https://www.youtube.com/watch?v=hzUlXEyvJeA")

orange_county = media.Movie("Orange County",
                            "Lets go to Stanford",
                            "https://upload.wikimedia.org/wikipedia/en/7/78/Orange_county_poster.jpg",
                            "")

robin_hood = media.Movie("Robin Hood",
                         "Getting merry with his men",
                         "https://upload.wikimedia.org/wikipedia/en/9/91/Robinhood_1973_poster.png",
                         "https://www.youtube.com/watch?v=c5Qph47c2uE")

warrior = media.Movie("Warrior",
                      "Two brothers swinging arms",
                      "https://upload.wikimedia.org/wikipedia/en/e/e3/Warrior_Poster.jpg",
                      "https://www.youtube.com/watch?v=I5kzcwcQA1Q")

movies = [donnie_darko, black_swan, dune, orange_county, robin_hood, warrior]

fresh_tomatoes.open_movies_page(movies)
