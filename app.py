import streamlit as st
import pandas as pd

# ✅ Updated caching decorator
@st.cache_data
def load_data():
    movies = pd.read_csv("movies.csv")
    ratings = pd.read_csv("ratings.csv")
    return movies, ratings

# 🎬 Extract unique genres from the movies dataset
def get_unique_genres(movies):
    genre_set = set()
    for genres in movies['genres']:
        genre_set.update(genres.split('|'))
    return sorted(genre_set)

# 🎯 Recommend top 5 movies in the selected genre
def recommend_movies(genre, movies, ratings):
    # Filter movies by genre
    genre_movies = movies[movies['genres'].str.contains(genre, case=False, na=False)]

    # Merge with ratings data
    merged = pd.merge(genre_movies, ratings, on='movieId')

    # Compute average rating and rating count per movie
    movie_stats = merged.groupby('title')['rating'].agg(['mean', 'count']).reset_index()
    movie_stats.columns = ['title', 'avg_rating', 'rating_count']

    # Filter out movies with low number of ratings (optional)
    movie_stats = movie_stats[movie_stats['rating_count'] >= 10]

    # Sort by average rating
    top_movies = movie_stats.sort_values(by='avg_rating', ascending=False).head(5)

    return top_movies

# 🖼️ Streamlit UI
def main():
    st.title("🎬 Genre-Based Movie Recommender")
    st.write("Pick a genre to discover the top-rated movies based on viewer ratings.")

    movies, ratings = load_data()
    genres = get_unique_genres(movies)

    selected_genre = st.selectbox("🎭 Select a Genre", genres)

    if st.button("🎥 Get Recommendations"):
        top_movies = recommend_movies(selected_genre, movies, ratings)
        if not top_movies.empty:
            st.subheader("⭐ Top 5 Movies")
            for idx, row in top_movies.iterrows():
                st.markdown(f"**{row['title']}**  \n⭐ {row['avg_rating']:.2f} — {int(row['rating_count'])} ratings")
        else:
            st.warning("No recommendations found for this genre.")

if __name__ == "__main__":
    main()
