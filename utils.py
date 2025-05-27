from datetime import datetime

def print_unique_domains(data):
    seen = set()
    for entry in data:
        cn = entry["common_name"]
        if cn not in seen:
            print(cn)
            seen.add(cn)

def print_full_details(data):
    for entry in data:
        cn = entry["common_name"]
        exp = entry["not_after"]
        print(f"{cn:40} expires at {exp}")