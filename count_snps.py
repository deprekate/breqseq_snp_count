#!/usr/bin/env python3

import sys
import pandas as pd



if len(sys.argv) < 2:
	print("usage: python3 count_snps.py INDEX.HTML")
	exit()


#-------------------------------------------------------------------------------------------------#
'''
flag = False
html_table_text = ''

with open(sys.argv[1]) as fp:
	for line in fp:
		if not flag and line.startswith("<!--Output Html_Mutation_Table_String-->"):
			flag = True
		elif flag and line.startswith("</table>"):
			html_table_text += line
			flag = False
		elif flag:
			html_table_text += line
html_table_pd = pd.read_html(html_table_text)
'''
#-------------------------------------------------------------------------------------------------#

html_table_pd = pd.read_html(sys.argv[1], header=1, encoding='utf-8')[0]

gene_snp_counts = dict()

for index, row in html_table_pd.iterrows():
	if pd.isna(row['annotation']):
		continue
	elif 'intergenic' in row['annotation']:
		gene_snp_counts['intergenic'] = gene_snp_counts.get('intergenic', 0) + 1
	else:
		row['gene'] = row['gene'].encode('ascii', 'xmlcharrefreplace').decode()\
									      .replace('&#8594;', '')\
									      .replace('&#8592;', '')\
									      .replace('&#160;', ' ')
		gene_names = row['gene'].split()
		for name in gene_names:
			gene_snp_counts[name] = gene_snp_counts.get(name, 0) + 1/len(gene_names)


print('GENE', 'SNPS', sep='\t')
for key, value in gene_snp_counts.items():
	print(key, value, sep='\t')
