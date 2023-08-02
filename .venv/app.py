import streamlit as st
import pandas as pd
import pickle
import requests
import pandas as pd

url = "https://api.themoviedb.org/3/movie/movie_id?language=en-US"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer 78c3494e4cc05cb34e2e7abfec9e65ec"
}

response = requests.get(url, headers=headers)

print(response.text)

movies_list = pickle.load(open('movies.pkl', 'rb'))

movies_list = movies_list['title'].values

movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))

movies = pd.DataFrame(movies_dict)

simelarity = pickle.load(open("simelarity.pkl", "rb"))

st.title("Movies Recomendation System")


selected_movie_name = st.selectbox("which Movie did you want", movies_list)

def fetch_poster(movi_id):
    pass

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    
    distances = simelarity[movie_index]
    
    movie_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x : x[1])[1 : 6]
    
    recommended_movies = []
    
    for i in movie_list:
        movie_id = i[0]
        
        #fetching poster
        
        recommended_movies.append(movies.iloc[i[0]].title)
    
    return recommended_movies

if st.button('recommend'):
    recommendations = recommend(selected_movie_name)
    for i in recommendations:
        st.write(i)
