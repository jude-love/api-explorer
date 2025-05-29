import os

from google.cloud import language_v1
from flask import Flask, send_file, request, jsonify, make_response
from database import engine, SessionLocal, Base, User, Product, Purchase, Complaint
import requests

app = Flask(__name__)


# Create the database tables if they don't exist
with app.app_context():
    Base.metadata.create_all(bind=engine)

@app.route("/")
def index():
    return send_file('src/index.html')

@app.route("/create_user_profile", methods=["POST"])
def create_user_profile():
    user_data = request.json
    print(f"Saving user data: {user_data}")

    db = SessionLocal()
    try:
        new_user = User(name=user_data['name'], email=user_data['email'])
        db.add(new_user)
        db.commit()
        return {"message": "User profile created successfully"}
    finally:
        db.close()

@app.route("/process_query", methods=["POST"])
def process_query():
    query_data = request.json
    if 'query' in query_data:
        user_query = query_data['query']
        print(f"Processing natural language query: {user_query}")

        # Placeholder for Google Cloud Natural Language API integration
        # You would typically initialize the client with credentials here
        # client = language_v1.LanguageServiceClient()

        # document = language_v1.Document(content=user_query, type_=language_v1.Document.Type.PLAIN_TEXT)

        # # Perform sentiment analysis or other NLP tasks
        # sentiment = client.analyze_sentiment(request={'document': document}).document_sentiment
        # entities = client.analyze_entities(request={'document': document}).entities

        # # Process the API response to determine intent and extract parameters
        # # Based on intent and entities, call your internal API endpoints

        # For now, just acknowledge receipt and indicate where processing would go
        response_message = f"Received query: '{user_query}'. Processing with NLP (placeholder for Google Cloud NL API)."

        return jsonify({"message": response_message})

    return jsonify({"error": "Invalid request, 'query' field is missing"}), 400

@app.route("/users", methods=["GET"])
def get_users():
    db = SessionLocal()
    try:
        users = db.query(User).all()
        return jsonify([user.__dict__ for user in users])
    finally:
        db.close()

@app.route("/products", methods=["GET"])
def get_products():
    db = SessionLocal()
    try:
        products = db.query(Product).all()
        return jsonify([product.__dict__ for product in products])
    finally:
        db.close()

@app.route("/purchases", methods=["GET"])
def get_purchases():
    db = SessionLocal()
    try:
        purchases = db.query(Purchase).all()
        return jsonify([purchase.__dict__ for purchase in purchases])
    finally:
        db.close()

@app.route("/complaints", methods=["GET"])
def get_complaints():
    db = SessionLocal()
    try:
        complaints = db.query(Complaint).all()
        return jsonify([complaint.__dict__ for complaint in complaints])
    finally:
        db.close()
    








def main():
    app.run(port=int(os.environ.get('PORT', 80)))

if __name__ == "__main__":
    main()
