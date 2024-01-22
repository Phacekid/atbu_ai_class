"""We have two water jugs, one measures 4 Gallons (4G) while the other measure 3 Gallons (3G). But there is no measuring label mentioned on either of these two jugs i.e. we cannot know the exact amount filled in the jug. 
Now, assuming there is an infinite amount of water supply, can we measure all 1G, 2G, 3G, 4G using these unmarked jugs.
Hint: We can empty the jugs, and transfer water from one jug to other.
The Final Result should contain 2G and 4G"""
def measure_water():
    jug_4 = 0
    jug_3 = 0
    
    # Step 1: Initial state
    print(f"{jug_4},{jug_3}")

    # Step 2: Fill the 3-gallon jug
    jug_3 = 3
    print(f"{jug_4},{jug_3}")

    # Step 3: Pour water from the 3-gallon jug to the 4-gallon jug
    jug_4 = jug_3
    jug_3 = 0
    print(f"{jug_4},{jug_3}")

    # Step 4: Fill the 3-gallon jug again
    jug_3 = 3
    print(f"{jug_4},{jug_3}")

    # Step 5: Pour water from the 3-gallon jug to the 4-gallon jug until it's full
    jug_4 += 1
    jug_3 -= 1
    print(f"{jug_4},{jug_3}")

    # Final state with 2 gallons in the 4-gallon jug and 4 gallons in the 3-gallon jug
    print(f"Final Result: {jug_4},{jug_3}")

# Run the function
measure_water()