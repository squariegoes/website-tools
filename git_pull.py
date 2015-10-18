import git


DIRS = [
    '/home/jstewart1/sample'
]


def main():
    for git_dir in DIRS:
        pull(git_dir)


def pull(git_dir):
    g = git.cmd.Git(git_dir)
    g.pull()
    print 'Git pulled {}'.format(git_dir)


if __name__ == "__main__":
    main()