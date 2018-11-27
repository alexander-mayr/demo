import falcon
import json

import numpy as np

LINKSTATIONS = [
	[0, 0, 10],
	[20, 20, 5],
	[10, 0, 12],
]

class ApiResource():
	def on_get(self, req, resp):
		x = int(req.get_param("x"))
		y = int(req.get_param("y"))

		point = np.array([x, y])

		if(None in point):
			resp.status = falcon.HTTP_400
			return

		powers = []

		for s in LINKSTATIONS:
			d = np.linalg.norm(np.array(s[:2] - point))
			r = s[2]

			if(d > r):
				powers.append(0)
			else:
				powers.append((r - d) ** 2)

		print(powers)
		print("")
		i = np.argmax(powers)
		o = LINKSTATIONS[i]

		resp.status = falcon.HTTP_200
		resp.body = json.dumps([ o[0], o[1], powers[i] ])

app = falcon.API()
app.add_route("/api/v1/linkstations/best/", ApiResource())

