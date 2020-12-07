from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

items = []

class Item(Resource):
    def get(self, name):
        for item in items:
            if item["name"]==name:
                return item
        return {"item": None}, 404

    def post(self, name):
        #new_item = get
        item = {"name": name, "price": 12.00}
        items.append(item)
        return item

    def put(self, name):
        pass

    def delete(self, name):
        pass


api.add_resource(Item, '/item/<string:name>')


app.run()
