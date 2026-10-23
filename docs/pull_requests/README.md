# Pull request workflow and evidence

This repository can be uploaded to GitHub or GitLab with its `.git` history intact.
Real pull requests must be created on the hosting service and cannot be manufactured
by making merge commits locally. No hosted PR count is claimed by this ZIP.

1. Create a remote repository and push the default branch (`git push -u origin HEAD`).
2. Create a focused feature branch for a genuine change (`git switch -c feature/topic`).
3. Commit the implementation and tests, then push (`git push -u origin feature/topic`).
4. Open a PR on the hosting service and complete the supplied template.
5. Review, run CI, and merge. Repeat for distinct substantive contributions.

For a preflight draft, run `python prepare_pr.py --base main --head feature/topic --title "Implement topic"`.
If your default branch is `master`, pass `--base master` instead.

A GitHub CLI option, after authentication, is:
`gh pr create --base main --head feature/topic --title "Implement topic" --body-file pr_draft.md`

This command is **not** executed by the offline ZIP. The GitHub service's PR URLs,
IDs, reviewers, and timestamps are the evidence of authentic PRs.
