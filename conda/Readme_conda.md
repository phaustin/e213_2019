See https://conda.io/docs/user-guide/tasks/manage-environments.html#create-env-from-file


1. To export a conda environment (say e213) that works on both windows and macs

      conda env export -n e213 --no-builds > e213_env.yml

1. To use this environment on your computer

      conda env create -f e213_env.yml

