"""Markdown report-building helpers for DataLens."""

from __future__ import annotations

import pandas as pd

from datalens.analysis import group_by_summary, summarize


def _dataframe_to_markdown(df: pd.DataFrame) -> str:
    """Convert a DataFrame into a simple Markdown table."""
    headers = list(df.columns)

    lines = [
        "| " + " | ".join(headers) + " |",
        "| " + " | ".join("---" for _ in headers) + " |",
    ]

    for _, row in df.iterrows():
        values = [str(value) for value in row]
        lines.append("| " + " | ".join(values) + " |")

    return "\n".join(lines)


def build_report(df: pd.DataFrame) -> str:
    """Build a Markdown report from a DataFrame."""
    summary = summarize(df)
    breakdown = group_by_summary(df, by="category")

    return (
        "# DataLens Report\n\n"
        "## Summary\n\n"
        f"{_summary_to_markdown(summary)}\n\n"
        "## Revenue by Category\n\n"
        f"{_dataframe_to_markdown(breakdown.reset_index())}\n"
    )


def _summary_to_markdown(summary: dict) -> str:
    lines = []

    for key, value in summary.items():
        lines.append(f"{key}: {value}")

    return "\n".join(lines)
