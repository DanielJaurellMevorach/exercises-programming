def test_movie_count():
    movies = [
        {'title': 'Movie 1', 'director': 'Director 1'},
        {'title': 'Movie 2', 'director': 'Director 2'},
        {'title': 'Movie 3', 'director': 'Director 1'},
        {'title': 'Movie 4', 'director': 'Director 3'},
        {'title': 'Movie 5', 'director': 'Director 1'},
    ]
    
    # Test case 1: Director 1 has 3 movies
    assert movie_count(movies, 'Director 1') == [1, 3, 5]
    
    # Test case 2: Director 2 has 1 movie
    assert movie_count(movies, 'Director 2') == [2]
    
    # Test case 3: Director 3 has 1 movie
    assert movie_count(movies, 'Director 3') == [4]
    
    # Test case 4: Director 4 has 0 movies
    assert movie_count(movies, 'Director 4') == []
    
    # Test case 5: Empty movie list
    assert movie_count([], 'Director 1') == []
    
    print("All test cases pass")

test_movie_count()