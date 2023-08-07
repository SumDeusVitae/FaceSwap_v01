from flask import Flask, request, render_template
from swap import swapping_face
# Create a Flask app
app = Flask(__name__)

# Define a route for the index page


@app.route('/', methods=['GET', 'POST'])
def index():
    # Check if the request method is POST (when the form is submitted)
    if request.method == 'POST':
        # Get the uploaded images from the form
        image1 = request.files['file1']
        image2 = request.files['file2']

        # Define paths for storing the uploaded images and the result image
        background = fr"static\images\background.jpg"
        face = fr"static\images\face.jpg"
        result = fr"static\images\result.png"

        # Save the uploaded images to the specified paths
        image1.save(background)
        image2.save(face)

        # Perform face swapping on the uploaded images
        swapping_face(background, face)

        # After face swapping, return the result image path to be displayed on the index page
        return render_template('index.html', result=result)

    # If the request method is GET (initial page load), render the index.html template
    return render_template('index.html')


# Run the Flask app if this script is executed directly
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
