def read_log_file(filepath):
    """Wczytuje plik logu i zwraca listę jego linii."""
    with open(filepath, "r", encoding="utf-8") as f:
        return f.readlines()



def analyze_logs(log_lines):
    total_requests = len(log_lines)
    ip_counts = {}
    status_counts = {}

    for line in log_lines:
        parts = line.split()
        if len(parts) < 9:
            continue

        ip = parts[0]
        try:
            status = int(parts[8])
        except ValueError:
            continue  # pomiń linie z błędnym kodem

        ip_counts[ip] = ip_counts.get(ip, 0) + 1
        status_counts[status] = status_counts.get(status, 0) + 1

    most_common_ip = max(ip_counts, key=ip_counts.get) if ip_counts else None
    most_common_status = max(status_counts, key=status_counts.get) if status_counts else None

    return {
        "total_requests": total_requests,
        "most_common_ip": most_common_ip,
        "most_common_status": most_common_status,
        "ip_counts": ip_counts,
        "status_counts": status_counts
    }

def main():
    filepath = input("Podaj ścieżkę do pliku logów: ")
    try:
        log_lines = read_log_file(filepath)
        results = analyze_logs(log_lines)

        print("\n=== Wyniki analizy logów ===")
        print(f"Całkowita liczba żądań: {results['total_requests']}")
        print(f"Najczęstszy adres IP: {results['most_common_ip']}")
        print(f"Najczęstszy kod statusu: {results['most_common_status']}")
    except FileNotFoundError:
        print("Błąd: nie znaleziono pliku.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")


if __name__ == "__main__":
    main()