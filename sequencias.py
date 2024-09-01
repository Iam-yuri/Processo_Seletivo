def next_element(sequence):
    if len(sequence) < 2:
        return None

    difference = sequence[1] - sequence[0]
    if all(sequence[i] + difference == sequence[i + 1] for i in range(len(sequence) - 1)):
        return sequence[-1] + difference

    if sequence[0] != 0 and all(
            sequence[i] * (sequence[1] // sequence[0]) == sequence[i + 1] for i in range(len(sequence) - 1)):
        ratio = sequence[1] // sequence[0]
        return sequence[-1] * ratio

    if all(sequence[i] == (int(i ** 0.5) + 1) ** 2 for i in range(len(sequence))):
        return (int(len(sequence) ** 0.5) + 2) ** 2

    if len(sequence) >= 3 and all(sequence[i] == sequence[i - 1] + sequence[i - 2] for i in range(2, len(sequence))):
        return sequence[-1] + sequence[-2]

    if len(sequence) > 2:
        return sequence[-1] + (sequence[-1] - sequence[-2])

    return None


# Testando as sequências
sequences = {
    'a': [1, 3, 5, 7],
    'b': [2, 4, 8, 16, 32, 64],
    'c': [0, 1, 4, 9, 16, 25, 36],
    'd': [4, 16, 36, 64],  #
    'e': [1, 1, 2, 3, 5, 8],
    'f': [2, 10, 12, 16, 17, 18, 19]
}

for key, seq in sequences.items():
    print(f"Próximo elemento da sequência {key}: {next_element(seq)}")
