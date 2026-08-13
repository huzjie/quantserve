from quantserve.serve.streaming import sse_chunk, sse_done, token_event


def test_sse():
    assert sse_chunk({"a": 1}).startswith("data: ")
    assert sse_done() == "data: [DONE]\n\n"
    assert token_event("hi", "m", 1)["choices"][0]["delta"]["content"] == "hi"
