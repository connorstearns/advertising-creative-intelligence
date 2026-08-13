import pandas as pd
import streamlit as st

from src.access_control import require_demo_access
from src.spotify_recommendations import signal_status
from src.usertesting_config import (
    APP_TITLE,
    AUDIENCE_ORDER,
    AUDIENCE_REGISTER,
    CAMPAIGN_PLATFORM,
    FIT_LABEL_TONE,
    FIT_LABEL_SUMMARY,
    HEALTH_STATUS_TONE,
    MEDIA_ROLE_ORDER,
    MEDIA_ROLES,
    SIGNAL_META,
    STRATEGIC_FLOW,
    TOPIC_ORDER,
    TOPICS,
)
from src.usertesting_data_loader import load_workbook
from src.usertesting_theme import APP_CSS
from src.usertesting_ui_components import (
    format_signal_value,
    render_diagnostic_card,
    render_fact_card,
    render_flow,
    render_insight_card,
    render_learning_summary,
    render_role_diagnosis,
    render_role_signal,
    render_section_header,
    render_status_chip,
    safe_table,
)

KPI_SIGNALS = [
    "engagement_rate",
    "landing_engagement_rate",
    "content_progression",
    "repeat_account_engagement",
]

st.set_page_config(page_title=APP_TITLE, page_icon=":material/insights:", layout="wide")
st.markdown(APP_CSS, unsafe_allow_html=True)

if not require_demo_access(st.secrets, st.session_state):
    st.stop()


@st.cache_data(ttl=600)
def get_data():
    return load_workbook()


def status_tone(status: str) -> str:
    return HEALTH_STATUS_TONE.get(status, "neutral")


def fit_tone(label: str) -> str:
    return FIT_LABEL_TONE.get(label, "neutral")


def ordered_options(frame: pd.DataFrame, column: str, canonical_order: list[str] | None = None) -> list[str]:
    if column not in frame.columns:
        return []
    values = sorted(v for v in frame[column].dropna().unique().tolist())
    if not canonical_order:
        return values
    ordered = [value for value in canonical_order if value in values]
    remainder = [value for value in values if value not in ordered]
    return ordered + remainder


def apply_filters(frame: pd.DataFrame, selections: dict[str, list[str]]) -> pd.DataFrame:
    filtered = frame.copy()
    for column, selected in selections.items():
        if selected and column in filtered.columns:
            filtered = filtered[filtered[column].isin(selected)]
    return filtered


workbook = get_data()
assets = workbook.get("report_creative_assets")
topic_audience = workbook.get("report_topic_audience_learning")
format_environment = workbook.get("report_format_environment_learning")

with st.sidebar:
    st.markdown(
        """
        <div class="eyebrow">Prepared for UserTesting — Parent Brand</div>
        <h2 style="margin:.35rem 0 0; color:#F4F7F8; line-height:1.02;">
            Creative Learning<br><span class="signal-accent">/system</span>
        </h2>
        <p style="color:#A7B1B8;font-size:.82rem;margin-top:.65rem">
            Real Human Intelligence campaign · Diagnostics + production planning
        </p>
        """,
        unsafe_allow_html=True,
    )
    page = st.radio(
        "Navigate",
        [
            "Creative Learning Overview",
            "Topic × Audience Learning",
            "Format / Environment Learning",
            "Creative Asset Detail",
        ],
        label_visibility="collapsed",
    )
    st.divider()
    st.markdown(render_status_chip("Illustrative demo", "neutral"), unsafe_allow_html=True)
    st.caption("Illustrative prototype — sample data shown for demonstration purposes.")
    st.caption("Instrument provides the Real Human Intelligence campaign platform, hero concept, and messaging registers. Current structures, produces, measures, and interprets the activation variants shown here.")

if page == "Creative Learning Overview":
    render_section_header(
        "Creative Learning System",
        "Is each campaign expression doing its job — and what should we make next? "
        f"Built on Instrument's {CAMPAIGN_PLATFORM} platform, this view turns structured media tests into "
        "creative learning and a next production decision.",
        "Real Human Intelligence · Media learning system",
    )
    render_flow(STRATEGIC_FLOW)

    if assets.empty:
        render_insight_card("Illustrative asset data is not available.", title="Data unavailable", tone="info")
    else:
        st.markdown("<div style='height:1.1rem'></div>", unsafe_allow_html=True)
        row1 = st.columns(3)
        row2 = st.columns(3)
        with row1[0]:
            audience_sel = st.multiselect("Audience", ordered_options(assets, "audience", AUDIENCE_ORDER))
        with row1[1]:
            topic_sel = st.multiselect("Topic", ordered_options(assets, "topic", TOPIC_ORDER))
        with row1[2]:
            role_sel = st.multiselect("Media role", ordered_options(assets, "media_role", MEDIA_ROLE_ORDER))
        with row2[0]:
            format_sel = st.multiselect("Format", ordered_options(assets, "format"))
        with row2[1]:
            environment_sel = st.multiselect("Environment", ordered_options(assets, "environment"))
        with row2[2]:
            variant_sel = st.multiselect("Variant", ordered_options(assets, "variant"))

        filtered = apply_filters(
            assets,
            {
                "audience": audience_sel,
                "topic": topic_sel,
                "media_role": role_sel,
                "format": format_sel,
                "environment": environment_sel,
                "variant": variant_sel,
            },
        )

        if filtered.empty:
            render_insight_card(
                "No illustrative assets match this filter combination. Broaden the filters to see learning signals.",
                title="No matching assets",
                tone="info",
            )
        else:
            top_row = filtered.loc[filtered["engagement_rate"].idxmax()]
            watchlist = filtered[filtered["health_status"].isin(["Watch", "Needs Action"])]
            action_row = watchlist.iloc[0] if not watchlist.empty else top_row
            render_learning_summary(
                str(top_row["diagnosis"]),
                str(action_row["recommended_action"]),
                status_tone(str(action_row["health_status"])),
            )
            st.caption(
                f"Based on {len(filtered)} matching illustrative assets, including “{top_row['asset_name']}”."
            )

            signal_columns = st.columns(4)
            for column, signal in zip(signal_columns, KPI_SIGNALS):
                meta = SIGNAL_META[signal]
                current = float(filtered[signal].mean())
                prior = float(filtered[f"{signal}_prior"].mean())
                with column:
                    render_role_signal(meta["label"], current, prior, meta["value_format"])

            render_diagnostic_card(
                "Portfolio signal summary",
                "Additional signals · current slice",
                [
                    ("Qualified reach", format_signal_value(filtered["qualified_reach"].mean(), "number")),
                    ("Avg. frequency", format_signal_value(filtered["frequency"].mean(), "decimal")),
                    ("Engaged landing visits", format_signal_value(filtered["engaged_landing_visits"].mean(), "number")),
                    ("Priority-account engagement", format_signal_value(filtered["priority_account_engagement"].mean(), "percent")),
                    ("High-intent page activity", format_signal_value(filtered["high_intent_page_activity"].mean(), "percent")),
                    ("Matching assets", str(len(filtered))),
                ],
                f"{len(filtered)} illustrative assets match the current filters across {filtered['media_role'].nunique()} media role(s).",
                "Portfolio slice",
                "neutral",
            )

            st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)
            safe_table(
                filtered.sort_values("engagement_rate", ascending=False),
                "report_creative_assets",
                columns=["asset_name", "audience", "topic", "media_role", "format", "environment", "variant", "health_status"],
            )

elif page == "Topic × Audience Learning":
    render_section_header(
        "Topic × Audience Learning",
        "Which propositions resonate with which audiences? Compare each illustrative topic across Builder and "
        "Creator messaging registers.",
        "Message-market fit",
    )
    if topic_audience.empty:
        render_insight_card("Topic × audience learning data is not available.", title="Data unavailable", tone="info")
    else:
        legend_columns = st.columns(2)
        for column, audience in zip(legend_columns, AUDIENCE_ORDER):
            with column:
                st.caption(f"**{audience}** — {AUDIENCE_REGISTER.get(audience, '')}")
        st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)
        for topic in TOPIC_ORDER:
            topic_rows = topic_audience[topic_audience["topic"] == topic]
            if topic_rows.empty:
                continue
            definition = TOPICS.get(topic, {})
            render_insight_card(definition.get("buyer_tension", ""), title=topic, tone="info")
            columns = st.columns(2)
            for column, audience in zip(columns, AUDIENCE_ORDER):
                row = topic_rows[topic_rows["audience"] == audience]
                if row.empty:
                    continue
                values = row.iloc[0]
                labels = [
                    str(values["attention_label"]),
                    str(values["engaged_visit_label"]),
                    str(values["content_progression_label"]),
                    str(values["account_quality_label"]),
                ]
                overall = max(set(labels), key=labels.count)
                with column:
                    render_diagnostic_card(
                        audience,
                        topic,
                        [
                            ("Attention", render_status_chip(values["attention_label"], fit_tone(values["attention_label"]))),
                            ("Engaged visit rate", render_status_chip(values["engaged_visit_label"], fit_tone(values["engaged_visit_label"]))),
                            ("Content progression", render_status_chip(values["content_progression_label"], fit_tone(values["content_progression_label"]))),
                            ("Account quality", render_status_chip(values["account_quality_label"], fit_tone(values["account_quality_label"]))),
                        ],
                        str(values["interpretation"]),
                        FIT_LABEL_SUMMARY.get(overall, overall),
                        fit_tone(overall),
                    )
            st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)

elif page == "Format / Environment Learning":
    render_section_header(
        "Format / Environment Learning",
        "Where does each idea work best? Different environments earn different jobs — technical media rewards "
        "depth, LinkedIn rewards identifiable accounts, and programmatic and search reward rising intent.",
        "Activation architecture",
    )
    if format_environment.empty:
        render_insight_card("Format and environment learning data is not available.", title="Data unavailable", tone="info")
    else:
        for start in range(0, len(format_environment), 2):
            columns = st.columns(2)
            for column, (_, row) in zip(columns, format_environment.iloc[start : start + 2].iterrows()):
                status, tone, change = signal_status(
                    float(row.get("current_value", 0)),
                    float(row.get("prior_value", 0)),
                    False,
                )
                value_format = str(row.get("value_format", "number"))
                with column:
                    render_diagnostic_card(
                        f"{row.get('format', 'Format')} · {row.get('environment', 'Environment')}",
                        str(row.get("evaluation_focus", "Evaluation focus")),
                        [
                            ("Evaluation focus", str(row.get("evaluation_focus", "Not available"))),
                            (
                                "Current / prior",
                                f"{format_signal_value(row.get('current_value', 0), value_format)} / "
                                f"{format_signal_value(row.get('prior_value', 0), value_format)}",
                            ),
                            ("Change", f"{change:+.1%} directional"),
                        ],
                        str(row.get("recommended_action", "Continue monitoring format and environment fit.")),
                        status,
                        tone,
                    )
        st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
        for row in format_environment.itertuples():
            render_insight_card(row.interpretation, title=f"{row.format} · {row.environment}", tone="neutral")

else:
    render_section_header(
        "Creative Asset Detail",
        "Inspect a single illustrative execution: its taxonomy, the job it is meant to perform, the question it "
        "is designed to answer, and what to make next.",
        "Asset-level diagnostics",
    )
    if assets.empty:
        render_insight_card("Illustrative asset data is not available.", title="Data unavailable", tone="info")
    else:
        asset_names = assets.sort_values("asset_name")["asset_name"].tolist()
        selected_name = st.selectbox("Select an illustrative asset", asset_names, label_visibility="collapsed")
        row = assets[assets["asset_name"] == selected_name].iloc[0]
        topic_definition = TOPICS.get(str(row["topic"]), {})
        role_definition = MEDIA_ROLES.get(str(row["media_role"]), {})

        render_fact_card(
            str(row["asset_name"]),
            "Asset taxonomy",
            [
                ("Campaign", str(row["campaign"])),
                ("Audience", str(row["audience"])),
                ("Audience segment", str(row["audience_segment"])),
                ("Topic", str(row["topic"])),
                ("Media role", str(row["media_role"])),
                ("Format", str(row["format"])),
                ("Environment", str(row["environment"])),
                ("Variant", str(row["variant"])),
                ("Asset ID", str(row["asset_id"])),
                ("Health", render_status_chip(str(row["health_status"]), status_tone(str(row["health_status"])))),
            ],
        )

        st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
        info_columns = st.columns(3)
        with info_columns[0]:
            render_insight_card(topic_definition.get("buyer_tension", "Not available"), title="Buyer tension", tone="info")
        with info_columns[1]:
            render_insight_card(role_definition.get("job", "Not available"), title="Job of the asset", tone="neutral")
        with info_columns[2]:
            render_insight_card(topic_definition.get("learning_question", "Not available"), title="Learning question", tone="info")

        st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)
        signal_columns = st.columns(4)
        for column, signal in zip(signal_columns, KPI_SIGNALS):
            meta = SIGNAL_META[signal]
            with column:
                render_role_signal(
                    meta["label"],
                    float(row[signal]),
                    float(row[f"{signal}_prior"]),
                    meta["value_format"],
                )

        render_diagnostic_card(
            "Additional signals",
            str(row["media_role"]),
            [
                ("Qualified reach", format_signal_value(row["qualified_reach"], "number")),
                ("Avg. frequency", format_signal_value(row["frequency"], "decimal")),
                ("Engaged landing visits", format_signal_value(row["engaged_landing_visits"], "number")),
                ("Priority-account engagement", format_signal_value(row["priority_account_engagement"], "percent")),
                ("High-intent page activity", format_signal_value(row["high_intent_page_activity"], "percent")),
                ("Variant", str(row["variant"])),
            ],
            "See diagnosis and recommended action below.",
            str(row["health_status"]),
            status_tone(str(row["health_status"])),
        )

        st.markdown("<div style='height:0.4rem'></div>", unsafe_allow_html=True)
        render_role_diagnosis(str(row["diagnosis"]), str(row["recommended_action"]), status_tone(str(row["health_status"])))

for warning in workbook.warnings:
    st.sidebar.caption(warning)
