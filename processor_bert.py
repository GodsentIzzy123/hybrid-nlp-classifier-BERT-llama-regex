import joblib
from sentence_transformers import SentenceTransformer

# Load the embedding model
embedding_model = SentenceTransformer('all-MiniLM-L6-v2')

# Load classifier and label encoder
classifier = joblib.load("models/log_classifier.joblib")
label_encoder = joblib.load("models/label_encoder.joblib")  # <- Add this

def classify_with_bert(log_message):
    embedding = embedding_model.encode(log_message)
    probabilities = classifier.predict_proba([embedding])[0]
    if max(probabilities) < 0.5:
        return "Unclassified"
    prediction = classifier.predict([embedding])
    label = label_encoder.inverse_transform(prediction)  # <- Decode label
    return label[0]


if __name__ == "__main__":
    logs = [
  
      "Multiple bad login attempts detected on user 8538 account",
      "Boot process terminated unexpectedly due to kernel issue",
      "User 7153 made multiple incorrect login attempts",#
      "API intrusion detection system flagged user 6771",
      "Server 46 restarted without warning during data migration",
      "Hello Virgil Van Dijk, Liverpool needs you "


    ]

    for log in logs:
        label = classify_with_bert(log)
        print(log, "--->", label)
