INPUT_DATA_PATH = 'input_data/'
PREF_LABELS_FILE = 'prefLabels.txt'
ALT_LABELS_FILE = 'cleanAltLabels.txt'

def load_agrovoc_prefLabels():
    concepts = []
    with open(INPUT_DATA_PATH + PREF_LABELS_FILE, "r") as concepts_file:
        lines = concepts_file.readlines()
        concepts = [concept.strip() for concept in lines]
    return concepts


def load_agrovoc_altLabels():
    concepts = []
    with open(INPUT_DATA_PATH + ALT_LABELS_FILE, "r") as concepts_file:
        lines = concepts_file.readlines()
        concepts = [concept.strip() for concept in lines]
    return concepts