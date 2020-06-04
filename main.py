from flask import Flask, jsonify, request

app = Flask(__name__)

movies = [
   {
       "name" : '3 idiots',
       "casts" : ["kareena kapoor","amir khan","boman irani","sharman joshi"],
       "genre" : ['comedy','drama']
   },
   {
       "name" : 'deewar',
       "casts" : ["amitabh baccha","sunil datt"],
       "genre" : ['family','drama']
   }
]

@app.route('/', methods=['GET'])
def get_movies():
    return jsonify(movies)

@app.route('/',methods=['POST'])
def post_movies():
    movie = request.get_json()
    movies.append(movie)
    return jsonify({"movie added ": "OK"})


if __name__ == '__main__':
    app.run(host='localhost', port=8088,debug=True)



