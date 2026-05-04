import solid_geometry as sg


choice = int(input("Enter choice (1-cube, 2-cylinder, 3-sphere): "))

if choice == 1:
	side = float(input("Enter side: "))
	print(sg.cube_volume(side))
elif choice == 2:
	radius = float(input("Enter radius: "))
	height = float(input("Enter height: "))
	print(sg.cylinder_volume(radius, height))
else:
	radius = float(input("Enter radius: "))
	print(sg.sphere_volume(radius))
