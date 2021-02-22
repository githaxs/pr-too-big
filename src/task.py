from base_task import BaseTask


class Task(BaseTask):
    """
    Verifies the Title of a Pull Request matches a provided regex.
    """

    def _execute(self, github_body) -> bool:
        self.pass_text = ""

        return (
            github_body.get("pull_request", {}).get("changed_files", 0)
            <= self.settings.get("max_changed_files", float("inf"))
            and github_body.get("pull_request", {}).get("additions", 0)
            <= self.settings.get("max_additions", float("inf"))
            and github_body.get("pull_request", {}).get("deletions", 0)
            <= self.settings.get("max_deletions", float("inf"))
        )

    def _requested_action(self, github_body) -> bool:
        if github_body.get("requested_action").get("identifier") == "override":
            self.pass_text = "%s has overridden the original result" % github_body.get(
                "sender"
            ).get("login")
            return True
        return False

    def _get_task_name(self):
        return "PR Too Big"

    def _get_task_slug(self) -> str:
        return "pr-too-big"

    def _get_fail_summary(self) -> str:
        return "This pull request has too many changes."

    def _get_fail_text(self) -> str:
        return ""

    def _get_pass_summary(self) -> str:
        return ":+1:"

    def _get_pass_text(self) -> str:
        return self.pass_text

    def _get_actions(self):
        return [
            {
                "label": "Override",
                "identifier": "override",
                "description": "Allow exception for PR Too Big",
            }
        ]
