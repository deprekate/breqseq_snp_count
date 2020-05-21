import sys
import os.path


def read_fasta(filepath):
	my_contigs = dict()
	name = ''
	seq = ''
	with open(filepath, mode="r") as my_file:
		for line in my_file:
			if(line.startswith(">")):
				my_contigs[name] = seq
				name = line.split()[0]
				seq = ''
			else:
				seq += line.replace("\n", "").upper()
		my_contigs[name] = seq

	if '' in my_contigs: del my_contigs['']
	return my_contigs

header_line = ''
flag = False
with open(sys.argv[1]) as fp:
	for line in fp:
		if line.startswith('     CDS             '):
			header_line = line.replace('CDS', '').strip()
			flag = False
		elif line.startswith('                     /locus_tag='):
			header_line = line.replace('/locus_tag=', '').replace('"', '').strip()
			flag = False
		elif line.startswith('                     /translation='):
			print(">", header_line, sep='')
			print(line.replace('/translation=', '').replace('"', ''). strip())
			flag = True
		elif line.startswith('                     /'):
			flag = False
		elif line.startswith('ORIGIN'):
			flag = False
		elif not line.startswith('                     '):
			flag = False
		elif flag:
			print(line.replace('"', '').strip())

