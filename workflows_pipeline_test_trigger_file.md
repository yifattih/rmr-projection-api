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
Cause: The job step in change of detecting the environment based on branch name was not writing the ENVIRONMENT value to the outputs.
Solution: added redirection to the ${GITHuB_OUTPUT} variable
