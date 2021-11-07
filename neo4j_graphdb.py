from flask import Flask, request, jsonify
from flask_cors import CORS
from neo4j import GraphDatabase

app = Flask(__name__)
CORS(app)

neo4j_session = GraphDatabase.driver("neo4j://localhost:7687", auth=("test", "password"))

@app.route("/add-movie", methods=["POST"])
def add_movie():
    data = request.get_json()
    if data['movie_type'] == "hollywood":
        db = neo4j_session.session(database="hollywood")
    else:
        db = neo4j_session.session(database="bollywood")
    properties = "{movie_title: '" + data['movie_title'] + "', release_year: " + str(data['release_year']) + "}"
    query = "CREATE (:{movie_genre} {properties})"
    query = query.format(movie_genre=data['movie_genre'], properties=properties)
    db.run(query)
    return jsonify({'status': 'Success'}), 200


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')



# from flask import Flask, request, jsonify
# from flask_cors import CORS

# app = Flask(__name__)
# CORS(app)

# # add neo4j connection

# @app.route("/netflix-movie", methods=["POST"])
# def add_movie():
#     data = request.get_json()

#     # add movie details in Neo4j database
    
#     return jsonify({'status': 'Success'}), 200


# if __name__ == "__main__":
#     app.run(host='0.0.0.0', port='8080')