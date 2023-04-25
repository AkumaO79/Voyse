from flask import Flask, render_template, request, json
import pandas as pd

app = Flask(__name__)
app.template_folder = "templates"
app.static_folder = "static"


@app.route("/")
def hello_world():
    return render_template("index2.html")


@app.route("/storeData", methods=["POST"])
def store_data():
    if request.method == "POST":
        # Get the uploaded CSV file
        file1 = request.files["transcript"]
        file2 = request.files["summarization"]
        file3 = request.files["arrayData"]

        jsonData = file3.read().decode("utf8")

        jdata = json.loads(jsonData)

        # jdata.keys()

        # jdata Variable holds the Charts JSON data

        # Read the CSV file into a pandas DataFrame
        df1 = pd.read_csv(file1)
        contents = file2.read()

        # Get the column names
        t_columns = list(df1.columns)

        # Get the data as a list of dictionaries
        t_data = df1.to_dict("records")

        # Render the template with the data
        return render_template(
            "dashboard.html",
            t_columns=t_columns,
            t_data=t_data,
            content=contents,
            chartsData=jdata,
        )


if __name__ == "__main__":
    app.run(debug=True, port=3000)
