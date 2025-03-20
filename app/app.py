cat << EOF >> ~/ag-web/app/app.py
#
# Reasoning Engine
#
NB_R_ENGINE_ID = "REASONING_ENGINE_ID"

from vertexai.preview import reasoning_engines
remote_agent = reasoning_engines.ReasoningEngine(
    f"projects/{PROJECT_ID}/locations/{LOCATION}/reasoningEngines/{NB_R_ENGINE_ID}"
)

# Endpoint for the Flask app to call the Agent
@app.route("/ask_gemini", methods=["GET"])
def ask_gemini():
    query = request.args.get("query")
    log.info("[ask_gemini] query: " + query)
    retries = 0
    resp = None
    while retries < MAX_RETRIES:
        try:
            retries += 1
            resp = remote_agent.query(input=query)
            if (resp == None) or (len(resp["output"].strip()) == 0):
                raise ValueError("Empty response.")
            break
        except Exception as e:
            log.error("[ask_gemini] error: " + str(e))
    if (resp == None) or (len(resp["output"].strip()) == 0):
        raise ValueError("Too many retries.")
        return "No response received from Reasoning Engine."
    else:
        return resp["output"]
EOF