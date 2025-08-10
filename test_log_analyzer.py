import pytest
from log_analyzer import analyze_logs


@pytest.mark.parametrize(
    "log_lines, expected_total, expected_status_counts, expected_ip",
    [
        # Brak logów
        ([], 0, {}, None),

        # Jeden log, jeden kod HTTP
        (
            ['192.168.0.1 - - [10/Aug/2025:10:00:00 +0000] "GET / HTTP/1.1" 200 1234'],
            1,
            {200: 1},
            "192.168.0.1"
        ),

        # Trzy logi z różnymi kodami
        (
            [
                '192.168.0.1 - - [10/Aug/2025:10:00:00 +0000] "GET / HTTP/1.1" 200 1234',
                '10.0.0.2 - - [10/Aug/2025:10:01:00 +0000] "POST /login HTTP/1.1" 404 321',
                '192.168.0.1 - - [10/Aug/2025:10:02:00 +0000] "GET /about HTTP/1.1" 500 222'
            ],
            3,
            {200: 1, 404: 1, 500: 1},
            "192.168.0.1"
        ),

        # Trzy logi, wszystkie 200 OK
        (
            [
                '192.168.0.1 - - [10/Aug/2025:10:00:00 +0000] "GET / HTTP/1.1" 200 1234',
                '192.168.0.1 - - [10/Aug/2025:10:01:00 +0000] "POST /form HTTP/1.1" 200 111',
                '192.168.0.1 - - [10/Aug/2025:10:02:00 +0000] "GET /about HTTP/1.1" 200 321'
            ],
            3,
            {200: 3},
            "192.168.0.1"
        ),
    ]
)
def test_analyze_logs(log_lines, expected_total, expected_status_counts, expected_ip):
    result = analyze_logs(log_lines)
    assert result["total_requests"] == expected_total
    assert result["status_counts"] == expected_status_counts
    assert result["most_common_ip"] == expected_ip
