#!/usr/bin/env python3.6

# Note: Code was Developed in the Abasht Laboratory at the University of Delaware under
# the supervision of Dr. Behnam Abasht
# website: http://canr.udel.edu/faculty/behnam-abasht/


####################################Filtering_a_VCF_By_Chromosome######################################
#################################Code Written by M. Joseph Tomlinson IV########################################

# Code was written to extract a specific chromosome from a VCF. The program has two main files, a script file (Filter_for_Chromosomes.py)
# and a input paramter file called "Chromosome_Parameter_File.txt". A user first changes the parameter file to their specific inputs/outputs.
# Specifically, a user changes the input file name, desired output file name and the
# specific chromosome/chromosomes of interests, saving the newly changed paramter file without changing the name.

# Running of the Script
# The script can be run either locally using the standard "run" procedures of python
# or on a HCP server using the standard HPC UNIX run command of "python Filter_for_Chromosomes.py"
# on the command line or qsub file. Please note if the provided VCF file is HUGE, the python program cannot be run
# on a local computer and requires an HPC setting.  

# General Overview of How the Program Runs
# The program parses through the provided VCF file pulling out the header of the data and the specific data from
# the chromosomes of interest from the VCF file.

# Output from the Program
# The program outputs two files. The first file is a "VCF_General_Info.txt" file that includes general information
# about how many variants were in the VCF file and also how many datapoints were extracted for the specific chromosome/chromosomes
# of interest. The second file is the actual data of interest extracted from the VCF file, which is made up of the header of the
# data with the specific chromosome variants.

# Note: This is a general VCF parser script that was specifically developed to parse VCF files from GATK pipelines (Fall 2017)
# time period and if new styles of VCF files are introduced the code could break. 



############################Code to Parse the Parameter File################################################
#Definition splits up a line based on tab
#to return the input value from that line
def split_variable (line):
    key,value = line.split("\t")
    return (value)

#Put desired list of chromosomes into a python list
def get_chromosomes (desired_chromosomes):
    chromosomes = desired_chromosomes.split(",")
    return (chromosomes)

def read_parameter_file (input_file):
    file_parameters=[line.strip() for line in input_file]

    #Retrieve all the various lines of input (keys and values)---need to get just input parameters
    input_line_1=file_parameters[1]
    input_line_2=file_parameters[2]
    input_line_3=file_parameters[3]
    
    #Split the key, value pairs of information from the parameter file
    input_file_name = split_variable(input_line_1)
    output_file_name = split_variable(input_line_2)
    desired_chromosomes = split_variable(input_line_3)

    list_of_chromosomes=get_chromosomes(desired_chromosomes)
    
    return{'input_file':input_file_name, 'output_file':output_file_name, 'chromosomes':list_of_chromosomes}

#############################################################################################################


#Definition splits the data based on the tab
#to retrieve the data from the file (data is tab-delimited)
def split_data(line):
    line_variables=line.split("\t")
    return (line_variables)

#Function to opens up VCF and Parse Through VCF Results
#Retrieves the header and the actual data and skips all the extra
#information at the begining of the file
def vcf_file(file_name):
    with open (file_name) as vcf_file:
        vcf_data=[]
        header_info=[]
        for line in vcf_file:
            if line.startswith("##"): #extra information at begining of file
                pass
            elif line.startswith("#CHROM"): #retrieves file header
                header_info.append(line)
                #print (header_info[0])
                pass
            else: 
                vcf_data.append(line) #actual data from the file
                #print(axiom_data[0])
        vcf_file.close()
        return {'header':header_info, 'data':vcf_data}
        #returns the header and data


def main():

    #Opens the parameter file to get all the required inputs for the rest of the code
    input_file = open('Chromosome_Parameter_File.txt', 'r') #Open the file in python
    parameters=read_parameter_file(input_file) #Definition to parse through a file for parameters
    input_file.close() ####Close the intial file

    #Returning the actual values from the read_parameter_file function (slightly redundant but needed)
    input_file_name = parameters['input_file']
    output_file_name = parameters['output_file']
    chromosome_list=parameters['chromosomes']

    ###Parsing File VCF 
    vcf_data=vcf_file(input_file_name)
    vcf_header=(vcf_data['header'])
    
    vcf_chrom=open(output_file_name+".txt","w")
    
    vcf_chrom.write(vcf_header[0])

    vcf_SNP_data=(vcf_data['data'])

    #Find all Chromosomes That Match Input Parameter
    total_vcf_data=0
    chrom_data_point=0
    for x in range(len(vcf_SNP_data)):
        split_line=split_data(vcf_SNP_data[x])
        chromosome_of_SNP=split_line[0]
        for chromosome in chromosome_list:
            if chromosome_of_SNP == chromosome:
                vcf_chrom.write(vcf_SNP_data[x])
                total_vcf_data+=1
                chrom_data_point+=1
            else:
                pass
                total_vcf_data+=1

    vcf_chrom.close()

    vcf_info=open(output_file_name+"_VCF_General_Info.txt","w")
    vcf_info.write("The total number of ALL variants (SNPs and Indels) in file: " + str(total_vcf_data)+"\n")
    vcf_info.write("The total number of Mitochondrial variants: " + str(chrom_data_point))
    vcf_info.close()

main()        












