from task_interfaces import MetaTaskInterface, SubscriptionLevels


class Task(MetaTaskInterface):
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
            <= settings.get("max_changed_files", float("inf"))
            and github_body.get("pull_request", {}).get("additions", 0)
            <= settings.get("max_additions", float("inf"))
            and github_body.get("pull_request", {}).get("deletions", 0)
            <= settings.get("max_deletions", float("inf"))
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
