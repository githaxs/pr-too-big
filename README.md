# Title Lint

> Ensure all pull requests follow a standard naming convention

Following a standard naming convention on Pull Requests.

Useful for linking Jira tickets to Pull Requests or following Conventional Commit messaging.

### Installation
To Install globally:

```yaml
# githaxs_settings/ghx.yml

title-lint:
  # install on all repos
  org: true
  # install on select repos
  repos:
    - api-microservice
    - websiteservice
```

Or add a configuration block in the repo itself, see configuration section below.

### Configuration

The following parameters can be set locally or globally:
- regex


To configure global settings:

```yaml
# githaxs_settings/ghx.yml

title-lint:
  org_settings:
    # Cannot be overriden by repo specific settings
    final:
      regex: "[A-Z]+-[0-9]+"
    # Default value if repo specific settings do not exist
    default:
      regex: "[A-Z]+-[0-9]+"
```

To configure repo specific settings:
```yaml
# api-microservice/ghx.yml

title-lint:
  repo_settings:
    regex: "fix|feat: .*"
```
