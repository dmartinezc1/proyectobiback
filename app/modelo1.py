import joblib
from sklearn.feature_extraction.text import TfidfVectorizer 

loaded_rf, tfidf_vectorizer = joblib.load("./random_forest.joblib")

def predict(w):
#    vect = TfidfVectorizer()
    x_test= tfidf_vectorizer.transform(w)
    return loaded_rf.predict(x_test)

