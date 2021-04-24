#!/usr/bin/env python
###############################################################################################################
#
# MassGEM_Plot.py
# Author: Gao Yueyao
# Python 3.6.10
# Requires the following Python packages:
# numpy(=1.18.1), pandas(1.0.3), matplotlib(3.2.1), seaborn(0.10.1)
#
###############################################################################################################
#
# Import dependencies
#
###############################################################################################################
import datetime
import pandas as pd
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as plt
import seaborn as sns
import argparse
###############################################################################################################
#
#Description of script
#
###############################################################################################################

parser = argparse.ArgumentParser(description="""
MassGEM_Plot takes a gene expression matrix (GEM) and a specific gene list.
This script returns the visualization of individual gene expression from the
requested genelist.""")

###############################################################################################################
#
# Required arguments
#
###############################################################################################################
parser.add_argument('-emx','--expression',dest='gene_expression_matrix',action='store',required=True,help="""
User input expression matrix (csv format)""")
parser.add_argument('-mega','--megainfo',dest='mega_info',action='store',required=True,help="""
User input sample mega info (csv format)""")
parser.add_argument('-genelist','--genelist',dest='genelist',action='store',required=True,help="""
User input gene list (txt format)""")
parser.add_argument('-smpl','--narg',nargs='+',dest='label_list',action='store',required=True,help="""
User input sample list""")
parser.add_argument('-o','--output_prefix',dest='output_prefix',action='store',required=True,help="""
User input sample list""")
args = parser.parse_args()

# Process the input infos
Input_emx = pd.read_csv(args.gene_expression_matrix,index_col='gene')
Mega_info = pd.read_csv(args.mega_info,index_col='sample')
input_genelist = pd.read_csv(args.genelist,sep='\t',header=None)[0].tolist()
Label_list = args.label_list
print('Label list are valid: ',Label_list)
print('MassGEM_Plot will generate the Plots based on the input gene list and label list')

# Merge the Mega file and expression matrix into a DF for plotting 
Input_emx_trans = Input_emx.transpose()
Plot_expDF = pd.concat([Input_emx_trans,Mega_info],axis=1)

# Grep the plotting df based on user input gene list and label list
def Grep_DF(GeneList,LabelList):
    SortedDF = Plot_expDF[GeneList+["Label","TimePoint"]]
    Selected_SortedDF = SortedDF[SortedDF["Label"].isin(LabelList)]
    return(Selected_SortedDF)

# Create the PdfPages object to which we will save the pages:
# The with statement makes sure that the PdfPages object is closed properly at
# the end of the block, even if an Exception occurs.
def PdfPlot(Plot_Name,GeneList,Expression_DF):
    with PdfPages(Plot_Name) as pdf:
        
        for geneID in GeneList:
            fig = plt.figure(figsize=(8,6))
            ax = fig.add_axes((0.1, 0.2, 0.8, 0.7))
            ax = sns.lineplot(x="TimePoint", y=geneID,markers=True,dashes=False,hue="Label",data=Expression_DF,palette="Set2",lw=1.8)
            plt.title(geneID,fontsize=15)
            ax.set_ylabel('Gene Expression')
            # Shrink current axis by 1%
            box = ax.get_position()
            ax.set_position([box.x0, box.y0, box.width * 0.90, box.height])
            # # Put a legend to the right of the current axis
            ax.legend(loc='center left', bbox_to_anchor=(1, 0.5))
            pdf.savefig()  # saves the current figure into a pdf page
            plt.close()

        d = pdf.infodict()
        d['Title'] = Plot_Name
        d['Subject'] = Plot_Name
        d['Keywords'] = Plot_Name
        d['CreationDate'] = datetime.datetime.now()
        d['ModDate'] = datetime.datetime.today()
        
    return(pdf)
 
PdfPlot('{}_MassGEM_plots.pdf'.format(args.output_prefix),input_genelist,Grep_DF(input_genelist,Label_list))
 

 


 
