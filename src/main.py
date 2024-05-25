import logging
import sys
import os
import argparse

from github import *
from scm import *

try:
  log_level = os.environ.get('LOG_LEVEL', 'INFO')
  logging.basicConfig(stream=sys.stdout, level=log_level, format='time=\'%(asctime)s\'\tlevel=\'%(levelname)s\'\tname=\'%(name)s\'\tmsg=\'%(message)s\'')
  log = logging.getLogger(__name__)
  log.debug('Setting up environment variables')
  GITHUB_ORG = os.environ.get('GITHUB_ORG', None)
  GITHUB_USER = os.environ.get('GITHUB_USER', None)
  GITHUB_API_TOKEN = os.environ.get('GITHUB_API_TOKEN', None)
  log.debug(f'Added the following ENV_VARS: {GITHUB_ORG}, {GITHUB_USER}, {GITHUB_API_TOKEN}')
except Exception as e:
  log.error(f'Error initiliazing the context: {e}')
  exit(1)

def main():
  parser = argparse.ArgumentParser(
    prog='ghutils',
    description='A command line tool to automate git operations and GitHub API interactions',)
  parser.add_argument('-t', '--target', help='The target repository to interact with', default=None)
  parser.add_argument('-v', '--verbose',
    action='store_true')
  parser.add_argument('-u', '--user', help='The authenticated user to interact with', action='store_true')
  args = parser.parse_args()
  if len(sys.argv) == 1:
    log.debug('No arguments provided')
    sys.exit(0)
  if args.user is True:
    get_authenticated_user()
    exit(0)
  if args.target is not None:
    log.debug(f'Target repository: {args.target}')
    get_octocat()
  exit(0)

if __name__ == '__main__':
  main()
