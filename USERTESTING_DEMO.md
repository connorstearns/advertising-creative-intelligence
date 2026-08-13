# UserTesting Creative Learning System Demo

This repository includes a third pitch prototype, alongside the existing Spotify Advertising and
Codecademy demos. Neither of those apps or their sample data is modified by this addition.

The prototype demonstrates how Current would turn a new campaign platform into structured media
learning for **UserTesting — Parent Brand**. Instrument is developing the parent brand's campaign
platform, **Real Human Intelligence**; Current structures activation variants, measures them, and
turns the signals into the next creative production decision.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run usertesting_app.py
```

## What the prototype demonstrates

- **Creative Learning Overview** — cross-functional filters across audience, topic, media role,
  format, environment, and variant, with a live "What We're Learning" / "Next Creative Decision"
  summary that responds to the selected slice
- **Topic × Audience Learning** — Verified Human Network, API / MCP Integrations, and Real-Time
  Human Input compared across Builder and Creator messaging registers
- **Format / Environment Learning** — which format/environment pairings earn which KPI (engagement
  quality, identifiable account signals, or high-intent behavior)
- **Creative Asset Detail** — taxonomy, buyer tension, job of the asset, learning question, signals,
  diagnosis, and recommended next action for a single illustrative execution

## Important caveat

All bundled data is illustrative and pitch-safe. It does not represent actual UserTesting campaign
performance. The parent-brand name and visual identity are not finalized and are not used in this
prototype — the platform is referred to only as "Real Human Intelligence."

## Deployment

A third Streamlit Community Cloud app can be created from this same repository using
`usertesting_app.py` as the app entrypoint. Configure `app_password` in Streamlit secrets to require
demo access, and append the deployed URL to the `STREAMLIT_APP_URLS` repository variable used by the
keep-awake workflow.

## Future productionization

A live version would require approved access to paid-media delivery by asset ID, web/landing
analytics for content progression and engaged visits, CRM/account data for identifiable and
priority-account engagement, and a consistent taxonomy mapping campaign, audience, topic, media
role, format, environment, and variant for every asset.
