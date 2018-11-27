import requests

points = [
	[0, 0],
	[100, 100],
	[15, 10],
	[18, 18]
]

for p in points:
	x = p[0]
	y = p[1]

	r = requests.get("http://localhost/api/v1/linkstations/best?x=" + str(x) + "&y=" + str(y)).json()

	if(r[2] == 0):
		print("No suitable Link station found for point " + str(p))
	else:
		print("Best Link station for point " + str([x, y]) + " is " + str(r[:2]) + " with power " + str(r[2]))