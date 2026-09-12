import os
from datetime import datetime

def generate_log(data):
    if not isinstance(data, list):
        raise ValueError("data must be a list")

    today = datetime.now().strftime("%Y%m%d")
    filename = f"log_{today}.txt"

    with open(filename, 'w') as f:
        for entry in data:
            f.write(f"{entry}\n")

    print(f"Log generated: {filename}")
    return filename

if __name__ == "__main__":
    generate_log(["System start", "User login"])