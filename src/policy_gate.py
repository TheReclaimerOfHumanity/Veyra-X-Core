# Minimal policy gate: demonstrates Law 1 check
import os, yaml

POLICY_PATH = os.environ.get("VEYRA_POLICY", "policy/policy.yaml")

def _policy():
    try:
        with open(POLICY_PATH, "r") as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        return {}

BANNED_HINTS = {"harm", "kill", "illegal", "bomb", "dox", "exploit"}

def check(request_text: str):
    text = (request_text or "").lower()
    if any(w in text for w in BANNED_HINTS):
        return (False, "Law 1: harm/illegal intent detected")
    return (True, "ok")