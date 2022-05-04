# stay on track
def reward_function(params):
    import math

    all_wheels_on_track = params["all_wheels_on_track"]
    x = params["x"]  # float  agent's x-coordinate in meters
    y = params["y"]  # agent's y-coordinate in meters
    closest_waypoints = params[
        "closest_waypoints"
    ]  # [int, int] indices of the two nearest waypoints.
    distance_from_center = params["distance_from_center"]  # float
    is_crashed = params[
        "is_crashed"
    ]  # Boolean flag to indicate whether the agent has crashed.
    is_offtrack = params["is_offtrack"]  # Boolean gone off track.
    is_reversed = params[
        "is_reversed"
    ]  # boolean flag to indicate if the agent is driving clockwise (True) or counter clockwise (False).
    heading = params["heading"]  # float agent's yaw in degrees
    progress = params["progress"]  # float percentage of track completed
    speed = params["speed"]  # float meters per second (m/s)
    steering_angle = params["steering_angle"]  # float
    steps = params["steps"]  # int number steps completed
    track_length = params["track_length"]  # float track length in meters.
    track_width = params["track_width"]  # float width of the track
    waypoints = params[
        "waypoints"
    ]  # [(float, float), ]list of (x,y) as milestones along the track center
    total = [
        all_wheels_on_track,
        x,
        y,
        closest_waypoints,
        distance_from_center,
        is_crashed,
        is_offtrack,
        is_reversed,
        progress,
        speed,
        steering_angle,
        steps,
        track_length,
        waypoints,
    ]

    # Example of rewarding the agent to stay inside the two borders of the track
    reward = 1e-3

    # Give a high reward if no wheels go off the track and
    # the car is somewhere in between the track borders
    if all_wheels_on_track and (0.5 * track_width - distance_from_center) >= 0.05:
        reward = 1.0

    # Example of penalize steering, which helps mitigate zig-zag behaviors
    # Read input parameters
    abs_steering = abs(
        params["steering_angle"]
    )  # Only need the absolute steering angle

    # Calculate 3 marks that are farther and father away from the center line
    marker_1 = 0.1 * track_width
    marker_2 = 0.25 * track_width
    marker_3 = 0.5 * track_width

    # Give higher reward if the car is closer to center line and vice versa
    if distance_from_center <= marker_1:
        reward = 1.0
    elif distance_from_center <= marker_2:
        reward = 0.5
    elif distance_from_center <= marker_3:
        reward = 0.1
    else:
        reward = 1e-3  # likely crashed/ close to off track

    # Steering penality threshold, change the number based on your action space setting
    ABS_STEERING_THRESHOLD = 15

    # Penalize reward if the car is steering too much
    if abs_steering > ABS_STEERING_THRESHOLD:
        reward *= 0.8

    return float(reward)
