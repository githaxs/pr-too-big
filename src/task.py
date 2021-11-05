from task_interfaces import SubscriptionLevels
from task_interfaces import TaskInterface
from task_interfaces import TaskTypes


class Task(TaskInterface):
    """
    Checks Pull Requests are manageable for review.
    """

    name = "PR Too Big"
    slug = "pr-too-big"
    pass_text = ""
    fail_text = ""
    fail_summary = "This Pull Request has too many changes."
    subscription_level = SubscriptionLevels.FREE
    actions = [
        {
            "label": "Override",
            "identifier": "override",
            "description": "Allow exception for PR Too Big",
        }
    ]

    type = TaskTypes.WORKFLOW

    def execute(self, github_body, settings) -> bool:
        self.pass_summary = ""

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
            return True

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

    @property
    def pass_summary(self) -> str:
        return self._pass_summary

    @pass_summary.setter
    def pass_summary(self, pass_summary):
        self._pass_summary = pass_summary
