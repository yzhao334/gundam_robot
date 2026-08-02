# Running GGC Gundam URDF in Isaac Lab on Google Colab

This guide explains how to use the provided Jupyter Notebook (`colab_isaac_lab_test.ipynb`) to simulate the Gundam URDF model using NVIDIA Isaac Lab on Google Colab, and save the resulting video to Google Drive.

## Prerequisites
1. A Google account to access Google Colab and Google Drive.
2. The notebook requires a GPU. In Colab, go to **Runtime > Change runtime type** and select a GPU (e.g., T4, L4, or A100).

## Steps to Run

1. **Upload Notebook to Colab:**
   Upload the `colab_isaac_lab_test.ipynb` file to your Google Drive and open it with Google Colaboratory. Alternatively, you can go to [colab.research.google.com](https://colab.research.google.com/), click "Upload", and select the file.

2. **Mount Google Drive:**
   Run the first cell in the notebook. It will prompt you to authorize Colab to access your Google Drive. This is required so the environment can save the recorded video directly to your Drive.

3. **Install Dependencies:**
   The notebook will automatically download and install NVIDIA Isaac Sim and Isaac Lab via `pip` from NVIDIA's PyPI index. Note that this step might take several minutes due to the size of the packages.

4. **Run the Simulation:**
   Execute the remaining cells. The notebook will:
   - Initialize the Isaac Sim AppLauncher.
   - Load the modified `GGC_TestModel_rx78_20170112.urdf` (with friction and damping set to 0.0) and replace `package://` mesh paths with absolute paths so the importer can resolve them.
   - Spawn the robot into the scene using the `Articulation` wrapper.
   - Set up an offline camera for recording.
   - Apply a simple sinusoidal joint trajectory to all degrees of freedom to demonstrate sample motion.
   - Step the physics simulation and collect camera frames.

5. **Retrieve the Video:**
   Once the simulation completes, the script uses `imageio` to encode the frames into an `.mp4` video file.
   The video will be saved to your Google Drive at `/content/drive/MyDrive/gundam_isaac_lab_motion.mp4`.
   You can then download and view the video from your Google Drive.
