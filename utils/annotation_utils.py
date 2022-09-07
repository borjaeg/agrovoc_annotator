from typing import List

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
#from nltk.tokenize import RegexpTokenizer

def annotate_sentence(sentence: str, ontology_subset: List[str]) -> List[str]:
    """
    Given a sentence, this function returns the IOB annotation format of it.
    """
    lemmatizer = WordNetLemmatizer()
    #tokenizer = RegexpTokenizer(r"\w+")

    found_concepts = []
    annotated_sentence = ["O"] * len(sentence.split(" "))
    previous_token = "O"
    # ontology_subset = sorted(ontology_subset, key=len, reverse=True)

    # annotations = download_annotations(sentence)
    for concept in ontology_subset:
        if len(concept) >= 3 and concept not in stopwords.words(
            "english"
        ):
            if concept.isupper():  # acronym
                occurrences = [
                    i for i in range(len(sentence)) if sentence.startswith(concept, i)
                ]
            else:
                occurrences = [
                    i
                    for i in range(len(sentence))
                    if sentence.lower().startswith(concept.lower(), i)
                ]
            for annotate_from in occurrences:
                found_concepts.append(concept)
                annotate_to = annotate_from + len(concept)
                annotation = {
                    lemmatizer.lemmatize(token): ix
                    for ix, token in enumerate(
                        sentence[annotate_from:annotate_to].split(" ")
                    )
                }
                if len(annotation) == 1:
                    #for ix, token in enumerate(tokenizer.tokenize(sentence)):
                    for ix, token in enumerate(sentence.split(" ")):
                        lemma_token = lemmatizer.lemmatize(token)
                        if annotation.get(lemma_token) is None:
                            previous_token = "O"
                        else:
                            if (
                                annotation[lemma_token] == 0
                                and annotated_sentence[ix] == "O"
                            ):
                                annotated_sentence[ix] = "B-Agr"
                                previous_token = "B-Agr"
                            elif (
                                annotation[lemma_token] > 0
                                and previous_token == "B-Agr"
                                and annotated_sentence[ix] == "O"
                            ):
                                annotated_sentence[ix] = "I-Agr"
                                previous_token = "I-Agr"
                elif len(annotation) >= 2:
                    for ix in range(len(sentence.split(" ")) - len(annotation)):
                        lemma_tokens = []
                        for ix_token in range(0, len(annotation)):
                            lemma_tokens.append(lemmatizer.lemmatize(sentence.split(" ")[ix_token + ix]))
                        for ix_annotation, annotation_part in enumerate(list(annotation.keys())):
                            if ix_annotation == 0 and lemma_tokens[ix_annotation] == annotation_part:
                                annotated_sentence[ix] = "B-Agr"
                            elif ix_annotation != 0 and lemma_tokens[ix_annotation] == annotation_part:
                                annotated_sentence[ix+ix_annotation] = "I-Agr"

                            #previous_token = "O"

    return annotated_sentence, list(set(found_concepts))