from base_task import BaseTask


class Task(BaseTask):
    """
    Verifies the Title of a Pull Request matches a provided regex.
    """

    def _execute(self, github_body) -> bool:
        return (
            github_body.get("pull_request", {}).get("changed_files", 0)
            <= self.settings.get("max_changed_files", float("inf"))
            and github_body.get("pull_request", {}).get("additions", 0)
            <= self.settings.get("max_additions", float("inf"))
            and github_body.get("pull_request", {}).get("deletions", 0)
            <= self.settings.get("max_deletions", float("inf"))
        )

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
        return ""

    def _get_actions(self):
        return None
