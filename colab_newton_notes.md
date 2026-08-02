# Running GGC Gundam URDF in NVIDIA Newton on Google Colab

This guide explains how to use the provided Jupyter Notebook (`colab_newton_test.ipynb`) to simulate the Gundam URDF model using the NVIDIA Newton physics engine on Google Colab, and save the resulting MP4 video animation directly to your Google Drive.

Unlike Isaac Sim, Newton is lightweight and perfectly stable on basic Colab environments (like the free T4 GPU tier).

## Prerequisites
1. A Google account to access Google Colab and Google Drive.
2. In Colab, go to **Runtime > Change runtime type** and ensure you have selected a **GPU** (e.g., T4). The Newton viewer requires it to efficiently calculate and render the simulation frames.

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
   Execute the final, largest cell. The script will:
   - Start an Xvfb virtual display so OpenGL can render without a physical monitor.
   - Build a Newton simulation model from the URDF file.
   - Load the `walk-forward.csv` trajectory data and map its column headers to the Newton Joint Degrees of Freedom (DOFs).
   - Initialize a `ViewerGL` renderer in headless mode.
   - Step through the physics simulation while setting the joint target positions frame-by-frame.
   - Capture the RGB array from the viewer into memory and write the final compiled video (`gundam_newton_motion.mp4`) to your Google Drive.

## Retrieval
Once the simulation completes, simply open your Google Drive and navigate to `/MyDrive/`. You will find `gundam_newton_motion.mp4` waiting there for you to download or watch directly in your browser.
