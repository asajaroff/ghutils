import os
import logging
import requests
from requests import HTTPError

log = logging.getLogger(__name__)

try:
  GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN")
  GITHUB_ORG = os.environ.get("GITHUB_ORG")
  headers_github = {'Authorization': f'Bearer {GITHUB_ACCESS_TOKEN}', 
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28'}
except NameError as err:
  log.critical(err)
  exit(1)

def make_get_request(url):
  try:
    r = requests.get(url, headers=headers_github)
    log.debug(f'GET {url}: {r.status_code}')
    r.raise_for_status()
    return r.json()
  except HTTPError as e:
    log.critical(f'HTTP error occurred: {e}')
    exit(4)

def get_octocat():
  response = make_get_request('https://api.github.com/octocat')
  print(response)
  return True

def get_authenticated_user():
  response = make_get_request('https://api.github.com/user')
  print(f'Authenticated as \'{response["login"]}\'')

def get_repository(repository_name):
  url = f'https://api.github.com/repos/{GITHUB_ORG}/{repository_name}'
  response = make_get_request(url)
  log.debug(response)
