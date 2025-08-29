# Memory (Schema & API)

**Tables:**  
- events(id, ts, source, type, payload, tags)  
- profiles(id, kind, name, attrs)  
- knowledge(id, scope, content, rationale, links)  
- vectors(id, ref_table, ref_id, emb, dim)  

**APIs:**  
- remember()  
- recall()  
- link()  
- summarize()  

**Encryption:** at rest; keys local only