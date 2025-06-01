#time for the big boy part.

# https://spacy.io/usage/spacy-101
# use tokenization and text classification to parse text

import spacy
import en_core_web_sm
from task.task_class import task
import dateparser
import re
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

nlp = en_core_web_sm.load()

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

def get_next_weekday(target_day_name: str, base_date=None):
    if base_date is None:
        base_date = datetime.now()
    
    target_day_name = target_day_name.strip().lower()
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]

    if target_day_name not in weekdays:
        return None

    today_idx = base_date.weekday()
    target_idx = weekdays.index(target_day_name)

    delta_days = (target_idx - today_idx + 7) % 7
    delta_days = delta_days or 7

    result_date = base_date + timedelta(days=delta_days)
    return result_date.strftime("%m/%d/%Y")

def parse_date(date_str):
    weekdays = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
    date_str_clean = date_str.strip().lower()

    if date_str_clean in weekdays:
        return get_next_weekday(date_str_clean)

    parsed = dateparser.parse(
        date_str,
        settings={
            'PREFER_DATES_FROM': 'future',
            'RELATIVE_BASE': datetime.now()
        }
    )

    if parsed:
        return parsed.strftime("%m/%d/%Y")
    return None


def parse_text(text):
    doc = nlp(text)

    task_name = text
    task_deadline = None

    for ent in doc.ents:
        if ent.label_ in ("DATE", "TIME"):
            task_deadline = ent.text
            pattern = r"\b(?:by|on|at|in|next|the following)\s+" + re.escape(ent.text)
            task_name = re.sub(pattern, "", task_name, flags=re.IGNORECASE)
            task_name = task_name.replace(ent.text, "").strip()

    if task_deadline:
        deadline_date = parse_date(task_deadline)
    else:
        deadline_date = None

    task_priority = infer_priority(task_name)

    return task(task_name.strip(), deadline_date, task_priority)
    



#example usage
#text = "submit the final project by tuesday"
#parsed_task = parse_text(text)
#print(f"task details -> task name: {parsed_task.task_name}, deadline: {parsed_task.task_deadline}, priority: {parsed_task.task_priority}, created at: {parsed_task.created_at}")

# example usage 2
# inputs = [
#     "email the teacher about the exam",
#     "submit the application by june 6th",
#     "turn in the assignment by next week",
# ]

# for i, input_text in enumerate(inputs):
#     parsed_task = parse_text(input_text)
#     print(f"{i+1} task details -> task name: {parsed_task.task_name}, deadline: {parsed_task.task_deadline}, priority: {parsed_task.task_priority}, created at: {parsed_task.created_at}")