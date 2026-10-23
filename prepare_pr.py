"""Offline pull request preparation. Does not create or claim hosted PRs."""
import argparse
import json
import subprocess
from pathlib import Path


def git(*args):
    return subprocess.check_output(['git', *args], text=True).strip()


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--base', default='main', help='Base branch or ref')
    p.add_argument('--head', required=True, help='Existing feature branch or ref')
    p.add_argument('--title', required=True)
    p.add_argument('--output', default='pr_draft.md')
    args = p.parse_args()
    git('rev-parse', '--verify', args.base)
    git('rev-parse', '--verify', args.head)
    changes = git('diff', '--stat', f'{args.base}...{args.head}')
    commits = git('log', '--format=%h %s', f'{args.base}..{args.head}')
    if not changes:
        p.error('No file differences between base and head; refusing empty PR draft')
    body = (f'# {args.title}\n\nBase: `{args.base}`  Head: `{args.head}`\n\n'
            '## Changed files\n```\n' + changes + '\n```\n\n'
            '## Commits\n```\n' + commits + '\n```\n\n'
            '## Validation\n- [ ] Tests executed and results recorded\n'
            '- [ ] Human reviewer approved\n\n'
            'This is an offline draft, **not** an opened GitHub/GitLab pull request.\n')
    Path(args.output).write_text(body, encoding='utf-8')
    print(json.dumps({'draft': args.output, 'base': args.base, 'head': args.head, 'hosted_pr_created': False}))


if __name__ == '__main__':
    main()
