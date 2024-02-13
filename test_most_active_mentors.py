"""A module containing unit tests for the most_active_mentors module.

This module contains unit tests for the count_comments_per_user and
get_mentor_count functions in the most_active_mentors module.
The tests use mock GitHub issues and comments to test the functions' behavior.

Classes:
    TestCountCommentsPerUser: A class to test the count_comments_per_user function.
    TestGetMentorCount: A class to test the
        get_mentor_count function.

"""
import unittest
from datetime import datetime, timedelta
from unittest.mock import MagicMock

from classes import IssueWithMetrics
from most_active_mentors import (
    count_comments_per_user,
    get_mentor_count,
)


class TestCountCommentsPerUser(unittest.TestCase):
    """Test the count_comments_per_user function."""

    def test_count_comments_per_user(self):
        """Test that count_comments_per_user correctly counts user comments.

        This test mocks the GitHub connection and issue comments, and checks that
        count_comments_per_user correctly considers user comments for counting.

        """
        # Set up the mock GitHub issues
        mock_issue1 = MagicMock()
        mock_issue1.comments = 2
        mock_issue1.issue.user.login = "issue_owner"
        mock_issue1.created_at = "2023-01-01T00:00:00Z"

        # Set up 21 mock GitHub issue comments - only 20 should be counted
        mock_issue1.issue.comments.return_value = []
        for i in range(22):
            mock_comment1 = MagicMock()
            mock_comment1.user.login = "very_active_user"
            mock_comment1.created_at = datetime.fromisoformat(f"2023-01-02T{i:02d}:00:00Z")
            mock_issue1.issue.comments.return_value.append(mock_comment1)

        # Call the function
        result = count_comments_per_user(mock_issue1)
        expected_result = {"very_active_user": 20}

        # Check the results
        self.assertEqual(result, expected_result)

