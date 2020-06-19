def get_genesis_states(susceptible, exposed, infected, recovered, dead):
    genesis_states = {
        'susceptible': susceptible,
        'exposed': exposed,
        'infected': infected,
        'recovered': recovered,
        'dead': dead
    }
    return genesis_states
