from Exceptions import InvalidOperatorPlacement, InvalidMultipleDots

def is_operand(token):
    """Check if a token is an operand (a number)."""
    if token.count('.') > 1:
        raise InvalidMultipleDots("Cannot have more than one '.' in a number.")
    try:
        float(token)
        return True
    except ValueError:
        return False

def resolve_sign_streak(streak):
    """
    Resolve a streak of '-' and '~' into a single effective sign or None.

    Rules:
    - A single tilde (`~`) flips the sign.
    - Odd number of minuses (`-`) results in a negative sign (`unary_minus`).
    - Even number of minuses results in no effect (neutral).
    - Tilde and minus can combine, e.g., `~--3` is valid.
    - Consecutive tildes (`~~3`) are invalid and raise an exception.
    """
    if not streak:
        return None

    tilde_count = streak.count('~')
    minus_count = streak.count('-')

    # Validation: No more than one tilde allowed in a streak
    if tilde_count > 1:
        raise InvalidOperatorPlacement("Invalid sequence of consecutive tildes.")

    # Resolve tilde and minus combination
    if tilde_count == 1:
        if minus_count == 0:
            return '~'
        # A tilde flips the result of the minuses
        if streak[0] != '~':
            raise InvalidOperatorPlacement("Tilde can only be after an operator.")

        if minus_count % 2 == 0:
            return '-'  # Tilde results in unary minus
        return None  # Tilde and odd minuses cancel out (neutral)

    # No tilde, resolve minuses only
    if minus_count % 2 == 1:
        return '-'  # Odd number of minuses
    return None  # Neutral (even number of minuses)

def attach_unary_minus(precedence, stack, token):
    """Check if unary minus should attach based on precedence."""
    if token == 'unary_minus' and stack[-1] == 'unary_minus':
        return False
    return precedence[stack[-1]] >= precedence[token]
