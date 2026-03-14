# 🎬 Movie Recommendation System using Streamlit

A **web-based movie recommendation system** built with **Streamlit** that recommends **top-rated movies based on selected genres**. The system analyzes user rating patterns from a public dataset to suggest the best movies.

---

# 📌 Overview

This application allows users to:

- Select a movie **genre** from the sidebar
- View the **Top 5 movie recommendations** in that genre
- Discover movies based on **average user ratings**

The system uses two datasets:

- **movies.csv** — Contains movie titles and genres
- **ratings.csv** — Contains user ratings for movies

---

# 🧰 Tech Stack

- **Python**
- **Streamlit**
- **Pandas**
- **NumPy**

---

# 📁 Project Structure

```
movie-recommender
│
├── app.py               # Main Streamlit application
├── movies.csv           # Dataset containing movie information
├── ratings.csv          # Dataset containing user ratings
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

---

# ⚙️ Features

- 🎯 Genre-based movie filtering
- ⭐ Rating-based recommendation system
- 📊 Displays top 5 highest rated movies
- 🖥️ Interactive Streamlit web interface
- 📂 Uses real-world movie rating dataset

---

# 📊 Dataset Description

## movies.csv

| Column Name | Description |
|-------------|-------------|
| movieId | Unique identifier for each movie |
| title | Movie title |
| genres | Pipe-separated list of genres |

Example:

```
movieId,title,genres
1,Toy Story (1995),Adventure|Animation|Children|Comedy|Fantasy
```

---

## ratings.csv

| Column Name | Description |
|-------------|-------------|
| userId | Unique identifier for user |
| movieId | Movie identifier |
| rating | Rating given by user |
| timestamp | Time of rating (UNIX format) |

Example:

```
userId,movieId,rating,timestamp
1,1,4.0,964982703
```

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/movie-recommender.git
cd movie-recommender
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3️⃣ Run the Application

```bash
streamlit run app.py
```

The application will open automatically in your browser:

```
http://localhost:8501
```

---

# 💡 Recommendation Logic

The recommendation system works using the following steps:

1. Load **movies.csv** and **ratings.csv**
2. Merge both datasets using **movieId**
3. Extract all unique **movie genres**
4. When a user selects a genre:
   - Filter movies belonging to that genre
   - Calculate **average rating** for each movie
   - Count total ratings per movie
5. Filter movies with **minimum rating threshold** (e.g., 10 ratings)
6. Sort movies by **highest average rating**
7. Display **Top 5 recommended movies**

---

# 📈 Example Output

When a user selects a genre like **Action**, the app displays:

| Movie Title | Average Rating |
|-------------|---------------|
| Movie A | 4.7 |
| Movie B | 4.6 |
| Movie C | 4.5 |
| Movie D | 4.4 |
| Movie E | 4.3 |

---

# 🔮 Future Improvements

- Add **content-based filtering**
- Add **collaborative filtering**
- Improve UI with **movie posters**
- Deploy the app using **Streamlit Cloud**
- Add **user login & personalized recommendations**

---

# 👩‍💻 Author

**Thumma Manojna Reddy**

AI / ML Enthusiast  
B.Tech CSE (AI & ML)

GitHub  
https://github.com/thummamanojnareddy

LinkedIn  
https://www.linkedin.com/in/manojna-reddy-thumma-536b9730b/

---

⭐ If you found this project helpful, consider **starring the repository**!
