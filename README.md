# Filtering_a_VCF_By_Chromosome
Code to extract a specific chromosome or chromosomes from a VCF file

Note: Code was Developed in the Abasht Laboratory at the University of Delaware under the supervision of Dr. Behnam Abasht
website: "http://canr.udel.edu/faculty/behnam-abasht/"

####################################Filtering_a_VCF_By_Chromosome######################################
#################################Code Written by M. Joseph Tomlinson IV########################################

Code was written to extract a specific chromosome from a VCF. The program has two main files, a script file (Filter_for_Chromosomes.py)
and a input paramter file called "Chromosome_Parameter_File.txt". A user first changes the parameter file to their specific inputs/outputs.
Specifically, a user changes the input file name, desired output file name and the
specific chromosome/chromosomes of interests, saving the newly changed paramter file without changing the name.

# Running of the Script
The script can be run either locally using the standard "run" procedures of python
or on a HCP server using the standard HPC UNIX run command of "python Filter_for_Chromosomes.py"
on the command line or qsub file. Please note if the provided VCF file is HUGE, the python program cannot be run
on a local computer and requires an HPC setting.  

# General Overview of How the Program Runs
The program parses through the provided VCF file pulling out the header of the data and the specific data from
the chromosomes of interest from the VCF file.

# Output from the Program
The program outputs two files. The first file is a "VCF_General_Info.txt" file that includes general information
about how many variants were in the VCF file and also how many datapoints were extracted for the specific chromosome/chromosomes
of interest. The second file is the actual data of interest extracted from the VCF file, which is made up of the header of the
data with the specific chromosome variants.

# Note: This is a general VCF parser script that was specifically developed to parse VCF files from GATK pipelines (Fall 2017)
time period and if new styles of VCF files are introduced the code could break. 

####################################Files Provided in Repository#######################################################
Filter_for_Chromosomes.py (python script to run program)
Chromosome_Parameter_File.txt (paramter file that users change to change program inputs)

#Example Dataset to Run
Test_Dataset.txt (Test dataset for a user to try---simplified VCF file)

Test_Output.txt (example output file after filtering)
Test_Output_VCF_General_Info.txt (example overview file from program)
