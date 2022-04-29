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
    {
        "github_body": {"githaxs": {"full_event": "check_run.requested_action"}, "requested_action": {"identifier": "override"}, "sender": {"login": "foo"}},
        "settings": {},
        "expected": "foo has overridden the original result"
    }
]


def test():
    for test_case in test_cases:
        task = Task()
        settings = test_case["settings"]
        result = task.execute(test_case["github_body"], settings)
        assert result == test_case["expected"]
