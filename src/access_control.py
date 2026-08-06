import hmac
import inspect
import logging
from collections.abc import Mapping, MutableMapping
from html import escape

import streamlit as st

LOGGER = logging.getLogger(__name__)
AUTHENTICATED_KEY = "demo_authenticated"
PASSWORD_KEY = "demo_password_input"


def get_app_password(secrets: Mapping) -> str | None:
    try:
        value = secrets.get("app_password")
    except (FileNotFoundError, KeyError):
        return None
    if value is None:
        return None
    password = str(value)
    return password if password else None


def access_is_granted(
    secrets: Mapping,
    session_state: MutableMapping,
    submitted_password: str | None = None,
) -> bool:
    configured_password = get_app_password(secrets)
    if configured_password is None:
        if not session_state.get(AUTHENTICATED_KEY):
            LOGGER.warning(
                "Streamlit secret 'app_password' is not configured; allowing local demo access."
            )
        session_state[AUTHENTICATED_KEY] = True
        return True

    if session_state.get(AUTHENTICATED_KEY):
        return True
    if submitted_password is None:
        return False
    if hmac.compare_digest(submitted_password, configured_password):
        session_state[AUTHENTICATED_KEY] = True
        return True
    return False


def _caller_app_title() -> str | None:
    """Resolve the title from the active Streamlit entrypoint."""
    frame = inspect.currentframe()
    try:
        current = frame.f_back if frame else None
        while current is not None:
            value = current.f_globals.get("APP_TITLE")
            if value is not None:
                title = str(value).strip()
                if title:
                    return title

            filename = str(current.f_code.co_filename).replace("\\", "/").lower()
            if filename.endswith("/codecademy_app.py") or filename == "codecademy_app.py":
                return "Codecademy Creative Intelligence"
            if filename.endswith("/app.py") or filename == "app.py":
                return "Spotify Advertising Creative Intelligence"

            current = current.f_back
        return None
    finally:
        del frame


def require_demo_access(
    secrets: Mapping,
    session_state: MutableMapping,
    *,
    eyebrow: str = "Access-controlled demo",
    title: str | None = None,
    description: str = "Enter the demo password to view the sample dashboard.",
) -> bool:
    if access_is_granted(secrets, session_state):
        return True

    resolved_title = title or _caller_app_title() or "Spotify Advertising Creative Intelligence"

    _, center, _ = st.columns([1, 1.35, 1])
    with center:
        st.markdown(
            f"""
            <div class="access-panel">
              <div class="eyebrow">{escape(eyebrow)}</div>
              <div class="access-title">{escape(resolved_title)}</div>
              <div class="access-copy">{escape(description)}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        with st.form("demo_access_form", clear_on_submit=False):
            password = st.text_input(
                "Demo password",
                type="password",
                key=PASSWORD_KEY,
                placeholder="Enter password",
            )
            submitted = st.form_submit_button(
                "View dashboard",
                type="primary",
                width="stretch",
            )
        if submitted:
            if access_is_granted(secrets, session_state, password):
                st.rerun()
            st.error("That password is not valid.")
    return False
