import pandas as pd
import numpy as np
from sentence_transformers import SentenceTransformer
import faiss

dataset=pd.read_csv("spacenews.csv")
news_dataset=dataset[["title","author","content","date"]]
news_dataset.dropna(inplace=True)
import re
def clean_text(text):
    text=text.lower()
    text=re.sub(r'[^a-zA-z0-9\s]',' ',text)
    text=re.sub(r'\s+',' ',text)
    return text
news_dataset["clean_content"]=news_dataset["content"].apply(clean_text)
model=SentenceTransformer('all-MiniLM-L6-v2')
# embeddings=model.encode(news_dataset["clean_content"].values)
# embeddings=np.array(embeddings)
# np.save("content_embeddings.npy",embeddings)
embeddings=np.load("content_embeddings.npy")
dimension=embeddings.shape[1]
faiss_index=faiss.IndexFlatL2(dimension)
faiss_index.add(embeddings)
# faiss.write_index(faiss_index,"content_faiss_index.index")
def get_similar_news(query,model=model,faiss_index=faiss_index,count=3):
    query_embedding=model.encode([query])
    distance,indices=faiss_index.search(query_embedding,count)
    results=[]
    for i in range(count):
        idx = indices[0][i]
        news_item = {
            "title": news_dataset["title"].iloc[idx],
            "author": news_dataset["author"].iloc[idx],
            "date": news_dataset["date"].iloc[idx],
            "content": news_dataset["content"].iloc[idx]
        }
        results.append(news_item)
    return results