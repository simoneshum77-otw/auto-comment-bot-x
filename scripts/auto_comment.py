#!/usr/bin/env python3
"""
Auto Comment Bot - Python script example

This script demonstrates how to automatically add comments to new GitHub issues
using the GitHub API. This is an alternative approach to GitHub Actions workflows.

Requirements:
- python3
- PyGithub library (pip install PyGithub)
- GitHub personal access token with 'repo' scope

Usage:
    python auto_comment.py --token <GITHUB_TOKEN> --owner <OWNER> --repo <REPO> --issue <ISSUE_NUMBER>
"""

import argparse
import sys
from github import Github

def add_comment_to_issue(token, owner, repo, issue_number, comment):
    """Add a comment to a GitHub issue."""
    try:
        # Authenticate with GitHub
        g = Github(token)
        
        # Get the repository
        repository = g.get_repo(f"{owner}/{repo}")
        
        # Get the issue
        issue = repository.get_issue(number=issue_number)
        
        # Add comment
        issue.create_comment(comment)
        print(f"✅ Successfully added comment to issue #{issue_number}")
        return True
        
    except Exception as e:
        print(f"❌ Error adding comment: {e}")
        return False

def main():
    parser = argparse.ArgumentParser(description='Auto Comment Bot - Add comments to GitHub issues')
    parser.add_argument('--token', required=True, help='GitHub personal access token')
    parser.add_argument('--owner', required=True, help='Repository owner')
    parser.add_argument('--repo', required=True, help='Repository name')
    parser.add_argument('--issue', type=int, required=True, help='Issue number')
    parser.add_argument('--comment', default='Thank you for your contribution!', 
                       help='Comment text (default: "Thank you for your contribution!")')
    
    args = parser.parse_args()
    
    success = add_comment_to_issue(
        args.token,
        args.owner,
        args.repo,
        args.issue,
        args.comment
    )
    
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()