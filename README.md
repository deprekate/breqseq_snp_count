e breseq_tools


## snp_count
A script to count the number of SPSs per gene

Example

Run on included sample data:
```sh
$ python3 count_snps.py index.html | head
GENE	SNPS
AMNIBMGE_00001	28.0
intergenic	335
AMNIBMGE_00003	11.0
AMNIBMGE_00004	6.0
AMNIBMGE_00006	13.0
AMNIBMGE_00007	1.0
AMNIBMGE_00008	10.0
AMNIBMGE_00009	44.0
AMNIBMGE_00010	3.0
```


## mask_false_positives
A script to remove the SNPs already present at timepoint zero from subsequent later timepoints

Example

Run on included sample data:
```sh
$ python3 mask_false_positves.py FALSE_POSITVE_DIR TO_BE_MASKED_DIR

```
