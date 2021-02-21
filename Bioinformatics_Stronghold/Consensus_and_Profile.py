# Use multi_fasta() for reading the sequence
# Pass multi_fasta("roslainf_file.txt") as the argument to profile_matrix function
# Pass profile_matrix(multi_fasta("roslainf_file.txt")) to consensus function

def multi_fasta(fasta_file):
    file = open(fasta_file, "r")
    reading = file.readlines()
    file.close()
    
    sequence = []
    seqs = ""
    
    for dna_seq in reading:
        if not dna_seq.startswith(">"):
            dna_seq = dna_seq.replace(" ", "")
            dna_seq = dna_seq.replace("\n", "")
            seqs += dna_seq
            
        else:
            sequence.append(seqs)
            seqs = ""
            
    sequence.append(seqs)
    return [read for read in sequence if read != ""]



def profile_matrix(seq):
    sequences = [seqs for seqs in seq if ">" not in seqs]
    counter = {"A": [], "C": [], "G": [], "T": []}

    for rows in range(0, len(sequences[0])):
        A = 0
        T = 0
        G = 0
        C = 0

        for columns in range(0, len(sequences)):
            if sequences[columns][rows] == "A":
                A += 1

            elif sequences[columns][rows] == "T":
                T += 1

            elif sequences[columns][rows] == "G":
                G += 1

            else:
                C += 1

        counter["A"].append(A)
        counter["C"].append(C)
        counter["G"].append(G)
        counter["T"].append(T)
    
    new_counter = {key: str(values).replace(",", " ") for key, values in counter.items()}
        
    return new_counter

# The result from this function needs some manual modifications before submittion 
# Remove any [, ] or '. then copy and paste the result.

def consensus(profile):
    new_seq = ""
    old_dict = {key: [int(num) for num in values if num not in "[] "] for key, values in profile.items()}
    profiles = [ls for ls in old_dict.values()]

    for i in range(0, len(profiles[0])):
        my_index = []
        for lists in profiles:
            my_index.append(lists[i])

        position = my_index.index(max(my_index))

        if position == 0:
            new_seq += "A"

        elif position == 1:
            new_seq += "C"

        elif position == 2:
            new_seq += "G"

        else: 
            new_seq += "T"
            
    return new_seq
