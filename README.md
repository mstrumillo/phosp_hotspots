# phosp_hotspots

required knowledge:
alignment with domains cut out out of proteins
what pdb to map to (its sequence has to be in alignment)- its name and start of the domain
whats the domain
what are the phosphorylations
if theres regs/ active sites


required files:
alignment.ali
all_phosps
regulatory -------these two can be empty, but have to exist
active_sites------these two can be empty, but have to exist

how to prepare alignment.ali
its an alignment in ONE LINE fasta format, (https://www.biostars.org/p/9262/) with headers like 
>id; int domain_start; int domain_end
domain_start is necessary for correct phosphorylations assignment
eg
>FBpp0270092 pep:known chromosome:GCA_00 ;196;492
--------Y-EILEV----------------------------IGKG------
>NONE_15409 , MEDTR2G085200.1 ;134;418
--------F-EKLDK----------------------------IGQG------

how to prepare all_phosps
phospho file has to contain the protein id and the position, however script is set up to recognise pfam_scan.pl output which looks like this: 
SPECIES/ANIMALS/Celegans.phosp_output:Celegans, B0218.3, 191, T, PF00069.24, 35, 319, Pkinase
SPECIES/ANIMALS/Celegans.phosp_output:Celegans, B0218.3, 193, Y, PF00069.24, 35, 319, Pkinase
SPECIES/ANIMALS/Celegans.phosp_output:Celegans, B0545.1a, 533, S, PF00069.24, 375, 628, Pkinase
SPECIES/ANIMALS/Celegans.phosp_output:Celegans, B0545.1a, 534, T, PF00069.24, 375, 628, Pkinase
SPECIES/ANIMALS/Celegans.phosp_output:Celegans, B0545.1a, 538, T, PF00069.24, 375, 628, Pkinase
If this is not the case, correct line annotations are required in "phos_dataframe" fucntion

how to prepare regulatory
S, 742, P33981,
T, 312, P80192, 
T, 170, O00444, 
Y, 221, Q13164,
T, 260, Q8IWQ3,
T, 472, O00311,
is enough

how to prepare active
its the output of pfam_scan.pl, with the list of prediceted active sites at the end of line so: 
 A2ZVI7_8293     66    324     66    324 PF00069.24  Pkinase           Domain     1   264   264    245.8   4.3e-73   1 CL0016   predicted_active_site 211,189  
A3A2W5_8676     13    304     13    304 PF00069.24  Pkinase           Domain     1   264   264    227.6   1.6e-67   1 CL0016   predicted_active_site 157,138  
A3A2W5_8678     13    304     13    304 PF00069.24  Pkinase           Domain     1   264   264    227.6   1.6e-67   1 CL0016   predicted_active_site 157,138  


what variables to edit in 00.run_phosps_hotspots.py:
240 how_many_permuts=100####################HOW MANY PERMUTS (100 is the usual, but can be more or less)
229 pdb_name="PF00001_6fk7_A_55_306+55"##############thats the name that appears in alignment.ali + its start (thats how the columns named)


