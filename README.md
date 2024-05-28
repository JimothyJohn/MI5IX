![agents](docs/agents.png)

# MI5IX

A sandbox for multi-agent development powered by CrewAI and Streamlit.

## Quickstart

1. Set your environment variables in a file called .env using the [.env-example](.env-example) template:

```md
# Get yours here: https://platform.openai.com/account/api-keys
OPENAI_API_KEY=
OPENAI_API_VERSION=2024-02-01
# Get yours here: https://serper.dev/api-key
SERPER_API_KEY=
# Get yours here: https://console.cloud.google.com/google/maps-apis/home
GPLACES_API_KEY=
# Get yours here: https://console.groq.com/keys
GROQ_API_KEY=
# Get yours here: https://app.agentops.ai/settings/projects
AGENTOPS_API_KEY=
# Optional for Azure users
AZURE_OPENAI_API_KEY=
AZURE_OPENAI_RESOURCE=
AZURE_OPENAI_DEPLOYMENT=
```

2. Either use the .devcontainer or alternatively:

```bash
docker build -t mi5ix:latest -f .devcontainer/Dockerfile .
docker run -p 8501:8501 --env-file .env -w $(pwd)/agency:/agency mi5ix:latest streamlit run /agency/app.py
```

3. Open your Streamlit app at [http://localhost:8501](http://localhost:8501):

![app](docs/streamlit.png)

### TODO

- [ ] Add chat GUI to bring the human back in the loop

- [ ] Add local Phi3 instance via Ollama
