logs = [
    "INFO",
    "DEBUG",
    "WARNING",
    "ERROR",
    "INFO",
    "CRITICAL",
    "WARNING"
]

for log in logs:

    if log == "CRITICAL":
        break

    if log == "INFO":
        continue

    if log == "WARNING" or log == "ERROR":
        print(log)