# section 1: github_client.py
# Person 1 can explain this section

import requests
import re
from typing import Tuple, Optional

class GitHubClient:
    def __init__(self, token: Optional[str] = None):
        """
        Initializes the GitHub client.
        :param token: Optional Personal Access Token. If not provided, requests might be rate-limited.
        """
        self.headers = {
            "Accept": "application/vnd.github.v3.diff"
        }
        if token:
            self.headers["Authorization"] = f"token {token}"

    def parse_pr_url(self, url: str) -> Tuple[str, str, int]:
        """
        Parses a GitHub PR URL and extracts the owner, repo, and PR number.
        Example: https://github.com/owner/repo/pull/123 -> ('owner', 'repo', 123)
        """
        # Regex to match https://github.com/owner/repo/pull/123
        pattern = r"github\.com/([^/]+)/([^/]+)/pull/(\d+)"
        match = re.search(pattern, url)
        if not match:
            raise ValueError(f"Invalid GitHub PR URL format: {url}")
        
        owner, repo, pr_number = match.groups()
        return owner, repo, int(pr_number)

    def get_pr_diff(self, owner: str, repo: str, pr_number: int) -> str:
        """
        Fetches the raw diff of the Pull Request from GitHub API.
        """
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls/{str(pr_number)}"
        response = requests.get(url, headers=self.headers)
        
        # GitHub v3 API returns diff if Accept header is mapped to v3.diff
        if response.status_code == 200:
            return response.text
        elif response.status_code == 404:
            raise Exception(f"PR not found. Ensure the URL is correct and the repo is accessible. {owner}/{repo}")
        elif response.status_code == 403:
            raise Exception(f"Rate limited or forbidden. Consider using a GitHub token. Error: {response.text}")
        else:
            raise Exception(f"Failed to fetch PR diff: {response.status_code} - {response.text}")

    def fetch_diff_from_url(self, pr_url: str) -> str:
        """
        Main entry point for Person 1's section. Takes a URL and returns the diff.
        """
        owner, repo, pr_num = self.parse_pr_url(pr_url)
        return self.get_pr_diff(owner, repo, pr_num)
