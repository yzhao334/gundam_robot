# Running GGC Gundam URDF in NVIDIA Newton on Google Colab

This guide explains how to use the provided Jupyter Notebook (`colab_newton_test.ipynb`) to simulate the Gundam URDF model using the NVIDIA Newton physics engine on Google Colab, and save the resulting MP4 video animation directly to your Google Drive.

Unlike Isaac Sim, Newton is lightweight and perfectly stable on basic Colab environments (like the free T4 GPU tier).

## Updates for Proper Humanoid RL Dynamics
The default Gundam URDF was not designed for dynamic physical simulation (it was rigidly anchored in the air with unscaled geometries and non-physical trajectory values). The notebook script now explicitly transforms the robot on-the-fly to be RL-ready:
1. **Dynamic Floating Base**: The static `base_link` anchor is severed, making the pelvis the new physical floating root so it can fall and interact with gravity.
2. **True Human Scale**: The robot and its masses/inertias are scaled down from an 18-meter anime mech to a physically realistic ~1.8-meter, ~80kg human scale.
3. **PD Joint Control**: Instead of teleporting the joints magically (which breaks physics engines), the simulation now properly utilizes physical **Forward Dynamics**. The joints are controlled via Proportional-Derivative (PD) controllers that exert calculated physical torques to achieve the target CSV angles.
4. **Unit Conversion**: The original CSV trajectory angles were mathematically converted from Degrees to Radians so the physics engine solves them correctly without instantly hitting joint limits.

## Steps to Run

1. **Upload Notebook to Colab:**
   Upload the `colab_newton_test.ipynb` file to your Google Drive and open it with Google Colaboratory. Alternatively, you can go to [colab.research.google.com](https://colab.research.google.com/), click "Upload", and select the file.

2. **Mount Google Drive:**
   Run the first code cell in the notebook. It will prompt you to authorize Colab to access your Google Drive. This is required so the environment can save the recorded video directly to your Drive without losing it when the session ends.

3. **Install Dependencies:**
   Run the second cell. This will install `xvfb` (a virtual display server for headless rendering on Linux), `imageio`, and the NVIDIA `newton` physics engine.

4. **Clone the Repository & Patch Paths:**
   Run the third cell. This clones the Gundam robot repository and dynamically updates the URDF mesh path definitions so that Newton can find them on the Colab filesystem.

5. **Run the Simulation & Render Video:**
   Execute the final, largest cell. The script will dynamically process the URDF into a physics-ready state, initialize the PD solver, load the `walk-forward.csv` trajectory data, step through the physics engine, and compile the final video (`gundam_humanoid_physics.mp4`) to your Google Drive.

## Retrieval
Once the simulation completes, simply open your Google Drive and navigate to `/MyDrive/`. You will find `gundam_humanoid_physics.mp4` waiting there for you to download or watch directly in your browser.
