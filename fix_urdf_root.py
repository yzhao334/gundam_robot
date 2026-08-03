import json

with open("colab_newton_test.ipynb", "r") as f:
    nb = json.load(f)

for cell in nb["cells"]:
    if cell["cell_type"] == "code":
        source = cell["source"]

        for i, line in enumerate(source):
            if "builder.add_shape_box(pos=(0.0, 0.0, -0.5), hx=10.0, hy=10.0, hz=0.5)" in line:
                source[i] = "builder.add_shape_box(body=-1, xform=wp.transform(np.array([0.0, 0.0, -0.5]), wp.quat_identity()), hx=10.0, hy=10.0, hz=0.5)\n"
                break

with open("colab_newton_test.ipynb", "w") as f:
    json.dump(nb, f, indent=2)
