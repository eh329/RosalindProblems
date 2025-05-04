def probability_of_dominant_allele(k, m, n):
    """
    Calculate the probability of offspring having at least one dominant allele.
    
    Args:
        k (int): Number of homozygous dominant individuals (AA)
        m (int): Number of heterozygous individuals (Aa)
        n (int): Number of homozygous recessive individuals (aa)
        
    Returns:
        float: Probability of offspring having at least one dominant allele
    """
    # Total population
    total = k + m + n
    
    # The key to this problem is to correctly calculate:
    # 1. The probability of selecting each possible mating pair
    # 2. The probability that each pair produces an offspring with a dominant allele
    
    # Calculate the probability of selecting each pair type
    # Note: For each pair, we're selecting WITHOUT replacement
    
    # 1. AA × AA: Both homozygous dominant
    p_AA_AA = (k/total) * ((k-1)/(total-1))
    
    # 2. AA × Aa: Homozygous dominant and heterozygous
    # We can select either one first, so multiply by 2
    p_AA_Aa = 2 * (k/total) * (m/(total-1))
    
    # 3. AA × aa: Homozygous dominant and homozygous recessive
    # We can select either one first, so multiply by 2
    p_AA_aa = 2 * (k/total) * (n/(total-1))
    
    # 4. Aa × Aa: Both heterozygous
    p_Aa_Aa = (m/total) * ((m-1)/(total-1))
    
    # 5. Aa × aa: Heterozygous and homozygous recessive
    # We can select either one first, so multiply by 2
    p_Aa_aa = 2 * (m/total) * (n/(total-1))
    
    # 6. aa × aa: Both homozygous recessive
    p_aa_aa = (n/total) * ((n-1)/(total-1))
    
    # Probability that offspring has at least one dominant allele for each pair type
    
    # AA × AA: 100% dominant (all offspring AA)
    prob_dominant_AA_AA = 1.0
    
    # AA × Aa: 100% dominant (half AA, half Aa)
    prob_dominant_AA_Aa = 1.0
    
    # AA × aa: 100% dominant (all Aa)
    prob_dominant_AA_aa = 1.0
    
    # Aa × Aa: 75% dominant (25% AA, 50% Aa, 25% aa)
    prob_dominant_Aa_Aa = 0.75
    
    # Aa × aa: 50% dominant (50% Aa, 50% aa)
    prob_dominant_Aa_aa = 0.5
    
    # aa × aa: 0% dominant (all aa)
    prob_dominant_aa_aa = 0.0
    
    # Total probability = sum of (probability of pair × probability offspring has dominant allele)
    total_probability = (
        p_AA_AA * prob_dominant_AA_AA +
        p_AA_Aa * prob_dominant_AA_Aa +
        p_AA_aa * prob_dominant_AA_aa +
        p_Aa_Aa * prob_dominant_Aa_Aa +
        p_Aa_aa * prob_dominant_Aa_aa +
        p_aa_aa * prob_dominant_aa_aa
    )
    
    return round(total_probability, 5)
