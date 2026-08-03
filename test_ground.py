import newton
import warp as wp
import numpy as np

def run_sim():
    wp.init()
    builder = newton.ModelBuilder()
    builder.add_shape_box(body=-1, xform=wp.transform(np.array([0.0, 0.0, -0.5]), wp.quat_identity()), hx=10.0, hy=10.0, hz=0.5)
    model = builder.finalize()
    state = model.state()

    from newton.viewer import ViewerGL
    import matplotlib.pyplot as plt
    import os

    os.system('Xvfb :99 -screen 0 1024x768x24 &')
    os.environ['DISPLAY'] = ':99'

    viewer = ViewerGL(headless=True, width=640, height=480)
    viewer.set_model(model)
    viewer.set_camera(pos=(4.0, -4.0, 2.0), pitch=15.0, yaw=135.0)
    viewer.begin_frame(time=0.0)
    viewer.log_state(state=state)
    viewer.end_frame()
    img = viewer.get_frame().numpy()
    plt.imsave('ground_only.png', img)
    viewer.close()

if __name__ == "__main__":
    run_sim()
