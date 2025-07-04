import csv
import pytest
from pathlib import Path


@pytest.fixture
def path_csv_file():
    file_path = Path(__file__).parent.parent / "products.csv"
    if not file_path.exists():
        pytest.skip("Файл data.csv пока отсутствует — тест пропущен.")

    return file_path

@pytest.fixture
def new_test_data(tmp_path):
    csv_file = tmp_path / "test.csv"
    with open(csv_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["brand", "price", "rating"])
        writer.writeheader()
        writer.writerow({"brand": "apple", "price": "100", "rating": "4.5"})
        writer.writerow({"brand": "samsung", "price": "-100", "rating": "3.5"})
        writer.writerow({"brand": "samsung", "price": "-100", "rating": "-3.5"})
    return csv_file