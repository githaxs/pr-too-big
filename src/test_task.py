from .task import Task


test_cases = [
    {"settings": {}, "github_body": {}, "expected": True},
    {"settings": {"max_additions": 9}, "github_body": {}, "expected": True},
    {
        "settings": {"max_additions": 9},
        "github_body": {"pull_request": {"additions": 116}},
        "expected": False,
    },
    {
        "settings": {"max_additions": 9, "max_deletions": 9},
        "github_body": {"pull_request": {"additions": 116, "deletions": 8}},
        "expected": False,
    },
    {
        "settings": {"max_additions": 9, "max_deletions": 9},
        "github_body": {"pull_request": {"additions": 9, "deletions": 8}},
        "expected": True,
    },
]


def test():
    for test_case in test_cases:
        task = Task(test_case["github_body"])
        task.settings = test_case["settings"]

        assert task._execute(test_case["github_body"]) is test_case["expected"]
