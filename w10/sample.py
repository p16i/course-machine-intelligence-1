from bayesian.bbn import build_bbn


def f_prize_door(prize_door):
    return 0.33333333


def f_guest_door(guest_door):
    return 0.33333333


def f_monty_door(prize_door, guest_door, monty_door):
    print prize_door
    if prize_door == guest_door:  # Guest was correct!
        if prize_door == monty_door:
            return 0     # Monty never reveals the prize
        else:
            return 0.5   # Monty can choose either goat door
    elif prize_door == monty_door:
        return 0         # Again, Monty wont reveal the prize
    elif guest_door == monty_door:
        return 0         # Monty will never choose the guest door
    else:
        # This covers all case where
        # the guest has *not* guessed
        # correctly and Monty chooses
        # the only remaining door that
        # wont reveal the prize.
        return 1


if __name__ == '__main__':

    g = build_bbn(
        f_prize_door,
        f_guest_door,
        f_monty_door,
        domains=dict(
            prize_door=['A', 'B', 'C'],
            guest_door=['A', 'B', 'C'],
            monty_door=['A', 'B', 'C']))

    g.q()
