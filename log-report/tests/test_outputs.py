import json
from pathlib import Path

def test_report_exists():
    """The agent produced a report file."""
    assert Path("/app/report.json").exists(), "no report.json found"

def test_report_contents():
    """The report contains the correctly calculated metrics."""
    content = Path("/app/report.json").read_text()
    data = json.loads(content)
    
    assert "total_requests" in data, "Missing 'total_requests' key"
    assert data["total_requests"] == 6, f"Expected 6 total requests, got {data['total_requests']}"
    
    assert "unique_ips" in data, "Missing 'unique_ips' key"
    assert data["unique_ips"] == 3, f"Expected 3 unique IPs, got {data['unique_ips']}"
    
    assert "top_path" in data, "Missing 'top_path' key"
    assert data["top_path"] == "/index.html", f"Expected '/index.html' as top path, got {data['top_path']}"