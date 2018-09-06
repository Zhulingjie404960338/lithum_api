from flask import Flask
from flask.views import MethodView
from flask import request
from flask import jsonify
import json

app = Flask(__name__)
#app.config['SERVER_NAME'] = 'jiankong:5000'

def test(func):
    def inn(*args,**kwargs):
        if not request.args.get('name'):
            return "name is not get"
        ret = func(*args,**kwargs)
        return ret
    return inn

def test2(func):
    @test
    def inn2(*args,**kwargs):
        if request.args.get('name') == 'aaa':
            return "name is aaa"
        ret = func(*args,**kwargs)
        return ret
    return inn2

class HelloView(MethodView):
    @test2
    def get(self):
        name = request.args.get('name')
        return "hello get: " + str(name)

    def post(self):
        #import pdb;pdb.set_trace()
        data = json.loads(request.get_data())
        name = data.get("name")
        color = data.get("color")
        return jsonify({"Code": 200,
                        "Message": "",
                        "name": name,
                        "color": color})

    @classmethod
    def run(cls):
        return "classmethod run"
        #used: HelloView.run() is liked a = HelloView();a.run()

    @property
    def create(self):
        return "property create"
        #used: a=HelloViewer();a.create will be "property create"

    
        
        

app.add_url_rule('/', view_func=HelloView.as_view('tag'))





if __name__ == '__main__':
    app.run(debug=True)
