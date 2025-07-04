import sys
import subprocess
from pathlib import Path
from types import SimpleNamespace

from main import read_file


def test_check_format_file(path_csv_file):
    assert path_csv_file.suffix.lower() == ".csv"


def test_check_data(tmp_path, new_test_data):
    csv_file = new_test_data

    args = SimpleNamespace(file=str(csv_file))

    result = read_file(args)

    assert len(result) == 3
    assert result[0]["brand"] == "apple"
    assert result[0]["price"] == "100"
    assert result[1]["price"] == "-100"
    assert result[2]["rating"] == "-3.5"


def test_program_run(tmp_path, new_test_data):
    csv_file = new_test_data

    result = subprocess.run(
        [sys.executable, "main.py", "--file", str(csv_file)],
        capture_output = True,
        text = True,
        cwd = Path(__file__).parent.parent
    )


    assert result.returncode == 0




