from settings.config import settings

def log_calculation(expression, result):
    history_entry = f"{expression} = {result}"
    settings["history"].append(history_entry)

def show_history():
    for entry in settings["history"]:
        print(entry)
