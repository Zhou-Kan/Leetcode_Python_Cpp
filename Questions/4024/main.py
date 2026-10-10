
def nearest_drones(drones: list[list[int]], target: list[int]) -> list[int]:
    nearest_idx, nearest_dist = -1, float('inf')

    # Loop through the whole list and find out all drones within the range
    x_t, y_t = target[0], target[1]

    for i, drone in enumerate(drones):
        x, y, range = drone
        m_dist =  abs(x - x_t) + abs(y - y_t) 

        if m_dist < nearest_dist and m_dist <= range:
            nearest_dist = m_dist
            nearest_idx = i

    return nearest_idx


print(nearest_drones([[0,0,8],[2,2,9]], [3, 4]))