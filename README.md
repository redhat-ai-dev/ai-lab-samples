#  AI-lab samples

## Usage in ai-lab-template

This repository is being used in [ai-lab-template repository](https://github.com/redhat-ai-dev/ai-lab-template) as the Software Template source code for users to start with.

This repository is a copy of the AI Lab recipes source code under [ai-lab-recipes](https://github.com/containers/ai-lab-recipes/tree/main/recipes).

To contribute or make an update to these samples, open a Pull Request under [ai-lab-recipes](https://github.com/containers/ai-lab-recipes/tree/main/recipes). To pull in the latest changes to this repository, run `./pull-sample-app.sh`, and commit the changes.

You can then re-generate the Software Templates in [ai-lab-template](https://github.com/redhat-ai-dev/ai-lab-template) to use the latest AI samples from this repository.

## Usage in ai-lab-template-experiment

For the experimental Software Templates in [ai-lab-template-experiment](https://github.com/redhat-ai-dev/ai-lab-template-experiment), use the `experiment` branch. The [import-ai-lab-samples](https://github.com/redhat-ai-dev/ai-lab-template-experiment/blob/67c7d1b0c5ae9973f74d7d3bbeb849c442c214c7/scripts/import-ai-lab-samples#L4) script pulls in the sample applications from the `experiment` branch. The `experiment` branch is independent of other repositories and it is manually curated or maintained.
