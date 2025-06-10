# Prompt-based-API

## Purpose of this API

This API propose a simple way to send a text to be analyzed by an LLM (Currently asking OpenAI), to extract or convert information.

To achieve the goal, you have to use an existing prompt, or create you own prompt with your specification.

for example, to reformulate a text to make it rhymes, you can create  the following prompt:

```shell
$ curl -X 'POST' \
  'http://127.0.0.1:8080/prompts/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "title": "rhymes",
  "content": "reformulate the following text to create rhymes.",
  "description": "rewrite in rhymes."
}'
{
    "title":"rhymes",
    "content":"reformulate the following text to create rhymes.",
    "description":"rewrite in rhymes.",
    "id":78
}
```

Then use the ID (using `/{prompt_id}/generate`) to reformulate a text

```shell
$ curl -X 'POST' \
'http://127.0.0.1:8080/78/generate' \
-H 'accept: application/json' \
-H 'Content-Type: application/json' \
-d '{
"input": "The old lighthouse stood sentinel on the rugged coastline, its beam sweeping across the turbulent sea. A storm was brewing, the sky a bruised purple, and the wind howled like a banshee. Inside, the solitary keeper prepared for a long night, his thoughts drifting to distant shores and the loved ones he had left behind. He often wondered if they still remembered him, or if time, like the relentless tide, had washed away their memories. Every creak and groan of the ancient structure echoed the passage of years, a silent testament to countless storms weathered and ships guided to safety. There was a profound sense of purpose in his solitude, a quiet dignity in his vigil."
}'
{
    "sysprompt":"reformulate the following text to create rhymes.",
    "answer":"Certainly! Here is your text reformulated to create rhymes:\n\nUpon the rugged coast, the old lighthouse stands tall,  \nIts beacon sweeping wide, a guide through it all.  \nA storm’s on the rise, with a sky bruised and deep,  \nAnd the wind wails like banshees who never quite sleep.  \n\nWithin the worn walls, the lone keeper stays,  \nPreparing for night through the sea’s furious blaze.  \nHis thoughts drift afar to the loves he once knew,  \nTo distant, warm shores and a sky painted blue.  \n\nHe ponders if memories of him linger on,  \nOr if tides of the ages have rendered them gone.  \nEach creak and each groan in the lantern’s high tower  \nEcho decades of storms—and the lighthouse’s power.  \n\nThere’s quiet pride woven through all the years,  \nAnd a purpose that shines when the thunder appears.  \nIn solitary vigil, through darkness and foam,  \nHe lights the way home for the lost who may roam."
}

## Start the API

`./load.sh`

## Use the API

The API is documented with the standard Swagger, please go to <http://127.0.0.1:8080/docs>

## Architecture

```shell
├── app
│   ├── api
│   │   └── v1
│   │       └── routes
│   │           ├── items.py  # List of API routes
│   ├── core
│   │   ├── config.py    # Default values and .env file parsing
│   │   ├── crud.py      # CRUD definitions
│   │   ├── database.py  # Database configuration
│   ├── main.py
│   ├── models  # All schemas are defined here
│   │   ├── item.py
│   │   ├── prompt.py
│   └── services
│       ├── item_service.py  # Functions used by the route definitions
├── prompts.db  # Default database
├── pyproject.toml  # `uv` project definition
├── tests  # Used with pytest
│   ├── __init__.py
│   ├── test_db.py
│   └── test_prompt.py
└── uv.lock  # `uv` requirements
```

## Testing

To keep consistency please use `uv`: `uv run pytest tests`

## TODO

- Refactor this MVP using async
- Use a Virgin development DB in tests
- Implement a proper logging definition loglevel management, maybe in the settings part
- Implement managed Exceptions and HTTP return codes in case of error
- Add more functional tests using mocks
- Manage tags to group API endpoints in separate layers
