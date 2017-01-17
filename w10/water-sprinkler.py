from bayesian.bbn import build_bbn

# http://people.cs.ubc.ca/~murphyk/Bayes/bnintro.html


def f_cloudy( cloudy ):
    return 0.5

def f_sprinkler( cloudy, sprinkler ):
    tabs = [ cloudy, sprinkler ]

    if tabs == ['t','t']:
        return 0.1
    elif tabs == ['t','f']:
        return 0.9
    elif tabs == ['f','t']:
        return 0.5
    elif tabs == ['f','f']:
        return 0.5

def f_rain( cloudy, rain ):
    if cloudy == rain:
        return 0.8
    else:
        return 0.2

def f_wetgrass( rain, sprinkler, wetgrass ):
    tabs = [ sprinkler, rain, wetgrass ]

    if tabs == ['t','t','t']:
        return 0.99
    elif tabs == ['t','t','f']:
        return 0.01
    elif tabs == ['t','f','t']:
        return 0.9
    elif tabs == ['t','f','f']:
        return 0.1
    elif tabs == ['f','t','t']:
        return 0.9
    elif tabs == ['f','t','f']:
        return 0.1
    elif tabs == ['f','f','t']:
        return 0
    elif tabs == ['f','f','f']:
        return 1

    pass
if __name__ == '__main__':

    g = build_bbn(
        f_cloudy,
        f_rain,
        f_sprinkler,
        f_wetgrass,
        domains=dict(
            cloudy=['t','f'],
            rain=['t','f'],
            sprinkler = ['t','f'],
            wetgrass=['t','f']
        )
    )
