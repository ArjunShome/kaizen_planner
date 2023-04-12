#!/usr/bin/env python
"""
Forked from https://gist.github.com/810399
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile

# Pep8 codes
select_codes = []
ignore_codes = []
overrides = []

# Pylint codes
disable_codes = [
    'C0114', 'R0913', 'C0116', 'C0115', 'R0903', 'R0902', 'C0301', 'R1720',
    'E0237', 'W0703', 'W1514', 'W1203', 'W0707', 'E1101', 'R0911', 'R0801'
]


def system(*args, **kwargs):
    kwargs.setdefault('stdout', subprocess.PIPE)
    proc = subprocess.Popen(args, **kwargs)
    out, err = proc.communicate()
    return out


def check_branch_name():
    print('Executing rule to check branch name.')
    args = 'git rev-parse --abbrev-ref HEAD'.split()
    branch_name = system(*args).decode()

    default_message = f'Branch Name - {branch_name}\nThe name of the branch violates branch naming convention.'

    valid_branch_regex = '^(feature|bugfix|improvement|library|prerelease|release|hotfix)\\/Issue-\\d{1,3}-(FE|BE)-.+$'
    if not re.match(valid_branch_regex, branch_name):
        print(default_message)
        print('The branch name must follow the format as mentioned below.')
        print('\nIssue-{issue_number}-{BE or FE}-{2 or 3 words about feature}\nExample - Issue-77-BE-dashboard-apis')
        sys.exit(1)

    allowed_branch_types = ['feature', 'bugfix', 'improvement', 'library', 'prerelease', 'release', 'hotfix']
    branch_type, branch_name = branch_name.split('/')

    if branch_type not in allowed_branch_types:
        print(default_message)
        print("The branch is not created using git flow.\n")
        print('Please use the following command to create branch using git flow')
        print('\ngit flow feature start YOUR-BRANCH')
        sys.exit(1)

    if 'feature' in branch_name:
        print(default_message)
        print('The branch name contains the word "feature".')
        sys.exit(1)

    if len(branch_name.split('-')) > 7:
        print(default_message)
        print('The branch name must follow the format as mentioned below.')
        print('Branch name is too big. Please put maximum 3 or 4 words as branch description.')
        sys.exit(1)

    print('Branch name looks fine.')


def main():
    print('Executing pre-commit hooks.')
    check_branch_name()
    modified = re.compile('^\s*[AM]+\s+(?P<name>.*\.py$)', re.MULTILINE)
    files = system('git', 'status', '--porcelain').decode("utf-8")
    files = modified.findall(files)
    dir_path = os.path.dirname(os.path.realpath(__file__))
    app_path = os.path.join(dir_path, '../backend/', 'app')

    tempdir = tempfile.mkdtemp()
    for name in files:
        filename = os.path.join(tempdir, name)
        filepath = os.path.dirname(filename)

        if not os.path.exists(filepath):
            os.makedirs(filepath)
        with open(filename, 'w') as f:
            system('git', 'show', ':' + name, stdout=f)

    print('Executing pycodestyle hook.')
    args = ['pycodestyle', '--max-line-length=120']
    if select_codes and ignore_codes:
        print(u'Error: select and ignore codes are mutually exclusive')
        sys.exit(1)
    elif select_codes:
        args.extend(('--select', ','.join(select_codes)))
    elif ignore_codes:
        args.extend(('--ignore', ','.join(ignore_codes)))
    args.extend(overrides)
    args.append(app_path)
    output = system(*args, cwd=tempdir)
    if output:
        shutil.rmtree(tempdir)
        print("Don't forget to run 'black' command, and check the diff before committing.\n")
        print('PEP8 style violations have been detected. Please fix them\n'
              'Check for the pep8 violation by running the command "pycodestyle app"\n\n')
        print(output.decode())
        sys.exit(1)

    print('Executing pylint hook.')
    args = ['pylint']
    if select_codes and ignore_codes:
        print(u'Error: select and ignore codes are mutually exclusive')
        sys.exit(1)
    if disable_codes:
        args.extend(('--disable', ','.join(disable_codes)))
    args.extend(overrides)
    args.append(app_path)
    output = system(*args, cwd=tempdir)
    shutil.rmtree(tempdir)
    output_lines = [line for line in output.decode().split('\n') if line]
    if output and len(output_lines) > 2:
        print("Don't forget to run 'pylint' command, and check the diff before committing.\n")
        print('Pylint violations have been detected. Please fix them\n'
              'Check for the Pylint violation by running the command "pylint app"\n\n')
        print(output.decode())
        sys.exit(1)
    else:
        print(output.decode())


if __name__ == '__main__':
    main()
