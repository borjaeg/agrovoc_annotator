from flask import Flask, render_template
from flask import redirect, url_for
from flask import request, jsonify
from utils.annotation_utils import annotate_sentence
from utils.agrovoc_utils import load_agrovoc_prefLabels

agrovoc_pref_labels = load_agrovoc_prefLabels()

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("annotation.html")

@app.route("/annotate/<sentence>", methods=["GET"])
def annotate(sentence: str):
    print(sentence)
    annotated_sentence, found_concepts = annotate_sentence(sentence, agrovoc_pref_labels)
    return jsonify(
        found_concepts=found_concepts,
        annotation=annotated_sentence,
        status=200
    )


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5555, debug=True)