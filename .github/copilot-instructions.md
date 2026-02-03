# Copilot Instructions for escola-django-apirest

> NOTE: I could not find any source files in the opened workspace. This file is a draft scaffold tailored for a Django + DRF API project. I included specific guidance templates and examples you should replace with the project's real filenames, commands, and conventions. Reply with file paths (e.g., `manage.py`, `requirements.txt`, `pyproject.toml`, `api/`, `alunos/`) or give repo access and I will merge concrete, discoverable patterns into this file.

## Quick context (what to look for)
- Look for `manage.py`, `pyproject.toml` or `requirements.txt`, and a Django settings module (usually `project/settings.py`).
- Check for Django apps (folders with `models.py`, `views.py`, `serializers.py`), e.g. `alunos/`, `cursos/`.
- Check `urls.py` files for how the API is routed (DRF `routers` vs manual `path()` declarations).
- Inspect `tests/` or `**/tests.py` to see testing style (pytest vs Django TestCase).

## Big-picture architecture (what a coding agent must understand) 🔧
- This appears to be a Django REST API service. Prioritize these components in order: models (data shape), serializers (transformation + validation), views/viewsets (business logic + endpoints), and URL routing (API surface).
- If the repo uses `ModelViewSet` + `DefaultRouter`, prefer adding endpoints by updating `viewsets` and `routers` files. Otherwise follow existing manual `path()` conventions.

## Developer workflows & commands (add project-specific commands)
- Running locally (replace if different):
  - Install: `python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt`
  - Run server: `python manage.py runserver` or `./manage.py runserver`
  - Migrations: `python manage.py makemigrations && python manage.py migrate`
- Testing:
  - If `pytest` present: `pytest -q` (include `-k` examples when relevant)
  - Else: `python manage.py test`
- Formatting and linting (if present): `black .`, `ruff .`, `isort .`, `flake8`.
- DB & external services: note if `docker-compose.yml` or `.env` is used to provide Postgres/redis; prefer to run them via `docker compose up` when present.

## Project-specific conventions & patterns to follow 💡
- Tests: use fixtures located in `tests/fixtures/` (if present) and prefer `client`/`api_client` fixtures for endpoint tests.
- API versioning: prefer `path('api/v1/', include(...))` if present; add new endpoints under `v1` unless the project has a different pattern.
- Serializers: keep validation logic in `serializers.py`. If `services/` or `usecases/` folders exist, put complex business logic there, not in views.
- Responses: prefer consistent DRF `Response` objects and use status codes from `rest_framework.status`.

## Integration points & env dependencies ⚠️
- Check `settings.py` for `DATABASES`, `CACHES`, and third-party keys (SENTRY_DSN, STRIPE_*, AWS_*). Use `.env` or GitHub Secrets for these values.
- If `docker-compose.yml` exists, CI likely spins up dependent services via compose — mirror that in tests or local dev docs.

## Tests and assertions the agent should produce ✅
- Prefer small, focused tests mirroring the project's style: e.g., `test_aluno_list_returns_active_students` rather than broad integration tests when unit tests are commonly used.
- Use the project's existing fixtures and factories (`factories.py` or `factory_boy`) where available.

## Code change patterns & pull request guidance 🧭
- Keep migrations minimal and committed alongside model changes.
- When adding endpoints, add serializer + viewset + router entry + tests for status and core validation errors.
- Follow any `.pre-commit-config.yaml` or CI linting steps; run formatters locally before pushing.

## Where to add examples (placeholders to be replaced)
- Add a concrete example from the codebase where a `ModelViewSet` exists:

```md
Example: Add `PUT /api/v1/alunos/{id}/`
- File: `alunos/views.py` (extend `AlunoViewSet`)
- File: `alunos/serializers.py` (add fields and validation)
- Tests: `alunos/tests/test_update.py` (assert 200 and changed fields)
```

Replace the snippet above with real file paths and code samples once you allow access to the repo.

## Security & data handling notes 🔒
- Look for ad-hoc secrets in the repo — if detected, remove and move to env variables.
- Respect GDPR-like data handling patterns if `personal_data` or `cpf` fields exist: prefer hashing or redaction in logs.

## Helpful commands to run (agent checklist)
1. Run the project's test suite and report failures.
2. Run linters/formatters and fix simple issues (if CI config allows autoformat commits).
3. Add/modify tests for any behavioral change and ensure they run in CI.

---

If you want, I can:
- Merge this scaffold into an existing `.github/copilot-instructions.md` if you point me to it, or
- Update this draft with concrete examples if you grant read access to the repository or paste key files (`manage.py`, `settings.py`, `requirements.txt`, `pyproject.toml`, `urls.py`, and a representative app folder`).

Please tell me which approach you prefer or provide the files and I'll tailor this file with concrete, discoverable examples and then commit the change. 👇

*Drafted by GitHub Copilot using Raptor mini (Preview).*