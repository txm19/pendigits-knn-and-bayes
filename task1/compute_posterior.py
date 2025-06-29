import sys
from decimal import Decimal, getcontext, ROUND_HALF_UP

# Set decimal precision high enough for internal calculations
getcontext().prec = 8

# Helper function to round and format to 5 decimal places
def format_decimal(val):
    return str(val.quantize(Decimal('0.00001'), rounding=ROUND_HALF_UP))

# -------------------------
# Task 1: Posterior Probabilities
# -------------------------

def compute_posterior(observation_sequence):
    hypotheses = {
        'h1': {'prior': Decimal('0.1'), 'C': Decimal('1.0'), 'L': Decimal('0.0')},
        'h2': {'prior': Decimal('0.2'), 'C': Decimal('0.75'), 'L': Decimal('0.25')},
        'h3': {'prior': Decimal('0.4'), 'C': Decimal('0.5'), 'L': Decimal('0.5')},
        'h4': {'prior': Decimal('0.2'), 'C': Decimal('0.25'), 'L': Decimal('0.75')},
        'h5': {'prior': Decimal('0.1'), 'C': Decimal('0.0'), 'L': Decimal('1.0')}
    }

    result = []
    Q = observation_sequence
    result.append(f"Observation sequence Q: {Q}")
    result.append(f"Length of Q: {len(Q)}\n")

    result.append("Before Observations :")
    for h in ['h1', 'h2', 'h3', 'h4', 'h5']:
        result.append(f"P({h}) = {format_decimal(hypotheses[h]['prior'])}")

    # Compute initial next candy probabilities
    p_C = sum(hypotheses[h]['prior'] * hypotheses[h]['C'] for h in hypotheses)
    p_L = sum(hypotheses[h]['prior'] * hypotheses[h]['L'] for h in hypotheses)

    result.append(f"\nProbability that the next candy we pick will be C, given Q: {format_decimal(p_C)}")
    result.append(f"Probability that the next candy we pick will be L, given Q: {format_decimal(p_L)}\n")

    posteriors = {h: hypotheses[h]['prior'] for h in hypotheses}

    for i, obs in enumerate(Q):
        updated_posteriors = {}
        normalization_constant = sum(posteriors[h] * hypotheses[h][obs] for h in hypotheses)

        for h in hypotheses:
            updated_posteriors[h] = (posteriors[h] * hypotheses[h][obs]) / normalization_constant if normalization_constant != 0 else Decimal('0')

        posteriors = updated_posteriors

        result.append(f"After Observation {i+1} = {obs}:")
        for h in ['h1', 'h2', 'h3', 'h4', 'h5']:
            result.append(f"P({h} | Q) = {format_decimal(posteriors[h])}")

        # Compute updated next candy probabilities
        p_C = sum(posteriors[h] * hypotheses[h]['C'] for h in hypotheses)
        p_L = sum(posteriors[h] * hypotheses[h]['L'] for h in hypotheses)

        result.append(f"\nProbability that the next candy we pick will be C, given Q: {format_decimal(p_C)}")
        result.append(f"Probability that the next candy we pick will be L, given Q: {format_decimal(p_L)}\n")

    with open("result.txt", "w") as f:
        f.write("\n".join(result))


# -------------- Run from Command Line ----------------

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        compute_posterior(sys.argv[1])
    else:
        compute_posterior("")  # No observations case
