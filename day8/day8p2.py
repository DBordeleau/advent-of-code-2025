import math

def main():
    junction_boxes = []
    with open("../input/day8_input") as f:
        for line in f:
            x, y, z = map(int, line.strip().split(","))
            junction_boxes.append((x,y,z))
    
    # find all pairs and their distances
    pairs = []
    for i in range(len(junction_boxes)):
        for j in range(i + 1, len(junction_boxes)):
            dist = get_distance(junction_boxes[i], junction_boxes[j])
            pairs.append((dist, i, j))
    
    # sort by distance
    pairs.sort()

    # list of sets to track formed circuits
    circuits = []

    # connect the 1000 closest pairs
    for distance, i, j in pairs:
        box_i = junction_boxes[i]
        box_j = junction_boxes[j]

        # find which circuits (if any) contain these boxes
        circuit_i = None
        circuit_j = None

        for circuit in circuits:
            if box_i in circuit:
                circuit_i = circuit
            if box_j in circuit:
                circuit_j = circuit

        # if they're in the same circuit do nothing
        if circuit_i is not None and circuit_i is circuit_j:
            continue

        # if theyre both in circuits merge them
        if circuit_i and circuit_j:
            print(f"  Merging circuits of size {len(circuit_i)} and {len(circuit_j)}")
            circuit_i.update(circuit_j)
            circuits.remove(circuit_j)
        # if only one is in a circuit add the other
        elif circuit_i:
            circuit_i.add(box_j)
        elif circuit_j:
            circuit_j.add(box_i)
        # if neither are in circuits, create a new circuit
        else:
            circuits.append({box_i, box_j})
        
        print(f"Connecting boxes with X coords of {box_i[0]} and {box_j[0]}. The product of their coords is: {box_i[0] * box_j[0]}.")

def get_distance(box1, box2):
    # formula for euclidean distance from https://en.wikipedia.org/wiki/Euclidean_distance
    return math.sqrt(((box1[0] - box2[0]) ** 2) + ((box1[1] - box2[1]) ** 2) + ((box1[2] - box2[2]) ** 2))


if __name__ == "__main__":
    main()