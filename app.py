import pickle
import streamlit as st
import numpy as np

st.header('Books Recommender System Using Collaborative Method')

model = pickle.load(open('model.pkl','rb'))
books_name = pickle.load(open('books_name.pkl','rb'))
final_rating = pickle.load(open('final_rating.pkl','rb'))
book_pivot = pickle.load(open('book_pivot.pkl','rb'))

selected_books = st.selectbox(
    "Type or Select a Book",
    books_name
)

def recommend_book(book_name):
    book_list=[]
    book_id=np.where(book_pivot.index == book_name)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1),n_neighbors=6)

    poster_url = fetch_poster(suggestion)
    
    for i in range(len(suggestion)):
        books=book_pivot.index[suggestion[i]]
    for j in books:
        book_list.append(j)
    return book_list,poster_url

def fetch_poster(suggestion):
    books_name=[]
    ids_index=[]
    poster_url=[]

    for book_id in suggestion:
        books_name.append(book_pivot.index[book_id])

    for name in books_name[0]:
        ids = np.where(final_rating['Title'] == name)[0][0]
        ids_index.append(ids)
    for ids in ids_index:
        url=final_rating.iloc[ids]['Image-URL']
        poster_url.append(url)
    return poster_url
        
    
    
if st.button("Show Recommendation"):
    recommendation_book,poster_url = recommend_book(selected_books)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommendation_book[1])
        st.image(poster_url[1])
    with col2:
        st.text(recommendation_book[2])
        st.image(poster_url[2])
    with col3:
        st.text(recommendation_book[3])
        st.image(poster_url[3])
    with col4:
        st.text(recommendation_book[4])
        st.image(poster_url[4])
    with col5:
        st.text(recommendation_book[5])
        st.image(poster_url[5])