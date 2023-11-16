from flask import Flask, jsonify
from flaskext.mysql import MySQL
import os

app = Flask(__name__)

# MySQL Configuration
app.config['MYSQL_DATABASE_USER'] = os.environ.get('MYSQL_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.environ.get('MYSQL_DATABASE')
app.config['MYSQL_DATABASE_HOST'] = 'db'
mysql = MySQL(app)

@app.route('/')
def get_data():
    try:
        cursor = mysql.get_db().cursor()
        cursor.execute("SELECT * FROM data")
        data = cursor.fetchall()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/health')
def health():
    return jsonify({'status': 'OK'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)