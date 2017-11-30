import sys, re
from Bio.Align.Applications import ClustalwCommandline
from Bio import AlignIO

input_fa = sys.argv[1]
output_aln = input_fa +".aln"
output_fa = output_aln + '.fa' 

cmd = ClustalwCommandline('clustalw2', infile=input_fa, outfile=output_aln)

stdout, stderr = cmd()

align = AlignIO.read(output_aln, 'clustal')

AlignIO.write(align, output_fa, 'fasta')

