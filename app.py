# from tkinter import Button
import streamlit as st
import pickle
import numpy as np
import pandas as pd 

st.set_page_config(layout="wide")

def recommend_book(book):
    index = np.where(pt.index==book)[0][0]
    similar_books = sorted(list(enumerate(similarity_score[index])),key=lambda x:x[1],reverse=True)[1:6]
    
    data = []
    for i in similar_books:
        item = []
        temp_df = books[books['Book-Title'] == pt.index[i[0]]]
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Title'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Book-Author'].values))
        item.extend(list(temp_df.drop_duplicates('Book-Title')['Image-URL-M'].values))
        
        data.append(item)
    return data

books_df = pd.read_csv("Data/Books.csv")
ratings_df = pd.read_csv("Data/Ratings.csv")
users_df = pd.read_csv("Data/Users.csv")

st.header("Book Recommender System")
popular = pickle.load(open('popular.pkl','rb'))
books = pickle.load(open('books.pkl','rb'))
pt = pickle.load(open('pt.pkl','rb'))
similarity_score = pickle.load(open('similarity_scores.pkl','rb'))

book_list = pt.index.values
image_url = popular['Image-URL-M'].tolist()
book_title = popular['Book-Title'].tolist() 
book_author = popular['Book-Author'].tolist()
total_ratings = popular['num_ratings'].tolist()
avg_ratings = popular['avg_rating'].tolist()

# Streamlit header
st.sidebar.title("Data Used")

if st.sidebar.button("Show Data"): 
    st.subheader('This is the Books data we used in our model')
    st.dataframe(books_df)
    st.subheader('This is the Books Ratings data we used in our model')
    st.dataframe(ratings_df)
    st.subheader('This is the Users data we used in our model')
    st.dataframe(users_df)


# Streamlit header
st.sidebar.title("Top 50 Books")

# Display books if the button is clicked
if st.sidebar.button("SHOW"):
    # Number of columns per row
    cols_per_row = 5
    total_books = len(image_url)  # Assuming all lists have the same length

    # Calculate the number of rows needed
    # rows = (total_books + cols_per_row - 1) // cols_per_row
    rows = 8
    # Loop through each row
    for row in range(rows):
        cols = st.columns(cols_per_row)
        
        # Loop through each column in the current row
        for col_idx in range(cols_per_row):
            book_idx = row * cols_per_row + col_idx
            if book_idx < total_books:
                with cols[col_idx]:
                    st.image(image_url[book_idx])
                    st.text(book_title[book_idx])
                    st.text(book_author[book_idx])
                    st.text("Ratings: " + str(total_ratings[book_idx]))
                    st.text("Avg. Rating: " + str(round(avg_ratings[book_idx], 2))) 
                    
                    
st.sidebar.title("Recommend Books")
selected_book = st.sidebar.selectbox("Type or select a book from the dropdown",book_list)
if st.sidebar.button("Recommend Me"):
    moviee = recommend_book(selected_book)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.image(moviee[0][2])
        st.text(moviee[0][0])
        st.text(moviee[0][1])  
    with col2:
        st.image(moviee[1][2])
        st.text(moviee[1][0])
        st.text(moviee[1][1])
    with col3:
        st.image(moviee[2][2])
        st.text(moviee[2][0])
        st.text(moviee[2][1])
    with col4:
        st.image(moviee[3][2])
        st.text(moviee[3][0])
        st.text(moviee[3][1])
    with col5:
        st.image(moviee[4][2])
        st.text(moviee[4][0])
        st.text(moviee[4][1]) 
        
        