"""
Tower of Hanoi is a mathematical puzzle where we have three rods (A, B, and C) and N disks. Initially, all the disks are stacked in decreasing value of diameter i.e., the smallest disk is placed on the top and they are on rod A. The objective of the puzzle is to move the entire stack to another rod (here considered C), obeying the following simple rules: 

Only one disk can be moved at a time.
Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. a disk can only be moved if it is the uppermost disk on a stack.
No disk may be placed on top of a smaller disk.
"""

def tower_of_hanoi(n, source_rod, target_rod, auxiliary_rod):
    if n == 1:
        print(f"Move disk 1 from {source_rod} to {target_rod}")
        return
    tower_of_hanoi(n - 1, source_rod, auxiliary_rod, target_rod)
    print(f"Move disk {n} from {source_rod} to {target_rod}")
    tower_of_hanoi(n - 1, auxiliary_rod, target_rod, source_rod)

# Example usage
num_disks = 3
tower_of_hanoi(num_disks, 'A', 'C', 'B')