# stay on track
def reward_function(params):
    import math

    all_wheels_on_track = params['all_wheels_on_track']
    x = params["x"]                        # float  agent's x-coordinate in meters
    y = params["y"]                        # agent's y-coordinate in meters
    closest_waypoints = params["closest_waypoints"]          # [int, int] indices of the two nearest waypoints.
    distance_from_center = params['distance_from_center'] #float
    is_crashed = params["is_crashed"]      # Boolean flag to indicate whether the agent has crashed.
    is_offtrack = params["is_offtrack"]    # Boolean gone off track.
    is_reversed = params["is_reversed"]    # boolean flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    heading = params["heading"]            # float agent's yaw in degrees
    progress = params["progress"]          # float percentage of track completed
    speed = params["speed"]                # float meters per second (m/s)
    steering_angle = params["steering_angle"]# float
    steps = params["steps"]                # int number steps completed
    track_length = params["track_length"]  # float track length in meters.
    track_width = params["track_width"]    # float width of the track
    waypoints = params["waypoints"]        # [(float, float), ]list of (x,y) as milestones along the track center
    total = [all_wheels_on_track, x, y, closest_waypoints, distance_from_center, is_crashed, is_offtrack, is_reversed, progress, speed, steering_angle, steps, track_length, waypoints]

    reward = 1e-3

    rabbit = [0,0]
    pointing = [0,0]

    rabbit = [waypoints[closest_waypoints+1][0],waypoints[closest_waypoints+1][1]]
    radius = math.hypot(x - rabbit[0], y - rabbit[1])

    pointing[0] = x + (radius * math.cos(heading))
    pointing[1] = y + (radius * math.sin(heading))

    vector_delta = math.hypot(pointing[0] - rabbit[0], pointing[1] - rabbit[1])

    if vector_delta == 0:
        reward += 1
    else:
        reward += ( 1 - ( vector_delta / (radius * 2)))

    return float(reward)
