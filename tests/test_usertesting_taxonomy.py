import pandas as pd

from src.usertesting_config import (
    AUDIENCE_ORDER,
    MEDIA_ROLE_ORDER,
    SAMPLE_DIR,
    TOPIC_ORDER,
)


def test_creative_assets_cover_full_taxonomy():
    assets = pd.read_csv(SAMPLE_DIR / "report_creative_assets.csv")

    assert set(assets["audience"]) == set(AUDIENCE_ORDER)
    assert set(assets["topic"]) == set(TOPIC_ORDER)
    assert set(assets["media_role"]) == set(MEDIA_ROLE_ORDER)
    assert assets["asset_id"].is_unique
    assert assets[["diagnosis", "recommended_action", "health_status"]].notna().all().all()


def test_topic_audience_learning_has_full_matrix():
    matrix = pd.read_csv(SAMPLE_DIR / "report_topic_audience_learning.csv")

    assert set(matrix["topic"]) == set(TOPIC_ORDER)
    assert set(matrix["audience"]) == set(AUDIENCE_ORDER)
    assert len(matrix) == len(TOPIC_ORDER) * len(AUDIENCE_ORDER)


def test_format_environment_learning_has_current_prior_and_recommendation():
    fit = pd.read_csv(SAMPLE_DIR / "report_format_environment_learning.csv")

    assert fit[
        ["format", "environment", "evaluation_focus", "current_value", "prior_value", "recommended_action"]
    ].notna().all().all()
