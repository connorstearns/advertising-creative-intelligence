PAGE_BG = "#080B18"
CARD_BG = "#111834"
CARD_BG_ALT = "#161F42"
BORDER = "#26305A"
PRIMARY_ACCENT = "#4C6FFF"
TEXT_PRIMARY = "#F3F5FF"
TEXT_SECONDARY = "#8D96BC"
POSITIVE = "#4ADE9A"
WARNING = "#FFB55C"
DANGER = "#FF6B81"
INFO = "#7C9BFF"
PURPLE = "#B79CFF"

APP_CSS = f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {{
  --page-bg: {PAGE_BG};
  --card-bg: {CARD_BG};
  --card-bg-alt: {CARD_BG_ALT};
  --border: {BORDER};
  --accent: {PRIMARY_ACCENT};
  --text-primary: {TEXT_PRIMARY};
  --text-secondary: {TEXT_SECONDARY};
}}

html, body, .stApp, [class*="css"] {{
  font-family: "Inter", -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}}

.stApp {{
  color: var(--text-primary);
  background-color: var(--page-bg);
  background-image:
    radial-gradient(1100px 620px at 12% -12%, rgba(76, 111, 255, 0.20), transparent 62%),
    radial-gradient(900px 520px at 104% 4%, rgba(124, 155, 255, 0.13), transparent 58%);
  background-repeat: no-repeat;
}}

.block-container {{
  max-width: 1500px;
  padding: 2.1rem 2.5rem 4.5rem;
}}

[data-testid="stHeader"] {{
  background: rgba(8, 11, 24, 0.92);
  border-bottom: 1px solid rgba(76, 111, 255, 0.20);
}}

[data-testid="stSidebar"] {{
  background: #0A0E1E;
  border-right: 1px solid #1D2545;
}}

[data-testid="stSidebar"] > div:first-child {{
  background-image: linear-gradient(180deg, rgba(76, 111, 255, 0.12), transparent 16rem);
}}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stCaption {{
  color: var(--text-secondary);
}}

.signal-accent {{
  color: var(--accent);
  font-weight: 700;
}}

[data-testid="stSidebar"] div[role="radiogroup"] label {{
  padding: 0.62rem 0.85rem;
  margin-bottom: 0.22rem;
  border: 1px solid transparent;
  border-radius: 999px;
  transition: background 120ms ease, border-color 120ms ease, color 120ms ease;
}}

[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
  border-color: #33407A;
  background: #131B38;
}}

[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {{
  border-color: var(--accent);
  background: var(--accent);
  color: #FFFFFF;
  box-shadow: 0 6px 18px rgba(76, 111, 255, 0.35);
}}

[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p {{
  color: #FFFFFF !important;
  font-weight: 650;
}}

[data-testid="stSelectbox"] > div > div {{
  border-color: #33407A;
  border-radius: 10px;
  background: #121A38;
  color: #F3F5FF;
}}

[data-baseweb="popover"] ul {{
  border: 1px solid #33407A;
  border-radius: 12px;
  background: #111834;
}}

[data-baseweb="popover"] li:hover {{
  background: rgba(76, 111, 255, 0.16);
}}

[data-testid="stMultiSelect"] [data-baseweb="tag"] {{
  background-color: rgba(76, 111, 255, 0.22) !important;
  border: 1px solid var(--accent) !important;
  border-radius: 999px !important;
}}

[data-testid="stMultiSelect"] [data-baseweb="tag"] span {{
  color: var(--text-primary) !important;
}}

h1, h2, h3 {{
  color: var(--text-primary);
  letter-spacing: -0.02em;
  font-weight: 700;
}}

p, li, label {{ color: var(--text-primary); }}
.stCaption, [data-testid="stCaptionContainer"] {{ color: var(--text-secondary) !important; }}
hr {{ border-color: #1E2748 !important; }}

.eyebrow,
.section-kicker {{
  color: var(--accent);
  font-size: 0.72rem;
  font-weight: 700;
  letter-spacing: 0.09em;
  text-transform: uppercase;
}}

.section-header {{
  position: relative;
  padding: 1.6rem 1.7rem 1.5rem;
  margin: 0.4rem 0 1.25rem;
  overflow: hidden;
  border: 1px solid #212A4E;
  border-radius: 22px;
  background: linear-gradient(150deg, #131C3E 0%, #0C1230 75%);
  box-shadow: 0 24px 60px rgba(4, 8, 24, 0.45);
}}

.section-header::after {{
  content: "";
  position: absolute;
  top: -45%;
  right: -8%;
  width: 300px;
  height: 300px;
  background: radial-gradient(circle, rgba(76, 111, 255, 0.30), transparent 70%);
  filter: blur(4px);
  pointer-events: none;
}}

.section-title {{
  position: relative;
  z-index: 1;
  margin: 0.35rem 0 0.3rem;
  color: var(--text-primary);
  font-size: clamp(1.85rem, 3.4vw, 2.85rem);
  font-weight: 800;
  letter-spacing: -0.03em;
  line-height: 1.06;
}}

.section-copy {{
  position: relative;
  z-index: 1;
  max-width: 850px;
  color: var(--text-secondary);
  font-size: 0.98rem;
  line-height: 1.55;
}}

.hero-flow {{
  position: relative;
  z-index: 1;
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.5rem;
  margin-top: 1.15rem;
}}

.flow-step {{
  padding: 0.5rem 0.9rem;
  border: 1px solid #33407A;
  border-radius: 999px;
  background: rgba(18, 26, 56, 0.75);
  color: #F3F5FF;
  font-size: 0.78rem;
  font-weight: 600;
}}

.flow-step:first-child {{
  border-color: var(--accent);
  background: var(--accent);
  color: #FFFFFF;
  box-shadow: 0 6px 18px rgba(76, 111, 255, 0.35);
}}

.flow-arrow {{
  color: var(--accent);
  font-size: 0.9rem;
  font-weight: 700;
}}

.insight-card,
.diagnostic-card,
.role-card-header,
.role-signal,
.role-diagnosis {{
  border-color: #212A4E;
  background: var(--card-bg);
}}

.insight-card {{
  padding: 1.05rem 1.2rem;
  margin: 0.55rem 0;
  border: 1px solid #212A4E;
  border-left: 4px solid var(--card-accent, var(--accent));
  border-radius: 14px;
  background: #111834;
}}

.card-label {{
  color: var(--accent);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.07em;
  text-transform: uppercase;
}}

.card-title {{
  margin-top: 0.3rem;
  color: #F3F5FF;
  font-size: 1rem;
  font-weight: 650;
}}

.card-body {{
  margin-top: 0.4rem;
  color: var(--text-secondary);
  font-size: 0.88rem;
  line-height: 1.5;
}}

.status-chip {{
  display: inline-flex;
  align-items: center;
  padding: 0.3rem 0.68rem;
  border: 1px solid var(--chip);
  border-radius: 999px;
  background: color-mix(in srgb, var(--chip) 16%, #0C1230);
  color: var(--chip);
  font-size: 0.68rem;
  font-weight: 700;
  letter-spacing: 0.03em;
  text-transform: uppercase;
}}

.role-card-header {{
  margin-top: 0.9rem;
  padding: 1.2rem 1.3rem 0.95rem;
  border: 1px solid #212A4E;
  border-bottom: 0;
  border-radius: 18px 18px 0 0;
  background: linear-gradient(135deg, #182252, #0E1430);
}}

.role-card-title-row {{
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
}}

.role-card-title {{
  color: #F3F5FF;
  font-size: 1.24rem;
  font-weight: 750;
  letter-spacing: -0.02em;
}}

.role-card-job {{
  margin-top: 0.28rem;
  color: var(--text-secondary);
  font-size: 0.84rem;
}}

.role-question {{
  margin-top: 0.85rem;
  padding-top: 0.75rem;
  border-top: 1px solid #212A4E;
  color: #F3F5FF;
  font-size: 0.86rem;
  font-weight: 600;
}}

.role-signal {{
  min-height: 156px;
  padding: 0.95rem 1rem 0.75rem;
  border: 1px solid #212A4E;
  border-radius: 16px;
  background: #111834;
}}

.signal-topline {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 0.5rem;
}}

.signal-label {{
  color: var(--text-secondary);
  font-size: 0.72rem;
  font-weight: 650;
  letter-spacing: 0.015em;
}}

.signal-change {{ font-size: 0.76rem; font-weight: 700; }}

.signal-period {{
  margin-top: 0.6rem;
  color: var(--accent);
  font-size: 0.63rem;
  font-weight: 700;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}}

.signal-value {{
  margin-top: 0.12rem;
  color: #F3F5FF;
  font-size: 1.65rem;
  font-weight: 800;
  letter-spacing: -0.02em;
}}

.signal-prior {{
  color: var(--text-secondary);
  font-size: 0.72rem;
}}

.signal-sparkline {{
  display: block;
  width: 100%;
  height: 32px;
  margin-top: 0.5rem;
  overflow: visible;
}}

.role-diagnosis {{
  display: grid;
  grid-template-columns: 1fr 1.35fr;
  gap: 1.1rem;
  padding: 1rem 1.1rem;
  margin-bottom: 0.85rem;
  border: 1px solid #212A4E;
  border-top: 0;
  border-left: 4px solid var(--card-accent);
  border-radius: 0 0 18px 18px;
  background: #161F42;
}}

.role-diagnosis-item {{
  display: flex;
  flex-direction: column;
  gap: 0.28rem;
}}

.role-diagnosis-copy {{
  color: #F3F5FF;
  font-size: 0.85rem;
  line-height: 1.48;
}}

.diagnostic-card {{
  height: 100%;
  padding: 1.2rem 1.25rem;
  margin: 0.48rem 0;
  border: 1px solid #212A4E;
  border-top: 3px solid var(--accent);
  border-radius: 18px;
  background: linear-gradient(180deg, #141C40 0%, #0F1530 100%);
  box-shadow: 0 16px 38px rgba(4, 8, 24, 0.35);
}}

.diagnostic-card-top {{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
}}

.diagnostic-title {{
  margin-top: 0.3rem;
  color: #F3F5FF;
  font-size: 1.12rem;
  font-weight: 750;
  letter-spacing: -0.02em;
}}

.diagnostic-grid {{
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.68rem;
  margin-top: 1rem;
}}

.diagnostic-field {{
  padding: 0.75rem 0.8rem;
  border: 1px solid #212A4E;
  border-radius: 12px;
  background: #0C1230;
}}

.diagnostic-label {{
  color: var(--accent);
  font-size: 0.63rem;
  font-weight: 700;
  letter-spacing: 0.04em;
  text-transform: uppercase;
}}

.diagnostic-value {{
  margin-top: 0.28rem;
  color: #F3F5FF;
  font-size: 0.84rem;
  font-weight: 550;
  line-height: 1.4;
}}

.diagnostic-action {{
  display: flex;
  gap: 0.75rem;
  align-items: baseline;
  margin-top: 0.9rem;
  padding-top: 0.85rem;
  border-top: 1px solid #212A4E;
  color: #F3F5FF;
  font-size: 0.84rem;
  line-height: 1.45;
}}

[data-testid="stDataFrame"] {{
  overflow: hidden;
  border: 1px solid #212A4E;
  border-radius: 14px;
  background: #111834;
}}

[data-testid="stAlert"] {{
  border: 1px solid #212A4E;
  border-radius: 14px;
  background: #111834;
}}

@media (max-width: 900px) {{
  .block-container {{ padding: 1.25rem 1rem 3rem; }}
  .role-diagnosis {{ grid-template-columns: 1fr; }}
  .diagnostic-grid {{ grid-template-columns: 1fr; }}
}}
</style>
"""
