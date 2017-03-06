def twoMoviesForTime(flight_length, movie_lengths):
    lengthsMap = {}

    for movie in movie_lengths:
        left = flight_length - movie

        if left in lengthsMap:
            return True

        if movie in lengthsMap:
            lengthsMap[movie] += 1
        else:
            lengthsMap[movie] = 1

    return False


flight_length = 124
movie_lengths = [
    60,
    64,
    10,
]
print(twoMoviesForTime(flight_length, movie_lengths))

flight_length = 124
movie_lengths = [
    64,
    64,
    10,
]
print(twoMoviesForTime(flight_length, movie_lengths))
