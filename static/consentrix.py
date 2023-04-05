from flask import FLASK,jsonify
import requests

app = FLASK(__name__)


@app.route('/main', methods = ['GET'])
def unathorized():
 try:
   return jsonify({'error': 'Not authorized'}), 401
 except Exception as e:
   return jsonify({'msg' : e}), 500
