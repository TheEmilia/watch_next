import spacy

nlp = spacy.load("en_core_web_md")

with open("movies.txt", "r") as f:
    movie_descriptions = f.readlines()


def next_movie(description):
    most_similar = None
    description = nlp(description)
    for line in movie_descriptions:
        token = nlp(line)
        if most_similar is None or description.similarity(
            token
        ) > description.similarity(most_similar):
            most_similar = token

    return most_similar[:2]


# create a function to return which movies a user would watch next if they have watched Planet Hulk
planet_hulk_desc = "Planet Hulk: Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator."

print(next_movie(planet_hulk_desc))
