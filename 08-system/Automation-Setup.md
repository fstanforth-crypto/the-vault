---
type: meta
status: live
created: 2026-05-21
updated: 2026-05-21
tags: [system, automation]
---

# Automation Setup

What's already automatic, what needs you to flip a switch, what needs a one-time setup.

## Already running (no action needed)

These are wired in `.claude/settings.json` and live in `.claude/hooks/`. They fire whenever Claude Code is running in this vault.

- **`bump-updated.py`** — every note Claude edits gets its `updated:` YAML field stamped to today.
- **`session-start.py`** — every new Claude session begins with a status block (inbox count, active programs, stale safety docs) automatically injected into Claude's context.

## One command to enable — git pre-commit hook

Stamps `updated:` even when you edit notes in Obsidian directly (or anywhere else) — the bump happens at commit time. Run once per machine that uses the vault:

```bash
cd "/home/user/The Vault"
git config core.hooksPath .githooks
```

To verify:

```bash
echo "test" >> 00-command-center/Today.md
git add 00-command-center/Today.md && git commit -m "test"
# Should print: "pre-commit: bumped updated: on 1 note(s)"
```

Disable: `git config --unset core.hooksPath`.

## Even simpler alternative for Obsidian-only edits

If you don't want to fight with git for in-flight updates: install the Obsidian community plugin **"Update time on edit"**. It updates `updated:` in real time as you type in Obsidian, no commit needed. Combine it with the git pre-commit hook for redundancy, or use it alone if you don't care about non-Obsidian editors.

## Scheduled (GitHub Actions) — needs three one-time steps

The workflow file is already at `.github/workflows/agentic-os.yml`. To turn it on:

### 1. Create a private GitHub repo for the vault

In the GitHub UI: New repository → name it (e.g. `the-vault`) → **private** → empty (no README/.gitignore — we already have those). Copy the URL it gives you (e.g. `git@github.com:fstanforth/the-vault.git`).

### 2. Push the vault

```bash
cd "/home/user/The Vault"
git remote add origin <URL-FROM-STEP-1>
git branch -M main
git push -u origin main
```

### 3. Add your Anthropic API key as a secret

GitHub repo → Settings → Secrets and variables → Actions → New repository secret:
- **Name:** `ANTHROPIC_API_KEY`
- **Value:** your real key from https://console.anthropic.com/

### 4. Test the workflow manually before trusting the schedule

GitHub repo → Actions tab → "Agentic OS" → "Run workflow" → leave command as `/plan-today` → Run. Verify it succeeds and the commit it makes is sensible. If it fails, check the logs — most failures are auth (missing/bad API key) or the `claude` CLI flags drifting from what's in the workflow (verify `-p` and `--dangerously-skip-permissions` against current docs).

### What it does on autopilot

- **Mon–Fri 07:00 ET:** runs `/plan-today`, commits `Today.md` if changed.
- **Friday 16:00 ET:** runs `/weekly-review`, commits `Weekly-Review.md` if changed.

Adjust cron schedules in `.github/workflows/agentic-os.yml`. Cron times are UTC; the comments next to each line note the ET equivalent.

## Cost / safety notes

- The GitHub Action calls the Anthropic API directly — billed to your account on the API key.
- Estimate: `/plan-today` is a few thousand tokens per run, `/weekly-review` is larger. Two runs/weekday + one Friday = ~15 runs/week. Real cost depends on vault size; check your dashboard after week one.
- `/process-inbox` is intentionally **not** scheduled because it expects confirmation. If you want auto-triage, write a separate `/auto-inbox` slash command that triages without prompting and add it to the workflow.
- The action commits as `agentic-os[bot]` so it's easy to filter in `git log`.
- Failed runs land in the Actions tab — set up email notifications in your GitHub profile if you want to know fast.

## What's still NOT automatic

- **In real time while you type in Obsidian** — without the "Update time on edit" plugin, the `updated:` field only bumps at commit (pre-commit hook) or when Claude touches the file (PostToolUse hook).
- **Anything that needs external data** — pulling new DOT regulations, syncing client schedules, watching FMCSA bulletins — that's a separate build. Suggest writing a slash command (e.g. `/fmcsa-bulletins`) + a daily schedule entry that triggers it.

## Changelog of this setup

See `08-system/Changelog.md`.
