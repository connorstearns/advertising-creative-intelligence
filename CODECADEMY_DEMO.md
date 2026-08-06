# Codecademy Creative Intelligence Demo

This repository now includes a separate Codecademy pitch prototype alongside the existing Spotify Advertising demo. The Spotify app and its sample data remain unchanged.

## Run locally

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
streamlit run codecademy_app.py
```

## What the prototype demonstrates

- Activation Role Performance across Demand Creation, Reinforcement, Demand Capture, and Customer Growth
- Creative Territory diagnostics for:
  - The Job Changed. So Can You.
  - Make Readiness Visible
  - Stay Unfinished
- Audience, product, format, and channel fit
- Product-motion filtering for Pro, Workshops, Bootcamps, All Access, and Teams
- Fatigue and refresh recommendations
- A prioritized What To Make Next production queue
- Data requirements and taxonomy QA

## Important caveat

All bundled Codecademy data is illustrative and pitch-safe. It does not represent actual Codecademy campaign, product, subscription, search, or CRM performance.

## Deployment

A second Streamlit Community Cloud app can be created from this same repository using `codecademy_app.py` as the app entrypoint. Configure `app_password` in Streamlit secrets to require demo access.

## Future productionization

A live version would require approved access to paid-media delivery, creative asset taxonomy, web and product analytics, lifecycle/subscription events, Teams CRM outcomes, and search/AI visibility data. Asset IDs must consistently map territory, activation role, audience, growth motion, format, channel, variant, and destination.
