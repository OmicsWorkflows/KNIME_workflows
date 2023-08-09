
# CONSTANTS
# MODIF_TMA = "tma"

IMPORTANT_AMINOS = ["K"]  # old important aminos ["K", "S", "T", "Y", "R"]
NOT_COUNTABLE_AMINO_AT_FIRST_POSITION_IN_FASTA = "M"

LABEL_OVER_AMINOS = ["S", "T", "Y"]
LABEL_UNDER_AMINOS = ["K"]

LABEL_OK = "ok"
LABEL_UNDER = "under"
LABEL_OVER = "over"
LABEL_UNDEFINED = "undefined"
LABEL_ERROR = "error"

LABELS_PRIORITY = {
    LABEL_OK: 0,
    LABEL_OVER: 1,
    LABEL_UNDER: 2,
    LABEL_ERROR: 3,
}

SEQUENCE_RIGHT = "RS"
SEQUENCE_ASSIGNABLE = "AS"
SEQUENCE_WRONG = "WS"

DESIRED_OK = "desired"
DESIRED_COUNTABLE = "countable"
DESIRED_UNASSIGNABLE = "unassignable"

WITHOUT_MODIF_MASS = 0
UNKNOWN_MODIF_MASS = -1

##################################################################################################
##################################################################################################

class Amino:
    def __init__(self, amino_char):
        self.amino = amino_char
        self.mod1 = ""
        self.mod2 = ""
        self.mod1_natural_modification = False
        self.mod2_natural_modification = False
        self.natural_modification = False
        self.label = LABEL_UNDEFINED

    # def __str__(self):
    #     return str(pprint(self.get_data()))

    def __repr__(self):
        return str(self.get_data())

    def get_data(self):
        return vars(self)

    def set_modification_params(self, modif_params):
        self.mod1 = modif_params["mod1"]
        self.mod2 = modif_params["mod2"]
        self.mod1_natural_modification = modif_params["mod1_natural_modification"]
        self.mod2_natural_modification = modif_params["mod2_natural_modification"]
        self.natural_modification = self.mod1_natural_modification or self.mod2_natural_modification
        self.label_nterm = modif_params[self.amino + "_nterm"]
        self.label_other = modif_params[self.amino + "_other"]
        # if (modif_params["mass"] != WITHOUT_MODIF_MASS):
        #     print(self.amino + ": modif_params")
        #     print(modif_params)

    def modif_count(self):
        modif_count = 0
        if self.mod1 != "":
            modif_count += 1
        if self.mod2 != "":
            modif_count += 1
        return modif_count



#############################################################################
#############################################################################



class Sequence:
    def __init__(self, accession, sequence, proteins_dic, modifications_dic, fasta_initial_number="0"):
        self.accession = accession
        self.sequence_string = sequence
        self.proteins_dic = proteins_dic
        self.modifications_dic = modifications_dic
        self.fasta_initial_number = int(fasta_initial_number)
        self.errors = []

        self.sequence_array = self.sequence_to_array_of_amino_objects()
        self.n_term_old = self.check_n_term_old()
        self.n_term = self.check_n_term()
        self.first_amino_index = self.get_first_amino_index()
        self.all_amino_labels = self.get_all_amino_labels()

        self.set_amino_labels()
        self.label_old = self.get_sequence_label_old()
        self.label = self.get_sequence_label()

        self.sequence_correct = self.get_sequence_correct()

        self.desired = self.get_desired()

    def __repr__(self):
        return str(self.get_data())

    def get_data(self):
        return vars(self)

    def modification_params(self, mass):
        float_mass = float(mass)
        # print("mass: " + str(mass) + " -> " + str(float_mass))
        if float_mass in self.modifications_dic:
            return self.modifications_dic[float_mass]
        else:
            return self.modifications_dic[float(UNKNOWN_MODIF_MASS)]
            # return {
            #     "mod1": "unknown",
            #     "mod2": "",
            #     "natural_modification": False,
            # }

    def sequence_to_array_of_amino_objects(self):
        sequence_array = []
        modif_mass = ""
        modif_number_mode = False

        for char in self.sequence_string:
            if not modif_number_mode:
                if char != "[":
                    sequence_array.append(Amino(char))
                    sequence_array[len(sequence_array) - 1].set_modification_params(self.modification_params(WITHOUT_MODIF_MASS))
                else:
                    modif_number_mode = True
                    modif_mass = ""
            else:
                if char != "]":
                    modif_mass += char
                else:
                    modif_number_mode = False
                    sequence_array[len(sequence_array) - 1].set_modification_params(self.modification_params(modif_mass))


        return sequence_array


    def get_original_sequence(self):
        return self.sequence_string

    def get_sequence_without_modif(self):
        sequence = ""
        modif_number_mode = False

        for char in self.sequence_string:
            if not modif_number_mode:
                if char != "[":
                    sequence += char
                else:
                    modif_number_mode = True
            else:
                if char == "]":
                    modif_number_mode = False

        return sequence

    def get_sequence_with_modif(self):
        returned_sequence = ""
        for amino in self.sequence_array:

            returned_sequence += amino.amino + amino.mod1
            if amino.mod2 != "":
                returned_sequence += "_" + amino.mod2

        return returned_sequence


    def get_natural_modifications(self, amino):
        modifications = ""
        if amino.natural_modification == True:
            # if amino.mod1 != MODIF_TMA:
            if amino.mod1_natural_modification:
                modifications = amino.mod1
            # if amino.mod2 != "" and amino.mod2 != MODIF_TMA:
            if amino.mod2 != "" and amino.mod2_natural_modification:
                if modifications:
                    modifications += "_" + amino.mod2
                else:
                    modifications = amino.mod2
        return modifications


    def get_sequence_with_natural_modif(self):
        sequence = ""
        for index, amino in enumerate(self.sequence_array):
            sequence += amino.amino
            # if amino.amino in IMPORTANT_AMINOS:
            sequence += str(index + self.first_amino_index)
            sequence += self.get_natural_modifications(amino)

        return sequence


    def get_identificator(self):
        identificator = ""
        for index, amino in enumerate(self.sequence_array):
            natural_modifications = self.get_natural_modifications(amino)
            if amino.amino in IMPORTANT_AMINOS:
                identificator += amino.amino + str(index + self.first_amino_index) + natural_modifications
            elif natural_modifications:
                identificator += amino.amino + str(index + self.first_amino_index) + natural_modifications

        return identificator


    def get_protein_segment(self):
        first_k = None
        last_k = None
        for index, amino in enumerate(self.sequence_array):
            if amino.amino in IMPORTANT_AMINOS:
                if not first_k:
                    first_k = amino.amino + str(index + self.first_amino_index)
                else:
                    last_k = amino.amino + str(index + self.first_amino_index)

        protein_segment = ""
        if first_k:
            protein_segment += first_k
        if last_k:
            protein_segment += "-" + last_k

        return protein_segment


    def check_n_term_old(self):
        n_term = self.sequence_array[0]
        if n_term.amino == "K":
            return n_term.modif_count() == 2
        else:
            return n_term.modif_count() == 1

    def check_n_term(self):
        n_term = self.sequence_array[0]
        return n_term.label_nterm == LABEL_OK



    def set_amino_labels(self):
        for index, amino in enumerate(self.sequence_array):
            label = LABEL_OK
            if amino.amino in LABEL_UNDER_AMINOS:
                if index == 0:
                    if amino.modif_count() < 2:
                        label = LABEL_UNDER
                elif amino.modif_count() < 1:
                    label = LABEL_UNDER

            elif amino.amino in LABEL_OVER_AMINOS:
                # if amino.mod1 == MODIF_TMA:
                if not amino.mod1_natural_modification:
                    label = LABEL_OVER

            setattr(amino, "label", label)

        return True


    def get_all_amino_labels(self):
        all_amino_labels = ""
        for index, amino in enumerate(self.sequence_array):
            if index == 0:
                all_amino_labels += amino.label_nterm
            else:
                all_amino_labels += "," + amino.label_other
        return all_amino_labels


    def get_sequence_label_old(self):
        for amino in self.sequence_array:
            if amino.label != LABEL_OK:
                return amino.label

        return LABEL_OK


    def get_sequence_label(self):
        sequence_label = LABEL_OK
        for index, amino in enumerate(self.sequence_array):
            amino_label = amino.label_other
            if index == 0:
                amino_label = amino.label_nterm

            if LABELS_PRIORITY[amino_label] > LABELS_PRIORITY[sequence_label]:
                sequence_label = amino_label

        return sequence_label



    def get_first_amino_index(self):
        peptide_sequence = self.get_sequence_without_modif()
        if self.accession in self.proteins_dic.keys():
            protein_sequence = self.proteins_dic[self.accession]["sequence"]

            index = protein_sequence.find(peptide_sequence)
            if index >= 0:
                if (protein_sequence[0] == NOT_COUNTABLE_AMINO_AT_FIRST_POSITION_IN_FASTA):
                    return index + self.fasta_initial_number
                else:
                    return index + self.fasta_initial_number + 1
            else:
                self.errors.append("Peptide sequence is not found in protein sequence")
                return 0
        else:
            self.errors.append("Unknown protein accession")
            return 0



    def get_sequence_correct(self):
        peptide_sequence = self.get_sequence_without_modif()
        if self.accession in self.proteins_dic.keys():
            protein = self.proteins_dic[self.accession]

            if peptide_sequence in protein["enabled_sequences"].keys():
                return protein["enabled_sequences"][peptide_sequence].upper()

        return SEQUENCE_WRONG



    def get_desired(self):
        if self.sequence_correct == SEQUENCE_RIGHT:
            if self.label == LABEL_OK:
                return DESIRED_OK
            else:
                return DESIRED_COUNTABLE
        elif self.sequence_correct == SEQUENCE_ASSIGNABLE:
            return DESIRED_COUNTABLE
        elif self.sequence_correct == SEQUENCE_WRONG:
            return DESIRED_UNASSIGNABLE
        else:
            self.errors.append("Unknown value in column \"derired?\"")
            return DESIRED_UNASSIGNABLE


    def get_errors(self):
        errors_string = ""
        for error in self.errors:
            if not errors_string:
                errors_string = error
            else:
                errors_string += "; " + error

        return errors_string



##################################################################################################
##################################################################################################
