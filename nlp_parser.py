#time for the big boy part.

# https://spacy.io/usage/spacy-101
# use tokenization and text classification to parse text

import spacy
import task.task_class

# spacy test
# nlp = spacy.load("en_core_web_sm")
# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
# for token in doc:
#     print(token.text, token.pos_, token.dep_)

nlp  = spacy.load("en_core_web_sm")

def parse_text(text):
    doc = nlp(text)

    task_name = text
    task_deadline = None
    task_priority = ""

    for ent in doc.ents:
        if ent.label_ in ("DATE", "TIME"):
            task_deadline = ent.text
            task_name = text.replace(ent.text, "").strip()

    