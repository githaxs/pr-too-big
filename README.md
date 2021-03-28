# PR Too Big

> Making smaller pull requests is the #1 way to speed up your review time.

[Atlassian](https://www.atlassian.com/blog/git/written-unwritten-guide-pull-requests) and [Small Business Programming](https://smallbusinessprogramming.com/optimal-pull-request-size/) have made the case for using small pull requests to improve team efficiency and reduce errors.

PR Too Big will programatically enforce keeping pull requests small while also providing an override feature.

### Installation
To Install globally:

```yaml
# githaxs_settings/ghx.yml

pr-too-big:
  # install on all repos
  org: true
  org_settings:
    # Final settings cannot be overriden by repo specific settings
    final:
      max_changed_files: 10
      max_additions: 100
      max_deletions: 100
    # Default value if final and repo specific settings do not exist
    default:
      max_changed_files: 10
      max_additions: 100
      max_deletions: 100
  # install on select repos
  repos:
    - api-microservice
    - website
```

### Configuration
|parameter|description|required|default|
|---|---|---|---|
|max_changed_files| The maximum number of changed files in a pull request| no | 0 |
|max_additions| The maximum number of additions in a pull request as calculated by GitHub| no | 0 |
|max_deletions| The maximum number of deletions in a pull request as calculated by GitHub| no | 0 |

### Example Configuration
```yaml
# api-microservice/ghx.yml

pr-too-big:
  repo_settings:
    max_changed_files: 20
    max_additions: 200
    max_deletions: 200
```
