# AI-300T00: Operationalize Machine Learning and Generative AI Solutions — Day 3 (Part 2)

- **Date:** Wednesday, 3 June 2026 (21:30–01:30 IST)
- **Trainer:** Pauroosh Kaushal (Microsoft Certified Trainer), Koenig Solutions
- **Recording:** `…20260603_213018-Meeting Recording.mp4` (Part 2 of 2 listed under Wed 3 Jun) — the full Day 3 session
- **Length:** ~3:59:57  ·  **Captions:** 897

> Transcript captured from the on-screen auto-generated captions for personal study. Captions are machine-generated (Microsoft Stream) and may contain errors. Section headings were added at the points where the trainer moves to a new topic; the caption text itself is verbatim.

## Contents

- `[0:00]` Module 3 — GenAI Ops: Operationalize Generative AI Solutions
  - `[0:00]` Session start & agenda
  - `[11:28]` Generative AI models & agents
  - `[21:07]` LLMs with tools — agent examples
  - `[36:20]` Evaluating GenAI before production
  - `[52:15]` Token-based cost
  - `[55:13]` Foundry portal — model catalog & deployment
  - `[1:06:42]` RAG app & endpoints
  - `[1:14:04]` Create an agent & evaluators
  - `[1:30:54]` Foundry project — experiment to production
  - `[1:37:38]` Build an agent (weather agent) & prompt versions
  - `[1:51:07]` Managing prompts
- `[2:08:16]` Module 3 (continued) — Prompt Management & Evaluation
  - `[2:08:16]` Recap & tracking prompts in files (after break)
  - `[2:18:18]` Prompt evaluation — accuracy & relevance
  - `[2:24:16]` Batch testing & prompt templates
  - `[2:30:28]` Branching & comparing prompts
  - `[2:37:29]` Lab — manual evaluation & prompt optimization
  - `[2:44:55]` Baseline experiment & new agent versions
  - `[2:53:52]` Knowledge check & extended lab time
  - `[3:58:49]` Lab — quota limit troubleshooting

---


## Module 3 — GenAI Ops: Operationalize Generative AI Solutions  `[0:00]`


### Session start & agenda  `[0:00]`

**[0:22]** Ohh.

**[0:24]** Hello, everyone.

**[0:27]** A very good morning. And welcome to day three of this training.

**[0:36]** So.

**[0:38]** We'll wait for a few minutes, let all the participants join. Two, 3 minutes here.

**[0:45]** While the participants are joining, let me share the attendance link in the chat.

**[0:50]** Yeah.

**[2:39]** Participants, please find the attendance link, the QR code, and kindly mark your attendance for today's session.

**[3:41]** I hope there is no challenge with marking attendance. Let me share the QR code.

**[3:48]** with the participants, those who just joined.

**[3:55]** Please find the attendance link in the chat.

**[4:48]** So, let's get going.

**[4:55]** So after marking the attendance, you may even log into my clinic portal, right? And you can track your attendance as well. Any issues with your attendance, let me know. I can mark your attendance manually as well. So.

**[5:10]** All right, so let's get going with today's agenda, right? Let me share my screen.

**[5:31]** All right.

**[5:35]** So.

**[5:38]** Yeah.

**[5:40]** Welcome to day three and let's review what we discussed yesterday and then we'll have an overview of today's agenda.

**[5:51]** So, in the previous session, we further explored the Azure Machine Learning workspace. We have, sorry, we have able to register a model, then going ahead, how we can integrate Azure Machine Learning workspace with...

**[6:12]** GitHub that we discussed, how GitHub Azure Machine Learning integration is possible, how we can do CI/CD, how we can automate, let's say, continuous integration, automate model training, right, by creating a workflow in a GitHub action.

**[6:33]** Right, and so we have seen, let's say, if we have data in a main branch, if we are exploring or trying to improve our process, we may create a new feature branch, maybe making some edits here, right? And when we create a PR, right?

**[6:53]** the pull request so that we can merge the feature branch to the main branch. We may automate a workflow, right?

**[7:05]** Yeah, we may automate A workflow. So with the changes, we are able to train the model again. And if the results are okay, if the leads are disapproves, then it can be merged with the main branch and main branch can be updated then.

**[7:23]** So, so it's not applicable only just for model training, but we can do continuous deployment also, so CI/CD pipelines can be built using GitHub Actions. Going ahead, we talked about the deployment, the deployment of a model using Azure Machine Learning Workspace.

**[7:44]** We discussed the batch deployment, the online deployment.

**[7:49]** Right, so, so with that, we complete the Azure Machine Learning topics, right, related to the this training. OK, so let me go back here once, OK?

**[8:17]** Right, so let's let me paste the link in the chat, and...

**[8:31]** All right, so today's agenda would be, we'll start with the Microsoft Foundry. We'll talk about the Foundry portal. So it's a portal where we can build generative AI applications, the agentic AI applications, monitor them, right? So we will be exploring.

**[8:51]** the Foundry portal and...

**[8:55]** Oh, Bill.

**[8:57]** operationalize, we will build a generative AI solution. We'll see how to plan for Gen AI Ops, right, operationalizing the generative AI solution. So what are the challenges, what how the Foundry tools which are available, how we can make use of the tools.

**[9:20]** to build a scalable solution, AI solution, which we can deploy and later we can monitor our deployment.

**[9:29]** So let's get going. Talking about Gen AI Ops. So initially we'll discuss the generative AI applications. Then going ahead, we will try operationalizing Gen AI solution. So let's get going then.

**[9:49]** K.

**[9:54]** All right.

**[9:56]** So before we talk about agents, right, what agents are, we should be knowing what is a generative AI model.

**[10:07]** Or maybe if I get your opinion right, or like which generative AI models are we using, or are we using ChatGPT, Microsoft Copilot, or maybe we are using Cloud models?

**[10:26]** for some use case.

**[10:30]** Are we using these platforms any if I know in the chat?

**[10:37]** Yeah.

**[10:46]** Maybe to do day-to-day task or...

**[10:50]** If you are using Gemini models.

**[10:54]** Maybe on a Chrome Chrome browser, right?

**[11:05]** Mhm.

**[11:07]** K.

**[11:20]** Yeah, so...

**[11:23]** Maybe you may drop the message in the chat. OK.


### Generative AI models & agents  `[11:28]`

**[11:28]** If you are using any Genia model, any cloud platform, if you're using, or like if you're using for what applications, it would be interesting to hear. OK, so now what what this models are, these generative AI models? OK, these are.

**[11:48]** Nothing but the large language models. Okay, so these are pre-trained models. So in ML machine learning workspace, we used to train our own models, right? But there are models available which are pre-trained.

**[12:07]** Right, and these models, these are massive models trained on huge amount of text corpus, and so they have learned all kind of text which is publicly available with a given knowledge cutoff date. So, for example, if it is a GPT.

**[12:26]** a 4.1 model, right? It has a knowledge cutoff of July 2024. Okay. If we talk about more recent model, let's say from OpenAI, GPT, let's say 5.4, we have, it is trained on all kind of text till August 2025, right?

**[12:45]** So there are open AI models, or so we are not restricted only to the open AI models in Azure. We have the Foundry portal where we can build a generative AI solution, and it supports deployment of LLM, not only limited to...

**[13:05]** open AI. We can deploy Mistral models, right? Models from anthropic, including sonnet models, for example, deepseek models are there, right? So even we can deploy A hugging face model on the Foundry portal.

**[13:25]** So, these are the elements which are quite massive models, and we can simply create a Foundry project.

**[13:39]** Right, and we go ahead and with some few clicks only, we can go ahead and deploy a model, right? For example, we are deploying GPT 4.1 model now, so this is a type of large language model, right? We may deploy.

**[13:58]** A small language model also, right, which is having lower reasoning capability and maybe it's more useful to do day-to-day task and it provide a quick response as compared to the large language models, right? So.

**[14:17]** There are SLMs available that we can deploy. Like for example, we have 5-4 model. So this is a model from Microsoft. And once we are able to create a funded project, we can deploy this model. OK, now.

**[14:33]** That's a Jenia model, right?

**[14:37]** Okay, and these models, since they are trained on huge amount of text, they know text from different domains. So any query, if you have, we may write the query as a prompt. So we may provide the query or we may instruct the model.

**[14:55]** by writing a prompt and the model generates a response. So we may say, write me a, give me a short paragraph on artificial intelligence. It understands the human text here, the human text in a natural language form, right, able to understand.

**[15:15]** what the user wants to do, what is the user intend, right? And it generates the text, right? So it will be writing a short paragraph on artificial intelligence. Us maybe asking some question, right? Genia models can answer that, right, based on its knowledge base that.

**[15:36]** That it has.

**[15:38]** Right now.

**[15:42]** There could be some use case where the user intent is slightly complicated, which...

**[15:50]** Genia model alone cannot answer. So for example, we have Genia model deployed. Let's say we deployed GPT 4.1 model and we write a prompt that, can you tell me who won IPL 2026? Right. So.

**[16:09]** Or maybe we may ask, what's the current weather information in Dubai? OK.

**[16:17]** Right, so Jen AI itself cannot answer this question, okay? Or maybe we write a prompt that, can you, this is my Python code, and can you write test cases for my code and then execute them and...

**[16:38]** Provide me the results of the test. OK, so here we see that these tasks, right? We have these prompts. OK, Genia model cannot answer these prompts on its own. The reason because the current information.

**[16:56]** It's going beyond the knowledge cutoff, and it doesn't have that information. Gen AI model can write a code, but it cannot execute a code. OK, and there are some further, like, like let's say we are integrating a generative AI model with with a server.

**[17:16]** We have some data available at the server, we have Azure SQL database, which can be accessed via an endpoint, right? So JNM model cannot go to that endpoint, retrieve the data, and try to answer the user query. Okay, so it cannot.

**[17:35]** do that. So to improve the capability of the generative AI model, we build agents which have higher reasoning capability and it is using the model, the generative AI model as a brain.

**[17:55]** With tool extension with tool calling capability, so agents are.

**[18:04]** are nothing but the LLM or generative AI model with the tools. Tools could be, it could be inbuilt tools.

**[18:16]** So it could be an inbuilt tool provided by the Microsoft or if you are using some other platform, maybe LangChain framework, if you are using, there are tools available over there also. So there are inbuilt tools available. For example, we have code interpreter tool.

**[18:35]** So this is a tool. Using this tool, the LLM can not only write the code, execute the code, look at the output of the code execution, and it can answer the user query.

**[18:50]** Inbuilt tool could be a Bing tool.

**[18:55]** So that the LLM.

**[18:57]** Can use the Bing, which is a Microsoft search engine, right? Using Bing, it can retrieve certain websites and retrieve the web contents and try to answer the user query. OK, other tools could be like Outlook tool we have to connect to an output.

**[19:18]** Outlook mail so that LLM can access the mail, summarise a mail, maybe send a mail on our behalf. Okay, so this all things can be done. Now, we don't have only the inbuilt tools, but in the foundry portals, we can create our own custom tools also.

**[19:38]** This also we can do.

**[19:41]** Vatan.

**[19:44]** If, let's say, we have our own logic, maybe we write that logic as a Python code in a simple Python function where we are connecting to an API holding certain data, and this function is returning certain.

**[20:02]** Data, or so it returns certain results.

**[20:07]** Right, so this can be this logic can be wrapped as a tool. OK, so LLM can, depending on the user query. OK, let's say the query is, can you tell me what is the date of delivery of my order number 123?

**[20:26]** Agent understands, so agent gets the query. It uses LLM to take a decision that, should I make use of a pool or not? Because if that's a query, LLM cannot answer on its own. It uses the tools connected to it.

**[20:45]** So it will be using the custom tool.

**[20:49]** This custom tool will be called, which returns the result.

**[20:54]** to the LLM. LLM once it gets the result, it has the context available now and then it is able to answer the user query that this is your data of delivery.


### LLMs with tools — agent examples  `[21:07]`

**[21:07]** Okay, so here we note that LLM or the generative AI model, if it is connected to certain tools, maybe tool one, tool two, etc., it can make use of that tool. The tool has certain capability, the tool returns certain value back to the LLM.

**[21:26]** And LLM can answer the user query.

**[21:29]** So that's an agent, right?

**[21:34]** So just to give one simple example, let's say the prompt is, can you tell me the weather information?

**[21:44]** in Dubai or something. OK, then.

**[21:48]** The LLM, if it is connected to the Bing tool, the LLM gets the query, it understands that the user wants the correct current information, right? Then it cannot provide current weather information on its own, so it will be calling this tool.

**[22:09]** It will provide a tool input so that the tool can use that input. It will go and do web searching, etc. It will provide what it has retrieved. It provides the results to the LLM. Maybe the Bing tool is going to MSN any.

**[22:31]** any weather API, any weather website, and maybe going to certain news, for example, and...

**[22:39]** Getting the context, providing the context to the LLM. Now the LLM has the answer to the user query and it answers to the user query then.

**[22:51]** So, that's how we can leverage the capability of LM by making a tool call. So, it depends on the user intent, what the user wants to do. OK, and we can build an agent. OK, so to build an agent solution.

**[23:10]** Right, we need to 1st deploy a large language model and we need to provide a job description.

**[23:20]** What is the role of that agent? Maybe it's a simple use case where we are uploading a document and the agent is do is supposed to do the summarization, right?

**[23:33]** So we need to specify the description of the agent also that what is the role of the agent? What is the instruction of the agent? What is the role, what it is, what is the scope of work that it does? So maybe like we may specify the instruction that you are a...

**[23:54]** Summarizer.

**[23:56]** you will be receiving a document and gather information from the document and summarise in 200 words. Okay, so we may provide such instruction. If you're using agent for, let's say, to do the content writing, we may give the instruction to the agent.

**[24:17]** that you are a content writer and you write engaging articles.

**[24:25]** You can use tools connected so that you can get recent trends, recent information about a topic provided by the user, and you should be returning your results into paragraph or something. Okay, so that kind of instruction we need to provide.

**[24:45]** Okay, so that agent is guided properly and it works as expected. Okay, so another example could be, let's say it's a travel agent. So we specify that you are a travel agent and your role is to refer to certain document.

**[25:05]** Answer the user query. If user asks query anything not related to the travel, simply say I don't know. Okay, so you should be, the agent should be avoiding any other chit chat with the user, right? It should answer only travel related queries. So that's a.

**[25:25]** role we may define, okay, to the agent. So this will be controlling the agent behavior.

**[25:33]** Right.

**[25:35]** So based on the user intent, what is a business use case? Okay, we may have an agentic solution built where we provide a job description. Okay, now the agent is the solution is built considering who is the target audience.

**[25:55]** Right, whether it's the end user.

**[25:58]** So if it is end user, then agent solution is to be deployed as a web application.

**[26:05]** This we can do, right? Or if it is not end user, maybe it is used for internal purpose, right? So we should be knowing what type of users will interact with the agent, right? All right, maybe it's the developers using the agent to...

**[26:24]** To do test unit test case testing of scripts, we are using what the agent solving. OK, what pain points the agent solution is addressing. So, for example, if let's say we are building an agent which is a support ticket agent.

**[26:46]** And we have guided the agent that you should be collecting e-mail ID of the person, technical description of a person, and raise a support ticket as a text file, so this will be bringing automation in our.

**[27:04]** In our business process, right?

**[27:07]** So, so what pain point it's addressing it? So it's avoiding the manual work and bringing automation in our in our process, right? Maybe it's helping us with getting recent data from websites, or maybe it's a...

**[27:27]** personal assistant, personal chatbot we are doing, building so that we can improve the user experience. Right. So maybe we are building an insurance agent helping.

**[27:41]** The.

**[27:43]** The users, right? So users come to the to a web page, make a chat with this insurance agent. The insurance agent may connect with certain documents, answering the queries related to insurance, referring to that document, so making like...

**[28:03]** a chatbot can answer the user's query, right? So improving or enhancing the user experience. So what pain points, right, the agent is addressing, right?

**[28:18]** Further going ahead, let's see, like, so we can even define the suggested prompts, right? So, if let's say we are...

**[28:29]** Building an agent, deploying to a web page here, deploying as a web application, like we may provide certain display prompts, like which will be guiding the user that how to interact with our agent, so it may provide a display prompt.

**[28:50]** as a part of the chat window or maybe below the chat window so that the users, when they come, they can understand, right, how, what prompts I should be writing, in what tone I should be writing, right, and interact with the agent. Okay, so it could be, we may.

**[29:10]** specified display prompts in our solution that we are building, command prompts which are nothing but the system instructions, right? So that has to be written clearly.

**[29:24]** so that the model objective is clear and it behaves as expected.

**[29:31]** We can build the agent depending on what is the capability of the agent that we want to build. So if it's a simple agent, right? So if let's say the use case is building a chat bot, okay, referring to certain document and answering the user query.

**[29:51]** So in this scenario, we need to build a chatbot which can provide.

**[29:57]** the response in a quick way so that the user remains engaged in a conversation. Maybe the use case is a summarization. So these are primary functions where we may not need an LLM to do that task. We may go with some models like

**[30:17]** Five model, which are not high reasoning models, we may use such SLMs which can do basic NLP tasks like summarization of a document or...

**[30:34]** or let's say doing the sentiment analysis, understanding the intent of the user, right? So these are some primary functions which can be catered by cost-effective, okay?

**[30:50]** A sufficient reasoning model, but if let's say the function is complex, the task.

**[30:57]** Provided to the model is complex, right? For example, the task is...

**[31:05]** The LM is supposed to gather information from the web pages based on the content retrieved from the web pages. It needs to prepare a report and after that it needs to export the report as a docs file.

**[31:23]** Okay, so here LM needs to make a tool call, okay, to access the internet content. And then further, it needs to write the code, execute the code, to generate a document. So the LM need to interact with multiple tools here, right? So.

**[31:42]** If the task is complex, tool calling is to be done, we should be selecting a model which can handle tool calling. So these LMs should be having high reasoning capability.

**[32:00]** Okay, so that they can take a decision whether I should call tool one or tool two and it should be able to make a tool call, get the tool output. Maybe it need to call another tool and getting the response from that tool also. So it need to go iteratively, right?

**[32:20]** trying to perform the user task, right? So it should not forget in the middle like what it was doing. So it should be able to handle some large amount of text and work iteratively, right, and try to do the task. So models required is.

**[32:39]** a high reasoning model, maybe we can go with GPT 5.1 model or like the leading models, the high reasoning models available from different vendors. So if the model is supposed to refer to certain data, provide the answers to the users, then.

**[33:00]** We should be going with a high reasoning model.

**[33:04]** Further.

**[33:08]** If, let's say, let's take another example. If we have, let's say, CSV file, okay, and we want agent to do certain.

**[33:17]** calculations, right? Certain it need to 1st get the insights from the data, calculating certain risk factor, getting trends, it is able to find in the CSV file. So where mathematical equations are there, maybe it need to do certain calculations.

**[33:37]** Based on the calculation, it needs to do some inference. So these are certain scenarios where a model that we are deploying should be a high reasoning model. OK.

**[33:50]** Now, capabilities, so we may choose a model, so a model selection is important, right? Which model should be using for a given use case for a given task, right? That model selection we can do then.

**[34:09]** We may want to put some restrictions on our AI solution. So for example, let's say we are building a chatbot connected to certain healthcare records, the patient healthcare information, PHI data we may have. And if let's say the user comes in.

**[34:28]** and ask, can you tell me the account details of this person? Chatbot has the answer and it provides the account number details of a person, maybe insurance ID of a person, for example. So in this case, the chatbot.

**[34:48]** is providing PIS, the personal sensitive information, the personal identifiable information or the sensitive data is getting passed, right? So the chatbot is not behaving as expected. So we may want to add certain restrictions.

**[35:07]** so that even if the chatbot is generating a content which contains sensitive information, the generated response from the model need to be passed through certain content filter, certain safety filters, certain text philtres basically.

**[35:27]** And if the safety philtre finds that, right, the response contains sensitive data, those sensitive data will be masked. It could be, so the response may be blocked also, not provided to the user.

**[35:42]** So we may want to add certain safety features.

**[35:48]** Right, so that the application is enterprise grade and right, and the application do not it behaves as expected, so these are so based on the capability, like based on the use case, we may do the model selection.

**[36:08]** We may add certain components to our ES solution, like content filter, and try to build a robust solution.

**[36:18]** Then...


### Evaluating GenAI before production  `[36:20]`

**[36:20]** Let's say we are building an AI application and generative AI solution. Now, before we put it into the production, right, we need to test our application, right?

**[36:35]** So, we need to do evaluations. Evaluations can be done in the foundry. In the foundry, there are...

**[36:43]** Evaluators available, so there are certain evaluators or scorers are available, which allows which allow us to evaluate a model.

**[36:56]** For example.

**[36:58]** We have evaluator or even we can do manual evaluations also. So let's say we prepare certain test prompts.

**[37:09]** Right, we pass it to the agent here. Agent provides a response here. It generate a response. We may have ground truth values or maybe this responses will be picked up, provided to the human supervisor.

**[37:27]** Which may grade the responses into metrics, so we can have a rubric of metrics, like it can calculate the relevance score.

**[37:39]** It cheques that for the given prompt, the response generated by the model is relevant to the query or not. So out of five, the human can give a score maybe for 100 prompts like that.

**[37:57]** Right, and we can get the relevant score. Maybe we have the ground truth. What is the expected response of the model? So model generates a response. There is a ground truth or the expected response. Human can look at response and the ground truth.

**[38:15]** And able to score the similarity.

**[38:22]** Between the two texts, between the response and the expected response, so it can provide the similarity score. So, but using human, it's subjective because, right, the it's a manual process and time consuming and it may not be useful for, let's say we have.

**[38:43]** 500 test prompts and...

**[38:48]** Right, and human would be.

**[38:51]** assessing all those 500 test prompts. So we may go with automated evaluations also. Okay, this can be done in a...

**[39:03]** Azure Foundry, wherein we have the test prompts, we have the responses generated by the model. There are evaluators available which can evaluate.

**[39:16]** The text of these two, so how that evaluator works, the evaluator is basically another LLM which is judging another LLM, so there is a...

**[39:28]** There is a teacher element.

**[39:32]** or teacher model we have which gets the prompt.

**[39:37]** the responses of, let's say, a model, let's say GPT.

**[39:45]** 4.1 mini.

**[39:47]** Good.

**[39:48]** Okay, so this is our student LLM.

**[39:53]** Right.

**[39:55]** So the teacher LLM would be getting the responses and the test prompts and it can grade the student LLM. So, right, in terms of, let's say, relevance score, the fluency score, how fluent the response of the model is in terms of similarity score, right? So the teacher LLM has a

**[40:07]** Thank you.

**[40:16]** rule that it works as a grader or a scorer, and it would be scoring the given text. Maybe we have the ground truth values with us, so it can take the ground truth, take this response generated by the model, and tell how well

**[40:20]** It.

**[40:35]** the responses. Is it close to the ground or not?

**[40:37]** Ohh.

**[40:41]** Yep.

**[40:43]** Hey, what's up?

**[40:47]** Rohit.

**[40:47]** If, if that's.

**[40:52]** Maybe I can't.

**[40:53]** But you would get in a day.

**[41:00]** Correct.

**[41:06]** Now, so we have seen this two approach. Either it could be an automated approach, it could be the human supervisor approach, or the manual approach to do the application evaluation, right?

**[41:24]** Even we can go with the shadow rating, where we have a mix of the automated and manual, because there are some cases where we have some domain-specific.

**[41:43]** prompts, right? Maybe it's a prompt related to legal advice or prompt related. So maybe it could be a medical advice. So for example, if let's say we have a prompt that a person having a severe

**[42:01]** pain in the left side of the chest, right, and the person is sweating, right? What could it indicate, right? And if we give it to the LLM, right, it may tell that it's a chest pain and you should be taking such and such medicine or like.

**[42:22]** it may give certain suggestion that what it would be indicating, right? So that would be the response of the model, okay? But this response is quite in general, right? We need a human evaluator to evaluate the response of LLM, right? Because, right?

**[42:41]** Because, in this case, we need the manual evaluation of the LLM, right? Automated evaluation may not work very well, right? If we, if we try to do automated evaluation, the prompt, the test prompt.

**[42:58]** and the response of the model, okay? They seem justified, right? But if it is a manual, right, it will be looking at the severity, the risk level, and the manual evaluator may say that the response should not be a chest pain, right? It should be a sign of heart attack.

**[43:17]** Right, because that's more critical, and it should be avoided, so the manual evaluator should be acting for.

**[43:27]** critical for the edge test prompts, right? We need to do the manual evolutions. The expert evaluation has to be done, right? So we can have shadow rating while evaluating our application, which combines both automated

**[43:48]** With so automated with general test prompts, but if you have some edge test prompts, right, some nuance, right, cases, if we have right where expertise is required, the human expertise is required, so we can go with that.

**[44:07]** manual evaluations for those kind of prompts, right? So that's called as a shadow rating, right? Which is basically a mix of automated and manual evaluations. We'll talk more in details further when we go ahead and talk about evaluations.

**[44:27]** Okay.

**[44:29]** So, the AI solution should be evaluated.

**[44:34]** Well, so we may need to prepare test data, prepare certain smoke or the basic test, preparing the test prompts.

**[44:44]** Right, we may go with automated evaluations. We may try to have a mixed coverage, like that is, we should be including test prompts with variety of scenario so that the model should be able to handle a diverse prompts and.

**[45:03]** We should be able to know how the how our application is behaving for diverse use cases, right, for potential different prompts, right?

**[45:15]** So this these are the things we need to look at right when we are trying to build a robust AI solution. So before we go ahead and OK, yeah.

**[45:31]** So I think that's all clear so far.

**[45:37]** And think, would you like to add here?

**[45:48]** Alright.

**[45:50]** So if it's all good, so depending on our use case, we should be selecting a model, right? So we should be going with a few candidates for building our AI application. So there has to be 3 to 5 model.

**[46:09]** listed so that we can use them while we are going ahead with deployment of our AI application. So there has to be a lead model, which is the primary model, which takes the prompt, generate a response, right? So the lead model should be a model.

**[46:30]** With good capability to perform a use case, so maybe it would be a GPT 4.1 model. Now, it may happen that a session of GPT 4.1 may time out, or maybe there is high traffic and...

**[46:48]** it may fail, right, providing a response. So in the such scenario, we should be having an alternate model available, which could be a low cost deployment, maybe like GPT 4.1 mini model, which is more cost effective than GPT 4.1.

**[47:07]** Right, so it could take such a request which the lead model is not able to, if the lead model is not able to deliver.

**[47:17]** Still, if it fails, we should be having a backup model, so it could be a open source model available, or it could be it could be simple text rules are there, right? So, maybe providing using certain hard-coded rule and...

**[47:37]** it is providing a response to the user, right? So that could be the backup.

**[47:43]** Model for our AI application, so we should be selecting model and for our application, not just single, but the lead alternative model, for example, right? While doing model selection, we need to.

**[48:02]** Take care of our use case, right? What is the requirement, right? Do we want a real-time response? So if you're building a chatbot, real-time response is important, right? So the latency of our model should be low.

**[48:22]** Right. So we may go with SLMs for building a chatbot. We may not be using a high reasoning model which has higher thinking capability. It thinks for a longer time to plan how to answer the user query. So if the use case is simple, we may go with a lightweight.

**[48:42]** Model which can do real-time generation of the text for complex situations, right? Where the task is complex, then we go with high reasoning model, right? Then...

**[48:56]** Maybe we want a model which can take a batch of input and generate the response that, right? Depending on capability as well, right, we should be able to select a model. Let's say we built an application which is supposed to get an image from the user.

**[49:15]** maybe there's an image of an error, and based on that error screenshot, the model generates a response, provides a suggestion. So in that case, the model should be a multi-model model that we need to deploy, which can handle input as text and the images both.

**[49:34]** And generate text as an output.

**[49:38]** Or maybe there is another use case where model is supposed to generate an image. Maybe like for marketing campaign, right? We may want to create certain posters.

**[49:51]** Right, creating avatar for profiles, for example, right? So in those scenarios, we need to deploy a model which can generate an image.

**[50:03]** So, right.

**[50:07]** Maybe the model is supposed to make a tool call, right? So that depends on what capabilities required. We should be going ahead with the model selection, right? So there has to be an operational fit between the cost of consuming the model, what infrastructure is required.

**[50:27]** to run the model. So if let's say...

**[50:31]** The application that we build is expected to have low traffic, right? Then we may go with a lower VM and deploy our application, OK?

**[50:43]** If it's a high application, high traffic demand, right, we may go with a with a larger VM, right? Okay, but if if we use a larger VM for low traffic, then right, we are wasting our resources, the VM remains idle, for example, right latency and...

**[51:05]** So, these are, we should be considering all the criteria and looking for a best fit, the operational fit, and while selecting the model.

**[51:17]** So even in the Foundry, right, we have a model catalogue section where we can see what all models are available that we can use. And here we have seen already, like once we do the model selection,

**[51:35]** We may customise the model as per the use case. Right. Let's say we selected GPT 4.1.

**[51:43]** Then we need to update its instruction.

**[51:47]** or the system instruction or the prompt, how the model should behave. Maybe we want it to connect with certain tools.

**[51:56]** Connect with certain knowledge, the documents, right? And once you are able to build an application, we need to evaluate the application on test prompts, do the evaluation with rubric, right? Find a good balance between how much cost is like.


### Token-based cost  `[52:15]`

**[52:15]** So, cost would be calculated as per the tokens token usage. OK, how many are the input tokens, which are the prompt, which are nothing but the prompt text?

**[52:30]** the output tokens, right, the generated text by the model. So this constitute the total tokens consumed. And based on the tokens usage, the pricings are decided. So model should be able to generate sufficient amount of text, but not much.

**[52:49]** else there would be, so model should be giving an accurate text generation, right?

**[52:57]** without compromising on the number of tokens generated.

**[53:03]** So there has to be a good balance so that the model satisfy the quality metrics and having a reasonable cost as well, right? And.

**[53:16]** There would be a cost while operationalizing the solution, monitoring our solution, right, when we can create certain resources, use of Azure Monitor, for example, right, do the tracing.

**[53:32]** Of our application right where we can debug how how's my application doing OK.

**[53:41]** Great. So in Foundry, let me take you to the Foundry portal and we'll explore how we can deploy a model. What's a model catalogue there? We will be looking at the UI, right? Different, what tools are there in the Foundry portal?

**[54:02]** So, let's get going then.

**[54:06]** Let me go to Foundry Portal.

**[54:19]** So.

**[54:23]** Over here, I'm able to log in to.

**[54:26]** my subscription here and let me go to foundry portal by

**[54:35]** Going to ai.azure.com, so this is a foundry portal.

**[54:44]** Let me log in.

**[54:58]** Right now we see there are two projects already available created here.

**[55:06]** Okay.


### Foundry portal — model catalog & deployment  `[55:13]`

**[55:13]** So maybe we can switch to new foundry also we can do that. Maybe I'll.

**[55:20]** Okay, let me.

**[55:23]** So in this Foundry portal, I may go to one of the projects, let's say, or else we can click on start building and we need to create a new project here.

**[55:43]** All right.

**[55:45]** So, I'm in a project, and...

**[55:53]** We may go to Discover.

**[55:57]** Discover tab, and here we can see the featured models available on the Foundry. Maybe we can view all models. This can't be done. Okay, we can go to Model Leaderboard and see.

**[56:15]** Right, which are which are leading right, which LLMs are leading for a given task.

**[56:22]** We can explore what all tools, inbuilt tools are available, right? Using which we can connect and build our agents.

**[56:32]** Right, so let me go ahead here.

**[56:39]** Let's say view all model.

**[56:45]** And over here we may see inference task that based on the task we may.

**[56:56]** Based on the task, we may deploy a model, OK?

**[57:02]** So currently, as we see, the Foundry supports more than 11,000 models for deployment, right? This includes open AI models like GPT models.

**[57:15]** The opus model, right, anthropic models are available, deepseek models, right? Even we can find hugging face models, right? Meta models like llama models are available as well. So we have quite a variety of models available for deployment, right? And.

**[57:35]** We can go to inference task and let's say

**[57:40]** The task is doing the chat completion, making a chat with the model, right?

**[57:49]** So these are the models available, right?

**[57:54]** Maybe.

**[57:56]** We want to use LLM for detecting a language. Maybe we want to do document translation.

**[58:05]** Right, we want to do image classification.

**[58:14]** So these are different inference tasks. Maybe the task is to do the summarization. So if I click on this.

**[58:22]** These are the models available, right, for summarization purpose, okay?

**[58:34]** We may select the model, and...

**[58:42]** We can then go ahead and deploy the model.

**[58:46]** This can be done. Let me go back. Even, oh, yeah.

**[58:56]** So we can see these are the hugging face models of the label. Let me.

**[59:02]** Just uncheck it.

**[59:07]** All right.

**[59:10]** So, based on the task, we can philtre out the models and, right, we can do model selection.

**[59:20]** Then let me go to compare models section where we can compare the models. So let me compare 2 models. Let's say for a given use case, we selected GPT 4.1, GPT 4.1 mini.

**[59:38]** So, before we take a decision which model we should be using, we can compare them, OK?

**[59:47]** So right now we see GPT 4.1 has higher quality.

**[59:53]** So quality is basically, it's an average of all the performance metrics, like relevance score, groundedness, GPT similarity score, F1 score of the model. Okay, right. So there are certain metrics, right? The average of that.

**[1:00:13]** It will give the quality index and it has higher quality index. GPT 4.1 is more safe to use, that is, it's able to block.

**[1:00:26]** any prompt injections, right, able to block prompts which contains hateful message or violent prompts, abusive prompts, right? Those are getting blocked. So it has the lower safety value it indicates, the higher is the rejection.

**[1:00:51]** So, it's a better model, right?

**[1:00:56]** We have lower cost for GPT 4.1 mini, right? Throughput is the, it's basically how many requests it can handle over a time period. So GPT 4.1 mini has a higher throughput.

**[1:01:16]** Okay, so it can handle more number of requests in a given time. So because it has lower latency and can process more requests in a given time period.

**[1:01:31]** Alright, so both the models can do tool calling as we see both are tool calling enabled.

**[1:01:38]** Both can do the streaming, that is, so streaming is getting the text in the output as they are getting generated in real time, rather than all the text once the LLM generates, and then it is provided to the user. So, instead of that, we can do real-time streaming and...

**[1:01:59]** as a text is generated that appears as an output to the user. So these are...

**[1:02:07]** So this is way how we can compare the models, right?

**[1:02:20]** So we can look at the model leaderboard also and we can see.

**[1:02:27]** The.

**[1:02:29]** The top models related to the quality, the safety, right? The lower the value, the better is the safe model, right?

**[1:02:41]** Throughput tokens per second, right?

**[1:02:45]** So, throughput is measured in terms of the amount of togles generated per second. The higher the throughput, the better, the more requests the model can take, the more text it can generate in a given time period.

**[1:03:02]** So maybe I go ahead, compare GPT 5.5 with Opus 4.6. Okay, these two I'm selecting and I can compare them.

**[1:03:17]** Right.

**[1:03:19]** Okay.

**[1:03:21]** Before we go to the trade-off chart here, let me click on compare models. So that's how we can, we have seen this table and we can compare the models. Now we see the trade-off chart, like which is comparing the quality index right now with the cost.

**[1:03:41]** So the benchmark qualities compared against the cost. Maybe instead of cost, we may compare with the throughput or the safety feature of the model. And right now, all...

**[1:03:56]** So these sub models are available. Let me just take two models. Let's say.

**[1:04:03]** Let's say one nano model GPT 5.4.

**[1:04:12]** Okay, so these ones are selected.

**[1:04:18]** Maybe I'll just compare 2 models here, GPT 4.1 and let's say.

**[1:04:31]** Let's say the cloud model here, not for open one. Maybe we'll go with let's compare GPT 5 point.

**[1:04:45]** Let's take a more recent model from GPT.

**[1:04:49]** Let's say, OK, let's go with GPT 5.4.

**[1:04:54]** OK, that's fine, so we know that which model has a higher.

**[1:05:02]** Cost, it's the...

**[1:05:05]** The Opus 4.6, right? It has a higher cost. It also has a higher quality index. OK, maybe I compared GPT 5.4 with.

**[1:05:17]** 5.5, let's see. So 5.5 is better performing and it is more expensive. But if let's say the requirement is building a chatbot, GPT 4.1 is also good. So we may go with a lower quality index, we can build a chatbot.

**[1:05:37]** Why we need a pricier model if the use case is OK? Yeah, so that's a trade-off chart we can see, right?

**[1:05:51]** So further you can explore, right? So here we see these are.

**[1:05:58]** Like for different task, let's say by scenario, right? We can look at the leaderboard. So for example.

**[1:06:10]** The model.

**[1:06:12]** Let's say we want to build a solution with a good reasoning LLM. So we may go with Opus 4.5 and GPT 5.5. So it's providing top five models based on the reasoning capability, based on coding skills it has, right?

**[1:06:31]** We may choose one of the models from this so we can see codex is there from GPT.

**[1:06:38]** Right.


### RAG app & endpoints  `[1:06:42]`

**[1:06:42]** Let's say we are trying to build a ride application, right, where LLM is connected to a document. It's answering the questions by referring to the document. So in RAG, the groundedness is an important metric, right? How well the model is grounded to the given data. So because the model may hallucinate,

**[1:07:03]** It may provide the response by not referring to the document, but it may give a general answer. So higher the grounded test value, the better the model can refer to connected document and provide a response. So these are the top five models we have.

**[1:07:24]** So, these are these models are evaluated on a global.

**[1:07:31]** data sets, right?

**[1:07:34]** The performance is compared and we can see the leaderboard here.

**[1:07:43]** All right.

**[1:07:47]** Let me go to the build section here.

**[1:07:52]** where we can go ahead and deploy a portal.

**[1:08:07]** So.

**[1:08:10]** We may deploy a base model, a foundation model, even we can fine-tune a model and then we can deploy that. So right now deploy a base model.

**[1:08:22]** So, we can simply go ahead and...

**[1:08:25]** select, let's say GPD.

**[1:08:28]** Four O.

**[1:08:31]** We can select our model.

**[1:08:40]** And we can go with the default settings, right, with the default quota, right, else we can go to custom settings. We may define the provision throughput, right, where we have a dedicated compute to run our model, right, that.

**[1:09:00]** with specific guardrails with our own SKU, right? So we may go with some premium tier and deploy the model. Or else we can simply go with the default settings and the model would get deployed that.

**[1:09:16]** So here we see we are able to deploy a model. Maybe we can make a chat. This is the instruction. You are an AI system that help people find information. Let me just simply say hi in the chat playground.

**[1:09:34]** So it says, how can I assist you today? All good.

**[1:09:41]** Okay.

**[1:09:43]** So we can explore the deployed model in a chat playground.

**[1:09:48]** We can go to detail section and see we can we can get the endpoint here.

**[1:09:56]** Right. So this model is deployed to this endpoint. So from our client application, we provide the endpoint information, the key, the API key, right, to consume the model. We create a client handle and we submit a request, right?

**[1:10:14]** the model deployed generates a response and the response is sent back to the application. So we can consume the model by using the endpoint in our client application. This we can do. Maybe I'll just go back here and we can see.

**[1:10:35]** Call model. So how we can call this model using an API? We have a two option like using completions API or responses API.

**[1:10:47]** So, completion API is the...

**[1:10:55]** This we can use to complete a prompt. So we may use completion API. Using this API, we can submit the request to the model and get the response. So we may cheque here that we are able to 1st create a client handle.

**[1:11:13]** By passing endpoint, the API key, using chat completion.create, we are submitting the request to the model.

**[1:11:23]** where the prompt is, what's the capital of France? And it provided a response. Now, we have...

**[1:11:33]** a new API that's responses API and it's more flexible. It is it is stateful like so if you're using responses API, we start a conversation thread and we make a chat with the model. So the conversations are.

**[1:11:52]** Stored in the memory, right?

**[1:11:56]** And we need not to worry about the conversation happening. It is stateful API. And it's more flexible when we are trying to do our tool calling, when we are trying to build an agent. We can do agent building or we can use agent using

**[1:12:16]** completion API also, but we need to write more logic in that case. Here, it's easy to work with this API. So when we build an agent, mostly we would be using responses API and consuming the model. So we can see here.

**[1:12:36]** Client.responses.create. So this will allow us to submit a request and get the response. Further, we can cheque here.

**[1:12:50]** We can use curl command to consume the model. Right now we are using open AI SD key.

**[1:12:57]** to use our model, right?

**[1:13:00]** Just.

**[1:13:02]** The.

**[1:13:08]** Thanks.

**[1:13:14]** So, as we see, we are using Open AI SDK and...

**[1:13:20]** Creating, getting a client handle.

**[1:13:23]** and consuming the water.

**[1:13:26]** Right, authentication could be entry ID or the key authentication.

**[1:13:32]** So, where we specify the API key and...

**[1:13:36]** Use the the client, OK?

**[1:13:41]** So that's a sample code, how we can consume a model via the application.

**[1:13:47]** Okay.

**[1:13:49]** So maybe I'll just go ahead and...

**[1:13:55]** Let me delete this deployment. We don't need it.

**[1:14:03]** Alex.


### Create an agent & evaluators  `[1:14:04]`

**[1:14:04]** Let's look at other tabs like we can create an agent also, right? So if let's say we are using GPT 4.1, it can be saved as an agent. It can be connected to certain tools. So there are inbuilt tools available like code interpreter, file search is there.

**[1:14:23]** Using file search, we may connect to a document and we can do the rag.

**[1:14:30]** the retrieval augmented generation, we can connect to Bing web search tool using MCP, the model context protocol. We can connect to any MCP server, right? So it's easy to connect with, let's say, any MCP server available, right?

**[1:14:51]** So we can upload file directly or...

**[1:14:56]** We can connect with a knowledge base also. This can be done. There are guardrails available, so we have a memory.

**[1:15:05]** So since you are working with responses API, there it's a stateful API. There is short-term memory available where we are able to create a conversation and store the chat history.

**[1:15:21]** Guardrails are there, so when we do any model deployment, it comes with a default guardrail or a default safety filter, the content filter.

**[1:15:34]** So, that's a guardrail available. Right now, we see this is a default guardrail, which cheques the sanity of the input prompt.

**[1:15:49]** Right, so it's coming with certain controls. It can prevent gaolbreak attacks. Content safety is there like abusive prompts or the hateful prompts. So there are four filters, the sexual, abusive, or the hateful and violent.

**[1:16:08]** Right, these are four content safety features are there. Protected material philtres are there so that any response generated by the model, the output response, should not contain the copyright text or copyright images. Right.

**[1:16:28]** OK, so that's a guardrail available. We can create a one on guardrail also, depending on the use case.

**[1:16:37]** So we may see like we can deploy a model, we can use the model, create an agent, right? Connect with certain inbuilt tools. We can create our own tools, knowledge, memory. Okay, data can be uploaded and be used as a knowledge and.

**[1:16:56]** we can build a rag application. Model evaluations can be done. So evaluations are like, it could be a manual, it could be automated. And if you are doing with automated evaluations, we have evaluator catalog.

**[1:17:14]** So, where we have inbuilt evaluators.

**[1:17:22]** Right, like, for example, let me let me say this relevance evaluator we have. So what this evaluator is?

**[1:17:32]** It's A evaluator which assess how the how well the response matches the user intent or the question. So there would be a prompt, there would be a response generated by the model, then we pass it to the relevance evaluator. It provides the relevance score, right?

**[1:17:51]** in the range between 1:00 to 5:00, where 5 being the highest value. So it cheques for how well the model is providing, is giving a relevant output. So this is a built-in evaluator. We can create a Boron evaluator also.

**[1:18:08]** OK, for a specific use case, we have evaluated for groundedness. How will the model giving a grounded output?

**[1:18:17]** Et cetera, so we can cheque these evaluators others.

**[1:18:24]** So let me go back then. So that's the Foundry portal we have. Great.

**[1:18:39]** All right, let me go back then. Okay.

**[1:18:54]** Okay, so...

**[1:18:56]** When we are building a end-to-end solution, so we will have an ideation phase first, where we are defining our business use case. What is a business use case? For example, maybe we have certain logs, right?

**[1:19:17]** generated daily, an agent should be triggered at certain schedule, right? And it will be looking at the logs, summarising the log in a CSV file, and maybe sending a mail to a person. So something, some task it may do.

**[1:19:37]** It could be a chatbot, a personal assistant.

**[1:19:41]** It could be a content writer. So this could be a business use case, right? And for that use case, we need to do model selection.

**[1:19:52]** Right, what tools are required to complete that use case? So, for example, if let's say we have data available in Azure SQL DB file, right, we need to create a tool for fetching the data, providing the data as a context to LLM.

**[1:20:11]** Alan can refer to that data and generate a response, right? So what data source required, what model can is used for doing that use case, right? So we can go ahead and build an agent and we can try some basic simple prompts to know.

**[1:20:30]** The how, how?

**[1:20:34]** the agent or the generative AI, how it is behaving. Okay, so if it looks all good, then we can go ahead and build our application, right? Build an agent, right? Connecting the tools, maybe we want to fine-tune our model.

**[1:20:54]** So, fine-tuning is required, so to optimise a model.

**[1:21:01]** The first approach is to do the prompt engineering, where we are.

**[1:21:07]** Is giving a clear instruction to the model.

**[1:21:11]** what is its role, what it should do, what it should not do, right? So that will govern the behaviour of the model. So this way we can optimise our application so it behaves as expected. Further, we can, maybe we can connect with some knowledge, we can do the rag.

**[1:21:31]** Or we can connect with certain tools so that we can leverage the capability of the LLMs and it can perform a task.

**[1:21:41]** Further, if the model, if may hallucinate, it doesn't behave as expected. Maybe the style of generating the text or the tone, right, how the model generate text, if that is not consistent, even after writing a clear instruction, even the model is still.

**[1:22:02]** not behaving as expected. We can go with the fine tuning.

**[1:22:08]** We can do fine tuning.

**[1:22:14]** Or else, we can we can combine all these strategies together, right?

**[1:22:20]** And we can build our agent.

**[1:22:24]** Right, so we can fine tune models like GPT models in the Foundry portal.

**[1:22:30]** Right, we can go further ahead and add tracing.

**[1:22:38]** Okay, so that we can debug our application for a given prompts. So tracing would be telling us where our AI application is failing. So maybe like...

**[1:22:52]** If the prompt is, can you tell me what's my date of delivery of my order number this? Okay. The agent gets the prompt. It may be calling a tool. The tool returns a value and based on the value, it provided a response to the user.

**[1:23:12]** And maybe the response is not as expected. So we can add tracing so that we can look at the...

**[1:23:21]** Ohh.

**[1:23:22]** like the internally what the agent is doing. Is it calling a tool? Which tool it is calling? It's calling a tool with what input? And what is the response of the model? So everything can be logged. We can even log the span, right? The span of the chat.

**[1:23:42]** Right, what is the input time, time stamps, the output time stamp, when, how much the latency is there in generating a response? Right, so how many tokens are consumed, input and the output and the total tokens? That all can be logged.

**[1:24:02]** Right.

**[1:24:04]** And so we can debug, like what is the action agent has done and if it is misbehaving, how we can further improve our code. This can be done. So we can add tracing, we can build multi-agent orchestration patterns also.

**[1:24:23]** Using certain frameworks, like, like semantic kernel.

**[1:24:31]** We can use Land Graph, Crew AI, right? So these are certain frameworks available using which we can, even we can use the Microsoft Agent Service.

**[1:24:46]** which allow us to build multi-agent systems where agent one, let's say, is doing web scraping, passing the output to the next agent, which is doing the content writing, pass to a critic agent, which gives a feedback on what content is written.

**[1:25:07]** Based on that, agent who can improve the draught and finally we can get the report prepared, right? So we can go with multi-agents and try to solve a more complex workflow.

**[1:25:23]** Right, so we can, so this is the second phase where we are doing the experimentation, right? And deploying the model right to a managed endpoint, right? Then we can do testing our application.

**[1:25:42]** evaluating our agent. Finally, we can go ahead and publish the agent to an endpoint, maybe publishing to a channel like Slack or...

**[1:25:54]** Jira, or maybe...

**[1:25:56]** So, the agent may be published over a channel, or it can be consumed via an endpoint, right? This is possible. Once we are able to deploy the model, we need to go ahead and operationalize our solution. We need to monitor the cost, right? So, this is an iterative process where...

**[1:26:17]** We need to monitor our model with some new inputs, how the model is performing.

**[1:26:26]** In real-world scenario, right?

**[1:26:30]** So...

**[1:26:32]** how many requests it's getting per day per hour that we should be able to log using Azure Monitor. We can set alerts, right? If let's say the token consumption by our application exceeds a certain value. So we may.

**[1:26:51]** Generate an alert, and...

**[1:26:55]** Action can be taken, right? Maybe the model is not performing well in production. We may want to try improve the production code, right? So, just like how we have done in the MLOps, like we have a main branch, right, which contains the production code and...

**[1:27:15]** We may get a new branch where we are trying a different system instruction, right? And we may create a PR. And with this new system instruction, how well the model is doing? We may automate a workflow where we are doing the application evaluation.

**[1:27:37]** Is there any improvement in reduction in token usage or the accuracy of the model is improving? Is the relevant score improving? Right. That can be checked and if it is approved, then it may merge with the main branch. Right. Either.

**[1:27:56]** Maybe we want to change the LLM, right? Because the LLM may drift, right? This may happen.

**[1:28:06]** its performance degrades because maybe a newer version has come and we need to upgrade to the newer version of LLM. So we need to monitor the cost by tracking the token usage. We can estimate the cost, right? Is it complying to the data regulations?

**[1:28:26]** Right. Is it safe? Right. So even when the model is in production, right, we can log the prompt and the responses generated by the model and we can evaluate the model when it is in production. So evaluation can be done and.

**[1:28:45]** Based on the evolution, we may trigger an automated workflow and try to update.

**[1:28:51]** The production code, right?

**[1:28:54]** So...

**[1:28:56]** This can be done and we'll be exploring further, right, the tools like tracing component.

**[1:29:07]** In ML in in Foundry, we'll explore Azure Monitor, right? What are signals we can track and creating alerts, generating a creating a dashboard for different metrics? This this can be done.

**[1:29:28]** So that's the basics right of Gen AI Ops life cycle. So here we note that when we create the AI project, right, we may use AZD, which is a Azure Developer CLI, right? So using.

**[1:29:47]** AZD, we can it can use bicep template or use a Terraform template and it can provision resource, it can deploy the model. So that's a programmatic way how we can.

**[1:30:07]** Create the resources and deploy, let's say, an LLM. It can be done. So we have, we can use AZDCLI, or we can use certain templates.

**[1:30:22]** use the configuration file, provision the resources, deploy the resource, and right. So we can initialise a project using AZD. So for example, using AZD up, it would be using a bicep template and provisioning the resource. Initialising the project, we can simply go with AZD in it and

**[1:30:46]** It would be initializing; it would be providing a project structure, right?


### Foundry project — experiment to production  `[1:30:54]`

**[1:30:54]** With only the Foundry project created, then we can create resources by going to the Foundry UI, deploy the models, explore the models in the chat playground, right? So, once you are able to deploy the models or provisioning the resources when it's done.

**[1:31:14]** We can customise our application. We may add knowledge base, we can do the rag, current with Microsoft Fabric, okay, to connect with the data source. So there are many connectors are available, like Azure Data Lake, we have SharePoint can be connected.

**[1:31:34]** We can simply upload the files, right? Any data which is there in the BLOB storage can be connected and we can do the rag, okay? We can do model fine tuning, create certain agents by connecting to certain tools, right? So we are improving the functionality of our...

**[1:31:54]** Application.

**[1:31:56]** Right, we can make use of Foundry SDK, which is Azure AI projects. So, to install Foundry SDK, it's pip install Azure AI.

**[1:32:10]** Projects.

**[1:32:12]** So, this will install Foundry SDK, so that we can use the Foundry resources, right? So, for example, let's say we want to do the rack, okay? To do the rack, maybe we have data available in a storage account, the index is available.

**[1:32:33]** In a search service, the Azure Search Service, we need to connect the index to our LLM.

**[1:32:40]** Right, so to use the Azure Search Service, this can be connected to our Foundry project, and to use the Search Service, we use the Foundry SDK.

**[1:32:54]** So Foundry SDK allow us to use the Foundry tools. Like Foundry tools could be other services like let's say Azure Functions.

**[1:33:04]** which has certain logic and maybe it's wrapped and it is used as a tool. Connect the tool with the LLM. This we can do or maybe like using tracing.

**[1:33:20]** So, to use tracing, we need to use the Foundry SDK, use of Azure Monitor to monitor our application. So, for all these connections, we need to use the Foundry SDK, right?

**[1:33:37]** Then, prompt templates are available. We have evaluators available, tracing component, right? Content filter. So, to create resources, consume these resources, right? The Foundry SDK is required.

**[1:33:53]** So we can experiment, do application evaluation, then we can then deploy our application to production. We may use certain frameworks like semantic kernel for building a multi-agent systems to bring CICD.

**[1:34:14]** We can do GitHub actions, right?

**[1:34:18]** Right, monitor, we can, so we can monitor our application using Azure Monitor Application Insights, right, so that we can log the model performance in production.

**[1:34:32]** So.

**[1:34:34]** So we note that in Foundry, we have all the tools available, right?

**[1:34:42]** so that we can do Gen AI.

**[1:34:49]** All right, so with this information, I think I can just demonstrate this slack where we can go ahead and use AZD up and we can provision a Foundry project, right? Create other resources like...

**[1:35:08]** Application insight for for monitoring applications later on that we will be using, so.

**[1:35:16]** After that, we can go ahead and create an agent.

**[1:35:20]** And we can use the agent in the Foundry playground. OK, so that's an exercise we have, and...

**[1:35:30]** Let me, let me go ahead and...

**[1:35:35]** Let me demonstrate this. Any queries we have before we proceed.

**[1:35:56]** All right. So let me.

**[1:35:59]** Go to the foundry here.

**[1:36:10]** Alright, so we are in a project.

**[1:36:16]** And.

**[1:36:18]** OK, let me.

**[1:36:28]** Let me share the GitHub link here.

**[1:36:32]** where we can find all the lab instructions. So that's a GitHub repository.

**[1:36:53]** Okay, so over here we can go to docs and we can find all the lab instructions available. Right now we are at the first lab which is infrastructure setup.

**[1:37:08]** Yeah, which is our lab #7.

**[1:37:12]** Right, so.

**[1:37:18]** So it will be it uses the EZD up which uses the bicep template here in the intra folder and we can create the resources. So there's a bicep template available and using it we are able to create resources. I've already created the resources here and.


### Build an agent (weather agent) & prompt versions  `[1:37:38]`

**[1:37:38]** Let's now go ahead and create an agent. OK, so there is one agent already available, weather agent. OK, that's fine, but let me clone this Git repo. I have already done that and.

**[1:37:56]** Let me.

**[1:38:00]** Open this.

**[1:38:21]** So in this we have the ENV file.

**[1:38:26]** where we have updated the Foundry project endpoint.

**[1:38:32]** And we also specify the agent name and the model that we have deployed, the name of the deployment.

**[1:38:39]** So the environment file contains the details here. And so where we can find the Foundry project endpoint, we can go to home. And so for this project, here we have the Foundry project endpoint.

**[1:38:57]** Okay, so.

**[1:38:59]** To consume any resource or to create a resource in this project, we need to use this endpoint, right? And so this will allow us to connect to the Foundry resources, right? Then we have Azure OpenAI endpoint also, which allow us to consume an OpenAI model.

**[1:39:19]** which we have deployed on the Azure Cloud. So we have Azure Open AI endpoint. So we can use Open AI SDK.

**[1:39:31]** To submit a request to this model and to submit a request to model, we can use this endpoint, right?

**[1:39:40]** So once we are able to get the project endpoint, we update the environment variable there. And now over here in the source folder, we have a real, sorry, we have trail guide agent.

**[1:40:03]** Okay.

**[1:40:05]** Let me.

**[1:40:09]** And.

**[1:40:18]** So, using this PI file, we can create an agent, OK, and...

**[1:40:28]** So we see, we are loading the ENV. We are reading a text file here. Let me go with V1.

**[1:40:40]** So, in the prompt folder, there are certain prompts available, certain version prompts are there, like V1, V2, and V3.

**[1:40:52]** So V1 instruction, it's a basic.

**[1:40:56]** It's a basic instruction we have.

**[1:41:00]** So, you are helpful.

**[1:41:04]** guide assistant for this company.

**[1:41:08]** an outdoor gear company. Okay, help users with the trail recommendations, safety tips and gear suggestions for hiking. Keep response informative but concise. So that's the instruction provided. Okay, and using, so we are reading that instruction.

**[1:41:30]** Let me.

**[1:41:34]** So, that's V1 instructions.

**[1:41:40]** All right.

**[1:41:46]** So we are able to read the text file.

**[1:41:50]** Uh...

**[1:41:51]** By passing the the Foundry project endpoint, we get the project client here.

**[1:41:57]** Then using project client, we are creating our agent in Foundry, right, which uses the model 4.1, which uses this instruction, and we are able to create an agent with the version. So let's execute this file. That's Python.

**[1:42:18]** Yeah.

**[1:42:22]** All right.

**[1:42:26]** The.

**[1:42:29]** Let me, let me go ahead.

**[1:42:38]** It's.

**[1:42:58]** So we note that the agent is created, the version is 1. We can go to the build, we can go to the agents and we can see we are able to get our agent. We can open the agent playground.

**[1:43:17]** And so here are the instructions.

**[1:43:22]** And maybe I can just ask here where.

**[1:43:26]** Can I hike?

**[1:43:30]** Maybe, okay, and...

**[1:43:34]** And certainly something, okay.

**[1:43:38]** It will give certain recommendations.

**[1:43:50]** All right.

**[1:43:55]** So that's a prompt and we are able to get a response, right? So we are able to create an agent. So first we have used the AZT and the Azure Developer CLI, create the resources using Bicep template, then deploy the model.

**[1:44:14]** Again, using AZD and return a code to create an agent. Let's now see how to consume the agent using the code. Okay, so let me go back and...

**[1:44:31]** We go to the test section here.

**[1:44:40]** Yeah.

**[1:44:42]** And we have a PI file interact with agent.

**[1:44:52]** So where we are loading the agent, so first we create a project client. OK, right now we have V1 version available, so that's the agent available, right? We get.

**[1:45:08]** the agent name, get an OpenAI client so that we can submit a request to the agent.

**[1:45:15]** We are creating a conversation, uh, so...

**[1:45:21]** Right, and so conversation has a conversation ID, so that, so it's a stateful conversation where any chat we are doing with the model stays right in this conversation model can refer to the previous conversation and give an answer, right? And here we are using responses.create.

**[1:45:42]** To submit a response to the model with a given conversation ID.

**[1:45:47]** So, let me have a chat with this agent, so...

**[1:46:03]** All right, just.

**[1:46:20]** All right, so conversation started and here let me just ask provide.

**[1:46:27]** Three hiking.

**[1:46:30]** Suggestions.

**[1:46:34]** Near.

**[1:46:38]** Certainly something, okay.

**[1:46:53]** So here we have the third option as Blue Mountains and like Grand Canyon Track. And maybe since we are making a conversation, it would understand that what's the third option. Maybe I can just ask here.

**[1:47:09]** What is the best time?

**[1:47:14]** Two.

**[1:47:19]** To go to third option, you have suggested.

**[1:47:30]** So it should understand run Canyon track on its own and giving an answer. So let's see. So here it says no.

**[1:47:44]** Let me.

**[1:47:48]** So this was the first prompt.

**[1:47:51]** It provides the answer.

**[1:47:55]** So, what's the best time? So, the best time to hike the...

**[1:48:00]** So this track is in the blue mountain is during autumn, blah, blah. So it's able to understand the chat context and giving an answer, right? So we can make a conversation using responses API.

**[1:48:17]** Had it been chat completion? We need to add some more logic so that we can make a chat with our mom.

**[1:48:27]** All right, so that's a simple exercise where we have created an agent, right?

**[1:48:34]** And consume it.

**[1:48:37]** using this application here.

**[1:48:42]** All right.

**[1:48:48]** If that's all good.

**[1:48:58]** Maybe we can take this knowledge cheque now. OK, first ABC.

**[1:49:07]** If you can provide the response in the chat.

**[1:49:46]** First, let's see. OK.

**[1:49:55]** That's nice. Thank you so much. That's the correct answer. OK.

**[1:50:04]** Let's take the second one.

**[1:50:30]** See.

**[1:50:40]** Okay. Okay.

**[1:50:46]** That's great. So we use the AZD app and you'll be looking at in the lab also, right? So that's the command. Okay, great. So thank you for providing the responses. Great.

**[1:51:03]** Great.


### Managing prompts  `[1:51:07]`

**[1:51:07]** So, so the next agenda is to how we can manage our prompts, right? Because we need to...

**[1:51:18]** When we build the application, we may try a different prompt variants, different system instruction, right? So we should be able to track them. Okay, roll back to the previous version also. So we'll understand how we can do prompt versioning, how we can do agents versioning, right?

**[1:51:37]** how we can use GitHub for that, right? Use the Git and we can track our prompt files, right? So before we start with this module, I think we can take a short break here and then we continue with this topic then.

**[1:51:57]** Yeah.

**[1:51:59]** Is that all good?

**[1:52:04]** Okay, great, great. Thank you. So let me share the timer. Okay.

**[1:52:15]** See you guys in 15 minutes. Yeah.

**[2:07:46]** Ohh, so welcome back to the meeting.

**[2:07:54]** Okay.

**[2:07:57]** So, let's get going there, OK?

**[2:08:14]** Eat.


## Module 3 (continued) — Prompt Management & Evaluation  `[2:08:16]`


### Recap & tracking prompts in files (after break)  `[2:08:16]`

**[2:08:16]** So let's continue. So so far we have discussed the Foundry portal interface, right? What tools we have, how we can like create a genuine application, create an agent, how we can consume that agent. So let's go in further.

**[2:08:36]** Oh.

**[2:08:39]** Let's see how we can do the source control for the prompts. Okay, the version control, right? How we can do it. So since like when we are building our application, right, we may initially try with a prompt.

**[2:08:58]** or a system message, right? So the system instruction that we may have.

**[2:09:04]** So the system instruction is referred to the prompt, not the user prompt. So that's different. It's referring to the system instruction, and we need to do the versioning of the system instruction. OK, else we call it as a prompt.

**[2:09:24]** which guides the model and based on the instructions, the model behaves. So with an initial experimentation phase, right, we may try a basic prompt.

**[2:09:39]** Okay.

**[2:09:40]** So then later, with some more iterations, looking at the model behavior, etc., we may go with another version of the prompt. So we may have V1 version, then prompt would be enhanced. We have enhanced prompt.

**[2:10:00]** So there could be few more variants in the prompt. And finally, we may have the production ready prompt.

**[2:10:14]** Right, so this could be V3, right? Or we may have many such few more versions right of the prompt, so we so, and and let's say we are building the application, then we need to let's say if we want to go back like so in our main branch.

**[2:10:34]** which has the production data, the production code is present, and we may, we are using V3 version of.

**[2:10:46]** Of the system instruction, right, and using it when the model is generating a response. OK, so later on, let's say if you want to go to more stable version, if when we are doing the application monitoring, we realise V2 was better, so we may need to.

**[2:11:05]** Go back, right? We should be able to roll back to the previous version, updating the main branch with that, and use it in the production, right? So, so during development, right, we may have multiple versions, so testing prompts would be there, right?

**[2:11:24]** The production prompts would be there.

**[2:11:28]** Alright, so to track these prompts, first thing is the prompt should be saved in an appropriate file format. Maybe as a text file or maybe as a markdown file, right? So these are the two preferred ways. So if it's a simple prompt.

**[2:11:47]** A text file is sufficient, but if you want to have the rich text, right, more readable form, right, we may choose the markdown file to do the prompt versioning, right? So.

**[2:12:06]** And we can simply make use of Git through the versions, right? And for every version we will have a agent version as well. So for example. We created the agent right with V1 prompt.

**[2:12:26]** Right, then we would get the agent. With the version one, then we may update the agent with the newer or more advanced enhanced prompt here, right? So that would be the same agent, but.

**[2:12:45]** With the...

**[2:12:47]** Version 2 and so as we make any change like not only with the prompt if you are changing let's say

**[2:12:57]** Let's say we are adding a tool to the agent, adding a knowledge base, okay, so that any update we are doing, we are able to get a different version of our agent, right? So that's an auto versioning enabled in the, when the agents are created in the Foundry portal.

**[2:13:15]** right, we can roll back to any previous agent version, use that, and we can execute our application. Okay, this we can do, right? So that's versioning is possible in the Foundry, the agent versioning. It's done automatically and with any update.

**[2:13:36]** the agent versions gets updated.

**[2:13:40]** So, for example, we may have first V1, the basic prompt. Further, we may enhance it, right? We have V2 version, right? Further, we can get the production ready prompt, right? So, with the prompt versioning.

**[2:13:59]** We will also get the agent versioning done automatically, since we are updating our agent with the with the with the prompt variant, right? The agent is...

**[2:14:13]** Is specified by its definition. We have the agent name.

**[2:14:19]** We have the agent version, right? It will have the system instruction, the model that is the agent is using. It may be connected with certain tools, right? So these are the components of agent. We may have a prompt evaluation and as we discussing, right, the prompt.

**[2:14:38]** Should be saved either in text file or maybe in a marked on file, right? So, updating the prompt file, right? And we update the agent, so that would be updating the agent version as well, so that's what we would be doing in our second lab, so...

**[2:14:58]** Let me go back to the Foundry and let's try creating different agent versions and we can roll back to any previous agent version and we can consume that agent. Let's see how we can do that. So let me go back here.

**[2:15:20]** to the agents and we have the trail tide agent, the version V1 we have, right? So let's now...

**[2:15:32]** Go back to the same repository.

**[2:15:38]** And let's update our agent.

**[2:15:46]** So, will...

**[2:15:49]** Go to the agent here.

**[2:15:56]** The code where we are, where we are creating the agent.

**[2:16:01]** And this time, instead of V1 instruction, we will select V2.

**[2:16:08]** And let's update the agent with this instruction, so...

**[2:16:20]** All right, let me execute this Wi-Fi. The agent would get updated.

**[2:16:29]** Okay, so we are able to create the agent. This time we see it's a V2 version we have. And maybe we can go to the Foundry portals.

**[2:16:41]** So we now have V2 and if you go to the agent playground, we see we have updated with new instructions. What the instructions say, you are an expert, a guide here and you have access to a comprehensive knowledge.

**[2:17:01]** Base of trails, weather data, and gear recommendations. OK, here we provide personalised recommendations based on user experience level, weather conditions, location preference, I always prioritise safety.

**[2:17:22]** Right, et cetera, so maybe I write a prompt where...

**[2:17:27]** Can I?

**[2:17:29]** Pike and Sydney, OK.

**[2:17:38]** So this time the response is slightly different because we have updated the instruction and here it's saying, do you want more personalised advice? Because we have asked it to give personal recommendations and here it provides general information where

**[2:17:59]** It's providing.

**[2:18:01]** Gear tips, adventure work picks here.

**[2:18:05]** Oh, blah blah, so that's the format it has followed.

**[2:18:12]** Okay, so we see the response is slightly different because...


### Prompt evaluation — accuracy & relevance  `[2:18:18]`

**[2:18:18]** It's getting the the guidance, the behaviour from the instruction, and we get the response here, so that's a V2 agent we have. OK, maybe if I go back, let's try the V3 version.

**[2:18:36]** K.

**[2:18:37]** So if so this is more enhanced version, but let's see the V3.

**[2:18:45]** Let's create the agent.

**[2:18:51]** So...

**[2:18:53]** Okay, so the agent is created. We have version 3 here and

**[2:18:59]** So, let's look at the instruction.

**[2:19:08]** So, we have...

**[2:19:10]** V3. Now, the system instruction is this: We are specifying what is the core capability of the agent, so it can take a...

**[2:19:23]** input as an image, text, or voice also, right? So we are defining the scope. So what type of input the model may get, right? So the capability includes real-time weather information integration. So maybe we are connecting with a tool, right?

**[2:19:43]** Then.

**[2:19:44]** It would provide enterprise grade safety recommendations, multilingual support.

**[2:19:51]** is there and here is the recommendation framework. So looking at the user experience level, fitness, provide a recommendation. So that's a recommendation framework and always maintain the highest safety standards, provide specific guidance.

**[2:20:09]** Etcetera.

**[2:20:11]** So let me try the same prompt. Let's say.

**[2:20:15]** Where can I?

**[2:20:17]** Hike near.

**[2:20:19]** Sydney.

**[2:20:30]** So, the response contains safety tips for every recommendation, as we see here, because we have prioritised safety in the recommendations, right? So, the behaviour of model changes as we update the system instruction, right?

**[2:20:49]** And it also says, I can give personalised recommendation based on fitness level, experience and weather preferences. Okay, again, it's coming from the instructions only. So we note that with change in instruction, the model behaviour changes.

**[2:21:08]** The token usage changes, right?

**[2:21:14]** Right, the accuracy of the model, the relevance of the responses, right, with respect to prompt that changes, right?

**[2:21:25]** Okay, so we have...

**[2:21:28]** 3 versions and maybe we want to go back to a previous version, let's say 2 and want to consume the agent. So let's try doing that. We can go to the test folder here where we want to test our agent.

**[2:21:47]** Interact with agents and.

**[2:21:51]** Let me open this file.

**[2:21:55]** And this time.

**[2:21:59]** Let's have the V2 or maybe we can have V3 or V1, right? So.

**[2:22:06]** and we would be using that agent to generate the response. So let me execute.

**[2:22:23]** So we create a conversation thread here and let me just say

**[2:22:29]** Where can I hike near?

**[2:22:35]** Sydney, OK.

**[2:22:49]** So, we are able to get the responses from that model, right?

**[2:22:58]** So we can go back to the agent version and we can consume the agent. This can be done.

**[2:23:06]** So any update with the agent we are doing in the Foundry that updates the version and right the versioning is done in Foundry and we can consume the agent as well.

**[2:23:21]** All right.

**[2:23:23]** If that's all good.

**[2:23:30]** Let's go ahead then.

**[2:23:33]** So...

**[2:23:35]** So when we are creating a project in Foundry, okay, maybe we can use AZT, right, and we can provision the resources. The Azure Developer CLI will also allow us to create a project with an organised structure, right? So.

**[2:23:54]** We may note in the.

**[2:23:57]** VS Code also, right? The source contains all the code files, right? Where we are creating agents using the agents folder. We evaluate the agents using evaluators, right? So evaluation folder is different. Testing our agents is different.


### Batch testing & prompt templates  `[2:24:16]`

**[2:24:16]** So it could be a bulk batch testing, it could be simple interaction with the agent, right? The test include files like where we can do the tracing, right? Where we can log the tracing, right? Look at the trace.

**[2:24:35]** Of our agent, what the span of the chat or the metadata information that can be logged using the traces, right? So those all comes under test test and we get the test prompts under agents, we have the...

**[2:24:54]** two agents and for the recommendation agent here, the trial guide agent, we have prompts versioning done in a prompts folder.

**[2:25:06]** Right, so that's what we have here. So that's how we should be structuring the.

**[2:25:13]** Uh, our project folder, right?

**[2:25:17]** Now, the recommendation is if you want to do the system instruction version, the file format is text or the markdown files. If we have configuration metadata information, or maybe like if you have some responses that are generated by the model for...

**[2:25:37]** And we want to use it for evaluation, we may store it in a JSON file format, so this can be done. Then, if let's say we want to use the prompt template, right? The dynamic template. So, dynamic templates are the templates, like where...

**[2:25:57]** We can use a prompt template.

**[2:26:02]** Which includes both the static text and the variables are injected into that template, and we can get rid of doing prompt engineering. So, for example, let's say we want to build an application which does the document.

**[2:26:20]** Summarization: So, anytime we want to use this application, the document may be different, but other...

**[2:26:29]** details like role of the agent, right? The instructions would remain the same, right? So for example, the static text is, which doesn't change. Summarising the document in 200 words, it should be in two paragraphs and the tone is.

**[2:26:48]** Professional or something right, so we can specify how we want to do the summarization, and then we may have variable point right pointing to the document, and maybe next time the document would be different, but the summarising prompt remains the same.

**[2:27:08]** So, we can have the static text.

**[2:27:13]** the variable, the dynamic text we have. So we can get such a template, we can edit a template with proper variable injections, right? And then we can render the prompt.

**[2:27:28]** OK, once we are able to render the prompt, this prompt is passed to that LLM and LLM generates a response.

**[2:27:37]** So we can make use of the prompt templates to get rid of doing prompt engineering, writing the same thing again and again. So the repetitive task that we have, right, that can be put all together in a template and LLM always get that instruction and it follow the instructions and perform the task.

**[2:28:01]** So even if you're using a different framework, let's say LangChain, we are using semantic kernel framework, for example, right? They bring their own prompt templates, which we can use. Microsoft has one of the prompt templates, which is...

**[2:28:20]** Prompty, right?

**[2:28:24]** Which can be used right or?

**[2:28:28]** for building a prompt template and then using it in our LLM application. Okay, then documentations are stored in markdown files, the readme files, for example, other like documentation files are prepared using the markdown files.

**[2:28:49]** While we are doing the registration right of, let's say, prompts, we should be using version prefix like V1, V2, V3, so V1 instructions, V3 instructions, for example, giving a clear names using underscore and right.

**[2:29:09]** Like, let's say the prompt is V4.

**[2:29:12]** Ohh, let's say optimized.

**[2:29:17]** Concise prompt.

**[2:29:20]** dot text, right? So such kind of naming.

**[2:29:26]** K should be done right so that we can create a version of a prompt and. Then we can use it right.

**[2:29:37]** This can be done.

**[2:29:41]** Alright, so going ahead here, we see, like in our development environment, we may be trying different LLMs, we may be iterating over the prompts system message, trying a different safety filters, right? And...

**[2:30:00]** So, there would be a development environment, and we can have different environments even in the GitHub. So, in GitHub, if you go to the settings, we can see we can declare different environments, right, where we can work.

**[2:30:19]** On, let's say, on development environment, right? So there would be a main branch, right? And then we may...


### Branching & comparing prompts  `[2:30:28]`

**[2:30:28]** have another branch, a new branch where we are trying out a different prompt, right? So we have a prompt variant, right? Then we may try evaluating this prompt, doing certain evaluations.

**[2:30:48]** And if that improves, let's say, the performance of the model, like in terms of giving better accuracy or giving more relevant results, the relevance score is improving, or it is consuming less tokens than the previous version of the main branch.

**[2:31:07]** Right, we may then create a PR, right, and then we can merge after the approval, right? This can be done, so, so even if we have, let's say...

**[2:31:22]** A prompt, right? An improved prompt, right? So this, if you want to...

**[2:31:29]** use it in the production environment, it has to be first reviewed, evaluated, right, approved, and then it can be, we can make changes in the production environment. So GitHub allows, like as we have seen in the MLOps also, where...

**[2:31:48]** We can merge a feature branch to the main branch. Okay, if there is an improvement after triggering a certain workflow, the same thing can be done here also, right? Trying out a different prompt in a new branch and making PR triggering certain.

**[2:32:07]** automated workflows and merging with the main branch. Okay, this we can do.

**[2:32:15]** All right.

**[2:32:19]** So let me go ahead, go through this exercise here where we can.

**[2:32:27]** Sorry, uh, this is the...

**[2:32:31]** This is the exercise that we have seen, right, where we have tried V1, V2, V3 prompts. We are able to get agents with different versions and we have consumed them. So that's an exercise we'll try to do, okay, later.

**[2:32:49]** Let me go ahead, then.

**[2:32:53]** Any queries we have so far? Then would you like to add here?

**[2:33:04]** Alright, so that's good. So let's go ahead and see how we can create certain structured.

**[2:33:16]** experiments, right? We can do evaluations, right, and try to optimise our AI agents. So we may like build an agent, right? Now, this agent, before we put into production, has to be tested.

**[2:33:36]** It should be evaluated on some batch of inputs. The agent generates a response and the response should be evaluated, right?

**[2:33:46]** Based on the evaluations, we may we may compare different experiments, so there would be...

**[2:33:56]** baseline experiment, we need to 1st have where we may have, let's say, V3 instruction, right? And we are able to pass certain batch of inputs to the agent and it generates a response, right? The response need to be evaluated.

**[2:34:16]** So, and evaluations are...

**[2:34:22]** are stored maybe in a CSV file. So how do we evaluate the model responses using certain evaluation metrics like quality metrics? How is the quality of response generated? For example, intent resolution.

**[2:34:40]** So there are evaluators available. Inbuilt evaluators are there which are automated and they can do the intent resolution. That is, what is the intent of the user? What is the user query? And by looking at the response, is that query?

**[2:34:59]** Resolved right? Is that intent resolved by that LLM? So, by understanding the input prompt and the response of the model, evaluator scores the intent resolution.

**[2:35:14]** out of five, maybe 4 by 5, 5 by 5, 3 by 5, for example. So if it is, if it is about 3, it means that the test is passed, else the test is, it has failed.

**[2:35:34]** Now, that three is a default number. We may change it also if you want a higher threshold for doing the intended resolution. So let's say it is 4 by 5, right? It is automatically grade by the evaluator, the inbuilt evaluator we have in the Foundry.

**[2:35:53]** We can even do the manual evaluations. So once we get, once we are preparing this evaluations, the prompt, the response of the model, the human evaluator can do the intend resolution. That is, it would grade by looking at the prompt and the response.

**[2:36:13]** Is it resolving the intent of the user or not? So user may provide grade of four, 5, right, depending on its expertise and right.

**[2:36:26]** the evaluator expertise, right? Then we have relevance score. That's another metric. We have groundedness so that how well the model is referring to the document and providing a response. So there's a groundedness score. So human does the evaluation.

**[2:36:46]** Maybe 4, 5, 4.

**[2:36:50]** We also have a comment section where if there is a gap, what is the reason of the gap? Okay, that reason the comment has to be provided. So we can do the manual evaluations, we can do automated evaluations also, even if you are doing automated evaluations.

**[2:37:10]** The LLM is the teacher LLM is doing that evaluation, so if it grades 4 by 5, then...

**[2:37:20]** then it also provides the reason why it is 4 by 5. So that reason is also provided. So.


### Lab — manual evaluation & prompt optimization  `[2:37:29]`

**[2:37:29]** So, currently, in this next lab, we will be focusing on manual evaluations, and tomorrow we'll see how we can use the automated evaluators, right?

**[2:37:43]** So we can get the evaluation CSV file. We can create such a file. Now we may go ahead. So this is a baseline evaluations done on our production ready prompt. Maybe we.

**[2:38:00]** So this code is available in a main branch, right? We can create a new branch and where we are trying a different.

**[2:38:12]** prompt, another prompt variant, V4, right? Right, which is providing a more concise response. Okay, and with that, we pass the batch of input to the agent. Agent generates a response and...

**[2:38:31]** We are able to get the evaluation.

**[2:38:35]** File.

**[2:38:38]** Then.

**[2:38:40]** We may try optimising our application, maybe not using the prompt, but maybe we are using a different agent. The LLM we are changing. Let's say if we were using a deployed GPG 4.1 model, we may try, let's say.

**[2:39:00]** GPT.

**[2:39:02]** 4.1 mini or some other reasoning model. And again, we get the batch tests done, we get the evaluation CSV file, and we may compare all the CSV and make a conclusion how well is my...

**[2:39:21]** model giving an answer. Is it we can calculate the average of all the relevance score, groundedness score across all the test prompts and make a comment which prompt is doing better or is the other model giving a...

**[2:39:41]** better accuracy rate that we can check. And after making some conclusion, right, we can go ahead and merge with the main branch if there is an improvement using the other branches. Right. So we can create a PR and merge the PR to the main branch. Okay.

**[2:40:02]** This we can change. Even there are other parameters like the agent configurations, like maximum tokens we may change, whether the model is streaming enabled or not, right? So these are certain model parameters we may further change. We may change the model temperature.

**[2:40:22]** which will change the randomness of the model, right? The model may be more creative as we increase the temperature. So we may try optimising the temperature of our model and see what is the optimal temperature value. So these are certain variants we may

**[2:40:42]** Try, we may test in a different branch, so every every variant right we are doing it should be.

**[2:40:53]** For every variant in our application, we may create a new branch, right?

**[2:40:59]** We have the test prompts, right, stored and we evaluate the new branch, right? The responses are scored right now manually. We can do it automated also.

**[2:41:15]** Compare the branch and merge the winner branch to the main branch, so this we can do it.

**[2:41:27]** So, so that's how we can integrate the GitHub, right? And that the Genia application, right? And we may try optimising our application, tracking the changes, and right merging the winner branch with the main branch.

**[2:41:47]** Operating the main branch, right?

**[2:41:51]** This can be done.

**[2:41:54]** Right, so let's try doing this activity, right, where we will be testing the prompt optimization for our agent that we have created, and we will be creating evaluator CSV file, and we can compare those CSV files, right?

**[2:42:13]** This, we can do.

**[2:42:21]** If that's all good.

**[2:42:30]** OK, so let me go to the Foundry here. So currently here we see we have.

**[2:42:42]** Agent.

**[2:42:45]** The V3 version agent, right? So we'll use this agent because it's using the third prompt variant and.

**[2:42:57]** OK, so if we cheque the prompts, the V3 instructions, we have the V3 agent, right? So...

**[2:43:09]** Using this, we have already created the agent, right? We will go and go to the test and we will test our agent on a batch of inputs on our test prompt. Right now, we see we have 5 prompts here.

**[2:43:27]** Test prompts are available.

**[2:43:31]** Like, that's our first prompt.

**[2:43:35]** second prompt we have. So like we have 5 prompts here.

**[2:43:40]** And if you look at the spy file.

**[2:43:50]** This PI file first load all the prompts, right?

**[2:43:56]** Get the latest agent version. Right now it is version 3, right? And submit the prompt to the agent, gather the response, save the response in a JSON file in an experiments folder.

**[2:44:13]** So.

**[2:44:16]** So that's the logic here in the code. We first get a client handle, the project client handle, retrieve the agent, right, with the latest version.

**[2:44:31]** Right, and going further, passing, reading the text, the prompt text, right, passing it to the model, model generator response, and the responses for the log as a JSON file.

**[2:44:47]** So, we see JSON on dump and we are saving it as a JSON file, so...


### Baseline experiment & new agent versions  `[2:44:55]`

**[2:44:55]** Here we note under experiments, so this is our baseline experiment when the agent V3 version is used, right? That's the baseline JSON file we get.

**[2:45:11]** So...

**[2:45:14]** We can note that we have this prompt. So this is our first prompt.

**[2:45:21]** This is the prompt and this is the response of the model. We are able to log the token usage.

**[2:45:30]** That's our second prompt and the response. So we have 5 responses generated. Then we are manually creating this evaluation.csv.

**[2:45:41]** And if I show this...

**[2:45:52]** So it's manually evaluation done where the intent resolution is scored, relevance groundedness is scored, and the human evaluator provides the comment.

**[2:46:06]** So, this can be done in a in a in a in a one branch, then.

**[2:46:12]** We can go create a new branch that would be the optimized, concise branch, let's say, where we are creating a new agent.

**[2:46:23]** By simply changing the prompt, so the prompt would be V4.

**[2:46:30]** Right, that's the variant we we we want to try, so we get the agent version four and to that we are.

**[2:46:41]** Passing the test prompts.

**[2:46:46]** And we are able to log this.

**[2:46:50]** the responses of the agent.

**[2:46:54]** Great, so for every test prompt we get the response log in a JSON.

**[2:47:00]** We create the evaluation CSV.

**[2:47:03]** K.

**[2:47:15]** Yeah, and...

**[2:47:18]** So that's a human evaluation done, right? And we may compare these CSV files, right? Now, another variant could be instead of using when we are creating the agent, right?

**[2:47:32]** Instead of changing the prompt, we may want to.

**[2:47:38]** Change the LLM rather than GPT 4.1. I deploy GPT 4.1 mini and I want to log the responses here, right?

**[2:47:51]** So we can change the deployment and we are able to create a new agent version, right? So every change, any variant that we have, okay, would be a new branch right in the GitHub where we are.

**[2:48:10]** That.

**[2:48:11]** making the changes, right, doing the evaluations, right, and if the team approves or the lead person or admin approves, then right, then we can merge the PR to the main and update the main branch. Okay.

**[2:48:30]** So, that's how we can improve the code, right, while maintaining our structure, right? And we can streamline the process, do the collaboration, work with multiple branches, and right go.

**[2:48:47]** And update the production code, right? This can be done then.

**[2:48:54]** So right now here we have seen the human evaluation and doing the LM agent evaluations right. Tomorrow we'll see the auto the evaluators which can which is doing the auto metered evaluations.

**[2:49:15]** Right.

**[2:49:18]** So that we will do.

**[2:49:21]** Okay.

**[2:49:28]** Yeah.

**[2:49:30]** So, that's our...

**[2:49:32]** Third lab, OK.

**[2:49:39]** Maybe we can have this knowledge check.

**[2:49:44]** Before we can proceed with the lab performance, okay, let's have this knowledge cheque for first one. You may suggest the correct option.

**[2:50:10]** So here it says the experiment shows GPT-4 mini right reduces the cost by 75% while maintaining an average quality score of 4.1.

**[2:50:24]** Threshold is 4.2.

**[2:50:26]** and improving response time.

**[2:50:29]** Right.

**[2:50:31]** So, so for example, so basically in our main branch, maybe we are we have deployed GPT 4.4, we have deployed, we created a new branch, used the other LLM, and we have seen by evaluation response time.

**[2:50:50]** Is improved.

**[2:50:52]** Token consumption is lesser, right? So the cost reduces.

**[2:50:59]** But the quality score is 4.1, the threshold is 4.2. So what should we do?

**[2:51:17]** So we suggest B as an answer. So that's very correct, right? Because we are getting, let's say, improving response time, token usage is lesser, but it's at the tradeoff of the quality. So we may seek business stakeholder input whether.

**[2:51:37]** it justifies the quality reduction, right? So that's the correct answer. Thank you for the responses. Let's have the second one.

**[2:53:09]** We go back.

**[2:53:12]** So we say be here, OK?

**[2:53:20]** Okay, thank you.

**[2:53:22]** So, again, that's very correct, so...

**[2:53:26]** But with any new experiment, we should be doing in a separate Git branch, right, so that...

**[2:53:35]** We can isolate that specific change in that branch, and right, so we can see the individual modifications, the performance difference, right? That's very correct.

**[2:53:49]** Yeah.

**[2:53:51]** So.


### Knowledge check & extended lab time  `[2:53:52]`

**[2:53:52]** Thank you for taking this knowledge check.

**[2:53:57]** And if I go back here.

**[2:54:04]** Yeah, so today we have completed these labs, lab 7, 8, and 9. These labs we have explored. Let's try performing these labs.

**[2:54:21]** Okay, and any challenge or any lab, if you're doing previously and any challenge you found there, feel free to perform any of the previous lab also. That's all good. Okay, so we can spend some time here performing the labs.

**[2:54:40]** And tomorrow we will go ahead and talk about agent.

**[2:54:51]** Yeah, we'll talk about the agent observability.

**[2:54:57]** How we can monitor?

**[2:55:00]** Our agent application, so we can use evaluators, the which can do automated evaluations.

**[2:55:10]** that we would be exploring. We'll also further talk about what is fine tuning, how we can do fine tuning in the boundary portal.

**[2:55:22]** So these are the agenda for tomorrow's session.

**[2:55:28]** Okay, so let's perform labs 7 to 9.

**[2:55:33]** Can do that.

**[2:55:46]** Any.

**[2:55:48]** Anything would you like to add here? Let me share the attendance link in the chat.

**[2:56:00]** If anyone missed out marking the attendance, kindly mark your attendance. Attendance link is shared in the chat.

**[2:57:58]** Yeah.

**[3:41:37]** Raghu, maybe if I can add here, if you're not able to do easy login, if I take control.

**[3:41:44]** I see you are facing issue with AC login.

**[3:41:50]** Sure.

**[3:41:52]** Great, thank you.

**[3:41:57]** Yeah.

**[3:42:04]** So sometimes it happens that the browser do not open and we are not able to log in. So let me take control.

**[3:42:21]** So.

**[3:42:23]** If I try doing easy login.

**[3:42:30]** You may select the work account.

**[3:42:38]** And I think we get stuck here, right?

**[3:42:42]** Yeah.

**[3:42:43]** So.

**[3:42:44]** Getting.

**[3:42:45]** Yeah, let me go new terminal, kill the previous one and.

**[3:42:57]** I think we have done this step. So this time, easy login. Let's force it to open the browser. So use device code.

**[3:43:13]** So it says to go to the browser and use this code to authenticate. So I'll copy this code.

**[3:43:22]** Will open the browser, enter the code.

**[3:43:31]** So we need to pick the another account.

**[3:43:37]** The Azure account.

**[3:44:08]** So it is retrieving subscription. We may select enter. We don't want any change. It's the correct subscription ID. Hitting hit enter. Now it's all good. So we are able to log in using easy login. We can continue with the next step.

**[3:44:29]** I'm releasing control here.

**[3:44:29]** Okay.

**[3:44:31]** OK, I have a question: why used different account you while using a login?

**[3:44:40]** Because the resources that we have created, we are connecting that resource to the VS code using AZ login. We are logging to Azure to use the resources that we have deployed on Azure.

**[3:44:53]** Okay.

**[3:44:53]** So we need to use that account only here.

**[3:44:58]** Got it, got it.

**[3:45:01]** Yeah, great, great.

**[3:45:02]** Thank you so much for this.

**[3:45:05]** Yeah.

**[3:54:38]** Pauroosh, I got this error.

**[3:54:42]** Yeah, I was looking at it. What region did we select when we?

**[3:54:48]** Uh, Sweden, I guess, same.

**[3:54:52]** As mentioned, right? Okay.

**[3:54:53]** Kaur.

**[3:54:55]** Sweden Central.

**[3:54:56]** East Sweden Central, correct?

**[3:55:02]** Ohh.

**[3:55:05]** Vatan.

**[3:55:07]** Let me just take control.

**[3:55:24]** We'll do EZD again with Sweden Central ones. If not, then we will try changing the region to East US too. OK, let's see.

**[3:56:32]** Let's take Sweden Central only, as per instruction.

**[3:56:40]** If...

**[3:56:56]** All right.

**[3:57:00]** The template is not valid.

**[3:57:05]** According to the value, okay.


### Lab — quota limit troubleshooting  `[3:58:49]`

**[3:58:49]** OK, now it throws the quota limitation error, right?

**[3:58:57]** Insufficient quota.

**[3:58:59]** Gurpreet.

**[3:59:06]** Okay, let's try East US 2 because it's a training key temporarily. Sometimes the resources are not available in a particular region. So either we try West US, East US 2 or Sweden Central, right? We should be able to provision the resource here.

**[3:59:23]** Okay.

**[3:59:57]** Not sure where it is east.
