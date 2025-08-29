# Orchestrator (Contract)

**Inputs:** user_msg, identity, context  
**Outputs:** response, plan[], logs  

**Flow:**  
policy_gate → planner (stub) → tool_router (local only) → memory.remember(events)