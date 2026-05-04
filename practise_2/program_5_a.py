import json

with open("file1.json", "r") as f1:
    data1 = json.load(f1)

with open("file2.json", "r") as f2:
    data2 = json.load(f2)

merged = {**data1, **data2}

with open("merged.json", "w") as output:
    json.dump(merged, output)

print("Files merged")
