import pandas as pd

from datalens.report import build_report


def test_build_report():
    df = pd.DataFrame(
        {
            "category": ["A", "B", "A", "C"],
            "quantity": [10, 20, 30, 40],
            "revenue": [100.0, 200.0, 300.0, 400.0],
            "date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"],
        }
    )

    report = build_report(df)

    assert "# DataLens Report" in report
    assert "## Summary" in report


def test_build_report_contains_revenue_by_category():
    df = pd.DataFrame(
        {
            "category": ["A", "B", "A", "C"],
            "quantity": [10, 20, 30, 40],
            "revenue": [100.0, 200.0, 300.0, 400.0],
            "date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"],
        }
    )

    report = build_report(df)

    assert "## Revenue by Category" in report
    assert "A" in report
    assert "B" in report
    assert "C" in report


def test_build_report_contains_summary():
    df = pd.DataFrame(
        {
            "category": ["A", "B", "A", "C"],
            "quantity": [10, 20, 30, 40],
            "revenue": [100.0, 200.0, 300.0, 400.0],
            "date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04"],
        }
    )

    report = build_report(df)

    assert "row_count: 4" in report
    assert "total_revenue: 1000.0" in report
    assert "total_quantity: 100.0" in report
