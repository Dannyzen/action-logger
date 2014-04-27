import json
import bottle
from bottle import route, run, request, abort, response
from pymongo import Connection
 
connection = Connection('localhost', 27017)
db = connection.actions

@route('/action', method='POST')
def add_action():
    data = request.body.readline()
    if not data:
        abort(400, 'You gave me nothing. You fail.')
    entity = json.loads(data)
    print entity
    if not entity.has_key('actionName'):
        abort(400, 'I need an action')
    if not entity.has_key('time'):
        abort(400, 'I need a time')
    try:
        db['action'].save(entity)
    except ValidationError as valerr:
        abort(400, str(valerr))

run(host='localhost', port=8080)
