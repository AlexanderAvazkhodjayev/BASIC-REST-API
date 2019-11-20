from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
app.secret_key = 'Kyle'
api = Api(app)

items = []


class Item(Resource):
	def get(self, name):
		item = next(filter(lambda x: x['name'] == name, items), None)
		return {'item': None}, 200 if item else 404

	def post(self, name):
		if next(filter(lambda x: x['name'] == name, items), None):
			return {'message' : 'An item with name'{}' already exists}'.format(name)}, 400
		data = request.get_json() 
		item = {'name': name, 'price': data['price']}
		items.append(item)
		return item, 201


class ItemList(Resource):
	def get(self):
		return{"items":items}


api.add_resource(Item, '/item/<string:name>') #http://127.0.0.1:5000/student/Rolf
api.add_resource(ItemList, '/items')

app.run(debug=True)