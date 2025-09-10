# GitHub Actions Workflows Pipeline Testing Trigger File and Notes

## August-06-2025
File added for the first time.
This testing will compromise multiple actions runs, changes commits and pushes that do not add direct user value.
From this point on, commit history might get convoluted with lots of small fixes, changes, etc.
At this point, the first stable version of the app is finished and tested.
All changes that will be done will be related to infrastructure.

The api Cloud Run service was deleted to test the 'first_deploy' deployment strategy.

***Workflow failed***
Cause: The semantic-release action requires a Personal Access Token.
Solution: The token was created, added as secret named PAT to avoid conflicts with GITHUB_TOKEN vairbale, and added as environment variable in the workflow job.

***Workflow failed***
Note: semantic-release job succeed
Cause: The job step in charge of detecting the environment based on branch name was not writing the ENVIRONMENT value to the outputs.
Solution: added redirection to the ${GITHuB_OUTPUT} variable

Cause: Workflow did not run because of tags mismatch
Fix: cleaned up alpha.2 from changelog and deleted tag

Cause: The release was removed but not the tag and the semantic-release action failed
Fix: deleted tag

***Workflow failed***
Cause: The job step in charge of detecting the environment had a typo in the output name
Fix: The typo was removed. In addition, the release and release tags created

***Workflow failed***
Cause: client-payload needed quoting for valid json string
Fix: added quotes to all inputs

**Workflow is running now**
There is an error in infra repo workflow
This file will continue be used for testing


