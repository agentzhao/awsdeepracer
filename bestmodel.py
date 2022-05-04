def reward_function(params):
    if params['all_wheels_on_track']:
        reward = params['progress']
    else:
        reward = 0.001
    
    reward += ( params["speed"] / 5 )

    return float(reward)
