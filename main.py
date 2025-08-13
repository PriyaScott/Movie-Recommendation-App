import pandas as pd

# Movie data stored directly in code
data = [
    {"Title": "Inception", "Genre": "Sci-Fi", "Year": 2010, "Rating": 8.8},
    {"Title": "The Matrix", "Genre": "Sci-Fi", "Year": 1999, "Rating": 8.7},
    {"Title": "Interstellar", "Genre": "Sci-Fi", "Year": 2014, "Rating": 8.6},
    {"Title": "The Godfather", "Genre": "Crime", "Year": 1972, "Rating": 9.2},
    {"Title": "Pulp Fiction", "Genre": "Crime", "Year": 1994, "Rating": 8.9},
    {"Title": "The Dark Knight", "Genre": "Action", "Year": 2008, "Rating": 9.0},
    {"Title": "Avengers: Endgame", "Genre": "Action", "Year": 2019, "Rating": 8.4},
    {"Title": "La La Land", "Genre": "Romance", "Year": 2016, "Rating": 8.0},
    {"Title": "Titanic", "Genre": "Romance", "Year": 1997, "Rating": 7.9},
    {"Title": "The Shawshank Redemption", "Genre": "Drama", "Year": 1994, "Rating": 9.3},
    {"Title": "Forrest Gump", "Genre": "Drama", "Year": 1994, "Rating": 8.8}
]

# Convert to DataFrame
movies = pd.DataFrame(data)

print("🎬 Welcome to the Movie Recommendation App 🎬")
genre = input("Enter your favorite genre: ").strip()

# Filter movies by genre
filtered = movies[movies['Genre'].str.contains(genre, case=False, na=False)]
if filtered.empty:
    print(f"❌ Sorry, no movies found for genre '{genre}'.")
else:
    top_movies = filtered.sort_values(by='Rating', ascending=False).head(5)
    print("\nHere are your top recommendations:")
    for _, row in top_movies.iterrows():
        print(f"- {row['Title']} ({row['Year']}) ⭐ {row['Rating']}")
