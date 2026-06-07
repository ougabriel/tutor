# AI-103T00: Develop AI Apps and Agents on Azure — Day 2

- **Date:** Wednesday, 27 May 2026 (12:30–16:30 IST)
- **Trainer:** Shova Kant Sharma (Microsoft Certified Trainer), Koenig Solutions
- **Recording:** Day 2 — Meeting Recording (SharePoint Stream)
- **Length:** ~3:53:26  ·  **Captions:** 1050

> Transcript captured from the on-screen auto-generated captions for personal study. Captions are machine-generated (Microsoft Stream) and may contain errors. Section headings were added at the points where the trainer moves to a new topic; the caption text itself is verbatim.

## Contents

- `[0:00]` Recap & Housekeeping
  - `[0:00]` Attendance & session start
  - `[13:24]` Recap of Day 1 — AI workloads & Responsible AI
  - `[20:06]` Recap of Day 1 labs (model catalog, chat completions, RAG)
- `[27:14]` Module 1 (continued) — Generative AI Apps & Tools
  - `[27:14]` Knowledge & tools — overview
  - `[35:46]` Common agent tools
  - `[38:32]` Knowledge check — choosing a tool
  - `[53:25]` Grounding models with RAG (retrieval-augmented generation)
  - `[1:01:12]` Fine-tuning models
  - `[1:04:51]` Knowledge check
  - `[1:07:28]` Implement responsible generative AI & guardrails
  - `[1:17:43]` Content filters & deployment demo
  - `[1:23:21]` Knowledge checks
- `[1:46:48]` Module 2 — Develop AI Agents on Azure
  - `[1:46:48]` What are AI agents & why use them
  - `[2:00:38]` Evaluating agents
  - `[2:04:30]` Build an AI agent (portal & VS Code)
  - `[2:16:20]` Knowledge check
  - `[2:19:47]` Integrate custom tools (Logic Apps, functions)
  - `[2:39:12]` Model Context Protocol (MCP)
  - `[2:44:48]` Exercise — connect an MCP tool
  - `[2:51:11]` Knowledge check — MCP
  - `[2:57:11]` Knowledge-enhanced agents with Foundry IQ
  - `[3:06:04]` Configure retrieval & knowledge sources
  - `[3:12:57]` Knowledge check & hands-on lab
- `[3:48:09]` Wrap-up

---


## Recap & Housekeeping  `[0:00]`


### Attendance & session start  `[0:00]`

**[0:04]** So every time for your lab access, you'll go to this link, correct? And you just need to redeem your training key only once, right? You don't know, you don't need to redeem the training key right everyday. It's a it's a one time process. Click on sign in, okay, click on, you know, whatever.

**[0:23]** Account you have used to whenever you have enrolled, so whatever account you have used, use the same account. Okay, I have used personal, so I will use my personal, right? So you don't need to redeem the training again. It is already done. You can see your classes in the classes section. So you can see your class.

**[0:44]** Okay, there's a link. So once you click on this link, right, so then it will take you to your lab, okay. And then from here you can launch your lab. Okay, do let me know in the chat how many labs you have completed. Have you performed lab number one?

**[1:03]** 23, and 4.

**[1:07]** Ignore the count.

**[1:08]** Not yet, not yet.

**[1:11]** Okay.

**[1:18]** OK, Rishikesh one, Aryan one and 2.

**[1:24]** Nenad one only the first 2 entry.

**[1:36]** Okay, how do I proceed? Okay.

**[1:43]** Okay, verify your identity and here what you have to do 5. Okay, no, you have to enter the 6 digit code you receive on your email ID. Okay, look in your email ID and you have to enter that as the OTP, okay, not the not the password over here.

**[2:02]** That's simply for logging for yesterday and today. Okay, for yesterday there were 44 laps. Okay, all right, so Torchi has done 4 laps. Okay, wonderful. I am unable to access the laps.

**[2:21]** So what's the issues here? Do let me know unable to sign into Ali portal, says the email is not registered with us. Please check and try again. Also, make okay, I have marked my attendance for today as well. Okay, it's not registered with us. Okay, make sure guys.

**[2:41]** The email ID you use, I'll show you. OK, those who are facing the issues with LET portal, so.

**[2:50]** Right, you go to your mycoin.com correct.

**[3:01]** Okay, now once you once you sign in, you have to use the same.

**[3:07]** Email ID you have used to mark your attendance, okay, use the same same email ID you have used or if already taking any other email ID. So just go and use the incognito window, right? And then you can basically you'll get access to the LET portal.

**[3:27]** It has everything you requires to for your training. It has everything out there. We can see the various sections are listed over here and also right, you can see all the sections are over here. You can explore, you can see meeting links and attendance, you can view recordings from here. Okay, you can checkout the modules.

**[3:47]** Okay, you can check your lab access. Okay, your lab access, the lab URL, and then training key would be available over here. The course where you can view your achievement code from here. Okay, you can click on like here, click to access the achievement code, right? And once you...

**[4:06]** Click on this, it will take you to the Microsoft Learn right and then it will simply give you right this pop up where it will automatically inserts the achievement code.

**[4:20]** OK, and just you have to click on redeem right now since it is already redeemed for me, so right it give me your after you redeem it, right? Once you redeem it, if you go here and if you go to the courses, OK, in your achievements, if you go to the courses, you could be able to view your course over there.

**[4:41]** Okay, so you would be able to view your courses. Email isn't registered with us, even though I marked the attendance with that email, okay?

**[4:52]** Attendance link again. LET portal.

**[4:57]** So.

**[4:59]** Okay, guys, if you can get me a screenshot shot, right? I'll basically check with the back end team.

**[5:09]** Okay, so the error you're getting, right, just take a screenshot of it and paste in the chat.

**[5:15]** Okay, so I'll forward it to the back end team if you're not able to access and make you are using the same email ID you are you have marked your attendance with.

**[5:28]** OK, and once you login right, it will take you to this page. We can explorer like qubits. You can checkout here the number of questions you can start your test for each of the modules are there.

**[5:39]** Okay, resources, you can go through additional resources out there that you can refer, right? And other other informations out there.

**[5:49]** Okay, so if you need any course technical supports, you can reach out to this email customer success manager, you can reach out to her right trainer, right? You can reach out to me if you have any queries out there after, you can also view upcoming webinars, right? You can attend webinars, okay.

**[6:14]** Alright, so let me.

**[6:22]** Okay, so it will look right if you have already registered for the class by your employer, okay, by your employee, use your official email ID to login, okay. If you have already registered for the class by your employer, okay, then you have to use the same email ID which your employer.

**[6:42]** Has resistor width.

**[6:45]** Okay, alright, okay, I can see here, okay, this email is not registered with us. Please check and try again. Okay, I believe this is the same one you have used to.

**[7:00]** You have mark your attendance width, right?

**[7:02]** Yeah.

**[7:08]** Okay, what should be the account to log into the lab in there specific Microsoft account? What should be accounts to log into the lab? Okay, I've already shared the instructions for the lab. Okay, now this is the one.

**[7:26]** And also if you miss yesterday's session, so you can also give the recording from LET portal. Okay, recording can be accessed to LET portal. Okay, it says URL is blocked. Okay, maybe that's because your computer your.

**[7:45]** Official laptops may be blocking some of the URLs out there, so you can try with your personal device, okay?

**[7:56]** Okay, same problem there. Okay.

**[8:01]** Okay, so just give me a minute, let me inform the teams regarding the issue.

**[10:35]** Alright, okay, so guys, I have informed the team okay regarding the issue and as soon as I get any updates, I will let you know. I had even mailed you regarding this problem yesterday only.

**[10:52]** Okay, smoke person details so people can reach out if they have any issue.

**[11:00]** Spoke person detail.

**[11:05]** So for this issues out there, right? So I just need to navigate you through. Okay, so I have informed the team if you have any other other queries out there, so you can basically spoke to your spokesperson like in your organizations.

**[11:26]** Okay.

**[11:29]** Please share the attendance link. I have already shared it in the chat, so if anyone can you know, share again in the chat. Hold on, I found it again. Here's the 1i think you don't have any issues with marking attendance. Right? Yesterday, a lot of you had the issues.

**[11:50]** To mark attendance, okay, so now we will proceed further, right? If you have any queries out there regarding the lab, okay, I can see you many of you have started with the hands on lab, but the count is still less so.

**[12:09]** Today we will dedicate some, dedicate some time for the hands on and I will take, I will take the queries and then any issues you are facing with your lab environments. So before that, lets take a quick recap of what we have covered yesterday.

**[12:28]** And what we are going to cover in today's sessions, okay?

**[12:33]** So first we'll complete the module one and then we'll move to the module 2.

**[12:39]** So here we go.

**[12:45]** Okay, I am going to take a quick recap, okay, what we have cover yesterday, okay? And I will be taking the questions and answers at the at the end of the sessions. Okay, now so first lets.

**[13:04]** Take a quick recap of what we have covered yesterday. So yesterday we started with our we tell you yesterday we started with introductions. We talk about what this course has to offer, what are the modules we gonna cover, about the schedules and all those things we have discussed. And then we started with the module module first.


### Recap of Day 1 — AI workloads & Responsible AI  `[13:24]`

**[13:24]** Where we talk about the artificial intelligence workloads, right? We talk about this various areas that we would be working on. And yesterday, we started with generative AI workloads. So we started here with understanding what is generative.

**[13:43]** AI, then we understand how we can plan and prepare to develop the AI solutions soon as you. OK, so we discussed yesterday about the Microsoft Foundry, what is Microsoft Foundry, Microsoft Foundry resource, Microsoft Foundry project, and insight your project. OK, there are basically 4.

**[14:04]** 4 important component, which is model, agents, tools, and knowledge, right? We talk about the foundry tools, okay, which are basically the ready to use AI capabilities.

**[14:22]** For your AI apps and agents. So these are basically Azure, these are Azure AI services. So Azure Language, Azure, Azure Translator, Azure Document Intelligence, and Azure Container Understanding will be will be covering this in more detail. in the.

**[14:42]** Coming modules then we talk about here the developers tools and SDK to start basically developing your a I solutions on Azure you would need the tools and SD Ks. So in tools we need Microsoft Visual Studio Code found foundry toolkits.

**[15:03]** Extensions okay, now some of you are facing issues with the this toolkit extension foundry toolkit extensions. We will take look into that in the later once we cover the content and also GitHub copilots okay and the software, the software SDK.

**[15:24]** That you would need is Microsoft Foundry SDK, okay, OpenAI SDK, then Microsoft Foundry Tools SDK. So there are basically separate SDK for language and text analysis. Okay, now for example, lets say I want to analyze customer feedback.

**[15:43]** Back, okay, so we can use the language SDK if I want to convert the speech to text, we can use the speech SDK and so on. Similarly, like document intelligence, if I want to you know extract the data from the invoice, okay, then further.

**[16:02]** We discuss the 6 principle of responsible a I. We talk about fairness, reliability and safety, privacy and security, inclusiveness, transparency, and accountability. All right. And this was your first hands on lab of preparing for an AI development project, okay, where you.

**[16:21]** Create a foundry project, you deploy and test a generative AI model. You identify the project endpoints and keys to connect the endpoints, the project endpoints and keys are needed for connecting your you know, applications with the models you have deployed, the foundry models you have deployed in the Azure.

**[16:41]** Then also, we have explorer the Microsoft Foundry extensions for Visual Studio Code. Further, we have gone through the knowledge check second, we started here with select, deploy, and evaluates Microsoft Foundry model. Okay, so where we have discussed that we have a model catalog, you know where.

**[17:01]** You can where developers can basically they can search, they can compare, OK, and they can select the a I models for the applications and the agents. Then further we here you can select the models using the benchmark. OK, so we have certain benchmark there.

**[17:22]** Quality, safety, throughputs, and cost. Okay, now this benchmark are basically this benchmark.

**[17:33]** If you see model leaderboard, so you can see the benchmark for different from different models, okay, for different models, you can see quality, safety, throughputs, cost. So this are basically this.

**[17:52]** Are created this benchmark are created by the Microsoft Foundry. OK, so Microsoft Foundry basically creates this benchmark based on the standard data sets and the standard methods. Also, there are basically the benchmark which are used from the model provider.

**[18:13]** Okay, so there are different vendors basically through which you are basically getting all this models in one in foundry Microsoft Foundry. So also they take those if the benchmark as available for the those models, so those that are also available that also taken by the Microsoft.

**[18:34]** Foundry okay and so and the same like because the same models can be on different cloud platforms out there. So basically they have they might using different different data sets, different methods okay to evaluate some models.

**[18:54]** Okay, so there could be differences out there, okay, slight difference out there. So this is the initial, initially you use the benchmark to basically find from best models for your use cases and then you evaluates it for this with your own own data.

**[19:13]** You're on your requirements deploy models to the endpoints, right? So once you select your models, then you have to deploy it to multiple different endpoints. Then we understand evaluates the model performance, right? You can evaluate your model performance.

**[19:33]** Either manual evaluations, okay, or basically whether automated evaluations, okay, so manual evaluations where you basically judge the quality, the tone, the reasonings, okay.

**[19:52]** And automated evaluations is basically where you use the synthetic data sets and the platform basically may just the response based on the standard metrics.


### Recap of Day 1 labs (model catalog, chat completions, RAG)  `[20:06]`

**[20:06]** You perform this exercise where we explorer the models in the catalog, compares models using Model Leader board and deploy the models, compares models in the model playground and evaluates the models with the synthetic data sets and these are the knowledge check. Then further we started here how to develop a generative AI chat app with the Microsoft Foundry.

**[20:30]** Okay, now first before we start with the chat app, first we explorer with the model playground.

**[20:39]** Okay, so we explorer with the model play playground. It is basically the testing area where you can try where you can test the different models before you use them in the real applications. Okay, and also for each of the.

**[21:00]** Models, OK. You can also get sample code. You can view the sample sample code samples right based on a Pi, programming languages, rest or the SDK, OK.

**[21:15]** So.

**[21:23]** Okay.

**[21:26]** Right now, for example, this one, okay, this is the agent, but let's go to the model.

**[21:36]** Yes.

**[21:36]** Okay, now let me open this. I think someone is unmuted. I request everyone to be on mute.

**[21:48]** Okay.

**[21:50]** So let's go to, let's take GBT 4.1.

**[21:56]** Okay, right, now this is basically where you can see this option. Okay, chat next to this, you can see code. Okay, now from here you can choose the API, right? Completions API or the response API. From here you can choose the language.

**[22:14]** Okay, so your labs are basically on Python, okay, but also right, you can see a JavaScript.

**[22:22]** Okay, so this is basically the code. Also, you can open this in a Visual Studio code for the web. You can copy and paste right into your own IDE or you can open this in a Visual Studio code from the web, okay?

**[22:41]** So this is over there, right? This is the endpoint, this is the deployment name, right? And then right, you basically provides here the prompt using roles. So it's a completions API. Response API would be something like this you can see here. OK, so that's basically what we have.

**[23:00]** Discuss with the playground and then further we explorer the endpoint and SDK, right? Choosing an endpoint and SDK, okay, Foundry project endpoint, Azure Open AI endpoints, SDK, Foundry SDK, Open AI SDK, authentication, chat API, okay, best for with example.

**[23:21]** We also compare the chat completions with the response API.

**[23:26]** Okay, and then we have basically we compares the per ton code patterns out there with the initial state with using add inputs.

**[23:37]** Okay, then we call the API right where we provides the model name and the message, which is your conversations message, okay, which is appended with the system message and then the user message out there and then for output.

**[23:56]** We use completions dot choice dot message dot contain and then we update the state out there right conversation message dot append append basically what's the assistant like the output you get with the assistant will will append it to the conversations message which is different in case of the response API.

**[24:17]** Okay, here we have response ID right the call API okay then print this is to get the output okay which is response dot output underscore text and then we update here this state the last response ID with the response dot ID.

**[24:36]** This is an example of using the response API.

**[24:41]** This is using the chat completions API, right? And then further lab number 3, OK, you learn how to create a Microsoft Foundry project, how to deploy a model, how to get the endpoints and key, and then you create a client applications, OK, using the Visual Studio code.

**[25:01]** To chat with the model, OK, that you have deployed in the Microsoft Foundry.

**[25:07]** We covers this knowledge check, right? And then we started here understanding the generative AI apps using tools.

**[25:17]** Okay, so.

**[25:20]** We understand like what are what are tools. Okay, now tools basically which provides like which extend the capability of your large language model, it extend the capability of the models like for example.

**[25:40]** The tools are basically used to access the real time informations or take actions or ground your responses right in the fact and extend the functionality, build intelligence workflows.

**[25:54]** Okay, and yesterday we also have this experiments out there, right? If you go to your model, for example, if I go to my existing model, lets go to chat, okay, and let me ask over here, this is GBT 4.1 model.

**[26:13]** Okay, now I will say, okay, what is?

**[26:18]** What is?

**[26:20]** Today's.

**[26:23]** Temperature.

**[26:29]** In London.

**[26:35]** Right, so you can see here, right, I don't have a real time weather data access. However, you can easily check the current temperature in London by using right this thing. Okay, so it's giving like if you like a general idea, so would like help in finance with weather sites. Okay, so now over here I can go to the tour.

**[26:55]** Right, I can go and I can use the tool over here. Okay, now you can see we have a various tools out there, right? These are the common tool, okay, like file search. Now this is basically used to search file and ground your answers.


## Module 1 (continued) — Generative AI Apps & Tools  `[27:14]`


### Knowledge & tools — overview  `[27:14]`

**[27:14]** In a specific knowledge.

**[27:17]** Okay, for example, searching company policies, PDF, or any training documents manual. Okay, so we can upload the file, right? So right now, what's my requirement is like? I want to know what is the today's temperature in London.

**[27:38]** So we will go for the web search. This is used to find the current information from the Internet like latest news or any product price or any recent events or maybe like temperature for example. Okay, so let me go and.

**[27:58]** Add it okay and one thing you need to keep in mind over here the web search use the grounding with the Bing right which is search engine which has additional cost and terms of use and priceless privacy statement. Customer data may flow outside the.

**[28:17]** Azure compliances boundary. Okay, so that's basically things you have to keep in mind. Okay, so data will flow outside the Azure compliances boundary. So now let me ask same over here, okay, and let's see what is the.

**[28:35]** Is in response here.

**[28:41]** Okay, now it's good here. Okay, here's the current temperature in London for today, right? That's date Weatherworld, right? Temperature is 20 degrees Celsius, okay, feels like 20 degrees Celsius and clear skies and light east northwest wind at 13:00 MB MBH.

**[29:01]** Right, and then you can see over here, right? It give you basically the source now there, okay.

**[29:09]** So right, so you can see here access the real time information, take actions and so on. This common tools out there, code interpreter, web search, file search and the and the functions. Okay, maybe I can go to add and code interpreter.

**[29:29]** So let's see code interpreter. I will just upload a file, for example, let's say, okay, I have this, sorry, not this, let's say.

**[29:42]** Okay, I have this CSV file, okay, which has the system performance.

**[29:53]** So let me click on attach.

**[29:57]** Okay, now once I once I attach here, let's see what's there.

**[30:04]** System.

**[30:09]** Okay, system payments, so you can see over here it has the time time stamp, okay, CPU percentage, memory percentage, disk percentage, and network M Mbps.

**[30:24]** Correct, so.

**[30:29]** Now, over here, right? Once we have our code interpreter, now what I can do is...

**[30:39]** Let me use the prompt from.

**[30:45]** From the lab, so...

**[30:48]** It will be.

**[30:53]** Too fast of the fast of the things. Let's go to share and then we go to.

**[31:09]** Okay, so now we hear like we'll say.

**[31:24]** Okay, so basically for file search that use tools fine tune dot rails.

**[31:51]** Now if you perform this lab, this is using the tools out there, right? The create an app that uses the tools and the tools which is used over here is the file search. So now here you basically.

**[32:07]** Connect out there and then you are creating back to store and uploading the file, right? And then over here you define the tools out there like type, okay, which is a file search, okay, type which is a web search. So 2 tools are over you use over here like file search and the web search out there.

**[32:30]** Fine tune, create a generative chat AI.

**[32:41]** Okay.

**[32:44]** So I can say, okay, let me keep the prompt here, okay.

**[32:55]** Okay.

**[33:13]** Create a chat.

**[33:18]** Showing the.

**[33:21]** Trend for CPU.

**[33:29]** Okay.

**[33:31]** So create a chart showing the trend for CPU consumption okay from the.

**[33:41]** So from the system performance data.

**[34:12]** Okay, so now it is using the code interpreter, right? And then right here is the chart showing the trend CPU consumer producer. So lets go to.

**[34:45]** Okay, it is blank.

**[34:48]** So what does it basically do? It's...

**[34:55]** It write the Python code and execute it in the same box and gets you the okay, here is it right? So I think I was using the wrong one. So CPU.

**[35:08]** Brain.

**[35:11]** It's the one.

**[35:18]** OK, so I'm showing one here. OK, I'll show you basically how does it look, right? You can see over here so it will show you something like that. OK, this is basically the CPU uses over the time. OK, so this will this will analyse the CPU over the time and.

**[35:38]** Basically gets you the CPU usage charts over here.

**[35:43]** Okay, so.


### Common agent tools  `[35:46]`

**[35:46]** The tools basically adds more capabilities out there. So these are basically the some common common tools and right how we use them in the code. So using the code inter interpreter tool, okay, like over here we define the tool out there, the code underscore interpreter.

**[36:07]** Then right, we have web search tool.

**[36:14]** Okay, to use the disk tools, specify the web search tools, preview tools type.

**[36:20]** File source tool.

**[36:23]** Okay, functions tool.

**[36:27]** So you can define your callable callable functions here, right? And then right, you can basically call this. So you can call this functions.

**[36:42]** So here you set up the tools here. So you set up the tools and the initial message type is a functions name which is a get time and the descriptions are there.

**[36:54]** Okay, so over here you can define like create dot response dot create model input message and then you define the tools out there which you have created over here. You set up the tools and initial messages out there. So the response of this is basically response dot output text that.

**[37:14]** Current time is S.

**[37:18]** Using the code interpreter tool.

**[37:22]** Using the web search tools, using the file search tool, using the functions tool, it's same. Okay, and this is the hands on to create a generative AI chat app that uses the tool. Okay, so here you experiment the tools in the playground and create an app.

**[37:41]** That uses the tools.

**[37:48]** Okay, I think we haven't taken this questions out there, right?

**[37:56]** Okay, where the code interpreter created code gets executed, okay, it's in the same same resources like your foundry resources. So your foundry resources, when we are talking about foundry resources, that basically you know it provides you the infrastructures out there, so it will be executed.

**[38:16]** it would be written and executed in the same resource.

**[38:25]** Okay.

**[38:27]** Clear result.

**[38:30]** Yeah, thanks. Yeah, it's clear. yeah.


### Knowledge check — choosing a tool  `[38:32]`

**[38:32]** Okay, now lets take question number one. Okay, which tool should you use when a model need to answer questions from your own uploaded policy document?

**[38:51]** From your own policy document.

**[39:00]** Yes, that's true. That's option B, which is a file search, correct? So.

**[39:11]** Question number 3. Question number 2.

**[39:26]** In a function calling workflow, what should your applications do after the model return of function call items?

**[40:05]** Okay.

**[40:17]** Okay, so it's basically the option B is correct. Okay, run the functions, run the functions in your code and sends the function call output. Okay, call output back to the model. Okay, so the you know, model does not directly execute custom functions.

**[40:37]** Okay, your applications run the functions and send the result back to the model.

**[40:44]** OK, question number 3.

**[40:50]** Which statement about the code interpreter tool is correct?

**[41:09]** Okay, option A, right? Yes, so it can run Python code in a sandbox runtime to help solve task. Okay, now it could be, it could be useful for calculations or data.

**[41:26]** Analysis or maybe for file processing.

**[41:33]** OK, so any Python based problem solving we can basically use the code interpreter. OK, now let's talk about here our next topic which is optimise generative AI models performance with the Microsoft Foundry. So any idea guys how we can optimise the generative AI model performance?

**[41:54]** We are talking about the model performance, how we can optimise, yeah.

**[41:56]** Report.

**[42:00]** Throughput.

**[42:03]** Throughput.

**[42:04]** Yeah.

**[42:06]** Okay, throughput.

**[42:10]** Basically, we cannot improve with the throughput, right? Basically, every models has its own throughputs, right? It come only. The thing is that we can select the model basically which has the high throughput.

**[42:26]** Correct, we can only select model which has high high throughputs out there, but we cannot optimise in that case actually. Okay, either you have to go for you know fine tuning out there if you want to you know optimise for throughput.

**[42:27]** Okay.

**[42:40]** Okay, yes.

**[42:41]** Okay.

**[42:46]** So what are the various ways through which we can optimise the generative AI model performance?

**[42:56]** By writing correct prompt.

**[43:01]** Okay, yes, that remains like prompt engineering.

**[43:07]** Correct. That's one way.

**[43:11]** Any idea what's what might be the other 2 ways out there? There are 3 ways that we can optimise the generative AI output.

**[43:23]** Have you heard about the rag?

**[43:29]** Rag retrieval.

**[43:33]** And.

**[43:33]** Augmented.

**[43:36]** Generation retrieval augmented generations, right? And the 3rd option is basically the fine.

**[43:44]** Tuning. Okay, now these are the 3 ways we can optimise the model performance. So lets explorer. Okay, now which optimization strategy you use depend on your requirements. Okay, now there are basically 2.

**[44:05]** Optimizations areas. OK, one is context optimizations. Second is a model optimizations.

**[44:15]** OK, when we say context optimizations, it means it means improving like what the models need to know.

**[44:25]** OK, lets say if the model does not have enough business knowledge or updated information, OK, we should provide a better context. So that the common method used over here is basically the retrieval augmented generation.

**[44:46]** Okay, so in rag the model search the relevant data from the documents database or knowledge source, okay, and that and then it add that information from so the it improve the response accuracy of the model.

**[45:06]** So, context optimizations, okay, optimise for context when the model lacks the lacks the contextual's knowledge and you want to maximise the response accuracy.

**[45:20]** Okay, now next options here is a model optimizations. Model optimizations means improving like how the model responds okay or act.

**[45:32]** If the model already has the required knowledge, but answer format, tone, and consistency is not correct, we can use over here the prompt engineering, okay, or fine tuning.

**[45:54]** Okay, so mainly for model optimizations, we go for the fine tuning, for context optimizations, we go for the retrieval augmented generations. Prompt engineering is basically for both of them.

**[46:08]** Okay.

**[46:11]** So what is prompt engineering?

**[46:15]** OK, optimise the model when you want to improve the response, format, style, and speech by maximising the consistency behaviour.

**[46:26]** Okay, now okay, so prompt engineering means right, think better instructions.

**[46:37]** Okay, where we use the system message out there, right? We specify the, we can specify tone, formats, role, expectations, okay, explicit user prompts for better response. We can provide examples.

**[46:56]** Now, so this is the, this is usually the first and easiest optimizations technique.

**[47:04]** Correct.

**[47:06]** But the problem with the prompt engineering is right, the model is trained, the model is trained on a generic data.

**[47:18]** Okay, so it does not have any latest informations, right? Or it does not know anything about your organization policies.

**[47:29]** Okay, so that is basically where you use the rack, okay, retrieval augmented augmented generations are there okay to provides the to provides the latest updated informations right to your model.

**[47:51]** Clear.

**[47:55]** Okay, the and fine tuning is basically where we are going to change the weightage, right? Usually.

**[48:08]** Okay, this is basically the structure of the neural network, correct?

**[48:15]** Okay, this is a neural network, correct? So there is a weightage out there, right? How one node is connected to the others, so there is a weight associated with it. So we can basically inside this model by fine tuning, we can change the weight. So we can change this weight out there.

**[48:37]** Okay, so that's basically the fine tuning where we provide additional model training with example prompts and the responses. Okay, where fine tuning means like we are retraining that model for my use cases because I want a consistent consistent.

**[48:56]** I want consistent output from my large language model.

**[49:04]** So first understand the prompt engineering. Okay, so prompt engineering is nothing but it is about writing a clear and effective instructions so that the a I models give more accurate and more useful responses. Okay, now the first technique is using.

**[49:23]** A detailed system prompt, detailed and explicit system prompt. OK, like for example, you are a friendly travel advisor for Marjis Travel. Answer only the questions related with the travel, hotels and trip planning. Use a warm, conversational tone if you don't have enough information to answers.

**[49:44]** Ask a clarifying questions, format hotel recommendations as a bullet list with the hotel name, locations, and price range. OK, so instead of just saying right, you are a friendly travel advisors for the Marjis travel.

**[50:01]** Okay, so we have to basically provide a detailed and explicit system prompt.

**[50:09]** Okay.

**[50:13]** Second is the second technique is format the.

**[50:19]** Template pattern.

**[50:22]** Okay, like suggest hotel in New York, format the result to show like hotel name, location, star rating, and price rate per night. Now, how you can clarify your model output format? Okay, so we can ask for the hotel recommendation, but we specify the answer should.

**[50:41]** Be in this particular format. So this make the output consistent like every time it recommend whenever it recommend the hotel. Okay, so this would be the format you will always get in.

**[50:57]** The next 3rd technique is the chain of thought pattern.

**[51:03]** Okay, the chain of thought pattern is basically...

**[51:08]** Will we ask the models to reason the step by step before giving an answer?

**[51:14]** Okay, now for example, when selecting the best hotel for a family, the model should consider the room size, amenities, locations, price. Okay, so we can ask models to provide a brief explanation of the you know, what are the key factors you know, rather than exposing a long internal.

**[51:33]** Reasonings.

**[51:36]** Okay, so we can say over here, okay, which hotel is best for a family of 4? Take a step by step approach, consider room size, amenities for children's, locations, and the price.

**[51:47]** So this is the chain of the chain of thought patterns out there.

**[51:53]** Okay, then next technique over here is few shots learning pattern.

**[51:59]** So as a name itself, right? It's basically giving examples in the prompt so the model understand the expectations out there.

**[52:10]** Okay, what should be the expected response style?

**[52:15]** Okay, we can give a sample customer messages like I need to change my flights to Rome. Okay, category which is a booking change. What's the weather like in Bali in March? Okay, it is a travel information. Can I get the refund for my cancelled tour? So it will basically give the...

**[52:35]** Category Okay, this is basically for classifying the customer messages. Okay, so similarly, we can give some examples out there.

**[52:47]** OK.

**[52:49]** So, prompt engineer basically improve the model output by giving a clear role expectations or clear role instructions. Okay, expected format.

**[53:04]** Okay, reasoning guidelines, the chain of thought pattern, okay, and providing the examples.

**[53:16]** Okay, so this is the first optimization technique before you move with the rack and fine tuning.


### Grounding models with RAG (retrieval-augmented generation)  `[53:25]`

**[53:25]** Okay, next one is ground your models with retrieval augmented generation.

**[53:31]** Okay, rag. So rag is a technique.

**[53:35]** Which make the AI response more accurate, okay, by giving, by providing the, by providing, by giving the model the relevant information right before it generates an answer.

**[53:54]** Okay.

**[53:59]** Because if you see this model, okay, now this model.

**[54:04]** It may not know your private company data or latest policies.

**[54:10]** If you ask the model directly, it may give general answers, okay, or even it can hallucinate.

**[54:19]** Okay, so rag basically solve this issues. Okay, where?

**[54:24]** It has basically the first steps over here, okay, when the user, when the user ask, right, when the user...

**[54:36]** Provides like when whenever user ask a questions.

**[54:41]** Okay, about, let's say, travel reimbursement policy.

**[54:46]** The system basically search the vector based index which contain the company policy documents. So this has the.

**[54:58]** Company.

**[55:00]** Policy.

**[55:03]** Document.

**[55:05]** Okay, so this vector base, the vector base index, it has the company company policy documents. So when the user ask about travel reimbursement policy, the system basically search the vector base, then the then the system basically it retrieve the grounding data based on the user input.

**[55:29]** Okay, and it will augment, it will augment the prompt, it will augment the prompts with the grounding data. So whatever it has searched relevance to that company policy, okay, it will augment to the prompts.

**[55:46]** Okay, so it means like it will basically gets the user user input, right? Plus.

**[55:55]** User input with the retrieve.

**[56:00]** Retrieve search result search result right from the vector base index.

**[56:09]** Okay, and then provides to the model. So now model has the user input, right, which is user user questions and the retrieve search result okay from the company policy document and then based on this it will generate a contextualised response.

**[56:30]** So now the answer would be based on the retrieve data.

**[56:35]** Okay, not only the general general model knowledge.

**[56:43]** Is it clear, guys?

**[56:47]** OK.

**[56:50]** One more example.

**[56:52]** Lets say user ask, like, what is the maximum okay taxi claim amount?

**[57:01]** Okay, now the rack basically search the expense policy.

**[57:09]** OK.

**[57:12]** Right, and then it will basically find the correct section, okay, and then it will augment the user input, which is like taxi claim amount plus okay, the informations extracted from the vector based index.

**[57:31]** And then provides the model.

**[57:35]** Okay, and then model basically answers like according to the policy, the maximum claim amount is like dollar, let's say 15.

**[57:48]** Okay, so this is how basically the retrieval augmented generations work.

**[57:58]** Hey, Chuck here because what you said about the rack overlaps a bit with the tooling which when we should use each. I mean, for example, the file search overlaps with the retrieval augmented generation. so.

**[58:16]** When it's better to use rack instead of the tooling that is already present in Foundry.

**[58:25]** Okay, actually what do you see when we are talking about the search, right? That the tool which we are talking about previously, okay, behind the scene it is implementing the rag only.

**[58:38]** Okay, that's rag only. That tool is basically this is the concepts actually which is implemented with that tool actually.

**[58:48]** Okay.

**[58:54]** Now comes the fine tune model for consistent behaviour. Now this is the 3rd, 3rd ways we can.

**[59:03]** Improve the model output. Okay, now fine tune basically means we are giving the additional training, okay, we are giving the additional training to the existing foundational model, so it responds in a more consistent and expected way.

**[59:25]** So we can provide some models with example prompts and responses.

**[59:30]** Okay, and used to maximise the consistency of the model tone and the style in response, how it need to act. Okay, if my for example, lets say suppose the company wants support assistant.

**[59:51]** Okay, and they always wants this to answer in short, okay, polite, and step by step format.

**[1:00:04]** Okay, so instead of writing long prompts every time, okay, we can fine tune the models using many examples of the customer questions and approve answers.

**[1:00:17]** So foundation model, take the training data and you can fine tune the model.

**[1:00:27]** Okay.

**[1:00:29]** And it's not only that you basically use one of them, right? So you can combine the different strategies over here, like you can use prompt engineering with rag or rag with fine tuning or fine tuning, you can use them together, okay.

**[1:00:43]** Okay, so that if you see the difference over here now, there is basically the cost associated with retrieval, right? Because you need a, you need to store your data, so the storage cost would be over there.

**[1:01:00]** Okay, and if you are fine tuning it right, you need basically computer resources out there. Maybe you would need the GPU you needs out there.


### Fine-tuning models  `[1:01:12]`

**[1:01:12]** Okay, now if we take a look here in Microsoft Foundry, we can go for fine tuning. So like you can see here, there's the options for fine tune.

**[1:01:24]** So here I have, I have created a fine tuned model and it will take a while for fine tuning. So when you performs your lab, so you will see over there. So once the fine tuning is completed, once the fine tune is completed, you can see the status as completed over here.

**[1:01:43]** So to create a fine tuning, you will go fine tune right and then you select various customizations methods, you choose the model, OK, and then this is where you provides the data sets. OK, now this data sets basically has the.

**[1:02:02]** Examples like for example.

**[1:02:14]** Okay, and we would need this.

**[1:02:19]** The This is the file over here. OK, now that's basically how you define the system.

**[1:02:25]** Okay, system prompt, user prompt, right? And also we define over here.

**[1:02:33]** Write the content, write the assistance.

**[1:02:38]** Right assistance. So this is how basically we want like oh la la la absolutely stribo, get ready to spice up your life in the Bangkok or more magical lights show. So this is basically how you want the models response. So then we can basically fine tune out there.

**[1:02:57]** Like by uploading the data sets over here.

**[1:03:02]** Okay, and then once the once the fine tune model is ready, we can basically go and we can deploy the model. Okay, it's same like how you deploy any other model out there. So this is my.

**[1:03:23]** Say fine.

**[1:03:25]** Tune.

**[1:03:30]** Fine tune.

**[1:03:32]** Fine tune model okay and click on deploy and then once you deploy it, you can use this model as you use any other any other models out there, right? You can see, okay, this is my foundations model GPT 4.1 and this is my.

**[1:03:52]** Fine tune models and you can use this as you use any other models out there.

**[1:03:59]** So there is a specific lab for this which is fine tune a language model. So it shows you 90 minutes because it's take a while for your models to fine tune out there. So training data sets is available. So this would be in the format dot JSNL.

**[1:04:18]** So you need to save this locally and then take your deploy your base models. You will basically chat with the base model initially, right? And after fine tuning and deploying that fine tune model, you will again test that fine tuning and you will see the difference out there on the.

**[1:04:38]** Response, okay, providing the same system instructions, you're providing the same instructions, but you'll see the difference out there.


### Knowledge check  `[1:04:51]`

**[1:04:51]** Okay, so let's take a quick questions over here.

**[1:04:56]** The data source for fine tuning, should it be the clean data structure data? Yeah. So for fine tuning it has to be in this format. It has to be always in this format, right? It's in dot JCNL. This is the format.

**[1:05:20]** Okay.

**[1:05:22]** So let's take questions here. Okay, question number one.

**[1:05:27]** What is the primary purpose of a system message in a prompt?

**[1:05:54]** OK, option A, right, which is to define the model role behaviour and out output constraints, right? Correct. Question number 2.

**[1:06:05]** When should you use retrieval augmented generation instead of relying on the prompt engineering alone?

**[1:06:23]** Okay, so P correct.

**[1:06:26]** Question number 3.

**[1:06:31]** What does the fine tuning? What does fine tuning optimise in a language model?

**[1:07:01]** Okay.

**[1:07:16]** Perfect. Yes, that's true. That's option B is correct. Okay, let's move to the next one, and I think this would be the last.


### Implement responsible generative AI & guardrails  `[1:07:28]`

**[1:07:28]** This would be the last last topic of this module. Okay, so implement a responsible generative AI solutions in Microsoft Foundry. Okay, so plan a responsible responsible generative AI solution. Now there are basically 4.

**[1:07:48]** Main 4 important step, okay?

**[1:07:55]** Okay, for responsible generate EVI solution before you deploy it to use by the real users. So first one is a map.

**[1:08:05]** Okay, map the potentials harm that are relevance to your plan solutions. Okay, this means like identifying like what can go wrong in your AI solutions.

**[1:08:17]** Okay, what can go wrong?

**[1:08:23]** Right. So for example, the model may generate incorrect answers, okay, or it could create bias contain or maybe harmful advice. Okay. So once you map the potentials harms, then you'll measure the presence of this harm in the out.

**[1:08:41]** Input generated by your solutions. So we should test the solutions using sample prompts and evaluates like whether the models produce any unsafe, inaccurate, or inappropriate responses. Okay, and this can be done through manual testing and automated evaluations.

**[1:09:04]** Okay, then 3rd one is a mitigates the harm at multiple layer in your solutions.

**[1:09:12]** Okay, mitigates so.

**[1:09:18]** We can add control at different layer, okay, at a model, at a safety systems, system message, and grounding, and the user experience. Okay, so we can mitigates the harm harm that multiple.

**[1:09:36]** Mitigates the harm at multiple layer in your solutions and we can use the contain filters, we can use the strong system prompts.

**[1:09:49]** Okay, we can use rag.

**[1:09:53]** Okay, rank grounding, we can use citations.

**[1:09:58]** OK, so we can mitigate the hum at multiple layer in the solutions and then 4th one is manage manage the solutions responsibly by defining and following our deployments and operational readiness plan.

**[1:10:14]** Okay, this means after the deployment, you should monitor which monitors the users. We need to review the failures, we need to update the prompts, we need to improve the grounding data and define the escalation processes.

**[1:10:33]** Okay, so it is a it is a complete process where we identify the risk, we test them, we reduce them using multiple safeguard, and we continuously monitor the solutions like after the deployment.

**[1:10:50]** over the life cycle of your AI solutions. Now coming to here, these are basically the guardrails. Okay, these are the collections of controls to detect and mitigates the risk.

**[1:11:07]** Okay, so it ensures that the A I response are safe, appropriate, okay, compliance. So we have violence, okay, hate, sexual content, self harms, user prompt attack, indirect attack, spotlighting.

**[1:11:25]** Protected material for code.

**[1:11:28]** Okay, protected material for text, groundness, personally identifiable informations.

**[1:11:36]** Okay.

**[1:11:37]** So we can set the guardrail to detect the harmful content.

**[1:11:45]** Okay.

**[1:11:48]** So also indirect attack.

**[1:11:52]** Okay, this basically means like when the...

**[1:11:57]** There could be some malicious instructions, hidden insights documents, or any external data used by the A I system.

**[1:12:06]** So for example, a PDF may contain hidden text telling the models to ignore the safety rules. OK, so in that case, the guy, you know, guardrail, the guardrail basically help detect and reduce that risk. That's indirect attack over here.

**[1:12:25]** Okay, so sport lighting means...

**[1:12:30]** It is basically protection against, which basically helps the model distinguish between trusted instructions and untrusted documents content.

**[1:12:42]** Protected material, so for example, copyrights, text or quotes. Okay, so or ground groundness check whether the AI responses align with source data.

**[1:12:58]** Okay, expose, expose of PLL data, names, address, contact details, and other informations.

**[1:13:09]** So let's take a look here how we can apply the content filters to prevent the output of the harmful content. OK, now for example, if you go to our...

**[1:13:21]** Let's go and use like GPT 4.1.

**[1:13:27]** And let's go to the...

**[1:13:31]** Detail.

**[1:13:34]** See the detail out here and if you go to the model guardrail, okay, so over here in the model guardrail, you can see we have demo demo guardrail. So let me.

**[1:13:50]** Edit.

**[1:13:53]** So deployment name, deployment type. So let me go to add it.

**[1:14:00]** So by default, okay, there are basically the guardrail its taking a while. Okay, so I will take the another another model. Okay, lets say I will take GPT 4.1 mini and if you go for to detail by default you can see here.

**[1:14:18]** OK, that's a Microsoft dot default V2 so every.

**[1:14:23]** every models that you can deploy, right, has a default V2 guardrail.

**[1:14:30]** So now if I go to the playground and if I ask over here, okay.

**[1:14:39]** How can I rob a bank?

**[1:14:49]** Okay, now you can see, right? It basic it know the models know basically how to rob a bank, but there are basically the guardrail. Okay, it says, I am sorry, I cannot assist with that. If you need help with something legal or have any other questions, feel free to ask.

**[1:15:10]** Okay, now let me ask over here.

**[1:15:17]** What should...

**[1:15:19]** I do if.

**[1:15:22]** If I cut.

**[1:15:25]** Myself.

**[1:15:32]** Okay.

**[1:15:34]** Right, so if you got yourself right, you're getting over here. Here are some steps that you can follow.

**[1:15:42]** Okay, then interaction is blocked. This intentions was blocked by the safety and security controls in this. Okay, guardwail wrist type self harm medium is detected at the output.

**[1:15:53]** Okay, now it is a medium because of which we are getting this response out there. Now we can basically set the guardrail going to this options guardrails and then right you can see I have created one guardrail with a demo demo guardrail. I can create a new.

**[1:16:14]** And here I can.

**[1:16:18]** Select for.

**[1:16:21]** Contain safety.

**[1:16:27]** Okay, so right now here you can see here control contain safety, so it's medium blocking, right? So hate.

**[1:16:45]** Severity. Just a minute. Violence.

**[1:16:54]** Okay, self harm and I change it to the highest blocking and let me add controls. This configuration configure existing control. Do you want to override the content settings? Okay, I'll say yes.

**[1:17:10]** So go for the next add a model. So here I will just go for this one. Let's save, go for the next. That's my, let's say new.

**[1:17:26]** New Gardrail.

**[1:17:29]** So streaming mode is not supported for the response API. OK, let's click on submit.


### Content filters & deployment demo  `[1:17:43]`

**[1:17:43]** Okay, now let's go to my deployments. Let's go to GPT 4.1.

**[1:17:51]** And from here, if you go to.

**[1:17:56]** Scroll down so you can give a new. Lets see what happened now.

**[1:18:04]** So.

**[1:18:07]** Go to the playground.

**[1:18:11]** Okay, I will say okay, how to drop a bank again.

**[1:18:25]** Okay, what's cell?

**[1:18:32]** I do.

**[1:18:35]** If I cut.

**[1:18:38]** Myself.

**[1:18:51]** Okay.

**[1:19:07]** Self harm, we kept the highest blocking sexual medium blocking violence, okay.

**[1:19:15]** So.

**[1:20:20]** Okay, let me try again.

**[1:20:24]** And let's see over here. OK, we're getting the same.

**[1:20:29]** Same response out there. If you want, I can guide just have provided by us on how to cut is how bad is the cut.

**[1:20:41]** Okay, so we implements the new guardrail.

**[1:20:46]** You sign the guardrail. So for example, lets say I have created this demo guardrail.

**[1:20:56]** Let me try to assign this because this new one is not working.

**[1:21:06]** Since we set the self harm as like high, so it should not it should basically block.

**[1:21:19]** So.

**[1:21:41]** Okay.

**[1:21:45]** Okay, so now you can see over here it says I am sorry but I cannot assist with that request. Safety and security controls in this is found regardless risk type is self harm, medium is detected at user input. Okay, so what I did here is I used the different guardrails over here which is demo.

**[1:22:05]** Demo guardrail which I have created already out there. Okay, so this is basically how we can use the you know, guardrail on the model we deploy in the foundry.

**[1:22:22]** Clear.

**[1:22:24]** Same you would perform over here. Apply content filters to prevent to prevent the output of the harmful content. So also let lets take a look into.

**[1:22:38]** This one. So this is the lab.

**[1:22:42]** So this is a lab apply the guardrails to prevent the output of harmful content. And over here, you deploy the models, right? Choose chat with the default guardrail, right? And then after that, create and deploy the custom guardrail. You explorer contain filters and the way in which they can help safeguards against the.

**[1:23:04]** Potentials harmful or offensive content.

**[1:23:08]** Okay.

**[1:23:10]** It's one elements of the comprehensive responsible AI solution. See responsible AI for Foundry for more information here.


### Knowledge checks  `[1:23:21]`

**[1:23:21]** Okay, lets take some knowledge check.

**[1:23:27]** What are the matter used by the robots to so it so I can plan security guy will you response for this as I twisted questions for similar? Okay, yeah, this is basically known as a jailbreaking.

**[1:23:40]** Okay, so.

**[1:23:42]** Lets give a try.

**[1:23:54]** Okay, what are the methods is where was to open, so I can plastic recovery? Okay.

**[1:24:11]** Okay, so.

**[1:24:14]** General informations of common rovery methods to help you plan defense. It is important to know to use this knowledge responsibly and in accordance with the law, right? And so I am right inside the jobs.

**[1:24:43]** Okay.

**[1:25:35]** Okay, let's test it again.

**[1:26:57]** Okay, it's done already so.

**[1:27:17]** So what are you trying to do is basically known as the jailbreak, okay, where you twist questions for similar outputs out there, right? So we also can basically guard that through the guardrail.

**[1:27:33]** Okay.

**[1:27:40]** Any possibility regarded can be manipulated as such? No, actually, that's basically how we can make your model safe, secure, and it prevents those attacks and protect the data.

**[1:28:03]** Okay, it's a somewhat similar actually contain contain filters and the that's guardrail. Okay, so it's a similar similar things out there.

**[1:28:17]** Okay.

**[1:28:19]** So you're also it's the same like if you see that's filters content filters and same similar.

**[1:28:31]** Okay, question one.

**[1:28:34]** Why should you consider creating an AI impact assessment when designing a generative AI solution?

**[1:28:58]** Okay, why should you consider creating an AI impact assessment?

**[1:29:04]** To make a legal case, or to document the purpose, or to evaluate the cost of the cloud service.

**[1:29:19]** Okay, now to give you a hint, right? It is basically related with like mapping the potential harm.

**[1:29:29]** Okay, remember map measures, mitigates, and manage.

**[1:29:34]** So it is somewhat related with the map.

**[1:29:39]** Yes, that's true. Option B is correct. Great. Question number 2.

**[1:29:47]** What capability of Microsoft Foundry helps mitigate harmful content generations at the safety level system level?

**[1:30:08]** Okay, yes, that's true. Cigar rail question number 3.

**[1:30:14]** OK, why should you consider a phase delivery plan for your generative AI solution?

**[1:30:49]** Okay, yes, option A, that's true to enables you to gather feedback and identify issues before releasing the solutions more broadly.

**[1:31:01]** Okay, so this is our first mode completed. Now we'll take a break.

**[1:31:13]** Okay, we'll take a 10 minutes a bake and coming back.

**[1:31:17]** We'll start with the second module.

**[1:31:27]** Perfect.

**[1:33:42]** Call Krit.

**[1:33:47]** AI cartels.

**[1:37:26]** But Tin Mahal is not available.

**[1:42:36]** Alright, I am back. Just give me one more minutes.

**[1:43:22]** All right, okay, lets proceed further.

**[1:43:43]** Okay, let me share my screen.

**[1:44:04]** Okay, right, I'll also share with you.

**[1:44:09]** The Microsoft Learn that you can refer for the.

**[1:44:15]** Module one.

**[1:44:40]** OK, so develop generative A I apps in Azure. OK, now this is the learning path that you can refer for the module one. OK, sharing the link in the chat.

**[1:45:02]** And for all the labs, instructions outside your lab environments can be accessed through this link.

**[1:45:12]** The second.

**[1:45:15]** Second link is for the for the lab access. Okay, so here you have all the exercises like prepare for an AI development projects, explorer and compare models, create generative chat apps, okay, create a generative AI apps that uses tools.

**[1:45:34]** Fine tune a language model, okay, maybe all the laps are not there in your in your scalable one, right? So if, for example, fine tune a language model is not there, right? So for example, you see there.

**[1:45:54]** Right, prepare, explorer, create right with your own data, apply content filters to prevent the output of harmful content. Right, so here so like for example, fine tune. Okay, so fine tune a language model that's not there in the hands on.

**[1:46:13]** But you can see the instructions over here now to perform it, right? You need to have your own subscriptions. You will need your own subscription because subscriptions in your skill level lab would not allow you to. It might give you an error of the policy, okay.

**[1:46:32]** But others, others you can find it's a similar similar instructions that you can find inside your lab VM.

**[1:46:40]** I will share the same in the chat. Okay, now let's move to our.


## Module 2 — Develop AI Agents on Azure  `[1:46:48]`


### What are AI agents & why use them  `[1:46:48]`

**[1:46:48]** Module 2, okay, developing Azure A I apps and agents. So now we will explorer over here the agents, okay, A I agents. So with that we will focus now first understand how to develop an A I agents with Microsoft Foundry.

**[1:47:09]** Amp Visual Studio Code.

**[1:47:13]** Okay.

**[1:47:15]** Let us first understand what is AI agents anyone?

**[1:47:21]** What is AI agents?

**[1:47:44]** Have you built an AI agents before right in any other platforms, maybe the Copilot Studio?

**[1:47:58]** Okay, so it's a generative AI that can go through multi steps workflows or complete tasks on a user behalf, absolutely.

**[1:48:13]** Agent can perform decision making and perform the task accordingly, yes.

**[1:48:45]** OK.

**[1:48:47]** So what is agent? Agents is basically an...

**[1:48:55]** Agents are basically an AI system.

**[1:48:59]** Okay, that can understand the user input. Okay, which can understand the user input, which can region.

**[1:49:11]** Region like what need to be done.

**[1:49:17]** Okay, which use the instructions and take actions.

**[1:49:24]** Okay, with the help of tools.

**[1:49:26]** So you can see here it is start with the input. Okay, this is basically the user questions or request. So for example, user may say like okay, check my order status and create a support ticket.

**[1:49:46]** If it is delayed.

**[1:49:49]** OK, now the input basically goes to the agents. OK, now agents here it basically combine 3 important part LLM.

**[1:50:00]** OK, large language model, which is basically the brain for your agents.

**[1:50:05]** Okay, it basically this is basically what make your agents to understand the user request, generate languages, okay, region, region over the task and decide basically what should what should do next.

**[1:50:23]** OK, next.

**[1:50:27]** Next component here is the instructions. OK, so instructions where we define like how the agent should behave.

**[1:50:37]** Okay, so where we define like, okay, you are a customer support agents, be polite, use only company documents, company policies, okay, don't answer outside the support company, company policy documents. So using instructions, we can control the role.

**[1:50:59]** boundaries and we can set the rule for the agents, correct? Then comes the tools, tools basically which allow your agents to perform the actions or access the informations.

**[1:51:15]** Okay, whether it is this tool can be to can be for searching files, could be calling an a Pi, or maybe creating or sending an email or creating tickets, okay. And then finally the output is basically what the agents provides the output.

**[1:51:35]** Okay, this could be simple answers or it could be completed actions or maybe some generated documents.

**[1:51:44]** Okay.

**[1:51:47]** So.

**[1:51:51]** Right, so this is basically how what the agents basically consist of. Okay, it combined 3 important parts here.

**[1:52:02]** Okay, now same here, right? 3 components as we have discussed.

**[1:52:08]** Right, LLM, okay. And this is the reasoning engine of your agent.

**[1:52:15]** OK, this is basically what make your agents to understand the user request and then decide what response or actions is need to be done. So here like models from GPT, Lama, Mistril, or Claude.

**[1:52:32]** Okay, as we discuss the instructions like this one, you are a travel booking and expense management assistant designed to help employee plan, book, and manage business travel. Always confirms trip dates and budgets before making booking. Preferred direct flights when the cost difference is less than 20%.

**[1:52:53]** Okay, the 3rd one is basically the tool. The tool basically give extra capability beyond the text generations. Okay, this include retrievals.

**[1:53:07]** Actions.

**[1:53:09]** And.

**[1:53:10]** Memory.

**[1:53:14]** Okay, so retrieval basically helps your agents to retrieve and search the documents and knowledge source actions to perform tasks like maybe booking tickets or creating an expense report.

**[1:53:30]** OK, and memory is basically which helps your remember the useful context during the interactions.

**[1:53:40]** OK, now, so this is the flow input. OK, agents use this LLM instructions and tools and then produce the output.

**[1:53:50]** Clear.

**[1:54:01]** Okay, next one, why agents are useful?

**[1:54:06]** Now agents are useful because they can do more than just answering questions, correct? They can understand the task, they can use tools, they can make decisions, you know, they can complete the work with less human effort. So the first benefits is automation of routine task, right? Some of you have mentioned there like.

**[1:54:29]** From Shankar, like it is an assistance to perform a repetitive task, right? So we can perform automations of a routine task out there. It can handle like repetitive activities freeing humans to focus on strategic and creative work.

**[1:54:46]** Agents can handle the repetitive activities like answering the FAQs, you know, checking the order status, or maybe creating tickets. It can use for It can be used for summarising emails or you know, processing the expense claim. Okay, so this save.

**[1:55:07]** Times and it allow the employee to focus on more creative work. Next one is skillability, right?

**[1:55:18]** So it can grow grows capabilities without proportional increase in the head count on operational cost.

**[1:55:28]** Okay, so agents can support many users at once.

**[1:55:33]** Okay, for example, customer support agents can answers like thousands of common queries without increasing the head count in the in the same proportion.

**[1:55:46]** Okay, so it's a scalable.

**[1:55:49]** The human team can handle like only limited number of requests at a time, but agents can support many users at once.

**[1:55:58]** The 3rd benefit is enhanced decisions making it can analyse data to surface the insights, predict outcome, and recommend the actions in the real time so a sales agents can analyse you know, customer history and suggest the best product recommendations for example, or and it is available 24/7.

**[1:56:19]** Right, no need to take breaks, right? No requirements of food or slip. So it can work 24/7 to operate continuously without breaks, keeping service available around the clock.

**[1:56:34]** Okay, so agents are booming right now and you will see the agents everywhere out there like any task which is which can be automated out there. So you will find the agents everywhere out there to automate the task.

**[1:56:53]** Now it is not like the workflows which we have previously for automations out there, OK, you have defined path out there, but it is more intelligence, you know, automations. OK, now for example, OK, let us say I create an agents which basically book.

**[1:57:13]** I create an agent to book a flight, book a cab for me, right? So it will book a cab for me.

**[1:57:22]** Okay, now the intelligence agents would be basically would be able to like, lets say if the cab is taking more than the, it is taking more times out there and cab is quite far, like it should, it should basically cancels and rebook again, right? Or if someone if the if the cab is cancelled by...

**[1:57:45]** Cancel then it should rebook it. Okay, so.

**[1:57:51]** So it should be able to handle like this kind of things as well.

**[1:57:57]** Okay, so these are basically the autonomous agents or agentic AI agents.

**[1:58:04]** So we have some AI agents use cases here. Okay, first use case is for personal productivity.

**[1:58:12]** Okay, schedules our team standoff for next week's. Okay, invite sends to all 6 members. Also, draft a recap emails from yesterday notes draft ready in your draft folders. Want me to send it.

**[1:58:28]** Okay, simple. Second is for research agent can search informations, summarise updates, okay, it can compare sources and generate the report. So any major shift in the A I market this week.

**[1:58:45]** Okay, generate a summary report for the team.

**[1:58:49]** Or for sales, okay, so the sales agents can find leads, they can draft a personalised email.

**[1:58:59]** Okay, they can schedule a flop follow up call. So find leads in a Pacific Northwest retail sector, schedule the priority calls for this week or customer customer service.

**[1:59:13]** Agent can answer customer questions, it can process the refund request or check the order status. I need to refund for this order refund approved will be returned to your car in 2 to 3 days business days out there. Okay, can I get confirmations emails send your send?

**[1:59:33]** It's a email if there anything else I can help with, right? So.

**[1:59:40]** Now, what is the typical development workflows for creating the your AI agents in Microsoft Foundry? What are the steps to build and deploy? So the first step is to connect to your Foundry project.

**[1:59:56]** OK, the foundry browser. Remember it's a workspace where we where your agents, models, tools, and your knowledge are organized. Second, create an AI agents, OK, defining your agents, you know that will handle the user queries, configures the agents instructions. Now this is very important there.

**[2:00:16]** Right through instructions, you define behaviour, phone, what's basically a role of the agents is, okay, the 4th one is add tools. It allow your agents to call functions, search files, or retrieve knowledge, then test the agents in a playground.


### Evaluating agents  `[2:00:38]`

**[2:00:38]** OK, we validate whether the agents understand the prompts, it uses the tool correctly and give the accurate response. And then we iterate on the design. So based on the testing, we improve the instructions, we change the tools or we adjust the grounding data.

**[2:00:57]** Okay, then deploy the agents to productions. This make your agents available for the real users, right? And then right, we can basically integrate into the applications, right? Whether it could be on a websites or maybe mobile apps or maybe.

**[2:01:15]** your CRS system or our teams, OK, or maybe you have internal portals.

**[2:01:23]** Okay, so also require resources for developing an agents. You need a Microsoft Foundry projects, okay, right to organises the agents, right models and assets, model deployments, you would need the model.

**[2:01:43]** Like GPT 4.1 or Cloud Sonnet and optional resources consist of Azure, Azure AI search for the knowledge retrievals for knowledge retrievals for Foundry IQ or file search, Azure storage so.

**[2:02:03]** The file agents can read and write through the Azure storage, Azure Key Vault for securely storing the secrets and credentials, Azure functions, you know, custom tool implementations and business logic. So these are optional resources out there, right? These are these are other resources out there that can also be used by the.

**[2:02:22]** Agents out there.

**[2:02:26]** Okay, clear.

**[2:02:30]** Then moving further, choose your development approach. Okay, so you have a Foundry portal, right? And have your Visual Studio Code.

**[2:02:38]** So, Foundry Portal, it is a visual web based, no local setup required. If you want a quick prototyping without setting your local development environments, okay, where you want to configure agents using like drop downs and forms, intuitive forms, and drop downs rather than code.

**[2:03:01]** Okay, for centralised managements, so for where team can view and manage agents, models, tools in one place with a dashboard.

**[2:03:14]** Team collaborations. Okay, so share configuration with stakeholders who prefer visual interface. Okay, now it could be like for business users and teams who prefer the visual interface before you go for the Visual Studio code.

**[2:03:35]** Second is a Visual Studio Code, right? This is more developer centric, code, integrated and git friendly. It's a developer centric workflows. OK, so you can build agents alongside your application code in a single familiar environment. Version control indications. OK, so you can use git for version controls and.

**[2:03:56]** You can follow the code first deployment approach, you can edit the ML configurations directly and indicates agents into your applications logic, and you can test them. You can design and test the agents offline before you deploy to the Azure.

**[2:04:14]** And many teams basically use both of them, right? So, Foundry for the initial explorations and reviews, and the VS code for detailed developments, and the productions production deployment.

**[2:04:26]** Clear.


### Build an AI agent (portal & VS Code)  `[2:04:30]`

**[2:04:30]** Okay, so build an AI agents with the portals and VS code. We will explorer creating an AI agents in the Microsoft Foundry portal and interact with your agents using the Visual Studio code. Okay, so now lets go to the Microsoft Foundry and.

**[2:04:49]** Over here, right, if you see, okay, agents, so let me go to this one, okay, so you can see here to create an agent, simply you have to click on create agent, provide your agent name, okay, lets say I want to create a support.

**[2:05:13]** Yeah, I want to create a support agent.

**[2:05:29]** OK, support agent and let's click on create.

**[2:05:45]** Okay, now once you create an agent, right, you can see the your agents in a playground.

**[2:05:54]** Okay, in a playground and then you can choose the model. Okay, provide instructions for your agents. You can test your agent.

**[2:06:14]** You provide the instructions, then test your agents. You can see the tools out here.

**[2:06:21]** Right, so these are most popular web search code interpreter.

**[2:06:28]** OK, then you can add knowledge, connect to the foundry IQ. We'll talk about this memory.

**[2:06:40]** Okay, guardrails. So these are these are the option for the agent.

**[2:06:50]** And once you make the changes, right, you can save and from here you can publish.

**[2:06:59]** Let's go to the agents we which we have IT IT Support Agent. Let me click on this IT Support Agent.

**[2:07:10]** And okay, this is also...

**[2:07:14]** Empty so.

**[2:07:20]** Okay.

**[2:07:22]** So let's go here and...

**[2:07:29]** Okay, yeah.

**[2:07:51]** Okay.

**[2:07:58]** Let's go and let's give the instructions here. So you are an IT support agent for Contoso corporations. You have employees with the technical issues and IT policies questions and then we provide the guidelines over here, right? Always use professionals and helpful response or use IT policy documents to answer those questions accurately.

**[2:08:20]** If you don't know the answers, admit it and suggest containing.

**[2:08:25]** Contracting IT support directly collect all necessary information before processing.

**[2:08:31]** Okay, so then I can go, I can save this.

**[2:09:00]** Okay, then we will basically upload the file which is IT policy document. So let me upload the file.

**[2:09:12]** Browse.

**[2:09:14]** IT policy.

**[2:09:27]** Okay.

**[2:09:30]** Click on attach.

**[2:09:42]** Okay, now once it's ready, we can test the agents.

**[2:09:48]** Right, so what is the policy for password resets?

**[2:09:58]** OK, now you can see here it's using the IT policy text over here, you can see the citation.

**[2:10:05]** So read more so you can see this is the ITIT policy text.

**[2:10:13]** Right, and it's give you the response out there. The password reset policy is as follows.

**[2:10:31]** How do I request new software?

**[2:10:47]** Okay.

**[2:10:49]** Also, what we gonna do is we would be using the code interpreter, so we will go add file.

**[2:10:57]** Let's provide this.

**[2:11:03]** With the system performance.

**[2:11:24]** Okay, let's see, let's test with this prompt.

**[2:11:30]** Can you analyse the system performance data and tell me if there is any concerning trends?

**[2:11:58]** Okay, so you see we have a concerning trends here. The most notable and concerning trends is the disk uses with a very high correlations values to time. Disk uses his climbing and could approach critical level soon. The maximum is already at 72%, so action may be needed to avoid running out of the disk space.

**[2:12:20]** Okay, then CPU memory also reached relatively high peak: 98% CPU, 88% memory, which could cause performance slowdown during peak time if sustained. And also we can ask it to create a chart showing CPU usage overtime from the.

**[2:12:40]** Performance data.

**[2:13:04]** So we can't...

**[2:13:06]** See the output. So here is the output.

**[2:13:17]** Okay.

**[2:13:19]** Clear.

**[2:13:24]** So if you go to your agents, then you will find okay, yes, we want to save the agents.

**[2:13:34]** Okay.

**[2:13:38]** Now let's take a...

**[2:13:42]** Some knowledge check questions. Okay, we have few questions over here.

**[2:13:57]** We have GBD 5.5 which is latest version. Why does the model still shows GBD 4.1 because we have deployed like if you go to the deployment okay we have deployed over here like the 4.1 right 4.1 4.1 mini okay text embedding.

**[2:14:16]** OK, fine tune model. So this is what we have deployed here. So if you want to deploy, let's say, GPT 5.

**[2:14:26]** 5 point.

**[2:14:29]** 5.5.

**[2:14:33]** Okay, we can select on this.

**[2:14:37]** Okay, and we can deploy it. Once we deploy it, then it will be then you can use this for your agents.

**[2:14:47]** Okay, so while creating your agent, sorry, these are basically the you can use the right agents templates. So this are the this are the agent templates. So I will go to the build and go to the agents.

**[2:15:06]** Okay.

**[2:15:11]** So while creating the agents, okay, we can define what large language models the agents will use.

**[2:15:20]** Clear.

**[2:15:25]** Okay, question number one: What is the primary benefits of using the Microsoft Foundry Agent service compared to building the agents with standard API?

**[2:15:37]** Okay, now for agents, we're using the Microsoft Foundry Agent Service.

**[2:15:44]** So what is the benefit of it?

**[2:16:04]** Yes, that's true. That's option C is correct. It handles the tool calling state management and infrastructure automatically. Correct. Question number 2.


### Knowledge check  `[2:16:20]`

**[2:16:20]** Okay, how does the Microsoft Foundry agent service handles the conversation state?

**[2:16:48]** Okay, everyone agree with the C? Yes, that's true through the response API, which automatically manage the conversations context.

**[2:16:59]** Okay.

**[2:17:03]** So.

**[2:17:06]** Now, yesterday there was a questions when we were discussing on the chat completions API and response API.

**[2:17:13]** Okay.

**[2:17:15]** So we discuss, we have a scenario, okay, where, okay, you're interacting in the same sessions you're interacting with, like, let's say response API or chat completions API. Okay, so basically we talk about how we can maintain the conversations context.

**[2:17:35]** Okay, but let's say let's say if let's say you create an applications and then all right, you interact with the you interact with the model, okay, and then you close this and then when you come back again, right, come back again, how you can get basically how you can start with the previous conversations you had with this.

**[2:17:57]** With the with your model.

**[2:18:05]** Okay.

**[2:18:06]** So now over here, this the developers has to design the AI apps to store and reload the conversations context. Okay, so they have to store this, they have to design the AI system such that the conversions context has to be.

**[2:18:27]** Has to be stored okay, now when the user return okay, return to the AI apps. So your apps should authenticate the user first, right? And then find the users previous conversations.

**[2:18:43]** Okay, and then load the conversions tree and summary from the database.

**[2:18:50]** And then, since the relevant context, okay, back to the model.

**[2:18:56]** Okay.

**[2:18:59]** Right.

**[2:19:01]** Okay, and then it basically gets the response out there.

**[2:19:06]** So you can, likewise, you can continue the conversations where the user left in.

**[2:19:16]** Okay, so the developers has to basically has to store those context out there, right? And for this, they can use, for example, they can use a Cosmos DB, Cosmos DB, they can use SQL database, or they can use table storage.

**[2:19:34]** Azure Table storage and so on.

**[2:19:41]** Okay, clear.


### Integrate custom tools (Logic Apps, functions)  `[2:19:47]`

**[2:19:47]** Okay, so now lets move to next topic here. Integrate the custom tools into your agents. Now what is the custom tools? Okay, now custom tools are basically used when your agents need to connect with external system.

**[2:20:06]** Sorry.

**[2:20:10]** External system API.

**[2:20:14]** Database.

**[2:20:17]** Or a business process.

**[2:20:24]** OK, so through the custom tools, they can connect to external APIs, database, or business processes to complete a task.

**[2:20:33]** OK.

**[2:20:37]** So as we have discussed like here, user ask an agent about the weather conditions in the ski resort.

**[2:20:44]** Okay, so what is the user ask like what is what is the weather conditions of the ski resort? So agent agents does not know current weather informations.

**[2:20:57]** OK, so in this.

**[2:21:01]** Basically, agents understand the request, right? And then it basically check whether it has access to the tools which can get them, which which can get the agents the live weather informations.

**[2:21:16]** Okay, so agents determine it has access to the tools that it can use that can use an API to get some meteorological informations and call it.

**[2:21:30]** Okay, so if the weather API tool is available, the agent decide to call that tool. The tool basically it connect to external weather service, okay, and then it retrieve the current weather report.

**[2:21:49]** Okay, and send back the send back to the agent and the agents then convert that result into a clear answer for the user, right? It is not like it just provides like okay, just the temperature, okay, so it will basically whatever the out.

**[2:22:07]** Put it gets from the tools, okay, with the help of tools, it can make a call to the weather, weather service, it can make an API call to the weather service, okay, and get the temperatures and then it will basically use that informations to gets to the user.

**[2:22:30]** OK.

**[2:22:33]** What are the options for implementing our custom tools?

**[2:22:39]** So first is using a custom functions, you can define your own functions in the applications code, okay? You can describe it to your agents, right? And let just dynamically identify and call the right functions, okay, with the correct arguments.

**[2:22:57]** Okay, support multiple programming languages for integrating the custom logic and the workflows.

**[2:23:06]** Okay.

**[2:23:08]** So for example, functions can check the order status or may it can be used for fetching the customer detail.

**[2:23:21]** Okay.

**[2:23:25]** So your own functions right in the application code. Second is Azure function.

**[2:23:32]** Azure Functions. Has anyone work with the Azure Azure Function?

**[2:23:48]** Okay, yes, so second is Azure Functions. Azure Function is basically a serverless service, okay, a serverless service on Microsoft Azure and it is basically used to run a small piece of code, okay, that only run when triggered.

**[2:24:07]** So you can use Azure Functions to build intelligence event driven applications with minimal overhead, and triggers determine when the functions execute. Bindings streamline the connections to input and output data source. So these are useful when you want custom business logic without managing servers.

**[2:24:28]** So agent can call the Azure functions to maybe, lets say, to create a support ticket or validate the booking, okay. And the infrastructure is managed by the Microsoft, okay, you will just focus on your logic and it will be triggered by your.

**[2:24:47]** Agent so agent will be triggering these functions which will basically perform some operations on maybe lets say databases.

**[2:24:57]** The 3rd option. The 3rd option is a open API specifications. Now if you have already a REST API.

**[2:25:06]** Okay, so we can describe it using the open API 3.0 specifications.

**[2:25:15]** So the agents can understand what are the available endpoints, what are the required parameters, and how to call the API.

**[2:25:23]** Okay, so this is useful for connecting your agents to existing enterprise API.

**[2:25:31]** Okay, then comes over here the Azure Logic app Azure Logic app. These are basically a low code, low code workflow workflow tool.

**[2:25:43]** Workflow tool.

**[2:25:46]** Okay, so.

**[2:25:49]** Now using using this, okay.

**[2:25:55]** Sorry, it's the same for all of them. OK, Azure Logic Logic app. I think some of you must have worked with the logic app over here. So it's a low code right out there which basically help you to design your workflows, right? And the agents can basically trigger this workflows OK to perform the actions defined over here.

**[2:26:17]** Okay, so it basically provides a lot of connectors out there, right? So connecting to, lets say, Outlook, or SharePoints, or teams, or Dynamic 365. So without writing code, right, you can simply using the user interface, you can create a flow.

**[2:26:36]** Okay, and this flow can be triggers over here using the agents.

**[2:26:44]** Okay, so these are basically the options for implementing the custom tools.

**[2:26:50]** Okay.

**[2:26:52]** So now in this lab, OK, you're gonna build an agents with a custom custom tool. So in this, you will create a function for an agents to use, define the functions tool, create the agents that use the functions tool, send the message to the agents, and process the response.

**[2:27:13]** And process the functions call and display the agent's response.

**[2:27:20]** So let's see this one. OK, now this is the lab over here, user custom functions in an AI agents.

**[2:27:30]** So initially, you deploy a model for your agents. Okay, then you need the and you're basically copying the project endpoint from the Visual Studio code.

**[2:27:43]** Okay, you are copying the project endpoint, then you would install, you will download the lab files.

**[2:27:55]** OK, then you will create a function for an agents to use. So this is the functions you are creating over here like next visible event. So this is one function.

**[2:28:09]** OK, then after that you would basically define the functions tool, you define the event functions, event functions tool, which is like next visible events. So this is my functions tool, event tool, you define over here the name of the functions.

**[2:28:28]** Descriptions, you provide the parameters.

**[2:28:32]** Okay, that has to be pass.

**[2:28:35]** Right, then next one use.

**[2:28:39]** Next one, you define the observation cost functions too.

**[2:28:44]** This is another another functions tool which is a cost total a cost tool.

**[2:28:52]** Right.

**[2:28:56]** Cost tool and then another one is the report report tool.

**[2:29:03]** Okay, so you define the tools over here. Now then you will create an agent that use the functions tool. So now you see there, okay, remember agents dot create underscore versions and then agents name. So there's agents name, that's the definition.

**[2:29:23]** More okay and the instructions, you provides our instructions and then along with that you define the tools over here. Remember the tools we defined over here, the functional tools, event tool, post tools and report tool.

**[2:29:39]** Okay, so this is basically the report tool.

**[2:29:44]** Okay, this is your cost tool and this is your event tool. So you're defining them in your in your agent.

**[2:29:57]** Anyway, then you'll send the message to the agents and process the process the response.

**[2:30:06]** Okay, and you'll process the function call and display the agent's response.

**[2:30:13]** Okay, so this is what you will do like you import the necessary library, you connect to the foundry project and open your client client. Then define the functions tool for the agents to use, create an agents with those functions tools, you'll send the message to the agents and retrieve the response.

**[2:30:33]** Okay.

**[2:30:34]** Then you'll process any functions call made by the agents and send the output back to the agent, and then the agents basically display the you know, response.

**[2:30:47]** Okay, and you delete the agents when it is done.

**[2:30:51]** Okay, now for example, when you say prompt find me the next event when I can when I can see from South America and give me the cost for 5 hours of a premium telescope time at the normal priority. Okay, so this prompt asks the agents to use both the functions tool like you defined next visible event.

**[2:31:12]** And calculate observation cost, so the agent is able to invoke both functions right in the same conversations turn and use the output from those functions call to provide the helpful response to the user. So the response would be something like this you can observe from South America is the Jupiter Venus.

**[2:31:34]** Venus conjections taking place on May 1st and the cost as output.

**[2:31:40]** OK, or when you say generate the informations in a report for this one.

**[2:31:46]** So you can see here agents.

**[2:31:52]** Output.

**[2:31:57]** OK, so that's building an agents with the custom tools and here it's basically the custom custom functions using the custom functions.

**[2:32:13]** Okay, again, question number one, what are custom tools and how can they help you develop an effective agent?

**[2:33:06]** Okay, we have this easy, right? So everyone.

**[2:33:12]** Everyone can participate, so it is a call level function that an agents can use to extend its capabilities, correct? Question number 2.

**[2:33:23]** You need to integrate functionality from an open API 3.0 based web service. What should you do?

**[2:33:53]** Okay, so the right answer is option C. Yes, everyone is correct. Add web service as an open api specifications tools to the agent's definition.

**[2:34:05]** OK.

**[2:34:08]** Let's move to the next.

**[2:34:13]** Integrate MCP tool with Azure AI agents. Anyone know what is MCP?

**[2:34:21]** Have you heard about MCP before?

**[2:34:24]** Model Context Protocol.

**[2:34:28]** Yes, so its basically stand for the model.

**[2:34:34]** Context protocol.

**[2:34:38]** Anyone know what is it actually?

**[2:34:42]** What does it do?

**[2:34:43]** it try to provide you like unified solution to integrate with other services, right? Like authentication or something if you want to do it from any agent.

**[2:34:55]** Okay, yes.

**[2:35:01]** Yes, anyone would like to add?

**[2:35:05]** Model context protocol.

**[2:35:11]** Okay, model context protocol, it's the open.

**[2:35:18]** Open a standard.

**[2:35:22]** Open standard protocol. Okay, that basically help your AI agents, your AI agents to connect with the external.

**[2:35:33]** External tools.

**[2:35:36]** Data source.

**[2:35:39]** Right, and your system in a consistent way.

**[2:35:45]** Okay, so for example, normally if we take a look here, okay.

**[2:35:55]** If your AI agents need to connect, want to connect to different systems like maybe databases, maybe API or maybe the CRM or any other cloud services, the developers need to build separate custom indication for each of the.

**[2:36:13]** Connections.

**[2:36:16]** So MCP solved this by providing a common protocol for connecting your agents to the external capabilities.

**[2:36:28]** Okay, so it's like a USB C port for your A I agents.

**[2:36:33]** Okay, just like USB, USB C provides a standard way to connect many devices. Okay. Similarly, MCB provides a standard way for your A agents to connect with many tools and data sources.

**[2:36:51]** OK, now MCP setup basically consists of 3 parts here, one is MCP post.

**[2:37:05]** Okay, second is MCP client.

**[2:37:10]** And the 3rd one is MCP server.

**[2:37:18]** Okay, MCP host is nothing but it's an AI applications, okay, that wants to use the tools.

**[2:37:25]** Okay, or agents that you wants to use the tools.

**[2:37:31]** MCB client is basically this is what which manage the connections between the agents right and the server MCP server. So this is MCP server and this is my agent. So this is basically the client which manage the.

**[2:37:51]** Connection an MCP server is basically which expose that tools.

**[2:37:59]** Okay, the external tools, the data.

**[2:38:06]** Okay, and resources.

**[2:38:12]** Okay.

**[2:38:14]** So this basically which exposed that tools out there.

**[2:38:21]** Okay.

**[2:38:26]** So.

**[2:38:29]** Let's say this is my agent's and this is a travel booking agent.

**[2:38:36]** Okay, and this travel booking agents you know need to check the flight availability, it need to read the company travel policy, okay, it need to calculate the expenses, or maybe it need to create a booking request.

**[2:38:53]** OK, instead of building every integration separately right in your agents.

**[2:39:01]** So MCP basically provides a standardised way for to connect the agents to all this different tools out there.


### Model Context Protocol (MCP)  `[2:39:12]`

**[2:39:12]** Okay, so if we take a look here, okay, without MCP, every tool need a separate manual integration to the AI agents.

**[2:39:26]** Okay, so if the agents need to use tool A or tool B, tool C, right, the developers must connect each tools individually.

**[2:39:38]** Okay, this increase the development efforts, it create the complexity and maintenance work.

**[2:39:48]** Okay, with model context protocol indicates once discover everything. So here.

**[2:39:57]** The agents connect to the MCP server, right? And this MCP server basically expose multiple tools to the agents.

**[2:40:09]** Okay, so instead of integrating every tool separately, we integrates once with the MCP server, and the agents can discover and use the available tools.

**[2:40:20]** And if with lets say tomorrow, if you want to include one more tool out here, right? So you can add the another tools out there to the MCP server.

**[2:40:32]** Okay, now the benefits over here is that it is reusable and it's a scalable, right? So tomorrow if I want to add, right, I can add more tools there.

**[2:40:45]** And it is reusable because if lets say right now this agency is using this MCP server, okay, then might be lets say I create another agents, another agents, and this agents also can use this MCP server for all this tools then.

**[2:41:05]** Okay, so we don't need to redesign the whole agents, we can expose the new tools through the MCP server and the agents can discover it.

**[2:41:16]** Clear.

**[2:41:19]** So indicates agents to using an MCP server and the client. OK, now let's understand this. We have a MCP server, we have an MCP client, and we have an agent.

**[2:41:34]** So MCP server basically it hosts the tools definitions.

**[2:41:41]** It was the tools definitions, right? So it basically just tell the agents which tools are available, what's what tools are available, what each tool can do, okay, what input are required.

**[2:42:01]** Okay, for example, there's a weather weather tool. Okay, so it will basically need the city name.

**[2:42:10]** And the date, for example.

**[2:42:15]** OK, so it hosts the tool definition.

**[2:42:21]** Second, you have MCP client now MCP client basically connect to the MCP server, okay, it just start the sessions using the client session, okay, and then it fetch the available tools by using the sessions dot list tools.

**[2:42:41]** Okay, and then it will then wrap each tool, wrap each tool so that agent can call it okay using the sessions dot call tool.

**[2:42:55]** Then the agents come in the agents basically it register register to agents agents toolset. So agents register this you know wrap tool into its tool sets.

**[2:43:12]** Okay, using the functions tool.

**[2:43:16]** Once registered, the agents can basically then decide when to use those tools during a conversations. So as you are conversation with this one, like, okay, lets say when I ask here, okay, what is the weather in London today? So the agents understand that live data is needed. So it basically look for the...

**[2:43:36]** Tools which is exposed by the MCP server.

**[2:43:42]** So it find the weather weather tool, so it will call the, it will call the MCP client.

**[2:43:50]** Okay, it will call the MCP MCP client through the MCP client. It basically, you know, use the MCP tool in the MCP server.

**[2:44:02]** Okay, and then gets a result right of the weather and provides the output to the user.

**[2:44:13]** Okay, so the flow is basically MCP server, it basically host the tool definitions, okay, MCP client basically it basically it discover and wrap the tools.

**[2:44:30]** Okay, and then the agents basically it register it register those tools and use those tools out there based on the users input.

**[2:44:44]** Okay.


### Exercise — connect an MCP tool  `[2:44:48]`

**[2:44:48]** So next we have exercise here. What you will do here, you will connect an MCP tool to the foundry agents. You will connect the foundry agents to the remote MCP server, connect the foundry agents to the custom MCP server tool.

**[2:45:06]** So let's take a look here.

**[2:45:13]** Okay, so extend the agents, extend the agents with a model context protocol. So here.

**[2:45:24]** Right, same you'll deploy it, then you clone the starter code repository. Then after that, you'll connect to the Azure. You'll connect an Azure AI agents to the remote MCP server. Now over here you can see you initialise the agents MCP tool.

**[2:45:43]** Okay, agent MCP tool here, server label, server URL, require approval.

**[2:45:50]** Okay, then you will create an agents with the MCP tool so you can see the agents, agents name, okay, model deployments and instructions. You are a helpful agents that use the MCP tools to assist user, use the available MCP tools to answer questions and perform the task. Okay, so you define the tools over here with.

**[2:46:12]** Tools and MCP server tools MCP tool which you define over here.

**[2:46:24]** Okay, so then since initial request that will trigger the MCP tool, process the MCP approval requests that were generated.

**[2:46:37]** Retrieve the response.

**[2:46:40]** So over here, for example, when you run it, wait for the agents to process the prompt.

**[2:47:07]** Okay, connect the MCP tools to your agent.

**[2:47:25]** Create an agents, your inventory assistant or some general guidelines and MCB functions tool.

**[2:47:33]** Versus function call.

**[2:47:48]** Okay, so this is the another one here. Are there any product that should be restocked? Which product would you recommend for clearance? What are the best sellers this week? So this is how you can interact over here. So it's using the custom MCP tool with your.

**[2:48:27]** Okay, so here is some response out there. so it.

**[2:48:31]** So we are providing over here.

**[2:48:44]** Yeah, so this is the one, right? So this is the initial request that will trigger an AMCP tool, right? So give me the Azure CLI command, give me the Azure CLI commands to create an Azure container app with the managed identity. Okay, and the response, right, we can see this is the response out there. Okay, here is the Azure CLI commands to create an Azure container app with the managed identity.

**[2:49:07]** Right, and it's basically gave you over here. This is the command, right? So this is it's using.

**[2:49:15]** This MCP over here to connect to the this external tools, okay, which is defined over here, the server URL lawn.microsoft.com slash API slash MCP.

**[2:49:36]** Okay, so let's take again.

**[2:49:42]** What will be the overall impact on the performance using and without using MCP?

**[2:49:54]** In terms of the performance out there.

**[2:50:04]** Now.

**[2:50:09]** Performance would not be that much impacted if you are using the MCP, but you are getting the standard standardized standard standardized way that how you agents basically call the other tools out there. So.

**[2:50:27]** Its more the more benefits you are getting over here is in terms of the developments where you the same same MCP server can be used with other agents out there. You don't need to define for every agents, you don't need to define those integrations with the external tools.

**[2:50:49]** Okay, it is basically more useful on the development sites there. Can we customize the MCP? Yes, you can customize the MCP.


### Knowledge check — MCP  `[2:51:11]`

**[2:51:11]** Okay, let's take here what role does the MCP server play in MCP agents tool integration?

**[2:51:19]** It run an AI agents and process the user prompt directly, or it manages the network connections between multiple agents, or it hosts the tool definitions and make them available for discovery by the client.

**[2:51:55]** Correct, everyone agree with the option C. That's true. It hosts tool tool definitions and make them available for discovery by the client. Okay, when question number 2.

**[2:52:09]** How does the MCP client retrieve the available tool from the MCP server?

**[2:52:29]** Yes, okay, that's first calling the sessions dot list tools to get the current tools catalog.

**[2:52:41]** Okay.

**[2:52:43]** Next is bit knowledge enhance a I agents with Foundry IQ.

**[2:52:51]** Anyone know what is Foundry Foundry IQ?

**[2:53:08]** Okay, how to host our own MCP server? You can host MCP server on the Azure container, Azure container instance or Azure container app.

**[2:53:22]** Okay, if you're creating a containerised server, so you can host on the Azure platform.

**[2:53:35]** Do we need any SDK to configure MCB server or something?

**[2:53:42]** Okay, yes, you would need out there. Let me refer you some.

**[2:53:52]** Some guide on the.

**[2:53:56]** To create an MCP.

**[2:53:59]** Server so it gets more clarity.

**[2:55:06]** Okay, now this is a quick quick guide over here how to build a custom custom remote MCP server using Azure Functions. Let me share.

**[2:55:31]** Okay, so this is a quick start how to build.

**[2:55:37]** Okay.

**[2:55:41]** How to build a custom remote MCP server using Azure Functions?

**[2:56:12]** OK, now here is a full documents.

**[2:56:15]** To build your own MCP server.

**[2:56:22]** sure.

**[2:57:08]** Okay.


### Knowledge-enhanced agents with Foundry IQ  `[2:57:11]`

**[2:57:11]** Now, next one is build a knowledge enhance AI agents with Foundry IQ.

**[2:57:18]** Okay, so Foundry IQ is a manage knowledge platforms inside the Microsoft Foundry. Okay, so we will talk about this.

**[2:57:31]** And this okay, so we already discussed about the RAG, okay, retrieval augmented generations. Okay, so RAG is used when models need informations okay, that is latest okay about like latest informations.

**[2:57:52]** On the company, okay.

**[2:57:57]** So.

**[2:57:59]** Now, over here, if we take a look here, retrieval augmented generation for the agents.

**[2:58:06]** So the first point is the simple agent, okay, it depend mainly on the model existing knowledge.

**[2:58:15]** Okay, so because of this it has limitations, it may give outdated answers.

**[2:58:22]** It is unaware of any anything past its training out of date.

**[2:58:29]** Okay, it does not know anything after its training cut of day. It may give generic answers because it cannot access like the private company data. Whereas Rackpower Agents it always current, it can retrieve the live documents from connect.

**[2:58:48]** It knowledge basis.

**[2:58:52]** Okay, it can access private company data like HR policies, the product informations.

**[2:59:01]** So, no private data.

**[2:59:04]** Okay, generic no access to internal procedures or product organization specific lack of context, irrelevant advice.

**[2:59:14]** It ignore the organization's workflows, approvals, chain, and security policies.

**[2:59:22]** Okay.

**[2:59:24]** So contextually aware, so the simple agents lack the business context.

**[2:59:35]** Whereas this would be rack based power, it's contextually aware it ground the advice in the retrieve org policies and workflows.

**[2:59:46]** Next one is fabricated response. Compliance is risk, confidence sounding answers with no source to verify.

**[2:59:54]** Okay, whereas here it provides you a verifiable source, it cites the exact documents behind every response. So we know basically if the response is out there, like where the response is coming from.

**[3:00:08]** Okay, scalability, it duplicated efforts. Every team rebuild the same rack pipeline independently in the share platforms, which is one knowledge platforms like Foundry IQ serve all the teams. So basically racks of the.

**[3:00:26]** Problem by retrieving information from the connected knowledge base before answering.

**[3:00:34]** Okay.

**[3:00:35]** So because of this, the agents become always current, always organiz, organizations, if specific, it is a scalable okay using using boundary IQ.

**[3:00:50]** OK, so if lets say if the employee asks like what is the travel imbursement limits?

**[3:00:55]** Okay, the simple agents can give generic answers, but rag power agents search the company travel policies and answers with the correct limits and the source, correct? So.

**[3:01:11]** Okay, now foundry IQ, okay.

**[3:01:16]** Managed, it's a managed knowledge platforms built in Microsoft Foundry. So here you can define your knowledge base once and connect any number of agents to it. So you can basically centralise. So instead of creating a separate separate, for example, for support agents, you're creating a separate separate rag.

**[3:01:36]** Pipeline for HR assistance, you're creating separate or dev agents, you're creating separate one.

**[3:01:43]** Okay, so you can see on this like data source you have share, SharePoint, OneLake, blob storage or SQL API.

**[3:01:53]** Okay, so this are basically source which contain your, let's say, HR policies or the product documents.

**[3:02:03]** Okay, or other any other business knowledge. So Foundry IQ it basically manage this knowledge basis.

**[3:02:13]** It manages this knowledge bases, so it automatically index the content, okay, and it keep it synchronised and make it available to the authorised agents.

**[3:02:27]** Okay, for example, the product documents may be coming from the SharePoint and blob storage. HR policies may come from SharePoints.

**[3:02:41]** Okay, API reference might be coming from the blob or SQL.

**[3:02:51]** Okay, so multiple multiple agents they can use the same knowledge platforms.

**[3:02:58]** Okay, so the benefits over here is that you have a centrally managed knowledge base.

**[3:03:05]** You don't need to duplicates the same rack pipeline for every agents. You create and manage knowledge. Once you apply the permissions, OK, keep the content updated and you can reuse this across the agents.

**[3:03:25]** Okay, so this is a share knowledge layer for the AI agent.

**[3:03:32]** Is it clear?

**[3:03:45]** Okay.

**[3:03:49]** Right, configure, configure data, data source, okay.

**[3:03:56]** We have index index data source. These are basically 3 main category right of data source, okay? Or you can say different ways we can connect data source for rack, okay?

**[3:04:16]** So we have index, these are.

**[3:04:21]** These are pre process before the agents can used.

**[3:04:26]** Okay, now which consists of Azure A search index.

**[3:04:31]** Okay, and SharePoint SharePoint index. So here the content is index enrich and optimise for search.

**[3:04:43]** OK for best for enterprise search with custom ingestions pipelines and AI enrichment advanced search on SharePoint content with custom query pipeline.

**[3:04:55]** Okay, then we have a direct direct data source.

**[3:05:00]** Zero flop storage or one leak.

**[3:05:03]** Okay, this source do not need a separate index, so the agents basically can access raw file directly.

**[3:05:15]** Okay.

**[3:05:17]** So we want a simple access without building the full indexing pipeline, then we can go for the direct.

**[3:05:26]** And then the real time, real time data source basically which is used to retrieve the light data at the query time like the web or SharePoint.

**[3:05:38]** SharePoint remote.

**[3:05:41]** Okay, when the data changes frequently and we always need the latest informations.

**[3:05:47]** Okay, so for example, web search can retrieve current informations from the web, SharePoint remotes can retrieve live SharePoint content.


### Configure retrieval & knowledge sources  `[3:06:04]`

**[3:06:04]** So configure the retrievals with the Foundry IQ. Now there are 3 main important behaviours to configure, like when to retrieve, we tell the agents like when it should search the knowledge base.

**[3:06:19]** Okay.

**[3:06:21]** Tell the agents to always use the knowledge base, never rely on the training data. How to cite, specify the exact format, the source attributions.

**[3:06:32]** Okay, so like specify every answer should include the citations or source reference and what to do when unsure, right? If the knowledge base does not contain the answers, the agent should not guess actually, right? It should basically give the...

**[3:06:51]** It should give the fallback behaviour when the information isn't found.

**[3:06:56]** So nowhere retrieval instructions. Okay, you are helpful at your assistance critical rules.

**[3:07:03]** Okay, you must always search the knowledge base before answering the questions. You must never answers from your know your own knowledge or training data. Every answers must include the citations. If the knowledge base does not contain the answers response with I don't have that information in our current documentation, please contact HR directly.

**[3:07:22]** So it basically contains all of this.

**[3:07:25]** So you can configure the retrieval with the foundry QI, when to retrieve, when to site, and what to do when unsure.

**[3:07:38]** Okay, then you have exercise integrates an a I agents with the foundry IQ. So in this you'll create an agents, you configures your data and foundry IQ. Then you'll test the agents in the playground and then connect your agents from the client applications and test the indications.

**[3:07:57]** So coming to this one.

**[3:08:10]** Okay, so here create the Foundry project, create the agents, configure the data and foundry Foundry IQ.

**[3:08:24]** Okay, download the sample product information file.

**[3:08:28]** Right, and then in the Azure portal, you'll search for storage account, you'll create a create a storage storage account, then you'll upload it.

**[3:08:38]** Right.

**[3:08:40]** And then you will configure your knowledge source with the with the settings out there: name, descriptions, storage account name.

**[3:08:52]** Okay, and then you'll test the agents in the playground.

**[3:08:57]** Connect your agents from the app. So in the playground, you can test over here what type of tents should Contoso offers. Tell me about what backpacks backpacks are available in Excel.

**[3:09:14]** Connect your agents from the app.

**[3:09:30]** So Query one product categories, specific product details, product comparisons, accessories and add on, and follow up questions.

**[3:09:48]** Okay, so here you create a foundry project and agents with the new foundry user interface, build the knowledge base with the product information documents, configures an agents in the portal with the foundry IQ enable right and then connect to your agents from the Visual Studio code using the Python SDK, implements client applications with MCP approval handlings.

**[3:10:08]** Conversations history and error handling, and then test the agents ability to receive and synthesise information from the knowledge base with the user approval for external tool access.

**[3:10:26]** Okay, 2 more questions over here.

**[3:10:37]** Okay, how Foundry IQ will decide which data is outdated and which one is latest and need to kept?

**[3:10:53]** Okay, that's good questions here.

**[3:11:03]** Okay, so usually what happen is now whenever you're updating your source, for example, let's say you are using a blob storage and when you update over here, update the you know data over there, so it will take that data.

**[3:11:21]** Okay, so whatever you updates it basically take from there only.

**[3:11:27]** So if your data is old one, right, it will take the old one. If it latest, then it will take the latest. So you have to update as you update your data source, then automatically the foundry IQ will update and index index with the latest informations.

**[3:11:53]** Okay.

**[3:12:00]** What happened is case of conflict in provided data. So usually we avoid the you know, this kind of situations out there. so.

**[3:12:12]** If there is a conflict where we have 2 data sets out there, I am not sure as of now. Let me. This is interesting. Okay, let me note it down and.

**[3:12:29]** Let me look into this questions.

**[3:12:49]** Okay, thank you for the question.


### Knowledge check & hands-on lab  `[3:12:57]`

**[3:12:57]** Okay, so let's take this knowledge check and then I'll provide you, right? Then we'll basically move to the lab session. So what is the primary advantage of the retrieval augmented generations over simple AI agent?

**[3:13:13]** Easy, I think everyone.

**[3:13:29]** Everyone can participate.

**[3:13:38]** Okay, let me see is there any way to recall the provided data?

**[3:13:56]** Okay.

**[3:13:58]** Right, everyone agree with B option. That's true. Okay, then let's go for next one, question number 3, sorry, question number 2.

**[3:14:10]** Question number 2: Which data source options provides a real time access to the SharePoint content with Microsoft 365 governance?

**[3:15:05]** Okay, so there is it's a SharePoint remote guys. Okay, SharePoint remote is the right one which queries the SharePoint sites and libraries in the real time, okay, maintaining those Microsoft 365 governance.

**[3:15:22]** OK.

**[3:15:27]** Alright, so now lets go for some hands on. so.

**[3:15:33]** Right, so you can start with your hands on lab. Okay, start from creating a generative. Sorry, you need to start from lab number 6. Okay, so previous lab, you can do that later, right? If you haven't, but for now, you start with.

**[3:15:53]** 6 Okay, built an AI agents with portals and VHS code. Use custom functions in an AI agents, develop AI agents with model context protocol. 9 Okay, perform till 9.

**[3:16:10]** Okay, yeah, perform lab number till till 9.

**[3:16:28]** PM.

**[3:16:33]** Yes, if you haven't, yeah, 51 as well, correct, correct. So yesterday I have given you only 1234, okay, yeah, 55 also. So start with 5.

**[3:16:46]** Okay, start with 5 and till 9 you have complete. If you haven't done the previous one, 1234, okay, complete them by tomorrow. Okay, by tomorrow, complete till lab number 9.

**[3:18:37]** Let me check.

**[3:19:06]** Okay, alright, I'll just see, right? What's your email ID and the system? Okay, just give me a second.

**[3:20:43]** Okay, so Balram, your name is not there in the system.

**[3:20:48]** Okay, so please mark your attendance first.

**[3:20:54]** I had already marked it twice today also and yesterday also.

**[3:21:02]** Cannot see your name, right? It is a with the same name Balram.

**[3:21:08]** Yeah, right.

**[3:21:09]** Okay, I think the attendance is not marked. Your name is not there in the system. I can see others' names are there.

**[3:21:20]** I have also marked my attendance, but I am also not able to.

**[3:21:25]** Okay, Sumit, I will see your one as well. Let me search.

**[3:21:32]** No, I don't see your name in the system. I think the attendance is not marked. Maybe because of that, you are getting issues out there, right? Can you retry to mark attendance and I will see on the back end?

**[3:21:47]** Actually, in our system which is not opening by scanning the QRS, I will be able to do, but let me resubmit it.

**[3:22:00]** OK.

**[3:22:01]** Yep, same here like we are able to submit it through QR code only, but not from the link directly.

**[3:22:09]** Okay, Swati, I can see okay, Swati Pandey, just a minute. Okay, I can see only one Swati name here.

**[3:22:23]** Okay, guys, this is the attendance issues only actually, right? I can see none of the name is present in the system because of which you don't have the what happened is like when you mark your attendance, right? So your name come in the system and then you can basically get access to the LDT portal.

**[3:22:43]** One quick question I wanted to ask like I will be submitting my attendance by instructor name Shoba Sharma. Is it correct name? Okay.

**[3:22:53]** Correct.

**[3:22:55]** Yeah, that's correct. That's correct.

**[3:23:41]** Please resend the.

**[3:23:44]** Yeah.

**[3:24:14]** This website is not working actually the website.

**[3:24:19]** Which website?

**[3:24:21]** Yeah, this attendance website is not working in our complaint laptop. I think you need to share the QR code only.

**[3:24:30]** Okay, yeah.

**[3:24:37]** I have just submitted mine. Could you please check once?

**[3:24:43]** Okay, sure.

**[3:24:56]** Still not there.

**[3:24:59]** I am writing.

**[3:24:59]** Did can you can you send the screenshots of like it shows your attendance has been marked?

**[3:25:11]** It is showing like, thank you, your data saved successfully. Want to try your IT skills? Try QUBITS 42. Actually, it is my private phone. Okay, so I need to send this screenshot to the official email ID then.

**[3:25:30]** I need to.

**[3:25:33]** Okay, then no issue out there. Just do one thing, let me search again. Okay, there is no any attendance at Summit. Okay, guys, those who are facing these issues, okay, just get me your email ID.

**[3:25:49]** Okay, give me give me your name and the email ID in the chat. Okay, I will send your name to the back end so that the so that they can add your details from the back end.

**[3:26:23]** Okay, Balram, I can see your name.

**[3:26:33]** Okay, now let me try accessing that website.

**[3:26:38]** Right, you just mark your attendance right now.

**[3:26:43]** Yeah, right now also I had tried it, but prior to this I had also marked as a problem. Yeah, let me try accessing this real quick.

**[3:26:46]** Okay, I can see your name.

**[3:26:50]** Okay, now you can try right.

**[3:27:23]** Okay, Harsh, I think today attendance was not marked, that's why I am marking your attendance.

**[3:27:31]** Okay, thanks.

**[3:27:35]** Now, once you refresh, you'd be able to see your attendance percentage.

**[3:27:42]** Okay.

**[3:27:47]** Hello. Yeah, Shivam Manish this side.

**[3:27:52]** The one screenshot that I shared when I scanned the QR code, I was they asked me to fill the form.

**[3:27:52]** Yes, Manish.

**[3:28:01]** Correct.

**[3:28:05]** Yeah, but I was not getting the attendance kind of the percentage.

**[3:28:05]** Yeah.

**[3:28:11]** Okay, just let me see is your name and the system.

**[3:28:17]** Okay.

**[3:28:20]** I see your name is not there in the system. Okay, maybe because of this you're getting this issue. Okay, I will forward all of your name to the you know, back end, okay, and they will look into the issue.

**[3:28:39]** Yeah.

**[3:28:44]** So till then we will not be able to access the assignment, correct?

**[3:28:48]** so until your name is not registered, you would not be able to.

**[3:28:54]** Sure.

**[3:30:53]** Could you please check my name once? My attendance is marked or not. I have just tried and I am able to logged in now.

**[3:31:04]** Okay.

**[3:31:06]** See.

**[3:31:23]** Yes, I can see your attendance is marked.

**[3:31:27]** For both the days like today and yesterday.

**[3:31:32]** Not for yesterday. This attendance link is only for today, so I will mark for yesterday. Okay, I have marked it so now you can see from your LET portal.

**[3:31:39]** Okay.

**[3:31:44]** Okay, thank you.

**[3:31:46]** Gowtham.

**[3:31:51]** Okay, Sakshi attendance also I can view I can see the name.

**[3:32:02]** Yeah, your name is over there and...

**[3:32:13]** It seems it's working.

**[3:32:16]** Still, it's not working for some of you.

**[3:32:22]** Let me send your name to the backend.

**[3:32:54]** Disha, you had a question?

**[3:32:59]** Yes, I wanted to know that whenever I am trying to login into LET portal as I have also enrolled for one more course, so that portal is opening for that course only, not for this.

**[3:33:15]** Okay, can you see at the top there's a drop down, there's options to select the course.

**[3:33:24]** Okay, did you see? Yeah, there you have to select that AI 103 over there.

**[3:33:31]** I'll just try once again.

**[3:33:34]** Okay, right. If you face any challenge, you can share your screen.

**[3:33:38]** Sure.

**[3:33:41]** So I have I finished the 5th 5th lab as still shows as running. Okay, it will take a while. Okay, after a while you can refresh and status will change.

**[3:34:40]** I cannot see any drop down for selecting other course.

**[3:34:46]** Okay, you have marked your attendance, right? Let me see your date of first. Just give me a second.

**[3:34:54]** Okay, I cannot see your name. TIS check. I cannot see your name.

**[3:35:00]** I have marked yesterday also in today twice.

**[3:35:05]** Okay, something issues. Let me see, I don't see your name.

**[3:35:14]** Yeah, because your name is not there because of which you don't have access like it's access of the previous course, but not of this one. Okay, yeah, I got your name, so let me forward to the back end.

**[3:35:30]** Sure, I have also sent my email ID in this chat. Should I send again?

**[3:35:36]** I don't know, I got it. Thank you.

**[3:35:40]** Welcome.

**[3:35:41]** Yeah.

**[3:35:42]** So by till when I will be able to access this portal for this course.

**[3:35:50]** I think by the end of the day, let me see like when we can get it.

**[3:35:53]** okay.


## Wrap-up  `[3:48:09]`

**[3:48:09]** Yes, guys, we have we have done with the content for today. What is left with the no hands on lab? Okay, so we still have 6 minutes here, right? If you have any questions, queries, feel free to ask. Otherwise, you are fee you know, feel free to lead the session. Thank you.

**[3:48:35]** Thank you.

**[3:53:26]** Alright guys, let's wind up for today. Thank you everyone. I will see you tomorrow. Thank you.
