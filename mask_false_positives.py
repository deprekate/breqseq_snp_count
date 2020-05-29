#!/usr/bin/env python3

import os
import sys
import pandas as pd



if len(sys.argv) < 3:
	print("usage: python3 mask_false_positives.py OUTPUT_FOLDER_0 OUTPUT_FOLDER_X")
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
# read in timepoint zero to get false positives already present in the population

html_table_pd = pd.read_html(sys.argv[1] + 'index.html', header=1, encoding='utf-8')[0]

false_positives = dict()

for index, row in html_table_pd.iterrows():
	if pd.isna(row['position']):
		continue
	else:
		false_positives[row['position']] = row['annotation']

#-------------------------------------------------------------------------------------------------#
# read in timepoint zero to get false positives already present in the population

def remove_html_markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
            if c == '<' and not quote:
                tag = True
            elif c == '>' and not quote:
                tag = False
            elif (c == '"' or c == "'") and tag:
                quote = not quote
            elif not tag:
                out = out + c
    return out.rstrip()

row_html = ''
row_name = None
with open(sys.argv[2] + 'index.html', 'r') as fp, open(sys.argv[2] + 'index_temp.html', 'w') as outfile:
	for line in fp:
		if line.startswith('.polymorphism_table_row'):
			outfile.write(line)
			outfile.write('.polymorphism_table_row_bad {background-color: rgb(255,0,0); text-decoration: line-through;}\n')
		elif line.startswith('<!-- Print The Table Row -->'):
			row_html += line
		elif line.startswith('<!-- End Table Row -->'):
			row_html += line
			outfile.write(row_html)
			row_html = ''
		elif line.endswith('<!-- Position -->\n'):
			row_html += line
			if remove_html_markup(line).replace(',', '') in false_positives:
				row_html = row_html.replace('polymorphism_table_row', 'polymorphism_table_row_bad')
		elif row_html:
			row_html += line
		else:
			outfile.write(line)

os.rename(sys.argv[2] + 'index.html', sys.argv[2] + 'index_original.html')
os.rename(sys.argv[2] + 'index_temp.html', sys.argv[2] + 'index.html')
			


'''
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

'''
