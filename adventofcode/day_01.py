from typing import List


def all_elf_calorie_counts(file_contents: List[str]) -> List[int]:
    elf_calorie_counts: List[int] = []
    cur_elf_calories = 0
    for input in file_contents:
        try:
            cur_elf_calories += int(input)
        except ValueError:
            elf_calorie_counts.append(cur_elf_calories)
            cur_elf_calories = 0
    if cur_elf_calories > 0:
        elf_calorie_counts.append(cur_elf_calories)
    return elf_calorie_counts


def top_n_elf_calorie_count(file_contents: List[str], n: int = 1) -> int:
    """ """
    elf_calorie_counts = sorted(
        all_elf_calorie_counts(file_contents), reverse=True
    )
    n = min(len(elf_calorie_counts), n)
    return sum(elf_calorie_counts[0:n])


def greatest_elf_calorie_count(file_contents: List[str]) -> int:
    """ """
    return top_n_elf_calorie_count(file_contents)
