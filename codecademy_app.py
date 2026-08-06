import pandas as pd
import streamlit as st

from src.access_control import require_demo_access
from src.codecademy_config import APP_TITLE, CREATIVE_TERRITORIES, MOTIONS, ROLE_ORDER, ROLE_PERFORMANCE
from src.codecademy_data_loader import load_workbook
from src.spotify_recommendations import role_health, signal_status
from src.theme import APP_CSS
from src.ui_components import (
    format_signal_value,
    render_diagnostic_card,
    render_insight_card,
    render_role_diagnosis,
    render_role_header,
    render_role_signal,
    render_section_header,
    render_status_chip,
    safe_table,
)

st.set_page_config(page_title=APP_TITLE, page_icon=":material/analytics:", layout="wide")
st.markdown(APP_CSS, unsafe_allow_html=True)

if not require_demo_access(st.secrets, st.session_state):
    st.stop()


@st.cache_data(ttl=600)
def get_data():
    return load_workbook()


def status_tone(status: str) -> str:
    return {
        "Improving": "positive",
        "Stable": "neutral",
        "Watch": "warning",
        "Needs Action": "danger",
    }.get(status, "neutral")


def filter_motion(frame: pd.DataFrame, motion: str) -> pd.DataFrame:
    if frame.empty or motion == "Portfolio" or "growth_motion" not in frame.columns:
        return frame.copy()
    return frame[frame["growth_motion"] == motion].copy()


workbook = get_data()
with st.sidebar:
    st.markdown(
        """
        <div class="eyebrow">Pitch prototype</div>
        <h2 style="margin-top:.35rem; color:#F4F7F5;">Codecademy Creative Intelligence</h2>
        <p style="color:#9EFF8A;font-size:.82rem;margin-top:-.4rem">
            Creative diagnostics + production planning
        </p>
        """,
        unsafe_allow_html=True,
    )
    motion = st.selectbox("Growth motion", MOTIONS, index=0)
    page = st.radio(
        "Navigate",
        [
            "Activation Role Performance",
            "Creative Territories",
            "Audience + Product + Channel Fit",
            "Fatigue + Refresh Needs",
            "What To Make Next",
            "Data Requirements / QA",
        ],
        label_visibility="collapsed",
    )
    st.divider()
    st.markdown(render_status_chip("Illustrative demo", "positive"), unsafe_allow_html=True)
    st.caption("Sample data only · Not client performance")
    st.caption("Directional framework · Pitch-safe")

if page == "Activation Role Performance":
    render_section_header(
        "Activation Role Performance",
        "Is each activation role doing its job? Current-period signals are compared with the prior period to diagnose health and direct the next production action.",
        "Role-specific learning system",
    )
    st.markdown(
        """
        <div class="hero-flow" style="margin:0 0 1rem">
          <span class="flow-step">Demand Creation</span><span class="flow-arrow">→</span>
          <span class="flow-step">Reinforcement</span><span class="flow-arrow">→</span>
          <span class="flow-step">Demand Capture</span><span class="flow-arrow">→</span>
          <span class="flow-step">Customer Growth</span>
        </div>
        """,
        unsafe_allow_html=True,
    )
    performance = filter_motion(workbook.get("report_role_signal_trends"), motion)
    if performance.empty:
        render_insight_card("Role-specific trend data is not available.", title="Performance data unavailable", tone="info")
    else:
        for role in ROLE_ORDER:
            definition = ROLE_PERFORMANCE[role]
            role_frame = performance[performance["role"] == role]
            health = role_health(role_frame)
            render_role_header(role, definition["job"], definition["question"], str(health["status"]), str(health["tone"]))
            columns = st.columns(3, gap="small")
            for column, (_, signal) in zip(columns, role_frame.head(3).iterrows()):
                with column:
                    render_role_signal(
                        str(signal.get("signal_label", signal.get("signal", "Signal"))),
                        float(signal.get("current_value", 0)),
                        float(signal.get("prior_value", 0)),
                        str(signal.get("value_format", "number")),
                        signal.get("lower_is_better", False),
                        str(signal.get("trend_values", "")),
                    )
            diagnosis = (
                "Signals are strengthening and this role is doing its job."
                if health["status"] == "Improving"
                else "Signals are holding within a narrow range."
                if health["status"] == "Stable"
                else "At least one primary signal is weakening and needs a focused creative response."
            )
            render_role_diagnosis(diagnosis, definition["recommendation"], str(health["tone"]))

elif page == "Creative Territories":
    render_section_header(
        "Creative Territory Performance",
        "Compare the three audience-led territories by activation role, signal trend, and next production move.",
        "Territory diagnostics",
    )
    territory_report = filter_motion(workbook.get("report_territory_analysis"), motion)
    columns = st.columns(3)
    for column, (territory, description) in zip(columns, CREATIVE_TERRITORIES.items()):
        row = territory_report[territory_report.get("creative_territory", pd.Series(dtype=str)) == territory]
        values = row.iloc[0].to_dict() if not row.empty else {}
        status = str(values.get("health_status", "Stable"))
        with column:
            render_diagnostic_card(
                territory,
                description,
                [
                    ("Audience", str(values.get("audience_segment", "Not available"))),
                    ("Product motion", str(values.get("growth_motion", motion))),
                    ("Strongest role", str(values.get("strongest_role", "Not available"))),
                    ("Watch role", str(values.get("weakest_role", "Not available"))),
                    ("Improving signal", str(values.get("improving_signal", "Not available"))),
                    ("Watch signal", str(values.get("watch_signal", "Not available"))),
                ],
                str(values.get("next_recommended_move", "Continue testing measured variants.")),
                status,
                status_tone(status),
            )

elif page == "Audience + Product + Channel Fit":
    render_section_header(
        "Audience + Product + Channel Fit",
        "Tie each creative execution to a learner need, product motion, activation role, channel, and role-relevant primary signal.",
        "Activation architecture",
    )
    fit = filter_motion(workbook.get("report_format_channel_fit"), motion)
    if fit.empty:
        render_insight_card("Format and channel fit data is not available.", title="Fit data unavailable", tone="info")
    else:
        for start in range(0, len(fit), 2):
            columns = st.columns(2)
            for column, (_, row) in zip(columns, fit.iloc[start : start + 2].iterrows()):
                status, tone, change = signal_status(
                    float(row.get("current_value", 0)),
                    float(row.get("prior_value", 0)),
                    bool(row.get("lower_is_better", False)),
                )
                value_format = str(row.get("value_format", "number"))
                with column:
                    render_diagnostic_card(
                        str(row.get("format", "Format")),
                        str(row.get("creative_territory", "Selected territory")),
                        [
                            ("Audience", str(row.get("audience_segment", "Not available"))),
                            ("Product motion", str(row.get("growth_motion", "Not available"))),
                            ("Activation role", str(row.get("creative_role", "Not available"))),
                            ("Channel", str(row.get("channel", "Not available"))),
                            ("Entry action", str(row.get("entry_action", "Not available"))),
                            ("Primary signal", str(row.get("primary_signal", "Not available"))),
                            (
                                "Current / prior",
                                f"{format_signal_value(row.get('current_value', 0), value_format)} / "
                                f"{format_signal_value(row.get('prior_value', 0), value_format)}",
                            ),
                            ("Change", f"{change:+.1%} directional"),
                        ],
                        str(row.get("recommendation", "Continue monitoring role and channel fit.")),
                        status,
                        tone,
                    )

elif page == "Fatigue + Refresh Needs":
    render_section_header(
        "Fatigue + Refresh Needs",
        "Which territory-role combinations are weakening, and what type of creative response is required?",
        "Creative health",
    )
    fatigue = filter_motion(workbook.get("report_fatigue_watchlist"), motion)
    if fatigue.empty:
        render_insight_card("No fatigue watchlist rows are available.", title="No current watchlist", tone="info")
    else:
        for start in range(0, len(fatigue), 2):
            columns = st.columns(2)
            for column, (_, row) in zip(columns, fatigue.iloc[start : start + 2].iterrows()):
                status, tone, change = signal_status(
                    float(row.get("current_value", 0)),
                    float(row.get("prior_value", 0)),
                    bool(row.get("lower_is_better", False)),
                )
                value_format = str(row.get("value_format", "number"))
                with column:
                    render_diagnostic_card(
                        str(row.get("asset_name", row.get("asset_id", "Asset"))),
                        f"{row.get('creative_territory', '')} · {row.get('creative_role', '')}",
                        [
                            ("Audience / motion", f"{row.get('audience_segment', '')} · {row.get('growth_motion', '')}"),
                            ("Format / channel", f"{row.get('format', '')} · {row.get('channel', '')}"),
                            ("Declining signal", str(row.get("signal_declining", "Not available"))),
                            (
                                "Current / prior",
                                f"{format_signal_value(row.get('current_value', 0), value_format)} / "
                                f"{format_signal_value(row.get('prior_value', 0), value_format)}",
                            ),
                            ("Change / frequency", f"{change:+.1%} · {row.get('frequency', '-')}x"),
                            ("Refresh type", str(row.get("recommended_refresh_type", "Refresh"))),
                        ],
                        str(row.get("recommended_action", "Refresh the weakening creative signal.")),
                        status,
                        tone,
                    )

elif page == "What To Make Next":
    render_section_header(
        "What To Make Next",
        "Turn role-specific signals into a prioritized creative production queue: scale, version, refresh, reframe, replace, or retire.",
        "Production planning",
    )
    recommendations = filter_motion(workbook.get("report_next_tests"), motion)
    if recommendations.empty:
        render_insight_card("No production recommendations are available.", title="No next tests", tone="info")
    else:
        for start in range(0, len(recommendations), 2):
            columns = st.columns(2)
            for column, (_, row) in zip(columns, recommendations.iloc[start : start + 2].iterrows()):
                with column:
                    render_diagnostic_card(
                        str(row.get("recommendation", "Recommended test")),
                        str(row.get("creative_territory", "Selected territory")),
                        [
                            ("Audience", str(row.get("audience_segment", "Not available"))),
                            ("Product motion", str(row.get("growth_motion", "Not available"))),
                            ("Activation role", str(row.get("creative_role", "Not available"))),
                            ("Signal to improve", str(row.get("signal_to_improve", "Not available"))),
                            ("Production action", str(row.get("production_action", "Not available"))),
                            ("Owner", str(row.get("owner", "Not assigned"))),
                        ],
                        str(row.get("rationale", "Not available")),
                        str(row.get("status", "Planned")),
                        "positive" if str(row.get("status", "")).lower() == "in production" else "info",
                    )

else:
    render_section_header(
        "Data Requirements / QA",
        "A reliable creative intelligence layer depends on approved source access, complete taxonomy, and consistent asset naming.",
        "Data foundation",
    )
    safe_table(workbook.get("data_requirements"), "data_requirements")
    gaps = workbook.get("qa_mapping_gaps")
    if gaps.empty:
        render_insight_card("No mapping gaps are present in the current demo data.", title="Mapping complete", tone="positive")
    else:
        render_insight_card(
            f"{len(gaps)} mapping gap(s) need attention before the next readout.",
            title="Taxonomy cleanup required",
            tone="danger",
        )
        safe_table(gaps, "qa_mapping_gaps")
    render_insight_card(
        "A live deployment would require clean asset IDs, product and audience mappings, paid-media delivery, lifecycle signals, and downstream subscription or CRM outcomes.",
        title="Operating requirement",
        tone="info",
    )

for warning in workbook.warnings:
    st.sidebar.caption(warning)
