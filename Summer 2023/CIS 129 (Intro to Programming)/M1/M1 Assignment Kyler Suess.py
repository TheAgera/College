while True:
    edge_input = input("Enter the value of one edge of the cube (or 'q' to quit): ")
    # Any time you want to stop using the program, press q, as this was built using a while-loop.
    if edge_input == "q":
        break
    # First validation check to make sure user doesn't break input
    if not edge_input.isdigit():
        print("Invalid input. Please enter a number.")
        continue
    # Convert string value to float, so it can be used to complete mathematical equations
    edge = float(edge_input)

    # Further validation checks to make sure the program doesn't break due to user input
    if edge <= 0:
        print("Please enter a positive number.")
    elif edge > 3.40e38:
        print("Input value is too large")
    else:
        # Calculate surface area of one side of the cube
        side_surface_area = edge ** 2

        # Calculate surface area of the cube
        cube_surface_area = 6 * side_surface_area

        # Calculate the volume of the cube
        cube_volume = edge ** 3

        # Output the results
        print("Surface area of one side of the cube:", side_surface_area)
        print("Surface area of the cube:", cube_surface_area)
        print("Volume of the cube:", cube_volume)
