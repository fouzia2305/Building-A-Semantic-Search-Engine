import streamlit as st
import pandas as pd
from sentence_transformers import SentenceTransformer
import faiss
import time
import torch 
import pickle



# Check if GPU is available
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load the DataFrame containing subtitles
df_subtitle = pd.read_csv('final_subtitles.csv')

# Load the SentenceTransformer model with GPU support
model = SentenceTransformer("all-MiniLM-L6-v2", device=device)
with open("subtitle_embds.pkl", "rb") as file:
    subtitle_embds = pickle.load(file)

# Load the index
index = faiss.IndexFlatL2(subtitle_embds.shape[1])
index.add(subtitle_embds)
faiss.write_index(index, 'index_subtitles')
index = faiss.read_index('index_subtitles')

# Function to perform search
def search(query):
    t = time.time()
    query_vector = model.encode([query])
    k = 5
    top_k = index.search(query_vector, k)
    print('totaltime: {}'.format(time.time()-t))
    
    # Retrieve the document names corresponding to the top_k indices
    top_k_ids = top_k[1].tolist()[0]
    document_names = [df_subtitle.loc[_id, 'name'] for _id in top_k_ids]
    
    return document_names

def main():
    
    
    
    # Set page config
    st.set_page_config(page_title="AI Movie Subtitle Explorer", page_icon="🎥", layout="wide")
    page_bg_img = '''
    <style>
    body {
        background-image: url("https://img.freepik.com/free-photo/movie-background-collage_23-2149876006.jpg?size=626&ext=jpg&ga=GA1.1.1776949639.1714148261&semt=ais");
        background-size: cover;
        font-family: Arial, sans-serif;
    }
    </style>
    '''
    st.markdown(page_bg_img, unsafe_allow_html=True)
    # Custom CSS styles
    st.markdown(
        """
        <style>
        

        .stTextInput>div>div>div>input {
            background-color: #82A78D; /* Juicy palm */
            color: #000000;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
            border: none;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
        }
        .stButton>button {
            background-color: #FF69B4; /* Hot pink */
            color: #FFFFFF;
            font-weight: bold;
            padding: 10px 20px;
            font-size: 18px;
            border: none;
            border-radius: 5px;
            box-shadow: 0px 0px 10px rgba(255, 105, 180, 0.5);
            transition: background-color 0.3s ease;
            animation: pulse 2s infinite; /* Apply animation */
        }
        .stButton>button:hover {
            background-color: #FF1493; /* Deep pink */
        }
        .stMarkdown>div {
            color: #000000;
            font-size: 18px;
            line-height: 1.6;
        }

        @keyframes pulse {
            0% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 105, 180, 0.7); }
            70% { transform: scale(1); box-shadow: 0 0 0 10px rgba(255, 105, 180, 0); }
            100% { transform: scale(0.95); box-shadow: 0 0 0 0 rgba(255, 105, 180, 0); }
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
   
    # Title and header
    st.title('🔍 Welcome to the AI Movie Subtitle Explorer! 🎬')
    st.subheader('Search for movie subtitles and explore relevant results.')

    # User input for search query
    query = st.text_input("Enter a subtitle here 🎥🔍")

    # Perform search when button is clicked
    if st.button("Search"):
        if query:
            results = search(query)
            st.write("Search Results:")
            for i, result in enumerate(results, 1):
                st.write(f"{i}. {result}")

if __name__ == "__main__":
    main()