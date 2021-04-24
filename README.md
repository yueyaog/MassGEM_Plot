# MassGEM_Plot
This repository is designed to visualize the expression of a large amount of genes as mutiple line plots and save them to a mutipage pdf.
## Motivation
Accurate detection of differentially expressed genes (DEGs) is not a travial task. Although there are visualization methods to present the expressions of a large amount of genes at the same time, biases introduced in normalization, scaling transformation, and replicate variability. So most researchers conduct careful 'eyeball' inspection to curate a reliable set of DEGs. This process can be time consuming and perhaps frustrating for most researchers. With MassGEM_Plot, you don't need to copy and paste to check gene expression line plot one by one any more. MassGEM_Plot takes a user input Gene Expression Matrix (GEM) and a user specified gene list to generate all the gene expression line plots you want at the same time. 
## Installation
All of MassGEM_Plot's dependencies can be installed through Anaconda3. The following installation commands are specified to create an Anaconda environment using Clemson's Palmetto cluster. But the dependencies can be easily install to any HPC system or even your own laptop! 
```
module load anaconda3/5.1.0-gcc/8.3.1

conda create -n MassGEM_Plot python=3.6 matplotlib numpy pandas seaborn
```
Once the anaconda environment has been created, you need to activate your environment to use MassGEM_Plot:
```
conda activate MassGEM_Plot
```
After that, simply clone MassGEM_Plot repository to use MassGEM_Plot
```
git clone https://github.com/yueyaog/MassGEM_Plot.git
```



