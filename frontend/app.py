import streamlit as st
import requests
import base64
import os

def get_base64(image_path):

    with open(image_path, "rb") as img:

        return base64.b64encode(img.read()).decode()

st.set_page_config(
    page_title="Movie Explorer",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

BASE_URL =  os.getenv(
    "BASE_URL",
    "http://127.0.0.1:8000"
)
background = get_base64(
    os.path.join(
        os.path.dirname(__file__),
        "images",
        "gh.jpeg"
    )
)
st.markdown(f"""
<style>

[data-testid="stAppViewContainer"] {{
    background:
        linear-gradient(
            rgba(10,10,10,0.75),
            rgba(10,10,10,0.75)
        ),
        url("data:image/jpeg;base64,{background}");

    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    background-attachment: fixed;
}}

.main {{
    background: transparent;
}}

section[data-testid="stSidebar"] {{
    background-color: #111827;
}}

.stButton > button {{
    width: 100%;
    height: 45px;
    border-radius: 10px;
    background: #E50914;
    color: white;
    font-weight: bold;
    border: none;
}}

.stButton > button:hover {{
    background: #B20710;
    color: white;
}}

div[data-testid="stMetric"] {{
    background: #1F2937;
    border-radius: 12px;
    padding: 15px;
}}

hr {{
    margin-top: 20px;
    margin-bottom: 20px;
}}

</style>
""", unsafe_allow_html=True)

st.title("🎬 Movie Explorer & Review Management System")

with st.sidebar:

    st.title("🍿 Movie Explorer")

    st.caption("FastAPI + Streamlit")

    st.divider()

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "🏠 Home",
        "🎬 View all Movies",
        "🎬 View a single Movie",
        "🔍 Search Movies",
        "➕ Add Movie",
        "✏️ Update Movie",
        "🗑️ Delete Movie"
    ]
)

if menu == "🏠 Home":

    st.markdown("""
    <div style="
    padding:30px;
    border-radius:15px;
    background:linear-gradient(135deg,#111827,#1F2937);
    border:1px solid #374151;
    ">

    <h1 style="color:#FFD700;">
    🎬 Movie Explorer
    </h1>

    <p style="color:white;font-size:18px;">
    Discover, Search, Update and Manage your Movie Collection.
    Built using FastAPI and Streamlit.
    </p>

    </div>
    """, unsafe_allow_html=True)

    st.divider()

    response = requests.get(f"{BASE_URL}/movies")

    if response.status_code == 200:

        movies = response.json()

        total_movies = len(movies)

        highest_rating = max(
            (movie["rating"] for movie in movies),
            default=0
        )

        total_languages = len(
            set(movie["language"] for movie in movies)
        )

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("🎬 Movies", total_movies)

        with col2:
            st.metric("⭐ Highest Rating", highest_rating)

        with col3:
            st.metric("🌍 Languages", total_languages)

        st.divider()

        st.info("""
🍿 Welcome!

This Movie Explorer demonstrates the complete Full Stack flow:

Frontend → API Request → FastAPI Backend → CRUD Operation →
JSON Response → Frontend Display
""")

    else:

        st.error("Unable to connect to the FastAPI backend.")

elif menu == "🎬 View all Movies":

    st.header("🎬 Movie Collection")

    response = requests.get(f"{BASE_URL}/movies")

    if response.status_code == 200:

        movies = response.json()

        if movies:

            for movie in movies:

                st.markdown(f"""
<div style="
background:#1F2937;
padding:18px;
margin-bottom:15px;
border-radius:12px;
border-left:6px solid #E50914;
">

<h3 style="color:#FFD700;">
🎬 {movie["movie_name"]}
</h3>

<b>🆔 ID:</b> {movie["id"]}<br>

<b>🎭 Genre:</b> {movie["genre"]}<br>

<b>🌍 Language:</b> {movie["language"]}<br>

<b>⭐ Rating:</b> {movie["rating"]}/10

</div>
""", unsafe_allow_html=True)

        else:

            st.warning("No movies available.")

    else:

        st.error("Failed to fetch movies.")

elif menu == "🎬 View a single Movie":

    st.header("🎬 View a single Movie")

    movie_id = st.number_input(
        "Enter Movie ID",
        min_value=1,
        step=1
    )

    if st.button("🔍 Find Movie"):

        response = requests.get(
            f"{BASE_URL}/movies/{movie_id}"
        )

        if response.status_code == 200:

            movie = response.json()

            if "message" in movie:
                st.warning("⚠️ Movie not found.")
            else:
                st.success("Movie found!")

                st.markdown(
                    f"""
                    <div style="
                        padding:20px;
                        border-radius:15px;
                        background:rgba(31,41,55,0.90);
                        border:1px solid #374151;
                        margin-top:15px;
                    ">

                    <h2 style="color:#FFD700;">
                        🎬 {movie["movie_name"]}
                    </h2>

                    <p style="color:white;font-size:16px;">
                        <b>🆔 ID:</b> {movie["id"]}
                    </p>

                    <p style="color:white;font-size:16px;">
                        <b>🎭 Genre:</b> {movie["genre"]}
                    </p>

                    <p style="color:white;font-size:16px;">
                        <b>🌍 Language:</b> {movie["language"]}
                    </p>

                    <p style="color:white;font-size:16px;">
                        <b>⭐ Rating:</b> {movie["rating"]}/10
                    </p>

                    </div>
                    """,
                    unsafe_allow_html=True
                )

        else:
            st.error("❌ Failed to fetch movie.")

elif menu == "🔍 Search Movies":

    st.header("🔍 Search Movies")

    st.write("Filter movies by Genre, Language or Rating.")

    col1, col2 = st.columns(2)

    with col1:
        genre = st.text_input("🎭 Genre")

    with col2:
        language = st.text_input("🌍 Language")

    rating = st.slider(
        "⭐ Rating",
        min_value=0,
        max_value=10,
        value=0
    )

    if st.button("🔍 Search"):

        response = requests.get(
            f"{BASE_URL}/movies/filter",
            params={
                "genre": genre if genre else None,
                "language": language if language else None,
                "rating": rating if rating != 0 else None
            }
        )

        if response.status_code == 200:

            movies = response.json()

            if movies:

                st.success(f"Found {len(movies)} movie(s).")

                for movie in movies:

                    st.markdown(f"""
<div style="
background:#1F2937;
padding:18px;
margin-bottom:15px;
border-radius:12px;
border-left:6px solid #22C55E;
">

<h3 style="color:#FFD700;">
🎬 {movie["movie_name"]}
</h3>

<b>🆔 ID:</b> {movie["id"]}<br>

<b>🎭 Genre:</b> {movie["genre"]}<br>

<b>🌍 Language:</b> {movie["language"]}<br>

<b>⭐ Rating:</b> {movie["rating"]}/10

</div>
""", unsafe_allow_html=True)

            else:

                st.warning("No matching movies found.")

        else:

            st.error("Search request failed.")

elif menu == "➕ Add Movie":

    st.header("➕ Add New Movie")

    st.write("Enter the details below to add a movie.")

    movie_id = st.number_input(
        "🆔 Movie ID",
        min_value=1,
        step=1
    )

    movie_name = st.text_input("🎬 Movie Name")

    genre = st.text_input("🎭 Genre")

    language = st.text_input("🌍 Language")

    rating = st.slider(
        "⭐ Rating",
        min_value=1,
        max_value=10,
        value=5
    )

    if st.button("➕ Add Movie"):

        if not movie_name.strip():

            st.error("Movie Name cannot be empty.")

        elif not genre.strip():

            st.error("Genre cannot be empty.")

        elif not language.strip():

            st.error("Language cannot be empty.")

        else:

            movie_data = {
                "id": movie_id,
                "movie_name": movie_name,
                "genre": genre,
                "language": language,
                "rating": rating
            }

            response = requests.post(
                f"{BASE_URL}/movies",
                json=movie_data
            )

            if response.status_code == 200:

                st.success(f"🎉 '{movie_name}' added successfully!")

                st.json(response.json())

            else:

                st.error("Failed to add movie.")

elif menu == "✏️ Update Movie":

    st.header("✏️ Update Movie")

    st.write("Update the details of an existing movie.")

    movie_id = st.number_input(
        "🆔 Movie ID",
        min_value=1,
        step=1
    )

    movie_name = st.text_input("🎬 Movie Name")

    genre = st.text_input("🎭 Genre")

    language = st.text_input("🌍 Language")

    rating = st.slider(
        "⭐ Rating",
        min_value=1,
        max_value=10,
        value=5
    )

    if st.button("✏️ Update Movie"):

        if not movie_name.strip():

            st.error("Movie Name cannot be empty.")

        elif not genre.strip():

            st.error("Genre cannot be empty.")

        elif not language.strip():

            st.error("Language cannot be empty.")

        else:

            updated_movie = {
                "id": movie_id,
                "movie_name": movie_name,
                "genre": genre,
                "language": language,
                "rating": rating
            }

            response = requests.put(
                f"{BASE_URL}/movies/{movie_id}",
                json=updated_movie
            )

            if response.status_code == 200:

                st.success(f"✅ Movie ID {movie_id} updated successfully!")

                st.json(response.json())

            else:

                st.error("Failed to update movie.")

elif menu == "🗑️ Delete Movie":

    st.header("🗑️ Delete Movie")

    st.warning(
        "Deleting a movie will permanently remove it from the collection."
    )

    movie_id = st.number_input(
        "🆔 Movie ID",
        min_value=1,
        step=1,
        key="delete_movie_id"
    )

    if st.button("🗑️ Delete Movie"):

        response = requests.delete(
            f"{BASE_URL}/movies/{movie_id}"
        )

        if response.status_code == 200:

            st.success(f"🗑️ Movie ID {movie_id} deleted successfully!")

            st.json(response.json())

        else:

            st.error("Failed to delete movie.")
st.divider()

st.markdown(
    """
<div style="
text-align:center;
padding:20px;
color:#9CA3AF;
font-size:15px;
">

🎬 <b>Movie Explorer & Review Management System</b><br><br>

Built using <b>FastAPI</b> ⚡ + <b>Streamlit</b> 🚀

</div>
""",
    unsafe_allow_html=True
)