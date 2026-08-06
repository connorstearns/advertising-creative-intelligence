from pathlib import Path

APP_TITLE = "Codecademy Creative Intelligence"
SAMPLE_DIR = Path(__file__).resolve().parents[1] / "data" / "codecademy_sample_exports"

TABS = [
    "report_role_signal_trends",
    "report_territory_analysis",
    "report_format_channel_fit",
    "report_fatigue_watchlist",
    "report_next_tests",
    "data_requirements",
    "qa_mapping_gaps",
]

ROLE_ORDER = [
    "Demand Creation",
    "Reinforcement",
    "Demand Capture",
    "Customer Growth",
]

ROLE_PERFORMANCE = {
    "Demand Creation": {
        "job": "Make Codecademy relevant when a professional first recognizes a skill gap.",
        "question": "Is the creative earning attention and making the need feel urgent and relevant?",
        "recommendation": "Refresh the hook, audience tension, or role-specific use case.",
    },
    "Reinforcement": {
        "job": "Build confidence through proof, comparison, and sequential messaging.",
        "question": "Is the creative making the promise more credible and reducing uncertainty?",
        "recommendation": "Strengthen the proof point, learner outcome, credential, or expert demonstration.",
    },
    "Demand Capture": {
        "job": "Meet active intent and route each learner to the right skill, format, and offer.",
        "question": "Is the experience converting expressed intent into the right next step?",
        "recommendation": "Improve query-to-offer alignment, pathway clarity, or destination relevance.",
    },
    "Customer Growth": {
        "job": "Turn an initial learning need into ongoing progression, retention, and customer value.",
        "question": "Is the system expanding engagement and guiding learners to the next capability?",
        "recommendation": "Improve next-skill recommendations, cross-sell sequencing, or re-engagement logic.",
    },
}

CREATIVE_TERRITORIES = {
    "The Job Changed. So Can You.": (
        "Turns professional disruption into capability by dramatizing how roles and expectations have changed."
    ),
    "Make Readiness Visible": (
        "Makes advancement tangible through projects, credentials, applied outcomes, and visible progress."
    ),
    "Stay Unfinished": (
        "Positions continuous learning as an identity and advantage, not a remedial obligation."
    ),
}

MOTIONS = ["Portfolio", "Pro", "Workshops", "Bootcamps", "All Access", "Teams"]

CHANNEL_GUIDANCE = {
    "Paid Social": "Audience-led need states, motion-first hooks, creator proof, and retargeting",
    "YouTube": "Role-change storytelling, expert demonstration, and applied education",
    "Paid Search": "High-intent skill, technology, product, and comparison demand",
    "Organic Search": "Skill-level discovery, comparison content, and answerable guidance",
    "AI Discovery": "Direct, quotable answers and recommendation visibility",
    "LinkedIn": "Teams buyer development, thought leadership, proof, and account activation",
    "CRM / Lifecycle": "Onboarding, progression, cross-sell, renewal, and win-back",
}
