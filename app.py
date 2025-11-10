import streamlit as st
import pandas as pd
import pickle

movies=pickle.load(open('movies.pkl','rb'))
movies_list=movies['title'].values
similarity=pickle.load(open('similarity.pkl','rb'))

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    moviess = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommended_movies = []



    for i in moviess:
        movie_id=i[0]
        # fetch poster from api

        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies





st.title('movie recommendation system')
selected_movie_name=st.selectbox('Select Movie',
                                 movies_list)
# option = st.selectbox(
#     'how would you like to see the recommendation?',
#     movies_list
# )

if st.button('recommend movies'):
    recommendations=recommend(selected_movie_name)
    for r in recommendations:

        st.write(r)



