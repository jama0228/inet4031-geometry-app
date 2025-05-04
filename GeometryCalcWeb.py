# imports
from flask import Flask, request, render_template, redirect, url_for
import cylinder  # <-- This is needed for the cylinder volume calculation
import sphere    # <-- This is needed for the sphere volume calculation

# Flask app setup
app = Flask(__name__)

# Flask route for the index page (home page)
@app.route("/", methods=["GET", "POST"])
def mainForm():
    if request.method == "POST":
        sphere_selected = request.form.get("sphere")
        cylinder_selected = request.form.get("cylinder")
        print("Selection was: ", sphere_selected, cylinder_selected)  # Prints to command line for troubleshooting

        if sphere_selected == "on":
            print("User selected sphere")  # Prints to command line for troubleshooting
            return redirect(url_for('sphereForm'))  # Redirect to the sphere calculations page

        elif cylinder_selected == "on":
            print("User selected cylinder")  # Prints to command line for troubleshooting
            return redirect(url_for('cylinderForm'))  # Redirect to the cylinder calculations page

    return render_template("index.html")  # Renders the home page with form

# Flask route for the cylinder calculations page
@app.route("/cylinder", methods=["GET", "POST"])
def cylinderForm():
    if request.method == "POST":
        radius = request.form.get("rad")  # Getting radius from the form
        height = request.form.get("hgt")  # Getting height from the form
        vol = cylinder.volume(int(radius), int(height))  # Calls the cylinder volume function
        return f"User entered: Radius {radius} and Height: {height}. <p>The Volume is: {vol}"
    return render_template("cylinder.html")  # Renders the cylinder page with the form

# Flask route for the sphere calculations page
@app.route("/sphere", methods=["GET", "POST"])
def sphereForm():
    if request.method == "POST":
        radius = request.form.get("rad")  # Only radius is required for the sphere volume calculation
        vol = sphere.volume(int(radius))  # Calls the sphere volume function
        return f"User entered: Radius {radius}. <p>The Volume is: {vol}"  # Displays the result
    return render_template("sphere.html")  # Renders the sphere page with the form

# Additional code here for other calculators (cube, etc.)

if __name__ == "__main__":
    app.run(debug=True)
