#time for the big boy part.

# https://spacy.io/usage/spacy-101
# use tokenization and text classification to parse text

import spacy
import task.task_class
import dateparser
from datetime import datetime, timedelta

# spacy test
# nlp = spacy.load("en_core_web_sm")
# doc = nlp("Apple is looking at buying U.K. startup for $1 billion")
# for token in doc:
#     print(token.text, token.pos_, token.dep_)

#CONFIG
HIGH_PRIORITY = [
    "exam",
    "test",
    "final",
    "deadline",
    "submit",
    "turn in",
    "presentation",
    "project",
    "application",
    "app",
    "interview",
    "assignment",
    "quiz",
    "report",
    "lab",
    "registration",
    "scholarship",
    "paper",
    "recommendation",
    "competition",
]

MEDIUM_PRIORITY = [
    "print",
    "email",
    "read",
    "draft",
    "meeting",
    "study",
    "revise",
    "edit",
    "club",
    "outline",
    "practice",
    "notes",
    "note",
    "feedback",
    "schedule",
    "organize",
    "brainstorm",
    "homework",
    "recording",
    "reading",
    "research",
    "vocabulary",
    "lecture"
]
LOW_PRIORITY = [
    "clean",
    "backpack",
    "locker",
    "decorate",
    "supplies",
    "pens",
    "flashcards",
    "organize",
    "folders",
    "binders",
    "scan",
    "back up",
    "reminder",
    "setup",
    "checklist",
    "prepare",
    "download",
    "calendar"
]

nlp  = spacy.load("en_core_web_sm")

def infer_priority(task_name):
    task_name_words = task_name.lower().split()
    if any(word in HIGH_PRIORITY for word in task_name_words):
        return "high"
    elif any(word in MEDIUM_PRIORITY for word in task_name_words):
        return "medium"
    elif any(word in LOW_PRIORITY for word in task_name_words):
        return "low"
    else:
        return None


def parse_text(text):
    doc = nlp(text)

    task_name = text
    task_deadline = None
    task_priority = ""

    for ent in doc.ents:
        if ent.label_ in ("DATE", "TIME"):
            task_deadline = ent.text
            task_name = text.replace(ent.text, "").strip()

        if task_deadline:
            if "tomorrow" in task_deadline.lower():
                deadline_date = (datetime.now() + timedelta(days=1)).strftime("%m/%d/%Y")

            elif "today" in task_deadline.lower():
                deadline_date = datetime.now().strftime("%m/%d/%Y")

            elif "monday" in task_deadline.lower() or "tuesday" in task_deadline.lower() or "wednesday" in task_deadline.lower() or "thursday" in task_deadline.lower() or "friday" in task_deadline.lower() or "saturday" in task_deadline.lower() or "sunday" in task_deadline.lower():
                deadline_date = dateparser.parse(task_deadline, settings={'PREFER_DATES_FROM': 'future'}).strftime("%m/%d/%Y")
            else:
                deadline_date = task_deadline
        else:
            deadline_date = None

        
    task_name = task_name.replace("by", "").strip()