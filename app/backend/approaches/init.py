from search_approach import Approach

# Create an instance of the Approach class
approach = Approach(
    search_client=search_client,
    openai_client=openai_client,
    auth_helper=auth_helper,
    query_language="en-US",
    query_speller="en-US",
    embedding_deployment="my-embedding-deployment",
    embedding_model="text-embedding-ada-002",
    openai_host="https://my-openai-instance.com",
    vision_endpoint="https://my-vision-instance.com",
    vision_token_provider=lambda: asyncio.get_event_loop().run_until_complete(get_vision_token()),
)

# Perform a search
results = await approach.search(
    top=10,
    query_text="sample query",
    filter="category eq 'example'",
    vectors=[],
    use_semantic_ranker=False,
    use_semantic_captions=False,
)

# Print the sources content
sources_content = approach.get_sources_content(results, use_semantic_captions=False, use_image_citation=False)
for content in sources_content:
    print(content)
