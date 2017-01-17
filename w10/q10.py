from bayesian.bbn import build_bbn

def f_burglar(burglar):
    return 0.01 if burglar == 't' else 1-f_burglar('t')

def f_earthquake(earthquake):
    return 0.000001 if earthquake == 't' else 1- f_earthquake('t')

def f_alarm(alarm, burglar, earthquake):
    tabs = [ burglar, earthquake, alarm ]

    if tabs == ['t','t','t']:
        return 0.98
    elif tabs == ['t','t','f']:
        return 1-f_alarm('t','t','t')
    elif tabs == ['t','f','t']:
        return  0.95
    elif tabs == ['t','f','f']:
        return  1-f_alarm('t','f','t')
    elif tabs == ['f','t','t']:
        return 0.41
    elif tabs == ['f','t','f']:
        return 1 - f_alarm('f','t','t')
    elif tabs == ['f','f','t']:
        return 0.001
    elif tabs == ['f','f','f']:
        return 1 - f_alarm('f','f','t')

def f_radio(earthquake, radio):
    tabs = [ earthquake, radio ]

    if earthquake == radio :
        return 1
    else:
        return 0

if __name__ == '__main__':

    g = build_bbn(
        f_burglar,
        f_earthquake,
        f_alarm,
        f_radio,
        domains=dict(
            burglar=['t','f'],
            earthquake=['t','f'],
            alarm = ['t','f'],
            radio=['t','f']
        )
    )

    g.q()
