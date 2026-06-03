from flask import Flask, render_template, request
import pandas as pd

app = Flask(__name__)

EXCEL_FILE = "coach_data.xlsx"

@app.route("/", methods=["GET", "POST"])
def index():
    results = None
    search_query = ""
    
    if request.method == "POST":
        search_query = request.form.get("coach_number", "").strip()
        
        if search_query:
            try:
                df = pd.read_excel(EXCEL_FILE, dtype=str)
                filtered_df = df[df["Coach Number"] == search_query]
                results = filtered_df.to_dict(orient="records")
            except Exception as e:
                print(f"Error: {e}")
                results = []

    return render_template("index.html", results=results, query=search_query)

if __name__ == "__main__":
    app.run(debug=True)
