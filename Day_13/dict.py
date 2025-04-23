# Group employees by department and sort by salary (descending)
data = [
    ('HR', 'Alice', 50000),
    ('HR', 'Bob', 60000),
    ('Tech', 'Charlie', 120000),
    ('Tech', 'Dave', 110000),
    ('Tech', 'Eve', 115000)
]

def group_by_department(data):
    from collections import defaultdict

    result = defaultdict(list)
    for dept, emp, salary in data:
        result[dept].append((emp, salary))

    for dept in result:
        result[dept].sort(key=lambda x: x[1], reverse=True)

    print(dict(result))

group_by_department(data)


# Create an inverted index from list of sentences
def invert_index(sentences):
    index = {}
    for i, sentence in enumerate(sentences):
        for word in sentence.split():
            index.setdefault(word, []).append(i)
    return index

sentences = ["the quick brown fox", "jumps over the lazy dog", "the dog barked"]
print(invert_index(sentences))


# Demonstrate shallow vs deep copy
import copy

original = {"marks": [45, 50, 60]}
shallow = original.copy()
deep = copy.deepcopy(original)

original["marks"].append(70)

print("Original:", original)
print("Shallow Copy:", shallow)
print("Deep Copy:", deep)


# Group words by their length
def word_length(words):
    length_dict = {}
    for word in words:
        length_dict.setdefault(len(word), []).append(word)
    print(length_dict)

words = ["hi", "hello", "hey", "bye", "thanks", "ok"]
word_length(words)


# Merge two dictionaries with max values for overlapping keys
def merge_dicts(d1, d2):
    for key, value in d2.items():
        d1[key] = max(d1.get(key, value), value)
    print(d1)

d1 = {'a': 5, 'b': 10}
d2 = {'b': 7, 'c': 3}
merge_dicts(d1, d2)
