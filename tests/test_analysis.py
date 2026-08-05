import pandas as pd
import pytest

from datalens.analysis import group_by_summary, rolling_average, summarize


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "date": [
                "2026-01-01",
                "2026-01-02",
                "2026-01-03",
                "2026-01-04",
            ],
            "category": ["coffee", "coffee", "tea", "tea"],
            "quantity": [2, 3, 1, 4],
            "revenue": [10.0, 15.0, 5.0, 30.0],
        }
    )


def test_summarize_basic_fields(sample_df):
    summary = summarize(sample_df)
    assert summary["row_count"] == 4
    assert summary["total_revenue"] == pytest.approx(60.0)
    assert summary["mean_revenue"] == pytest.approx(15.0)
    assert summary["total_quantity"] == pytest.approx(10.0)
    assert summary["category_count"] == 2
    assert summary["date_min"] == "2026-01-01"
    assert summary["date_max"] == "2026-01-04"


def test_summarize_handles_missing_optional_columns():
    df = pd.DataFrame({"id": [1, 2, 3]})
    summary = summarize(df)
    assert summary["row_count"] == 3
    assert "total_revenue" not in summary
    assert "category_count" not in summary


def test_group_by_summary_aggregates_and_sorts_descending(sample_df):
    result = group_by_summary(sample_df, by="category", value_column="revenue")
    assert list(result.index) == ["tea", "coffee"]
    assert result.loc["tea", "total_revenue"] == pytest.approx(35.0)
    assert result.loc["coffee", "total_revenue"] == pytest.approx(25.0)
    assert result.loc["coffee", "count"] == 2


def test_group_by_summary_missing_column_raises(sample_df):
    with pytest.raises(KeyError):
        group_by_summary(sample_df, by="nonexistent_column")


def test_rolling_average_smooths_daily_totals(sample_df):
    result = rolling_average(sample_df, column="revenue", window=2, date_column="date")
    assert list(result.index.date.astype(str)) == [
        "2026-01-01",
        "2026-01-02",
        "2026-01-03",
        "2026-01-04",
    ]
    # First value has no prior day, so rolling avg == the value itself.
    assert result["revenue_rolling_avg"].iloc[0] == pytest.approx(10.0)
    # Second value averages days 1 and 2.
    assert result["revenue_rolling_avg"].iloc[1] == pytest.approx(12.5)


def test_rolling_average_invalid_window_raises(sample_df):
    with pytest.raises(ValueError):
        rolling_average(sample_df, window=0)


def test_rolling_average_missing_column_raises(sample_df):
    with pytest.raises(KeyError):
        rolling_average(sample_df, column="not_a_column")
