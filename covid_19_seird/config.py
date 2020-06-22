def get_config(simulation_time_steps, r0, recovering_rate, exposure_rate, death_rate, death_proportion_rate,susceptible, exposed, infected, recovered, dead):
    MONTE_CARLO_RUNS = 1 # N monte carlo runs

    from cadCAD.configuration import append_configs
    from cadCAD.configuration.utils import config_sim
    from .model.state_variables import get_genesis_states
    from .model.partial_state_update_block import partial_state_update_block
    from .model.sys_params import get_sys_params
    from .sim_params import SIMULATION_TIME_STEPS

    sim_config = config_sim (
        {
            'N': MONTE_CARLO_RUNS,
            'T': range(simulation_time_steps), # number of timesteps
            'M': get_sys_params(r0, recovering_rate, exposure_rate, death_rate, death_proportion_rate),
        }
    )
    append_configs(
        sim_configs=sim_config,
        initial_state=get_genesis_states(susceptible, exposed, infected, recovered, dead),
        partial_state_update_blocks=partial_state_update_block
    )
    return {'sim_config':sim_config, 'append_configs':append_configs}