from flask import Flask, request, Response
from database import Database
import json

app = Flask(__name__)
database = Database()


@app.route('/api/v1/upload-person', methods=['GET'])
def upload_person():
    url = request.args.get('url')
    name = request.args.get('name')
    date = request.args.get('date')
    age = request.args.get('age')
    descr = request.args.get('descr')
    connection = request.args.get('connection')
    vk_id = request.args.get('vk_id')
    username = request.args.get('username')
    surname = request.args.get('surname')
    database.insert_values(url, name, date, age, descr, connection, vk_id, username, surname)
    return ''


@app.route('/api/v1/show-admins', methods=['GET'])
def show_admins():
    return Response(json.dumps(database.get_admins_list(), ensure_ascii=False),
                    mimetype='application/json; charset=utf-8')


@app.route('/api/v1/show-persons-by-vk-id', methods=['GET'])
def show_persons():
    vk_id = request.args.get('vk_id')
    return Response(json.dumps(database.get_people_by_vk_id(vk_id), ensure_ascii=False),
                    mimetype='application/json; charset=utf-8')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
