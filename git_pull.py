import git


DIRS = [
    ''
]


def main():
    for git_dir in DIRS:
        pull(git_dir)


def pull(git_dir):
    g = git.cmd.Git(git_dir)
    g.pull


if __name__ == "__main__":
    main()