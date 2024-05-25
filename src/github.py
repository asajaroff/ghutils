import os
import logging
import requests
from requests import HTTPError

log = logging.getLogger(__name__)

try:
  GITHUB_ACCESS_TOKEN = os.environ.get("GITHUB_ACCESS_TOKEN")
  GITHUB_ORG = os.environ.get("GITHUB_ORG")
  url=f'https://github.com/{GITHUB_ORG}/'
  headers_github = {'Authorization': f'Bearer {GITHUB_ACCESS_TOKEN}', 
    'Accept': 'application/vnd.github+json',
    'X-GitHub-Api-Version': '2022-11-28'}
except NameError as err:
  log.critical(err)
  exit(1)

def get_octocat():
  try:
    r = requests.get('https://api.github.com/octocat', headers=headers_github)
    log.debug(f'GET /octocat: {r.status_code}')
    r.raise_for_status()
    print(r.text)
    return True
  except HTTPError as e:
    log.critical(f'Error validating token: {e}')
    exit(4)

def get_authenticated_user():
  try:
    r = requests.get('https://api.github.com/user', headers=headers_github)
    log.debug(f'GET /user: {r.status_code}')
    r.raise_for_status()
    log.debug(r.json())
    rjson = r.json()
    print(f'Authenticated as: {rjson["login"]}, url is {rjson["url"]} and email is {rjson["email"]}')
    return True
  except HTTPError  as e:
    log.critical(f'Authentication error: {e}')
    exit(4)
