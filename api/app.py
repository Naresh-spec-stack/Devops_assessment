from flask import Flask, jsonify, request
import psycopg2
import yaml
import os

app = Flask(__name__)

CONFIG_PATH = os.getenv("CONFIG_PATH", "/config/config.yaml")

# Load mappings from YAML
def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

config = load_config()

db_config = {
    "user": os.getenv("DB_USER", "postgres"),
    "password": os.getenv("DB_PASSWORD", "password"),
    "host": os.getenv("DB_HOST", "postgres-service"),
    "port": os.getenv("DB_PORT", 5432),
    "database": os.getenv("DB_NAME", "mydb"),
}

@app.route("/<path:endpoint>", methods=["GET"])
def handle_request(endpoint):
    try:
        # Match endpoint in config.yaml
        mapping = next((m for m in config["mappings"] if m["api_endpoint"].strip("/") == endpoint.strip("/")), None)
        if not mapping:
            return jsonify({"error": f"No mapping found for {endpoint}"}), 404

        query = mapping["query"]
        params = []
        
        # Handle query parameters (simple WHERE clause)
        filters = []
        for key, value in request.args.items():
            if key in mapping["columns"]:  
                db_col = [col for col, api_field in mapping["columns"].items() if api_field == key]
                if db_col:
                    filters.append(f"{db_col[0]} = %s")
                    params.append(value)
        
        if filters:
            if "where" in query.lower():
                query += " AND " + " AND ".join(filters)
            else:
                query += " WHERE " + " AND ".join(filters)

        # Connect to DB
        conn = psycopg2.connect(**db_config)
        cur = conn.cursor()
        cur.execute(query, params)
        rows = cur.fetchall()
        col_names = [desc[0] for desc in cur.description]

        # Transform according to YAML mapping
        results = []
        for row in rows:
            obj = {}
            for col, val in zip(col_names, row):
                if col in mapping["columns"]:
                    obj[mapping["columns"][col]] = val
            results.append(obj)

        cur.close()
        conn.close()
        return jsonify(results)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=3000)
