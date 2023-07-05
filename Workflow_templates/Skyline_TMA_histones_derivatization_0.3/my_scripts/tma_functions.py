# def create_modifications_dic(input_table):
#
#     modifications_dic = {}
#
#     for index, row in input_table.iterrows():
#         # mod1 = row["mod1"]
#         # if mod1 == None:
#         #     mod1 = ""
#         # mod2 = row["mod2"]
#         # if mod2 == None:
#         #     mod2 = ""
#
#         print(row["mass"])
#         mass = float(row["mass"])
#         modifications_dic[mass] = {}
#         for col in row.keys():
#             modifications_dic[mass][col] = row[col] or ""
#         # {
#         #    "mod1": mod1,
#         #    "mod2": mod2,
#         #    "natural_modification": row["natural modification"],
#         #    "modification_name": row["Modification"],
#         #    "abbreviation": row["Abbreviation"],
#         #
#         # }
#
#     return modifications_dic


# def create_enabled_sequences_dic(input_table):
#
#     enabled_sequences_dic = {}
#
#     for index, row in input_table.iterrows():
#         if row["Protein Accession"] not in enabled_sequences_dic.keys():
#             enabled_sequences_dic[row["Protein Accession"]] = {
#                 row["sequence"]: row["type"]
#             }
#         else:
#             enabled_sequences_dic[row["Protein Accession"]][row["sequence"]] = row["type"]
#
#     return enabled_sequences_dic
import re


def get_sequences_from_fasta_file(fasta_path):
    f = open(fasta_path, "r")
    proteins = {}
    protein_accession = None
    lines = f.read().splitlines()
    for line in lines:
        if (line and line[0] == ">"):
            arr = line.split("|")
            protein_accession = arr[1]
            protein_name = arr[2]
            proteins[protein_accession] = {
                "name": protein_name,
                "sequence": "",
                "enabled_sequences": {},
            }
        else:
            proteins[protein_accession]["sequence"] += line

    return proteins

# def get_id_prefix_from_protein_name(protein_name):
#     id_prefix = ""
#     arr1 = protein_name.split("|")
#     if len(arr1) >= 3:
#         id_prefix = str(arr1[2].split("_")[0]) + "_"
#
#     return id_prefix
#
# def get_id_prefix_from_protein_name_by_regex(protein_name, regex):
#     if regex:
#         match = re.search(regex, protein_name)
#         if match:
#             print("match:")
#             print(match.group())
#             print(match.groups())
#             print(match[0])
#             print(match[1])
#             return match[1]
#     return ""

