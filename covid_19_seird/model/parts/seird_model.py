import numpy as np 


## Policies

def p_exposed_growth(params, substep, state_history, prev_state):
    exposed_population = params['infection_rate']*prev_state['infected']*(prev_state['susceptible']/(prev_state['susceptible']+ prev_state['exposed'] + prev_state['infected'] + prev_state['recovered'] + prev_state['dead']))
    return {'exposed_growth': max(np.ceil(exposed_population),0)}


def p_infected_growth(params, substep, state_history, prev_state):
    infected_population = params['exposure_rate']*prev_state['exposed'] - (1 - params['death_rate']) * params['recovering_rate'] * prev_state['infected'] - params['death_rate'] * params['death_proportion_rate'] * prev_state['infected']
    return {'infected_growth': max(np.ceil(infected_population),0)}


def p_recovered_growth(params, substep, state_history, prev_state):
    if prev_state['infected'] == 1:
       recovered_population = 1
    else:
        recovered_population = (1 - params['death_rate']) * params['recovering_rate'] * prev_state['infected']
    return {'recovered_growth': max(np.ceil(recovered_population),0)}

def p_dead_growth(params, substep, state_history, prev_state):
    if prev_state['infected'] == 1:
        dead_population = 0
    else:
        dead_population = params['death_rate'] * params['death_proportion_rate'] * prev_state['infected']
    return {'dead_growth': max(np.ceil(dead_population),0)}


## SUFs

def s_susceptible_population(params, substep, state_history, prev_state, policy_input):
    updated_susceptible_population = prev_state['susceptible'] - policy_input['exposed_growth']
    return ('susceptible', max(updated_susceptible_population, 0))


def s_exposed_population(params, substep, state_history, prev_state, policy_input):
    updated_exposed_population = prev_state['exposed'] + policy_input['exposed_growth'] - policy_input['infected_growth']
    return ('exposed', max(updated_exposed_population, 0))


def s_infected_population(params, substep, state_history, prev_state, policy_input):
    updated_infected_population = prev_state['infected'] + policy_input['infected_growth'] - policy_input['recovered_growth'] - policy_input['dead_growth']
    return ('infected', max(updated_infected_population, 0))
        

def s_recovered_population(params, substep, state_history, prev_state, policy_input):
    updated_recovered_population = prev_state['recovered'] + policy_input['recovered_growth']
    return ('recovered', max(updated_recovered_population, 0))


def s_dead_population(params, substep, state_history, prev_state, policy_input):
    updated_dead_population = prev_state['dead'] + policy_input['dead_growth']
    return ('dead', max(updated_dead_population, 0))
