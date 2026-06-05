from flask import Flask, render_template, request

app = Flask(__name__)

movies = {
    "action": [
        "John Wick",
        "Mad Max: Fury Road",
        "The Dark Knight",
        "Extraction",
        "Gladiator",
        "Mission Impossible",
        "Top Gun: Maverick"
    ],
    "comedy": [
        "The Mask",
        "Home Alone",
        "Mr. Bean's Holiday",
        "Central Intelligence",
        "The Hangover",
        "Jumanji",
        "Free Guy"
    ],
    "sci-fi": [
        "Interstellar",
        "Inception",
        "The Matrix",
        "Avatar",
        "Dune",
        "Blade Runner 2049",
        "Arrival"
    ],
    "horror": [
        "The Conjuring",
        "Insidious",
        "Annabelle",
        "The Nun",
        "A Quiet Place",
        "It",
        "Smile"
    ],
    "drama": [
        "Forrest Gump",
        "The Shawshank Redemption",
        "The Pursuit of Happyness",
        "Green Book",
        "Titanic",
        "The Pianist",
        "A Beautiful Mind",
        "The Social Network"
    ]
}

similarity_keywords = {
    "action": ["action", "fight", "war", "battle", "adventure", "hero"],
    "comedy": ["comedy", "comic", "funny", "humor", "laugh", "joke"],
    "sci-fi": ["sci-fi", "science", "future", "space", "technology", "robot"],
    "horror": ["horror", "scary", "ghost", "monster", "fear", "terror"],
    "drama": ["drama", "emotional", "life", "story", "inspiring", "realistic"]
}


def get_recommendations(user_input):
    user_input = user_input.lower().strip()

    for genre, keywords in similarity_keywords.items():
        if user_input in keywords:
            return genre, movies[genre], 100

    for genre, keywords in similarity_keywords.items():
        for keyword in keywords:
            if user_input in keyword or keyword in user_input:
                return genre, movies[genre], 80

    return None, [], 0


@app.route("/", methods=["GET", "POST"])
def home():

    recommendations = []
    genre = None
    score = 0
    message = None

    if request.method == "POST":

        interest = request.form["interest"]

        if interest.lower() == "exit":
            message = "Thank you for using the Movie Recommendation System."

        else:
            genre, recommendations, score = get_recommendations(interest)

            if genre is None:
                message = "No matching genre found. Try action, comedy, sci-fi, horror, or drama."

    return render_template(
        "index.html",
        recommendations=recommendations,
        genre=genre,
        score=score,
        message=message
    )


if __name__ == "__main__":
    app.run(debug=True)