import joblib
from sklearn.feature_extraction.text import TfidfVectorizer

# Load the saved model
rf = joblib.load('LogisticRegression.pkl')

# Load the TF-IDF vectorizer
tfid = joblib.load('TfidfVectorizer.pkl')  # Load the vectorizer used during training

# Define your predict_type function
def predict_type(arr):
    # Transform input text using the loaded vectorizer
    x = tfid.transform(arr).toarray()  # Convert to array
    # Make predictions
    res = rf.predict(x).tolist()  # Convert predictions to list
    return res

