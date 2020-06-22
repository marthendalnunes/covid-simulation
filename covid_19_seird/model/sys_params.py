def get_sys_params(r0, recovering_rate, exposure_rate, death_rate, death_proportion_rate):
        sys_params = {
                # 𝛽:  expected amount of people an infected person infects per day
                'infection_rate': [r0*recovering_rate],        
                # 𝛾: the proportion of infected recovering per day ( 𝛾  = 1/D)
                'recovering_rate': [recovering_rate],
                # 𝛿: expected rate that exposed people turn into infected
                'exposure_rate': [exposure_rate],
                # α: death rate
                'death_rate':[death_rate],
                # ρ: proportion of people dying daily, or (1/ρ) = days from infection until death
                'death_proportion_rate': [death_proportion_rate] # 9 days from infection do death
        }
        return sys_params
