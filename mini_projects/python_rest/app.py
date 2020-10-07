from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
#from json import dumps
import json
#import requests
from flask import jsonify

db_connect = create_engine('sqlite:///chinook.db')
app = Flask(__name__)
api = Api(app)

class Emp(Resource):
    def get(self):
        conn = db_connect.connect() # connecting to the db
        query = conn.execute("select * from employees") # selecting all employees
        employees = query.cursor.fetchall() # fetching the results
        IDs = [e[0] for e in employees] #creating a list of employees' IDs
        json_ids = [{'employees' : IDs}]
         
        #json_ids = json.dumps(json_ids, sort_keys=True, indent=4)
        
        return jsonify(json_ids)

class Track(Resource):
    def get(self):
        conn = db_connect.connect()
        query = conn.execute("select trackid, name, composer, unitprice from tracks LIMIT 20;")
        dict_list = []
        for q in query:
            #print (tuple((q.keys()),q)))
            pair = dict(zip(q.keys(),q))
            #print (pair)
            dict_list.append(pair)
        result = [{'data': dict_list}]
        result = jsonify(result)
        #result = json.dumps(result, sort_keys=True, indent=4)
        return result
    

api.add_resource(Emp, '/employees') # Route_1
api.add_resource(Track, '/tracks') # Route_2


if __name__ == '__main__':
     app.run(port='5002')
    
    #return (result)
        
        
    #query_keys=
    #tracks = query.cursor.fetchall()
    #for t in tracks:
     #   print (t)
    #result = [dict(zip(tuple (query.keys()), t)) for t in tracks]
    #print (result)
    #result = {'data': [dict(zip(tuple (query.keys()) ,i)) for i in query.cursor]}
    #return jsonify(result)
 

