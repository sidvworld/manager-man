#time for the big boy part.

# https://spacy.io/usage/spacy-101
# use tokenization and text classification to parse text

import spacy
import task.task_class


nlp = spacy.load("en_core_web_sm")
doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
for token in doc:
    print(token.text, token.pos_, token.dep_)
