from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# sample data
products = [
    {"id": 1, "name": "Tomato", "pricePerKg": 50, "unit": "per Kg"},
    {"id": 2, "name": "Potato", "pricePerKg": 40, "unit": "per Kg"},
    {"id": 3, "name": "Onion", "pricePerKg": 60, "unit": "per Kg"},
]

contact = {
    "phone": "9800000000",
    "email": "market@example.com"
}

@app.route("/")
def index():
    return render_template("index.html", products=products, contact=contact)

@app.route("/api/total", methods=["POST"])
def total_calc():
    data = request.get_json()
    items = data.get("items", [])
    total = 0
    for item in items:
        for p in products:
            if p["id"] == item["id"]:
                total += p["pricePerKg"] * float(item["kg"])
    return jsonify({"total": total})

if __name__ == "__main__":
    app.run(debug=True)
