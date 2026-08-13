import pandas as pd
import streamlit as st

from src.usertesting_theme import (
    DANGER,
    INFO,
    POSITIVE,
    PRIMARY_ACCENT,
    PURPLE,
    TEXT_SECONDARY,
    WARNING,
)


def render_section_header(title: str, copy: str, kicker: str = "Creative diagnostics") -> None:
    st.markdown(
        f"""
        <div class="section-header">
          <div class="section-kicker">{kicker}</div>
          <div class="section-title">{title}</div>
          <div class="section-copy">{copy}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_flow(steps: list[str]) -> None:
    step_html = '<span class="flow-arrow">&rarr;</span>'.join(
        f'<span class="flow-step">{step}</span>' for step in steps
    )
    st.markdown(f'<div class="hero-flow">{step_html}</div>', unsafe_allow_html=True)


def render_insight_card(
    body: str,
    title: str = "Portfolio signal",
    tone: str = "warning",
) -> None:
    accent = {
        "positive": POSITIVE,
        "warning": WARNING,
        "danger": DANGER,
        "info": INFO,
        "neutral": PRIMARY_ACCENT,
    }.get(tone, PRIMARY_ACCENT)
    st.markdown(
        f"""
        <div class="insight-card" style="--card-accent:{accent}">
          <div class="card-label">Insight</div>
          <div class="card-title">{title}</div>
          <div class="card-body">{body}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_status_chip(label: str, tone: str = "neutral") -> str:
    color = {
        "positive": POSITIVE,
        "warning": WARNING,
        "danger": DANGER,
        "info": INFO,
        "neutral": PRIMARY_ACCENT,
        "purple": PURPLE,
    }.get(tone, PRIMARY_ACCENT)
    return f'<span class="status-chip" style="--chip:{color}">{label}</span>'


def format_signal_value(value: float, value_format: str) -> str:
    if pd.isna(value):
        return "-"
    if value_format == "percent":
        return f"{value:.1%}"
    if value_format == "currency":
        return f"${value:,.0f}"
    if value_format == "decimal":
        return f"{value:.1f}"
    return f"{value:,.0f}"


def render_role_signal(
    label: str,
    current: float,
    prior: float,
    value_format: str,
    lower_is_better: bool = False,
    trend_values: str = "",
) -> None:
    if isinstance(lower_is_better, str):
        lower_is_better = lower_is_better.strip().lower() in {"true", "1", "yes"}
    raw_change = (current - prior) / abs(prior) if prior else 0.0
    directional_change = -raw_change if lower_is_better else raw_change
    tone = "positive" if directional_change > 0.02 else "danger" if directional_change < -0.02 else "neutral"
    arrow = "↑" if directional_change > 0.02 else "↓" if directional_change < -0.02 else "→"
    color = POSITIVE if tone == "positive" else DANGER if tone == "danger" else PRIMARY_ACCENT

    values = []
    for item in str(trend_values).split("|"):
        try:
            values.append(float(item))
        except ValueError:
            continue

    if len(values) >= 2:
        minimum, maximum = min(values), max(values)
        spread = maximum - minimum or 1
        points = " ".join(
            f"{index * (100 / (len(values) - 1)):.1f},{30 - ((value - minimum) / spread * 24):.1f}"
            for index, value in enumerate(values)
        )
        sparkline = (
            f'<svg class="signal-sparkline" viewBox="0 0 100 32" preserveAspectRatio="none">'
            f'<polyline points="{points}" fill="none" stroke="{color}" stroke-width="2.5" '
            f'stroke-linecap="round" stroke-linejoin="round"/></svg>'
        )
    else:
        sparkline = ""

    st.markdown(
        f"""
        <div class="role-signal">
          <div class="signal-topline">
            <span class="signal-label">{label}</span>
            <span class="signal-change" style="color:{color}">{arrow} {abs(raw_change):.1%} vs prior</span>
          </div>
          <div class="signal-period">Current period</div>
          <div class="signal-value">{format_signal_value(current, value_format)}</div>
          <div class="signal-prior">Prior period {format_signal_value(prior, value_format)}</div>
          {sparkline}
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_role_header(
    role: str,
    job: str,
    question: str,
    status: str,
    tone: str,
) -> None:
    st.markdown(
        f"""
        <div class="role-card-header">
          <div class="role-card-title-row">
            <div>
              <div class="role-card-title">{role}</div>
              <div class="role-card-job">{job}</div>
            </div>
            <div>{render_status_chip(status, tone)}</div>
          </div>
          <div class="role-question">{question}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_role_diagnosis(diagnosis: str, recommendation: str, tone: str) -> None:
    accent = {
        "positive": POSITIVE,
        "warning": WARNING,
        "danger": DANGER,
        "neutral": PRIMARY_ACCENT,
    }.get(tone, PRIMARY_ACCENT)
    st.markdown(
        f"""
        <div class="role-diagnosis" style="--card-accent:{accent}">
          <div class="role-diagnosis-item">
            <span class="card-label">Diagnosis</span>
            <span class="role-diagnosis-copy">{diagnosis}</span>
          </div>
          <div class="role-diagnosis-item">
            <span class="card-label">Recommended action</span>
            <span class="role-diagnosis-copy">{recommendation}</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_learning_summary(what_we_learned: str, next_decision: str, tone: str) -> None:
    accent = {
        "positive": POSITIVE,
        "warning": WARNING,
        "danger": DANGER,
        "neutral": PRIMARY_ACCENT,
    }.get(tone, PRIMARY_ACCENT)
    st.markdown(
        f"""
        <div class="role-diagnosis" style="--card-accent:{accent}">
          <div class="role-diagnosis-item">
            <span class="card-label">What we're learning</span>
            <span class="role-diagnosis-copy">{what_we_learned}</span>
          </div>
          <div class="role-diagnosis-item">
            <span class="card-label">Next creative decision</span>
            <span class="role-diagnosis-copy">{next_decision}</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_diagnostic_card(
    title: str,
    eyebrow: str,
    fields: list[tuple[str, str]],
    recommendation: str,
    status: str = "Stable",
    tone: str = "neutral",
) -> None:
    field_html = "".join(
        f"""
        <div class="diagnostic-field">
          <div class="diagnostic-label">{label}</div>
          <div class="diagnostic-value">{value}</div>
        </div>
        """
        for label, value in fields
    )
    st.markdown(
        f"""
        <div class="diagnostic-card">
          <div class="diagnostic-card-top">
            <div>
              <div class="card-label">{eyebrow}</div>
              <div class="diagnostic-title">{title}</div>
            </div>
            <div>{render_status_chip(status, tone)}</div>
          </div>
          <div class="diagnostic-grid">{field_html}</div>
          <div class="diagnostic-action">
            <span class="card-label">Next move</span>
            <span>{recommendation}</span>
          </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_fact_card(title: str, eyebrow: str, fields: list[tuple[str, str]]) -> None:
    field_html = "".join(
        f"""
        <div class="diagnostic-field">
          <div class="diagnostic-label">{label}</div>
          <div class="diagnostic-value">{value}</div>
        </div>
        """
        for label, value in fields
    )
    st.markdown(
        f"""
        <div class="diagnostic-card">
          <div class="diagnostic-card-top">
            <div>
              <div class="card-label">{eyebrow}</div>
              <div class="diagnostic-title">{title}</div>
            </div>
          </div>
          <div class="diagnostic-grid">{field_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def safe_table(frame: pd.DataFrame, tab_name: str, columns: list[str] | None = None) -> None:
    if frame.empty:
        render_insight_card(
            f"No demo rows are currently available for {tab_name.replace('_', ' ')}.",
            title="Data not available",
            tone="info",
        )
        return

    selected = [column for column in (columns or list(frame.columns)) if column in frame.columns]
    column_labels = {
        "asset_id": "Asset ID",
        "asset_name": "Asset Name",
        "campaign": "Campaign",
        "audience": "Audience",
        "audience_segment": "Audience Segment",
        "topic": "Topic",
        "media_role": "Media Role",
        "format": "Format",
        "environment": "Environment",
        "variant": "Variant",
        "health_status": "Health",
        "recommended_action": "Recommended Action",
    }
    column_config = {
        column: st.column_config.Column(column_labels[column])
        for column in selected
        if column in column_labels
    }
    st.dataframe(
        frame[selected],
        width="stretch",
        hide_index=True,
        column_config=column_config,
    )
