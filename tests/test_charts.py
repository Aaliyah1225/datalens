import os

import pandas as pd
import pytest

from datalens.charts import plot_by_category


@pytest.fixture
def sample_df():
    return pd.DataFrame(
        {
            "category": ["coffee", "coffee", "tea"],
            "revenue": [10.0, 5.0, 8.0],
        }
    )


def test_plot_by_category_writes_png_file(tmp_path, sample_df):
    output_path = tmp_path / "chart.png"
    result_path = plot_by_category(sample_df, output_path=str(output_path), by="category")
    assert result_path == str(output_path)
    assert os.path.isfile(output_path)
    assert os.path.getsize(output_path) > 0


def test_plot_by_category_missing_column_raises(tmp_path, sample_df):
    with pytest.raises(KeyError):
        plot_by_category(sample_df, output_path=str(tmp_path / "chart.png"), by="nonexistent")
