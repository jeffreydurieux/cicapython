# Clusterwise ICA

## TODO:

* convergence criteria
* functions to load nifti data into array/dict (nilearn module)
* functions that exports Sr spatial maps to nifti



### Algorithm steps:

1. randomP (or user defined clustering)
while(loss no longer decreases):
2. split_concatenate (split data and concatenate based on P)
3. groupicas (apply ICA on concatenated matrices)
4. reestimateP (reestimate clustering)
