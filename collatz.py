"""Compute and print the Collatz sequence starting at 27."""


def collatz(start: int) -> list[int]:
    n = start
    sequence = [n]
    while n != 1:
        n = n // 2 if n % 2 == 0 else 3 * n + 1
        sequence.append(n)
    return sequence


def main() -> None:
    sequence = collatz(27)
    for value in sequence:
        print(value)
    step_count = len(sequence) - 1
    assert len(sequence) == step_count + 1
    print(f"Total steps: {step_count}")


if __name__ == "__main__":
    main()
