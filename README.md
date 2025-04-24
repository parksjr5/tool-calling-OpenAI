# Practice tool calling with OpenAI

**Goal**: Develop agentic workflow to pull calendar events and forecasting weather to identify best time to run, and write back an event to block off running time.

Practicing multiple skills in this repositiory:
* working with OpenAIs new Response API code
* practice tool calling
* tool calling when multiple tools
* parallelizing AI agents
* thinking through AI agents + uses
* thinking through workflow of AI agents


**Personal Notes:**
Helpful to know exists - [Request](bodyhttps://platform.openai.com/docs/api-reference/responses/create)
* parallel tool calling: allow calling tools in parallel or not
* previous_response_id: allows for multi-turn
  * instructions: will not be carried over to next call if multi-turn activated
* include: can include files returned in search after tool call
* tool_choice: how the model should select which tool to choose when generating a response
* tools: the actual tools to call (web search, file search)

* gpt 4.1 nano is most cost effective for now