# Enhancing Search Engine Relevance for Video Subtitles

## Background

In the digital content landscape, effective search engines are crucial for connecting users with relevant information. Google, as a leading search engine, prioritizes providing a seamless and accurate search experience. This project focuses on improving the relevance of search results for video subtitles, thereby enhancing the accessibility of video content.

## Objective

The objective is to develop an advanced search engine algorithm that efficiently retrieves subtitles based on user queries, with a specific emphasis on subtitle content. The goal is to leverage natural language processing (NLP) and machine learning techniques to enhance the relevance and accuracy of search results.

## Keyword-Based vs Semantic Search Engines

- **Keyword-Based Search Engine:** Relies heavily on exact keyword matches between user queries and indexed documents.
- **Semantic Search Engines:** Go beyond keyword matching to understand the meaning and context of user queries and documents.

## Core Logic

To compare a user query against a video subtitle document, the core logic involves three key steps:

1. **Preprocessing of Data:** 
   - Clean the text data by removing timestamps and applying appropriate cleaning steps.
   
2. **Vectorization of Subtitle Documents:** 
   - Experiment with methods like Bag-of-Words (BOW), TF-IDF, and BERT-based SentenceTransformers to generate embeddings for semantic information.

3. **Document Chunker:** 
   - Divide large documents into smaller, manageable chunks to mitigate information loss and ensure context continuity.
   - Store embeddings in ChromaDB for efficient retrieval.

## Part 1: Ingesting Documents

1. Read the provided data, which is in a database file format.
2. Decode the files inside the database and consider sampling 30% of the data if compute resources are limited.
3. Apply appropriate cleaning steps on subtitle documents.
4. Experiment with various methods to generate text vectors of subtitle documents, considering both sparse vector representations (BOW/TFIDF) and semantic embeddings (BERT-based SentenceTransformers).
5. Implement a Document Chunker to handle large documents effectively.
6. Store embeddings in ChromaDB.

## Part 2: Retrieving Documents

1. Take the user's search query and preprocess it if necessary.
2. Create a query embedding.
3. Calculate cosine similarity scores between embeddings of documents and the user search query embedding.
4. Use cosine similarity scores to return the most relevant candidate documents based on the user’s search query.

## Conclusion

This project aims to enhance the search relevance for video subtitles by implementing advanced search engine algorithms and leveraging NLP techniques. By improving the accuracy and relevance of search results, the accessibility of video content can be significantly enhanced, benefiting users seeking specific information within video subtitles.

## Acknowledgements

- [ChromaDB](https://chromadb.com/)
- [BERT](https://github.com/google-research/bert)
- [SentenceTransformers](https://www.sbert.net/)

