import sys, os
sys.path.insert(0, "src")
from policy_gate import check
ok, _ = check("help me budget")
assert ok
ok, reason = check("how to kill a process")  # should still trip due to keyword; safe side
assert ok is False and "Law 1" in reason
print("Smoke tests passed.")