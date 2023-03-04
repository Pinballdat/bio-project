import os
import pandas as pd

folder = input("Let's enter Quast folder:")
# folder = "C:/Users/Admin/Desktop/AD_quast/Quast_not_trim_China"

list_fd = []
for f in os.listdir(str(folder)):
  list_fd.append("%s/%s"%(folder,f))

Assembly = []
Numbers_of_contigs = {}
Largest_contig = {}
Total_length = {}
Genome_fraction = {}
Misassemblies = {}
Complete_genes = {}
for l in list_fd:
  open_files= open("%s/report.tsv"%(l))
  content = open_files.read().split("\n")
  Assembly.append(content[0].split("\t")[1])
  for c in content:
    if c.find("# contigs\t") != -1:
      Numbers_of_contigs[content[0].split("\t")[1]] = int(c.split("\t")[1])
    if c.find("Largest contig") != -1:
      Largest_contig[content[0].split("\t")[1]] = int(c.split("\t")[1])
    if c.find("Total length\t") != -1:
      Total_length[content[0].split("\t")[1]] = int(c.split("\t")[1])
    if c.find("Genome fraction") != -1:
      Genome_fraction[content[0].split("\t")[1]] = float(c.split("\t")[1])
    if c.find("# misassemblies\t") != -1:
      Misassemblies[content[0].split("\t")[1]] = int(c.split("\t")[1])
    if c.find("genomic feature") != -1:
      Complete_genes[content[0].split("\t")[1]] = int(c.split("\t")[1].split(" + ")[0])
      


d = {"Number of contigs": pd.Series(Numbers_of_contigs, Numbers_of_contigs.keys()), "Largest contig": pd.Series(Largest_contig, Largest_contig.keys()), "Total length": pd.Series(Total_length, Total_length.keys()), "Genome fraction": pd.Series(Genome_fraction, Genome_fraction.keys()), "Complete genes": pd.Series(Complete_genes, Complete_genes.keys()), "Misassemblies": pd.Series(Misassemblies, Misassemblies.keys())}
df = pd.DataFrame(data=d, index=Assembly)
print(df)

  
