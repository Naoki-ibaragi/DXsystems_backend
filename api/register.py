import os
from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
from pathlib import Path


#Firebase Admin SDKの初期化
script_dir = os.path.dirname(os.path.abspath(__file__))
key_path = os.path.join(script_dir,"key.json")
print(key_path)
cred = credentials.Certificate(key_path)
firebase_admin.initialize_app(cred)
db = firestore.client()

def save_inquiry(request):
    try:
        # リクエストからデータを取得
        data = request.json
        company = data.get('company')
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        inquiry = data.get('inquiry')

        # Firestoreにデータを保存
        db.collection('inquiries').add({
            'company': company,
            'name': name,
            'email': email,
            'phone': phone,
            'inquiry': inquiry,
            'timestamp': firestore.SERVER_TIMESTAMP
        })

        return jsonify({'success': 0}), 200
    except Exception as e:
        return jsonify({'success': 1}), 500