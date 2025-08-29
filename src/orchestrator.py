# Veyra X seed orchestrator (local CLI)
from mem import remember_event, recall_last
from policy_gate import check as policy_check

def main():
    print("Veyra X seed online (local). Type 'quit' to exit.")
    while True:
        try:
            user = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if user.lower() in {"quit", "exit"}:
            break
        allowed, reason = policy_check(user)
        if not allowed:
            print(f"Refuse: {reason}")
            remember_event("cli", "refusal", {"reason": reason, "text": user})
            continue
        remember_event("cli", "user_msg", {"text": user})
        print("Veyra:", "Acknowledged.")
    for ts, src, typ, payload, tags in recall_last(3):
        print("Event:", ts, src, typ, payload, tags)

if __name__ == "__main__":
    main()