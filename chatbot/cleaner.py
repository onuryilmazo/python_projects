# cleaner.py

import re

def remove_chat_metadata(chat_export_file):
    pattern = r"\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}\s-\s[\w\s]+:\s+"  # e.g. "08.07.2023 22:17 - Callisnado: "
    with open(chat_export_file, "r") as corpus_file:
        content = corpus_file.read()
    cleaned_corpus = re.sub(pattern, "", content)
    return tuple(cleaned_corpus.split("\n"))

def remove_non_message_text(export_text_lines):
    messages = export_text_lines[1:-1]

    filter_out_msgs = ("<Media omitted>",)
    return tuple((msg for msg in messages if msg not in filter_out_msgs))
def clean_corpus(chat_export_file):
    message_corpus = remove_chat_metadata(chat_export_file)
    cleaned_corpus = remove_non_message_text(message_corpus)
    return cleaned_corpus
