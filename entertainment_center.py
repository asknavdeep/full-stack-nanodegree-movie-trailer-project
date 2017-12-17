import fresh_tomatoes
import media
#importing python modules to organise code logically





    # This is where new objects of the class Movie are created and are given respective values.

    #Batman Begins: movie title, IMDB rating, Release Date, Poster Image URL, Youtube Trailer URL
    batman_1=media.Movie("Batman Begins",
                         "8.3",
                         "15 June 2005",
                         "http://posterwire.com/wp-content/uploads/batman_begins_teaser_c.jpg",
                         "https://youtu.be/neY2xVmOfUM")
    #The Dark Knight: movie title, IMDB rating, Release Date, Poster Image URL, Youtube Trailer URL
    batman_2=media.Movie("The Dark Knight",
                         "9.0",
                         "18 July 2008",
                         "https://angryweb.files.wordpress.com/2008/05/joker20bannerif5.jpg",
                         "https://youtu.be/EXeTwQWrcwY")
    #The Dark Knight Rises: movie title, IMDB rating, Release Date, Poster Image URL, Youtube Trailer URL
    batman_3=media.Movie("The Dark Knight Rises",
                         "8.4",
                         "20 July 2012",
                         "http://images5.fanpop.com/image/photos/30700000/Tom-Hardy-as-Bane-in-The-Dark-Knight-Rises-HQ-bane-30728012-1600-2366.jpg",
                         "https://youtu.be/GokKUqLcvD8")
    #Inception: movie title, IMDB rating, Release Date, Poster Image URL, Youtube Trailer URL
    inception=media.Movie("Inception",
                          "8.8",
                          "16 July 2010",
                          "http://cdn.collider.com/wp-content/uploads/Inception-movie-poster-7.jpg",
                          "https://youtu.be/YoHD9XEInc0")
    #Dinkirk: movie title, IMDB rating, Release Date, Poster Image URL, Youtube Trailer URL
    dunkirk=media.Movie("Dunkirk",
                        "8.2",
                        "21 July 2017",
                        "https://orig00.deviantart.net/55a4/f/2017/187/d/9/d90a1a3fe173e96e786dffda9cc50301-dbfa97a.jpg",
                        "https://youtu.be/VQ01tJ4EWeg")
    #The Prestige: movie title, IMDB rating, Release Date, Poster Image URL, Youtube Trailer URL
    prestige=media.Movie("The Prestige",
                         "8.5",
                         "20 October 2006",
                         "https://images-na.ssl-images-amazon.com/images/I/41I9XGrG88L.jpg",
                         "https://youtu.be/ijXruSzfGEc")


    #array of the instances created and passed in the function open_movies_page() situated in fresh_tomatoes.py
    movies = [batman_1,batman_2,batman_3,inception,dunkirk,prestige]
    fresh_tomatoes.open_movies_page(movies)

