from task_interfaces import WorkflowTask, SubscriptionLevels
from typing import List, Dict

class Task(WorkflowTask):
    """
    Checks Pull Requests are manageable for review.
    """
    name: str = "PR Too Big"
    subscription_level: int = SubscriptionLevels.FREE
    actions: List[Dict] = [
        {
            "label": "Override",
            "identifier": "override",
            "description": "Allow exception for PR Too Big",
        }
    ]


    def execute(self, github_body, settings) -> bool:
        # A manual override has been requested
        if (
            github_body.get("githaxs", {}).get("full_event")
            == "check_run.requested_action"
            and github_body.get("requested_action", {}).get("identifier", "")
            == "override"
        ):
            self.actions = None
            self.pass_summary = (
                "%s has overridden the original result"
                % github_body.get("sender").get("login")
            )
            return self.pass_summary

        # Normal use case
        status = (
            github_body.get("pull_request", {}).get("changed_files", 0)
            <= (int(settings.get("max_changed_files", "0")) or float("inf"))
            and github_body.get("pull_request", {}).get("additions", 0)
            <= (int(settings.get("max_additions", "0")) or float("inf"))
            and github_body.get("pull_request", {}).get("deletions", 0)
            <= (int(settings.get("max_deletions", "0")) or float("inf"))
        )

        if status:
            self.actions = None

        return status