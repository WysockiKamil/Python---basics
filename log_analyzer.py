def analyze_logs(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    total_logs = len(lines)
    level_counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
    message_counts = {}

    for line in lines:
        if "[INFO]" in line:
            level_counts["INFO"] += 1
        elif "[WARNING]" in line:
            level_counts["WARNING"] += 1
        elif "[ERROR]" in line:
            level_counts["ERROR"] += 1

        # Wyciągamy komunikat po ] (ostatni fragment linii)
        message = line.split("]")[-1].strip()
        message_counts[message] = message_counts.get(message, 0) + 1

    return {
        "total_logs": total_logs,
        "level_counts": level_counts,
        "message_counts": dict(sorted(message_counts.items(), key=lambda x: x[1], reverse=True))
    }


def main():
    file_path = input("Podaj ścieżkę do pliku logów: ")
    result = analyze_logs(file_path)

    print(f"\nLiczba wpisów: {result['total_logs']}")
    print("\nPoziomy logów:")
    for level, count in result['level_counts'].items():
        print(f"{level}: {count}")

    print("\nNajczęstsze komunikaty:")
    for message, count in result['message_counts'].items():
        print(f"{message}: {count}")


if __name__ == "__main__":
    main()