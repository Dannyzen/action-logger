import json
import bottle
from bottle import route, run, request, abort, response
from pymongo import Connection
from time import time
 
connection = Connection('localhost', 27017)
db = connection.actions

@route('/action', method='POST')
def add_action():
    data = request.body.readline()
    print type(data)
    print data
    if not data:
        abort(400, 'You gave me nothing. You fail.')
    entity = json.loads(data)
    print type(entity)
    entity['time']= time()
    print entity['actionName']
    if not entity.has_key('actionName'):
        abort(400, 'I need an action')
    try:
        db["action"].update({ "action":entity['actionName'] },{ "$addToSet":{"time":time()} },upsert=True)
    except ValidationError as valerr:
        abort(400, str(valerr))

run(host='localhost', port=8080)
