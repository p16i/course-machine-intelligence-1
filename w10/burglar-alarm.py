from bayesian.bbn import build_bbn


# burglar, earthquake, alarm, jonh, mary problem

def f_burglar(burglar):
    return 0.001 if burglar == 't' else 1-0.001

def f_earthquake(earthquake):
    return 0.002 if earthquake == 't' else 1-0.002

def f_alarm(alarm, burglar, earthquake):
    tabs = [ burglar, earthquake, alarm ]

    if tabs == ['t','t','t']:
        return 0.95
    elif tabs == ['t','t','f']:
        return 1-0.95
    elif tabs == ['t','f','t']:
        return  0.94
    elif tabs == ['t','f','f']:
        return  1-0.94
    elif tabs == ['f','t','t']:
        return 0.29
    elif tabs == ['f','t','f']:
        return 1 - 0.29
    elif tabs == ['f','f','t']:
        return 0.001
    elif tabs == ['f','f','f']:
        return 1-0.001

def f_john(john, alarm):
    tabs = [john, alarm]
    if tabs  == ['t','t'] :
        return 0.90
    elif tabs == ['t','f']:
        return 0.05
    elif tabs == ['f','t']:
        return 1-0.90
    elif tabs == ['f','f']:
        return 1-0.05

def f_mary(mary, alarm):
    tabs = [mary, alarm]
    if tabs  == ['t','t'] :
        return 0.70
    elif tabs == ['t','f']:
        return 0.01
    elif tabs == ['f','t']:
        return 1-0.70
    elif tabs == ['f','f']:
        return 1-0.01


if __name__ == '__main__':

    g = build_bbn(
        f_burglar,
        f_earthquake,
        f_alarm,
        f_john,
        f_mary,
        domains=dict(
            burglar=['t','f'],
            earthquake=['t','f'],
            alarm=['t','f'],
            john=['t','f'],
            mary=['t','f']
        )
    )

    g.q()

