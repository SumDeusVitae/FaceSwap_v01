import matplotlib.pyplot as plt
import cv2
import os
import insightface
from insightface.app import FaceAnalysis


def swapping_face(back_orig, face_orig):
    # Set the backend for Matplotlib to 'agg' (Agg backend for non-interactive image generation)
    plt.switch_backend('agg')

    # Read the original background image
    img1 = cv2.imread(back_orig)

    # Prepare the FaceAnalysis model for face detection
    app = FaceAnalysis(name='buffalo_l')
    app.prepare(ctx_id=0, det_size=(640, 640))

    # Load the face swapping model
    swapping = insightface.model_zoo.get_model(
        'inswapper_128.onnx', download=False, download_zip=False)

    # Read the original face image
    img2 = cv2.imread(face_orig)

    # Get the detected face embeddings for both images
    face1 = app.get(img1)[0]
    face2 = app.get(img2)[0]

    # Create a copy of the background image to perform the face swapping
    img1_copy = img1.copy()
    img1_copy = swapping.get(img1_copy, face1, face2, paste_back=True)

    # Display the swapped image using Matplotlib
    plt.imshow(img1_copy[:, :, ::-1])
    plt.axis('off')
    plt.subplots_adjust(top=1, bottom=0, right=1, left=0, hspace=0, wspace=0)
    plt.margins(0, 0)

    # Save the swapped image to a file
    path = fr"static\images\result.png"
    if os.path.isfile(path):
        os.remove(path)
    plt.savefig(path)  # bbox_inches='tight' as second parameter as an optnion

    # Remove the original background and face images from the file system
    os.remove(back_orig)
    os.remove(face_orig)

    # Close the Matplotlib figure
    plt.close()

    # Return to the calling code (The swapped image has been saved to 'result.png')
    return
