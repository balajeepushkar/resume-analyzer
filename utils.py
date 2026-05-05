from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(text1, text2):
    tfidf = TfidfVectorizer()
    
    vectors = tfidf.fit_transform([text1, text2])
    
    similarity = cosine_similarity(vectors[0], vectors[1])
    
    return similarity[0][0]