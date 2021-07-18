# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import flask
from flask import request,jsonify
import GetRecipe

app = flask.Flask(__name__)
app.config["DEBUG"] = False

@app.route('/api/v1/getrecipe',methods=["GET"])
def getRecipeEndpoint():
    alreadyReq = False
    if 'url' in request.args:
        alreadyReq = True
        return jsonify(GetRecipe.GetRecipeByUrl(request.args['url']))
    if 'name' in request.args and not alreadyReq:
        return jsonify(GetRecipe.GetRecipeByName(request.args['name']))


if __name__ == '__main__':
    app.run()

