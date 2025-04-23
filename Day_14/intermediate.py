def sum_even(numbers: list[int]) -> int:
    return sum(num for num in numbers if num % 2 == 0)



def reverse_string(s: str) -> str:
    return s[::-1]



def fibonacci(n: int) -> list[int]:
    sequence =[0,1]
    while len(sequence) <n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]




def count_vowels(sentence: str) -> int:
    vowels = "aeiouAEIOU"
    return sum(1 for char in sentence if char in vowels)



def average_marks(marks: list[float]) -> float:
    return sum(marks) / len(marks) if marks else 0.0