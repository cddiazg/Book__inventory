import json

FILE_PATH = "./data/books.json"

def load_data():
  try:
    with open(FILE_PATH, "r") as file:
      data = json.load(file)
    return data
  except Exception:
    return []