import os
import re
from collections import Counter
from concurrent.futures import ThreadPoolExecutor

# 1. Mapper
def mapper(filename):
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read().lower()

    words = re.findall(r"[a-z]+", text)
    return [(word, 1) for word in words]


# 2. Combiner
def combiner(mapped):
    return Counter(dict_word for dict_word, count in mapped for _ in range(count))


# 3. Partitioner (2 reducers)
def partitioner(word):
    return sum(ord(c) for c in word) % 2


# 4. Reducer
def reducer(data):
    return dict(sorted(Counter(data).items()))


# 5. Run MapReduce
files = [
    os.path.join("input", f)
    for f in os.listdir("input")
    if f.endswith(".txt")
]

partitions = [[], []]

with ThreadPoolExecutor(max_workers=2) as executor:
    mapped_files = list(executor.map(mapper, files))

for mapped in mapped_files:
    combined = combiner(mapped)

    for word, count in combined.items():
        partitions[partitioner(word)].extend([word] * count)

with ThreadPoolExecutor(max_workers=2) as executor:
    results = list(executor.map(reducer, partitions))

print("Reducer 1:", results[0])
print("Reducer 2:", results[1])

final_result = dict(sorted({**results[0], **results[1]}.items()))
print("Final Word Count:", final_result)


import os

# Create output folder
os.makedirs("output", exist_ok=True)

# Save Reducer 1
with open("output/reducer1.txt", "w") as f:
    for word, count in sorted(results[0].items()):
        f.write(f"{word}: {count}\n")

# Save Reducer 2
with open("output/reducer2.txt", "w") as f:
    for word, count in sorted(results[1].items()):
        f.write(f"{word}: {count}\n")

# Save Final Merged Result
with open("output/final.txt", "w") as f:
    for word, count in final_result.items():
        f.write(f"{word}: {count}\n")

print("Results saved in output folder!")