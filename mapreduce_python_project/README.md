# Mini MapReduce Engine – Word Count

**Student Name:** Youssef Ahmed Kamal  
**Student ID:** 231006924  
**Programming Language:** Python

## Project Description
This project implements a simple MapReduce-like engine in Python without using Hadoop or Spark. It counts word occurrences across multiple text files using parallel processing.

## Project Steps
1. **Input:** Read text files from the input folder.
2. **Map:** Convert each word into a `(word, 1)` pair.
3. **Parallel Processing:** Execute mappers concurrently using threads.
4. **Combine & Partition:** Count words locally and distribute them between two reducers.
5. **Shuffle, Sort & Reduce:** Group and count words, sort the results, and save the output.

## How to Run
1. Open the project folder in VS Code.
2. Make sure Python is installed.
3. Run:

```bash
python main.py
```

No additional libraries are required.

## Output Files
- `reducer1.txt` – Results from Reducer 1.
- `reducer2.txt` – Results from Reducer 2.
- `final.txt` – Final combined word counts.

## Example
**Input:** `python python is easy`

**Output:**
```text
easy: 1
is: 1
python: 2
```

**Submitted by:** Youssef Ahmed Kamal  
**ID:** 231006924 