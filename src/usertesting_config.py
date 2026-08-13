from pathlib import Path

APP_TITLE = "UserTesting — Creative Learning System"
CLIENT_DISPLAY_NAME = "UserTesting — Parent Brand"
CAMPAIGN_PLATFORM = "Real Human Intelligence"
SAMPLE_DIR = Path(__file__).resolve().parents[1] / "data" / "usertesting_sample_exports"

TABS = [
    "report_creative_assets",
    "report_topic_audience_learning",
    "report_format_environment_learning",
]

STRATEGIC_FLOW = [
    "Campaign Platform",
    "Structured Media Tests",
    "Signals",
    "Creative Learning",
    "Next Production Decision",
]

AUDIENCE_ORDER = ["Builders", "Creators"]

AUDIENCE_REGISTER = {
    "Builders": (
        "AI Labs, model/evaluation teams, post-training teams, alignment teams, AI engineers, and other "
        "technical AI teams. Messaging register: infrastructure, reliability, signals, evaluation, "
        "integration, technical credibility."
    ),
    "Creators": (
        "Innovation teams, creative teams, brand teams, and product/experience teams. Messaging register: "
        "human reaction, creative confidence, real-time feedback, relevance, and understanding what will "
        "resonate."
    ),
}

TOPIC_ORDER = [
    "Verified Human Network",
    "API / MCP Integrations",
    "Real-Time Human Input",
]

TOPICS = {
    "Verified Human Network": {
        "buyer_tension": "AI teams need human feedback they can trust, but quality is hard to verify at scale.",
        "learning_question": "Is verified human quality differentiated enough to provide a strong reason to believe?",
    },
    "API / MCP Integrations": {
        "buyer_tension": "Human evaluation can be difficult to integrate into fast-moving AI workflows.",
        "learning_question": "Does infrastructure and integration framing increase relevance with technical buyers?",
    },
    "Real-Time Human Input": {
        "buyer_tension": "AI-assisted creation still needs real-world human reaction to understand what will actually resonate.",
        "learning_question": "Does immediate human feedback create a differentiated role for the platform in creative workflows?",
    },
}

MEDIA_ROLE_ORDER = [
    "Category Creation",
    "Contextual Authority",
    "Event Amplification",
    "Engagement & Learning",
    "Emerging Intent Capture",
]

MEDIA_ROLES = {
    "Category Creation": {
        "job": "Introduce Real Human Intelligence and establish relevance before buyers know to actively look for it.",
        "question": "Is the creative earning attention and making the underlying tension feel real and urgent?",
        "recommendation": "Refresh the hook or buyer tension before adding more reach behind the same opening.",
    },
    "Contextual Authority": {
        "job": "Build credibility inside the technical publications, communities, and conversations already shaping AI training and evaluation.",
        "question": "Is the creative making the platform's role more credible inside spaces buyers already trust?",
        "recommendation": "Deepen the proof or technical detail rather than broadening reach.",
    },
    "Event Amplification": {
        "job": "Build familiarity before, during, and after high-value industry moments.",
        "question": "Is the creative building durable familiarity around the event window?",
        "recommendation": "Pair event reach with a retargeting sequence rather than repeating the same static.",
    },
    "Engagement & Learning": {
        "job": "Turn initial attention into deeper engagement and behavioral signals.",
        "question": "Is the creative converting attention into meaningful content progression?",
        "recommendation": "Increase proof density or narrative depth in the next variation.",
    },
    "Emerging Intent Capture": {
        "job": "Intercept category and solution intent as awareness turns into active exploration.",
        "question": "Is the experience converting rising intent into the right next step?",
        "recommendation": "Sharpen landing-page relevance and add comparison or verification content.",
    },
}

SIGNAL_META = {
    "engagement_rate": {"label": "Engagement rate", "value_format": "percent"},
    "landing_engagement_rate": {"label": "Landing engagement rate", "value_format": "percent"},
    "content_progression": {"label": "Content progression", "value_format": "percent"},
    "repeat_account_engagement": {"label": "Repeat account engagement", "value_format": "percent"},
    "qualified_reach": {"label": "Qualified reach", "value_format": "number"},
    "frequency": {"label": "Avg. frequency", "value_format": "decimal"},
    "engaged_landing_visits": {"label": "Engaged landing visits", "value_format": "number"},
    "priority_account_engagement": {"label": "Priority-account engagement", "value_format": "percent"},
    "high_intent_page_activity": {"label": "High-intent page activity", "value_format": "percent"},
}

HEALTH_STATUS_TONE = {
    "Improving": "positive",
    "Stable": "neutral",
    "Watch": "warning",
    "Needs Action": "danger",
}

FIT_LABEL_TONE = {
    "Strong": "positive",
    "Moderate": "neutral",
    "Weaker": "warning",
}

FIT_LABEL_SUMMARY = {
    "Strong": "Strong fit",
    "Moderate": "Moderate fit",
    "Weaker": "Limited fit",
}
