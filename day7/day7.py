def main():
    with open("../input/day7_input") as f:
        grid = [line.rstrip("\n") for line in f]

    # find starting point
    for i in range(len(grid[0])):
        if grid[0][i] == 'S':
            start_beam = (1, i)
    
    # dict to keep track of how many beams are at each position since duplicate intermediate beam paths are relvant now
    # (beam_y, beam_x) -> # of beams that exist here across all timelines
    beams = {start_beam: 1}
    
    # set that tracks which splitters have been hit by a beam
    # activated_splitters = set()

    timelines = 0

    # keep splitting beams until no new beams are created
    while beams:
        # new_beams, new_splitters = split_beams(grid, beams, activated_splitters)
        # activated_splitters.update(new_splitters)
        beams, new_timelines = split_beams(grid, beams)
        timelines += new_timelines

    # every beam is 1 timeline
    print(timelines)

def split_beams(grid, beams):
    new_beams = {}
    new_timelines = 0
    # new_splitters = set()

    for beam, count in beams.items():
        beam_y, beam_x = beam
        hit_splitter = False
        
        for row in range(beam_y, len(grid)):
            if grid[row][beam_x] == '^':
                hit_splitter = True
                left_beam = (row + 1, beam_x - 1)
                right_beam = (row + 1, beam_x + 1)

                # if the beam is in bounds, split it, with count = the count in the original dict + the count in the new dict
                if check_bounds(grid, left_beam):
                    new_beams[left_beam] = new_beams.get(left_beam, 0) + count
                if check_bounds(grid, right_beam):
                    new_beams[right_beam] = new_beams.get(right_beam, 0) + count
                break

        # add the count to new_timelines when a beam path doesn't split (exits the manifold)
        if not hit_splitter:
            new_timelines += count

    return new_beams, new_timelines

def check_bounds(grid, coords):
    return 0 <= coords[0] < len(grid) and 0 <= coords[1] < len(grid[0])

if __name__ == "__main__":
    main()