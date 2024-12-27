import os
from firebase_admin import credentials, firestore, initialize_app, get_app, delete_app

def init_firebase():
    try:
        app = get_app()
    except ValueError:
        BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../"))
        cred_path = os.path.join(BASE_DIR, 'src', 'resource', 'landslide-firebase-service-account.json')
        cred = credentials.Certificate(cred_path)
        app = initialize_app(cred)
    return firestore.client()

def get_all_documents():
    db = init_firebase()
    docs = db.collection('points').stream()
    return {doc.id: doc.to_dict() for doc in docs}

def get_document_by_id(id):
    db = init_firebase()
    doc = db.collection('points').document(id).get()
    return doc.to_dict()

def close_connection():
    try:
        app = get_app()
        delete_app(app)
    except ValueError:
        print("Firebase app has not been initialized, skipping shutdown.")