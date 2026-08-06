PAGE_BG = "#050505"
CARD_BG = "#111111"
CARD_BG_ALT = "#1A1A1A"
BORDER = "#3A3A3A"
PRIMARY_YELLOW = "#FFD300"
TEXT_PRIMARY = "#FFFFFF"
TEXT_SECONDARY = "#B8B8B8"
POSITIVE = "#7BE495"
WARNING = "#FFB84D"
DANGER = "#FF6B6B"
INFO = "#8EA1FF"
PURPLE = "#C8A1FF"

APP_CSS = f"""
<style>
:root {{
  --page-bg: {PAGE_BG};
  --card-bg: {CARD_BG};
  --card-bg-alt: {CARD_BG_ALT};
  --border: {BORDER};
  --yellow: {PRIMARY_YELLOW};
  --text-primary: {TEXT_PRIMARY};
  --text-secondary: {TEXT_SECONDARY};
}}

.stApp {{
  color: var(--text-primary);
  background-color: var(--page-bg);
  background-image:
    radial-gradient(circle at 1px 1px, rgba(255, 255, 255, 0.075) 1px, transparent 1.15px),
    linear-gradient(180deg, rgba(255, 211, 0, 0.035), transparent 22rem);
  background-size: 17px 17px, 100% 100%;
}}

.block-container {{
  max-width: 1500px;
  padding: 2.1rem 2.5rem 4.5rem;
}}

[data-testid="stHeader"] {{
  background: rgba(5, 5, 5, 0.90);
  border-bottom: 1px solid rgba(255, 211, 0, 0.18);
}}

[data-testid="stSidebar"] {{
  background: #080808;
  border-right: 1px solid #2A2A2A;
}}

[data-testid="stSidebar"] > div:first-child {{
  background-image: linear-gradient(180deg, rgba(255, 211, 0, 0.08), transparent 16rem);
}}

[data-testid="stSidebar"] [data-testid="stMarkdownContainer"] p,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] .stCaption {{
  color: var(--text-secondary);
}}

.brand-wordmark {{
  display: inline-flex;
  align-items: center;
  margin-bottom: 1rem;
  color: #FFFFFF;
  font-size: 1.15rem;
  font-weight: 750;
  letter-spacing: -0.04em;
}}

.brand-box {{
  display: inline-flex;
  align-items: center;
  height: 1.5rem;
  padding: 0 0.18rem;
  margin-right: 0.05rem;
  border: 1px solid #FFFFFF;
  line-height: 1;
}}

.terminal-accent {{
  color: var(--yellow);
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-weight: 650;
}}

[data-testid="stSidebar"] div[role="radiogroup"] label {{
  padding: 0.62rem 0.7rem;
  margin-bottom: 0.18rem;
  border: 1px solid transparent;
  border-radius: 2px;
  transition: background 120ms ease, border-color 120ms ease, color 120ms ease;
}}

[data-testid="stSidebar"] div[role="radiogroup"] label:hover {{
  border-color: #4A4A4A;
  background: #151515;
}}

[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) {{
  border-color: var(--yellow);
  background: var(--yellow);
  color: #050505;
}}

[data-testid="stSidebar"] div[role="radiogroup"] label:has(input:checked) p {{
  color: #050505 !important;
  font-weight: 700;
}}

/* Keep the growth-motion selector visually distinct from the dark navigation. */
[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div {{
  min-height: 2.55rem;
  border: 1px solid #9A988F !important;
  border-radius: 2px !important;
  background: #F4F1E8 !important;
  box-shadow: none !important;
}}

[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] > div:focus-within {{
  border-color: var(--yellow) !important;
  box-shadow: 0 0 0 1px var(--yellow) !important;
}}

[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] span,
[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] input {{
  color: #050505 !important;
  -webkit-text-fill-color: #050505 !important;
  font-weight: 650;
  opacity: 1 !important;
}}

[data-testid="stSidebar"] [data-testid="stSelectbox"] div[data-baseweb="select"] svg {{
  color: #050505 !important;
  fill: #050505 !important;
}}

[data-baseweb="popover"] ul,
[data-baseweb="popover"] [role="listbox"] {{
  border: 1px solid #9A988F;
  border-radius: 2px;
  background: #F4F1E8;
}}

[data-baseweb="popover"] li,
[data-baseweb="popover"] [role="option"] {{
  background: #F4F1E8;
  color: #050505 !important;
}}

[data-baseweb="popover"] li:hover,
[data-baseweb="popover"] [role="option"]:hover,
[data-baseweb="popover"] [role="option"][aria-selected="true"] {{
  background: var(--yellow) !important;
  color: #050505 !important;
}}

h1, h2, h3 {{
  color: var(--text-primary);
  letter-spacing: -0.04em;
}}

p, li, label {{ color: var(--text-primary); }}
.stCaption, [data-testid="stCaptionContainer"] {{ color: var(--text-secondary) !important; }}
hr {{ border-color: #323232 !important; }}

.eyebrow,
.section-kicker {{
  color: var(--yellow);
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 0.7rem;
  font-weight: 750;
  letter-spacing: 0.11em;
  text-transform: uppercase;
}}

.section-header {{
  position: relative;
  padding: 1.45rem 1.55rem 1.35rem;
  margin: 0.4rem 0 1.25rem;
  overflow: hidden;
  border: 1px solid #383838;
  border-radius: 16px;
  background: linear-gradient(135deg, #121212 0%, #080808 70%);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.30);
}}

.section-header::after {{
  content: "/";
  position: absolute;
  right: 1.2rem;
  top: -1.5rem;
  color: rgba(255, 211, 0, 0.13);
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 8rem;
  font-weight: 800;
  line-height: 1;
}}

.section-title {{
  position: relative;
  z-index: 1;
  margin: 0.35rem 0 0.3rem;
  color: var(--text-primary);
  font-size: clamp(1.85rem, 3.4vw, 3rem);
  font-weight: 760;
  letter-spacing: -0.055em;
  line-height: 1.02;
}}

.section-copy {{
  position: relative;
  z-index: 1;
  max-width: 850px;
  color: var(--text-secondary);
  font-size: 0.98rem;
  line-height: 1.52;
}}

.hero-flow {{
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  gap: 0.55rem;
}}

.flow-step {{
  padding: 0.48rem 0.72rem;
  border: 1px solid #444444;
  border-radius: 2px;
  background: #101010;
  color: #FFFFFF;
  font-size: 0.78rem;
  font-weight: 650;
}}

.flow-step:first-child {{
  border-color: var(--yellow);
  box-shadow: inset 0 -3px 0 var(--yellow);
}}

.flow-arrow {{
  color: var(--yellow);
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 0.88rem;
}}

.insight-card,
.diagnostic-card,
.role-card-header,
.role-signal,
.role-diagnosis {{
  border-color: #383838;
  background: var(--card-bg);
}}

.insight-card {{
  padding: 1rem 1.1rem;
  margin: 0.55rem 0;
  border: 1px solid #383838;
  border-left: 5px solid var(--accent, var(--yellow));
  border-radius: 2px;
  background: #111111;
}}

.card-label {{
  color: var(--yellow);
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 0.66rem;
  font-weight: 750;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}}

.card-title {{
  margin-top: 0.28rem;
  color: #FFFFFF;
  font-size: 1rem;
  font-weight: 720;
}}

.card-body {{
  margin-top: 0.38rem;
  color: var(--text-secondary);
  font-size: 0.88rem;
  line-height: 1.5;
}}

.status-chip {{
  display: inline-flex;
  align-items: center;
  padding: 0.28rem 0.58rem;
  border: 1px solid var(--chip);
  border-radius: 2px;
  background: color-mix(in srgb, var(--chip) 13%, #090909);
  color: var(--chip);
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 0.66rem;
  font-weight: 750;
  letter-spacing: 0.05em;
  text-transform: uppercase;
}}

.role-card-header {{
  margin-top: 0.9rem;
  padding: 1.15rem 1.25rem 0.92rem;
  border: 1px solid #383838;
  border-bottom: 0;
  border-radius: 14px 14px 0 0;
  background: linear-gradient(120deg, #171717, #0D0D0D);
}}

.role-card-title-row {{
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 1rem;
}}

.role-card-title {{
  color: #FFFFFF;
  font-size: 1.22rem;
  font-weight: 760;
  letter-spacing: -0.03em;
}}

.role-card-job {{
  margin-top: 0.27rem;
  color: var(--text-secondary);
  font-size: 0.84rem;
}}

.role-question {{
  margin-top: 0.82rem;
  padding-top: 0.72rem;
  border-top: 1px solid #343434;
  color: #FFFFFF;
  font-size: 0.86rem;
  font-weight: 650;
}}

.role-signal {{
  min-height: 156px;
  padding: 0.92rem 0.98rem 0.72rem;
  border: 1px solid #383838;
  background: #111111;
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
  font-weight: 700;
  letter-spacing: 0.025em;
}}

.signal-change {{ font-size: 0.76rem; font-weight: 760; }}

.signal-period {{
  margin-top: 0.58rem;
  color: var(--yellow);
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 0.63rem;
  font-weight: 700;
  letter-spacing: 0.055em;
  text-transform: uppercase;
}}

.signal-value {{
  margin-top: 0.12rem;
  color: #FFFFFF;
  font-size: 1.65rem;
  font-weight: 780;
  letter-spacing: -0.04em;
}}

.signal-prior {{
  color: var(--text-secondary);
  font-size: 0.72rem;
}}

.signal-sparkline {{
  display: block;
  width: 100%;
  height: 32px;
  margin-top: 0.48rem;
  overflow: visible;
}}

.role-diagnosis {{
  display: grid;
  grid-template-columns: 1fr 1.35fr;
  gap: 1rem;
  padding: 0.9rem 1rem;
  margin-bottom: 0.85rem;
  border: 1px solid #383838;
  border-top: 0;
  border-left: 5px solid var(--accent);
  border-radius: 0 0 14px 14px;
  background: #171717;
}}

.role-diagnosis-item {{
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}}

.role-diagnosis-copy {{
  color: #FFFFFF;
  font-size: 0.84rem;
  line-height: 1.45;
}}

.diagnostic-card {{
  height: 100%;
  padding: 1.15rem 1.2rem;
  margin: 0.48rem 0;
  border: 1px solid #3A3A3A;
  border-top: 4px solid var(--yellow);
  border-radius: 4px;
  background: linear-gradient(180deg, #151515 0%, #101010 100%);
  box-shadow: 0 14px 35px rgba(0, 0, 0, 0.22);
}}

.diagnostic-card-top {{
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  gap: 1rem;
}}

.diagnostic-title {{
  margin-top: 0.28rem;
  color: #FFFFFF;
  font-size: 1.12rem;
  font-weight: 750;
  letter-spacing: -0.03em;
}}

.diagnostic-grid {{
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 0.68rem;
  margin-top: 1rem;
}}

.diagnostic-field {{
  padding: 0.72rem 0.75rem;
  border: 1px solid #343434;
  border-radius: 2px;
  background: #090909;
}}

.diagnostic-label {{
  color: var(--yellow);
  font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
  font-size: 0.62rem;
  font-weight: 720;
  letter-spacing: 0.045em;
  text-transform: uppercase;
}}

.diagnostic-value {{
  margin-top: 0.27rem;
  color: #FFFFFF;
  font-size: 0.84rem;
  font-weight: 620;
  line-height: 1.38;
}}

.diagnostic-action {{
  display: flex;
  gap: 0.72rem;
  align-items: baseline;
  margin-top: 0.9rem;
  padding-top: 0.82rem;
  border-top: 1px solid #373737;
  color: #FFFFFF;
  font-size: 0.84rem;
  line-height: 1.45;
}}

[data-testid="stDataFrame"] {{
  overflow: hidden;
  border: 1px solid #3A3A3A;
  border-radius: 3px;
  background: #111111;
}}

[data-testid="stAlert"] {{
  border: 1px solid #3A3A3A;
  border-radius: 3px;
  background: #111111;
}}

@media (max-width: 900px) {{
  .block-container {{ padding: 1.25rem 1rem 3rem; }}
  .role-diagnosis {{ grid-template-columns: 1fr; }}
  .diagnostic-grid {{ grid-template-columns: 1fr; }}
}}
</style>
"""
