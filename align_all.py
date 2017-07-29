#!/usr/bin/env python
# Import packages
import argparse
import subprocess
import os

# Arguments
parser = argparse.ArgumentParser(description=
"****************************************************************************\n"
"STAR alignment with default parameters for all files in specified directory,"
" compressed FASTA files with R1(/R2).fq.gz extensions are expected\n"
"****************************************************************************")
parser.add_argument("cores", type = int, help="Number of cores used (Default = 2)", default=2)
parser.add_argument("genomeDir", help="Reference genome directory")
parser.add_argument("-v", "--verbose", action="store_true", help="Prints what is going on")
parser.add_argument("-w", "--workdir", action = "store", help = "Input directory",
                    default = os.getcwd())
parser.add_argument("-o", "--outdir", action = "store", help = "Output directory",
                    default = os.getcwd())
args = parser.parse_args()

# Main program
iniDir = os.getcwd()
dirFiles = os.listdir(iniDir)
R1files = [f for f in dirFiles if "R1.fq.gz" in f]

for file in R1files:
    read1 = file
    read2 = file.replace("R1.fq.gz", "R2.fq.gz")
    outPreffix = file.replace("R1.fq.gz", "")
    if args.verbose:
        print("{} alignment started...".format(outPreffix))
    subprocess.call("STAR --runMode alignReads "
                    "--runThreadN {} "
                    "--genomeDir {} "
                    "--readFilesCommand zcat "
                    "--readFilesIn {} {} "
                    "--outFileNamePrefix {} "
                    "--outSAMtype BAM SortedByCoordinate"
                    "".format(args.cores, args.genomeDir, read1, read2,
                              outPreffix), shell = True)
    if args.verbose:
        print("... alignment done!")

if args.verbose:
    print("All alignments done!!! :D")
