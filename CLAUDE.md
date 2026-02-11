# DevLoop — AI-Assisted Issue Resolution

This section is used by the DevLoop GitHub Actions workflow.
The AI agent reads these instructions when triaging, fixing, and verifying issues.

## Project Context

- **Language**: Python
- **Test framework**: pytest
- **Test command**: `pytest`
- **Source directory**: `src/`
- **Test directory**: `tests/`

## Test Execution

Always run tests before creating a PR:

```bash
pytest --tb=short -q
```

If a specific test file is relevant to the issue:

```bash
pytest tests/test_<module>.py -v
```

## Commit Conventions

- Use conventional commits: `fix:`, `feat:`, `refactor:`, `test:`, `docs:`
- Reference the issue number: `fix: handle null input in parser (#123)`
- Keep commits atomic — one logical change per commit

## Pull Request Rules

- PR title: `fix: <short description> (#<issue>)`
- PR body must include:
  - **Root cause**: What caused the issue
  - **Fix**: What was changed and why
  - **Testing**: Which tests were added or modified
- Target branch: `main`
- Request review from the team (auto-assigned via CODEOWNERS if configured)

## DevLoop Labels

The following labels control the automation pipeline:

| Label | Meaning |
|-------|---------|
| `devloop` | Issue is a candidate for AI-assisted resolution |
| `devloop:triaging` | AI is analyzing the issue |
| `devloop:ready-to-fix` | Triage complete, ready for AI fix |
| `devloop:fixing` | AI is working on a fix |
| `devloop:pr-created` | Fix PR has been created |
| `devloop:deployed` | Fix has been deployed (set by CD pipeline) |
| `devloop:verified` | Post-deploy verification passed |
| `devloop:failed` | Something went wrong — needs human review |
| `devloop:needs-human` | AI cannot resolve this — human intervention required |
| `devloop:aborted` | Manually aborted by a human |

## Code Style

- Follow existing project conventions
- Use type hints for function signatures
- Keep functions focused and testable
- Add docstrings for public functions

## Boundaries

The AI agent should NOT:
- Modify CI/CD configuration files
- Change dependency versions without explicit instructions
- Alter database schemas or migrations
- Touch authentication or authorization logic without human review
- Make changes outside the scope of the assigned issue
