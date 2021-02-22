# PR Too Big

> Ensure all pull requests are manageable size for review

### Global Installation and Settings
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

### Local Installation and Settings

To configure repo specific settings:
```yaml
# api-microservice/ghx.yml

pr-too-big:
  repo_settings:
    max_changed_files: 20
    max_additions: 200
    max_deletions: 200
```
