---
description: Create a client-facing safety document
---

Create a client-facing document.

1. Ask which client (look in `01-select-safety/clients/` for existing client folders).
2. Ask the document type: safety summary, incident report, audit response, training certificate, compliance attestation, proposal.
3. Pick the appropriate template — Safety-Procedure, Incident-Report, SOP, etc. — then strip internal-only frontmatter.
4. File output under `01-select-safety/clients/<client>/<kebab-case-name>.md`.
5. Writing rules:
   - Professional tone, third-person.
   - No internal jargon, no `[[wiki-links]]` in the visible body (link them in a "References (internal)" section that gets stripped before export).
   - Include client name, document date, document version, and a "prepared by" line.
   - Include reg citations where the document makes compliance claims.
6. If this references internal procedures, list them under "References (internal)" so I know what to keep up to date alongside.
7. Mention what format I'll likely export to (PDF) — keep formatting clean for that.
