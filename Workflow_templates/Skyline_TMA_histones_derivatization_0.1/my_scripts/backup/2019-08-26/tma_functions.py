def create_modifications_dic(input_table):

    modifications_dic = {}

    for index, row in input_table.iterrows():
        mod1 = row["mod1"]
        if mod1 == None:
            mod1 = ""
        mod2 = row["mod2"]
        if mod2 == None:
            mod2 = ""

        modifications_dic[row["Mass"]] = {
           "mod1": mod1,
           "mod2": mod2,
           "natural_modification": row["natural modification"],
           "modification_name": row["Modification"],
           "abbreviation": row["Abbreviation"],
        }

    return modifications_dic


def create_enabled_sequences_dic(input_table):

    enabled_sequences_dic = {}

    for index, row in input_table.iterrows():
        if row["Protein Accession"] not in enabled_sequences_dic.keys():
            enabled_sequences_dic[row["Protein Accession"]] = {
                row["sequence"]: row["type"]
            }
        else:
            enabled_sequences_dic[row["Protein Accession"]][row["sequence"]] = row["type"]

    return enabled_sequences_dic


def get_sequences_from_fasta_file(fasta_path):
    f = open(fasta_path, "r")
    proteins = {}
    protein_accession = None
    for line in f:
        if (line[0] == ">"):
            arr = line.split("|")
            protein_accession = arr[1]
            protein_name = arr[2].split("\n")[0]
            proteins[protein_accession] = {
                "name": protein_name,
                "sequence": ""
            }
        else:
            proteins[protein_accession]["sequence"] += line.split("\n")[0]

    return proteins

def get_id_prefix_from_protein_name(protein_name):
    id_prefix = ""
    arr1 = protein_name.split("|")
    if len(arr1) >= 3:
        id_prefix = str(arr1[2].split("_")[0]) + "_"

    return id_prefix


