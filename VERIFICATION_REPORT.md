# Verification and limitations

- Git repository: included in ZIP with `.git` directory.
- Local feature commits: 100 staged source additions on separate branches.
- Local merge commits: 100 `--no-ff` merges into main.
- Hosted pull requests: **0 created or verified**; merges do not prove PRs.
- README: installation, build, run, usage and testing sections included.
- Dependency file: `requirements.lock` contains pinned direct dependencies; transitive graph is not fully locked.
- Runnable app entrypoint: `vogue_engine.dashboards.router:app`; actual HTTP startup must be verified in a compatible Python environment with installed dependencies.
- No API keys or `.env` files added.
