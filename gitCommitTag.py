import os
import tempfile
from subprocess import call

def create_temp_directory(reason):
    """ Creates a temporary directory and returns the path to it. """
    current_dir = os.getcwd()
    # change path accordingly - dir=current_dir
    # check temp dir - C:\Users\uC264789\AppData\Local\Temp
    return tempfile.mkdtemp(prefix='temp-{0}-'.format(reason))

def _invoke_cmd(args, **kwargs):
    """ Invokes a commandline command. """

    cwd = kwargs.get('working_directory')

    exit_code = call(args, cwd=cwd)

    if exit_code != 0:
        print('External command failed.')

def download_repo(repo_url,repo_path,repo_temppath):
    """ Download Repo2"""
    _invoke_cmd(['git',
                 'clone',
                 repo_url,
                 '--branch',
                 'master',
                 '--depth',
                 '1',
                 repo_path],
                 working_directory=repo_temppath)

def repo_tag(tag_version, tag_message, repo_directory):

    _invoke_cmd(['git',
                 'tag',
                 '-a',
                 tag_version,
                 '-m',
                 '"{0}"'.format(tag_message)],
                 working_directory=repo_directory)

    _invoke_cmd(['git',
                 'push',
                 '--tags'],
                 working_directory=repo_directory)

def main():
    repo_temppath = create_temp_directory('19072020')
    print("Repo temporary Path changed ----> "+repo_temppath)
    repo_name = 'infra-scripts'
    download_repo('https://github.com/tr/production-engineering_infrastructure-scripts.git', repo_name, repo_temppath)
    repo_directory = os.path.join(repo_temppath,repo_name)
    # Get commit number and tag to repo-2
    with open('git-commit.txt','r') as f:
        tag_name = f.read()
    repo_tag(tag_name, 'initial_tag_message',repo_directory)

if __name__ == '__main__':
    main()