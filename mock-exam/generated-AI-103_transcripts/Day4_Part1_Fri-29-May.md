# AI-103T00: Develop AI Apps and Agents on Azure — Day 4 (Part 1)

- **Date:** Friday, 29 May 2026 (12:30–16:30 IST)
- **Trainer:** Shova Kant Sharma (Microsoft Certified Trainer), Koenig Solutions
- **Recording:** Day 4 — Meeting Recording (Part 1 of 2, SharePoint Stream)
- **Length:** ~3:57:05  ·  **Captions:** 1049

> Transcript captured from the on-screen auto-generated captions for personal study. Captions are machine-generated (Microsoft Stream) and may contain errors. Section headings were added at the points where the trainer moves to a new topic; the caption text itself is verbatim.

## Contents

- `[0:00]` Recap & Module 3 (continued) — Speech
  - `[0:00]` Session start — Azure pricing & cost calculator
  - `[19:27]` Recap — text analysis agent
  - `[22:22]` Speech SDK — recognize once & speech config
  - `[31:43]` Speech agent with MCP server
  - `[48:37]` Azure Speech Voice Live (real-time)
  - `[1:05:34]` Speech translation
  - `[1:14:46]` Synthesizing translations & text-to-speech
  - `[1:26:09]` Knowledge check — speech
- `[1:41:02]` Module 4 — Extract Insights from Visual Data
  - `[1:41:02]` Introduction — Module 4
  - `[1:44:53]` Vision-capable (multimodal) models
  - `[1:53:42]` Analyze images — Chat Completions & Response API
  - `[2:05:11]` Knowledge check
  - `[2:08:06]` Image & video generation
  - `[2:20:05]` Generate images with AI tools (demo)
  - `[2:26:42]` Knowledge check
  - `[2:29:42]` Content understanding — structured info from visual content
  - `[2:37:27]` Schema training & image analyzer
  - `[2:51:50]` Build an image analyzer application
  - `[2:58:09]` Knowledge check
  - `[3:01:20]` Hands-on — content understanding (documents)
  - `[3:17:26]` Develop a content understanding client app
  - `[3:21:11]` Module 4 — last topic
  - `[3:34:34]` AI Search & document search
- `[3:39:30]` Q&A, Feedback & Closing
  - `[3:39:30]` Open Q&A
  - `[3:51:05]` Course feedback
  - `[3:55:01]` Closing remarks

---


## Recap & Module 3 (continued) — Speech  `[0:00]`


### Session start — Azure pricing & cost calculator  `[0:00]`

**[0:21]** And let's...

**[0:31]** Okay, so let me know the counts, how many labs you have completed.

**[0:41]** Okay, token utilizations, yes. So see every model basically has certain.

**[0:51]** No cost. Okay, so.

**[1:04]** Just give me a second.

**[1:19]** Okay, so I'm sharing my screen, right? For example, let's say if you go to...

**[1:27]** Let's say deployments, right? And I take this model.

**[1:34]** Okay.

**[1:36]** So, OK, let's keep the instructions as it is over here, right? And I'll simply interact here.

**[1:44]** With my GPT 4.1 model.

**[1:56]** Okay, so now from here you can see, okay, so this is basically the token, okay, its count basically the token out there, right? 23 input output. So input basically consist of, right? You will see this is the output.

**[2:16]** So the token count for this, sorry, the token count for this is 10, right? And input basically consists of the like high right along with the instructions you provide over here. Okay, so that's token can be view from here and if we go to the discover.

**[2:35]** And if you go to the model, right, and let's take.

**[2:41]** Any of the model over there, let's take the GPT 4.4.1.

**[2:51]** Chat.

**[2:53]** Completions and.

**[2:58]** Okay, now you can see over here, this is the benchmark cost, okay, so per 1,000,000 token, okay, so this is the cost benchmark cost $75, okay, now the same thing, right? You can see for other.

**[3:19]** Other models out there, you can compare it. Okay, you can compare some models and from here you can see the estimated cost.

**[3:29]** Okay, so you can see for estimated cost out there. So this is for 1,000,000 tokens.

**[3:36]** OK.

**[3:39]** Is it clear?

**[3:42]** Okay.

**[3:42]** This is the cost of site foundry, right? For the infrastructure we're paying.

**[3:49]** Sorry.

**[3:51]** This is the cost inside Azure AI Foundry. This is how much we are going to pay for the infrastructure that is running the model.

**[4:02]** so this is basically on the token actually.

**[4:06]** Okay, this is basically the cost associated with the token and the infrastructure part. Okay, which is, for example, let us say infrastructure part is a different.

**[4:18]** So we have cost calculator.

**[4:22]** Okay, in Azure we have a cost calculator, so let's go to the calculator, cost calculator. So this is a pricing calculator.

**[4:34]** And from here you can basically estimate the cost for each services on the Azure. Okay, so any services you're consuming it right, you can view from here. Now, for example, lets okay, so for example, lets say.

**[4:52]** You are using a storage account, okay, so you can click on this and you can see what is the estimated cost, okay? It depend on various things out there, right? On the regions, on the performance, on the account type, okay, and so on. And then you can see what is the estimated cost over here.

**[5:12]** Similarly, let's see for the foundry.

**[5:24]** He have his Foundry.

**[5:44]** Just a minute, it's I think foundry is not included over here, but any let's say let me search here.

**[5:52]** Foundry OK, what you're getting is Azure Contain Understanding in Foundry 2. OK, let me see this one.

**[6:02]** This is for the...

**[6:05]** For the 2, let me delete this.

**[6:18]** Okay.

**[6:28]** Okay, so depending on basically here right, you can see Azure continue understanding foundry too. So you know as you provide so over here the.

**[6:40]** Non text file layout formula right output as you provide this fields out there, right? You can basically guess the cost over here.

**[6:52]** For boundary, lets see we have a specific field.

**[8:26]** Okay, am I audible, guys?

**[8:32]** Yes, I'm audible. So there was some network issue. OK, got it, got it. Just give me a second, let me change.

**[9:22]** Okay, alright.

**[9:28]** Okay, I'm audible guys. Hope I'm audible to everyone.

**[9:36]** yes.

**[9:38]** Okay, all right, just give me a second.

**[10:06]** Okay.

**[10:09]** So I am sharing just a minute.

**[10:22]** Okay, so here I'm sharing my screen.

**[10:28]** Just a minute, let me.

**[11:42]** Okay, all right. Sorry guys, there was basically the internet was unstable. so.

**[14:31]** Okay.

**[14:35]** Yeah, sorry guys.

**[14:40]** I think now it's stable. Let me share my screen.

**[14:52]** Okay, I hope audible. I'm audible to everyone.

**[14:57]** Quick confirmation.

**[15:02]** Yes, can you hear me? Okay, all right. Yeah, thank you. Thank you everyone. Okay, so this is a Foundry model pricing. Okay, so I am sharing this in the chat. So lets go to.

**[15:04]** yes.

**[15:06]** Yeah.

**[15:17]** Okay, let's yeah, this is a Foundry model pricing, so you can see the you know, pricing over here.

**[15:28]** So now if you scroll down, okay, if you scroll down, so let's go to the pricing pricing table.

**[15:50]** Explore.

**[15:53]** So let's get for the overview.

**[16:00]** Okay, so now you can see from here, okay, so you can explorer the pricing options right for models, okay, so you can see the pricing details for the foundry models, okay, agent service and framework, right? So from here you can see the pricing detail for the foundry agent service, okay, knowledge and tools.

**[16:20]** OK, so you can see the pricing for the product like Foundry IQ, OK, Foundry tools, Azure Machine Learning, right? And similarly, you can see Foundry control plane local and edge like Foundry local. OK, so all the pricing for example here if you go to the.

**[16:39]** See pricing detail for the foundry foundry model. So then it will take you to this year so you can see there are various models out there. OK, so and then you can go through it. For example, this one open a pricing pages so you can go to Azure Open a I service pricing and you can.

**[16:59]** Basically, navigate for the pricing for the different models. of the.

**[17:06]** Open a I pricing. So once you navigate over here, so you can see over here this is like GPT 5.5 right pricing right 1,000,000 token. Okay, so this is basically for the model 5.0. So you can go through the pricing from this page clear.

**[17:30]** All right.

**[17:34]** Okay, so now lets move ahead. We have lot of lot of things to cover. so.

**[17:42]** And today's last day.

**[17:46]** So lets get started. We will just take a quick recap and we will proceed further. OK, so yesterday we started the 2 workloads, text and language and computer speech, correct? So we started here with analyzing the text with Azure Language.

**[18:06]** In foundry tool, okay, so we have talked about the foundry tool before, right? And we have, we have various services under under the foundry foundry tool, right? And we started yesterday with the Azure Azure language, how we can use Azure language for analysing the.

**[18:27]** Text so Azure Language and Foundry tools can be used to can be used for language detections, name entity recognitions, and PL detections. And to basically here we're using the text analytics API in the Azure Language Foundry tool.

**[18:49]** To connect to the API, we talk about the you need endpoints and you need the credentials. You are going to make a request with one or more text document, right? Along with basically the...

**[19:06]** What do you want to get, like whether it's a language detections or name entity organizations, you'll call that the specific functions and then you'll get output in the in the JSON formats for the language detections, name, entity, and your PLL detections.


### Recap — text analysis agent  `[19:27]`

**[19:27]** Okay, so we have covered this. Then also we talk about yesterday how we can develop a text analysis agent with Azure Language MCP server. Okay, so for your agent, right, we have Azure Language server, Azure Language MCP server.

**[19:46]** So we understood how the Azure Language MCP server can be used to perform the language detections, name entity recognitions, and PLL using the Azure Language MCP server, right, the process.

**[20:06]** Of using Azure Language Nsif Server with the agents, create an agents at the server tool, specify the agents instructions right, and the instructions you need to tell it to select the tool right when appropriate. Then you test the test the agents in the playground, then you build a client application.

**[20:24]** That user agent correct then.

**[20:29]** Further hands on, all right, and then the knowledge check.

**[20:35]** Sorry, and then we started with the speech okay, speech capable generative A I applications. So here we have explorer some models okay for speech speech capable models we have explorer in the Microsoft foundry foundry model.

**[20:54]** For we explorer the transcriptions model, okay, transcription models which basically convert your speech into the text and then we have speech synthesis model, right, which convert your text into the speech.

**[21:12]** Okay, so these are the basically the generative AI model like speech capable generative AI model. Then further we also talk about here how to create an speech enable app with Microsoft Foundry. Okay, so we have Azure speech like language, Azure Language.

**[21:31]** Right, we have Azure Speech in the Foundry tool, and this can be used for speech to text, text to speech, voice live, okay, and speech translation.

**[21:43]** To use the Azure Speech in Foundry tool, right, we'll again need an endpoints credentials to authenticate and then we'll create a.

**[21:52]** A language speech config object, okay, which is proxy object for the speech API operations.

**[22:03]** And for speech to text, okay, now for to implement speech to text, right, you would basically would be using this speech config objects, audio config objects, and then speech recognition objects which consist of a speech config and audio config.


### Speech SDK — recognize once & speech config  `[22:22]`

**[22:22]** And then you will basically call the method recognise once a sync, which will basically gets you the output, right? And the text transcript basically contain the text speech to text. Okay, then for text to speech, for text to speech.

**[22:43]** Okay, we have again the speech config, but here this would be the audio audio output config, right? The audio output config basically this is where you provides like whether it is a speaker or the file. So speaker is by default over there, right? So it can play the.

**[23:03]** Speech through the default speaker or it can be saved as a audio file. Then we have speech synthesizer if it is speech synthesizer that will basically call this method which is a SpeakTextAsync and here in the speech synthesizer we are call we can also provide the voice and the.

**[23:24]** Audio audio format, okay, then over here you gets a result which includes of the audio stream as the output when the region is basically synthesising audio completed. Okay, so text to speech, use the speech config.

**[23:43]** Audio config and speech synthesizer to convert your text into the spoken audio, right? So you get audio streaming over here, which you will be getting output as a file order through this speaker.

**[24:03]** Sorry, I have a small...

**[24:08]** Okay, so also we talk about the speech synthesis markup language.

**[24:13]** Okay, so this is a XML based language with customizations options. Now using using it, we can control the how the text is converted into the speech. Okay, using it we can make the speech sounds like the.

**[24:32]** Sounds like real, okay, by providing the speaking style like the silence, the pause, like the pronunciations, right, it to tell your systems like how to pronounce a difficult word, okay, and how to basically.

**[24:52]** Say how to tell how to read dates, numbers, times, right, addresses, so we can all define using the SSML.

**[25:04]** so I think we have covers still here yesterday.

**[25:10]** Right, did we did the knowledge check from this topic? Had we done the knowledge check?

**[25:22]** Okay, lets quickly take this. Okay, question number one, what information do you need from your Microsoft Foundry resource to consume it using the Azure Speech SDK?

**[25:49]** What information you needed, right?

**[25:52]** Easy, yes.

**[25:56]** Yes, okay.

**[25:59]** Yes, that's true. You need basically the endpoints and the key, OK, not the primary key, secondary key, Azure subscriptions ID and resource group name. No, we don't need them for connecting. We need the endpoints and the key. Question number 2.

**[26:18]** Which object should you use to specify that the speech input to be transcribed to text is in an is in an audio file?

**[26:39]** Okay, which of this which of this object basically define the audio source?

**[26:50]** Audio source. Remember which object should you use to specify that the speech input?

**[26:58]** Okay, the speech input okay to be transcribed it to the text is in audio file.

**[27:09]** Okay, if you talk about speech config, okay, in speech config, we basically we use a speech config for the connections. Okay, so if you see there, right, see speech config.

**[27:28]** Right, so connections now if we also let me also show you over here so built the.

**[27:43]** Okay, speech capable. So this is for analysing, analyse text, develop a text analysis agent, then speech capable generative AI model. Yeah, this is the one.

**[28:13]** Okay, this is basically for the model.

**[28:38]** Okay, so you can see over here, right? Speech config, speech config object, we provides over here the credentials, right endpoints and the credentials which is like token or key, okay? And then you can see the audio, right? Audio output file config.

**[28:59]** Okay, now this is basically where you have the audio file or speaker.

**[29:08]** Okay, so audio, audio config is used for the input audio sources.

**[29:18]** Audio, audio output config or audio config. Okay, so audio config take the microphone or file. Audio output config basically take the speaker right or the file.

**[29:32]** OK, so the right answer is option B.

**[29:38]** Okay, yeah, option B would be correct, clear.

**[29:43]** Okay, so there you take the audio.

**[29:50]** Clip.

**[29:52]** Okay, question number, question number 3.

**[29:57]** How can you change the voice using speech synthesis?

**[30:18]** How can you change the voice used in this speech synthesis?

**[30:23]** Okay.

**[30:57]** Okay, so yes, so most of you said B's, that's true. We will set the speech synthesis voice name property of the speech config object to the desired voice name. Okay, so that's how we can change the voice used in the space synthesis.

**[31:16]** Okay, which is...

**[31:21]** So.

**[31:23]** Now lets talk about here developer speech agents with Azure Speech MCP Server. Now similar to the Azure Language MCP Server, right? You using Azure Language MCP Server, right? We can basically perform the text analysis.


### Speech agent with MCP server  `[31:43]`

**[31:43]** Correct. So similarly, we can develop a speech agent with the MCP server. Okay, speech speech MCP server. So this basically gives those capabilities of the converting speech to text or text to speech.

**[32:01]** Okay, or speech translations, real time voice interactions.

**[32:10]** So if you see over here, okay, the user sends a prompt to the agents containing the text or a link to a audio file. The agents basically determine the task okay to be performed.

**[32:28]** Then the agent agent check the available MCP tools to find the best match. Then the agents call the selected tool through the MCP server, passing the relevant input.

**[32:44]** Then MCP server process the request using the Azure speech, OK, text to speech or speech to text.

**[32:55]** In the case of text to speech, the generated audio is saved as a file in the Azure storage. OK, now whenever you're using the Azure speech in the Foundry tool, right with this, an Azure storage would be needed out there where it will be like lets say.

**[33:13]** It will basically convert your speech into your speech to text or text to speech, okay, so that would be stored over here in the Azure storage. Okay, then the agents response to the user with the transcribed text or the link to the generated.

**[33:33]** Audio file. Okay, so this is basically the process out there.

**[33:41]** Okay.

**[33:43]** So within this Azure Speech MCP server, right, let's say.

**[33:53]** For example, let's say user says transcribe this customer call regarding.

**[34:00]** Okay.

**[34:02]** And convert it into convert or lets say like you have a customer customer call recording. So transcribe this customer call recording, right? The agents understand the task, okay.

**[34:23]** And if the user wants like audio converted to the text, the agents basically select the speech to text.

**[34:36]** It will basically use the speech to text tool.

**[34:44]** And if the user want text to be converted into the audio, okay, then the agents basically select okay, text to speech speech tool.

**[35:00]** Okay.

**[35:03]** So this is the basically MMCB server, right, which work as a bridge between the agent and the external service, right, which is Azure Speech.

**[35:18]** Okay, clear. I hope this is clear to everyone.

**[35:29]** Okay, and remember that here with the Azure store you would need Azure Storage, okay, so the generated audio file okay can be saved in the Azure storage, okay? And then basically the agents can return the you link to the audio.

**[35:48]** To the user.

**[35:52]** Okay, so if you see here using an Azure Language MCP server, so this steps is basically create an agent, connect the Azure Speech MCP server tool, okay, you would require so.

**[36:12]** So you see there right block container, container URL. So you need to provide Sir block container SAS URL over here. OK, require an Azure storage container SAS URL, specify the agents instructions to select the tool when appropriate, test in the agents playground, build a client applications that uses the.

**[36:32]** Agent OK, it's a similar to how we have used the Azure Language MCP server. OK, so let's see for the speech capability if we go to.

**[36:48]** Let's go to build, let's go to the agent.

**[36:53]** Built agent, right? And for example, let's say this one IT Support agent.

**[37:04]** Okay, and here.

**[37:10]** Let me go to the add right and you can see here is your languages and foundry tools browser or tools. Let's go to catalog right and then we can search for as your.

**[37:26]** As your sorry.

**[37:29]** As your speech MCP server.

**[37:36]** Okay.

**[37:41]** Yeah, there is it. Okay, Azure Speech MCP server that exposes your speech capabilities like which is speech to text, text to speech, or streaming streaming live.

**[38:00]** Okay, so you have labs for the same, right? How to use the Azure Speech in an agents? So in this, you will create an agents in the Microsoft Foundry, you will add and test the Azure Speech MCP tool, and then you'll create a client applications for an agent.

**[38:32]** Right, so this is there, right? You also need to use the Azure storage account, right? You need this storage account. So first you will create that storage account out there, right? And then you will generate the share access signature, right?

**[38:50]** So you'll create this share access signature token, OK. And once you create it, then you'll go to the Microsoft Foundry project, you're gonna create a project there, you'll create an agent, right? And you'll give the instructions to the agents, right? And after that, right, you will basically.

**[39:10]** Use this as your speech in Foundry tool connection.

**[39:15]** OK, then after that test the Azure speech tool in the playground. OK, so you'll say generate to be or not to be that is the questions as a speech.

**[39:29]** Okay. And then?

**[39:33]** Right.

**[39:36]** So then.

**[39:39]** Okay, for speech speech agents, you then and then you okay, you review this response which should include a link to the generated audio file. Okay, so for this you will get the generated audio file out there. Similarly, you can say transcribe the file at it provides provides the links out there.

**[40:01]** Okay.

**[40:04]** So text to speech, then it will review the output, which would be the transcription of the audio file.

**[40:15]** Okay, and then you can create a client application, right? And then you can connect to that agent okay and use in your client application.

**[40:29]** Okay, like synthesize better.

**[40:34]** As a speech using the voice, you also tell it that, okay, use this voice.

**[40:42]** Okay, so this is using.

**[40:46]** Sir, Azure speech in the agent. Okay, perfect.

**[40:59]** Clear case.

**[41:03]** Okay, question one: What 2 core capabilities does Azure Speech MCP server expose to agent?

**[41:47]** Yes, done.

**[41:50]** Okay, B yes, that's okay. These are the 2 core capabilities of the Azure Speech MCV server which is exposed to the agents, right? Speech to text recognitions and text to speech synthesis, correct?

**[42:09]** Okay, question number 2, great.

**[42:12]** Why does the Azure Speech MSP server require an Azure Storage account?

**[42:39]** Yes, that's true. This is to basically used to store input audio file and output audio file generated by the speech tool.

**[42:52]** Okay, question number 3.

**[42:56]** What credentials are needed when connecting the Azure Speech MCP server okay to a Foundry agent?

**[43:39]** Okay, yes, that's true. A found resource key, okay, and a sash URL for the blob container.

**[43:48]** Okay, this is a neat way in connecting Azure Speech MCB server to the foundry agent.

**[44:00]** Right here also you will.

**[44:04]** C.

**[44:12]** What's your speech?

**[44:17]** This is language, your speech.

**[44:37]** Okay, so here a foundry resource name, right? And then right, you have to provide the block container SAS URL. So once you create a separate block storage, then you will get the block container SAS URL that's you put over here okay to configure with your MCP server tool.

**[44:59]** Okay.

**[45:01]** Perfect. Okay, now next let's talk about here develop an Azure Speech Azure Space Voice Live agent in Microsoft Foundry.

**[45:15]** Okay, now the normal agents usually work with the text like the user type a questions, the agents process it and return a text response, right? But a voice live agent, okay, this basically allow the users to speak naturally and receive the spoken responses in real time.

**[45:36]** Okay, so for example, instead of typing, what is the status of my order? So user can simply speak questions, the agent, listen, understand the speech, okay, process the request, and then.

**[45:55]** Speak back the answer.

**[45:59]** Okay.

**[46:02]** Is it clear? So the flow over here is something like that user speak.

**[46:10]** OK, then voice, voice live.

**[46:16]** Captures the audio, right? Then the speech is.

**[46:26]** Converted.

**[46:28]** And processed.

**[46:32]** Correct. And then agent.

**[46:36]** Generate the response.

**[46:41]** Response, right? And this response is spoken.

**[46:48]** Back to the user.

**[46:53]** Okay, and this is useful for many scenarios out there, like lets say you have the users, right, who are, who are not good at typing, right, they can simply or.

**[47:12]** Basically, it is more faster out there, right? So for example, you can use the for customer support, you can have customer support voice board, or it can be used for appointment booking assistance, right? Where you can simply since the you can simply say to the agents, right, okay.

**[47:33]** Book an appointments for for 2 days or it could be used in like for banking and insurance, healthcare or for internal employee services, right? And you can see this is happening right now. So you get a call from like.

**[47:52]** For example, let us say you gets a call from bank regarding the loan credit card. Okay, so first the call is made by the assistant, right? And then when you confirm it, right, if you if you are interested, so then when you it says like, okay, if you are interested, please press one. So when you press one, so then.

**[48:13]** Basically, goes to the live live agents out there. So that's how organizations saving time out there because they can target the potentials customers right who are interested in that particular product.

**[48:28]** Okay, so I received that call, right? Okay.

**[48:34]** So.


### Azure Speech Voice Live (real-time)  `[48:37]`

**[48:37]** Okay, Azure Azure Speech, Azure Speech Voice Live. Okay, so Voice Live is basically for it's a real time event based conversations framework, okay.

**[48:58]** It means the user can speak naturally and the system can process audio continuously instead of waiting for the full audio audio file. and.

**[49:11]** Connect model to speech conversations in the voice live sections. So it basically connects the main part, your voice input, Azure speech in foundry tool, and foundry model. Okay, so all of this work together.

**[49:32]** Right inside the voice live sessions and authentications can be done right with Microsoft Intro ID and the a Pi key. OK, some advanced features include it provides a real time audio processing with support for multiple formats.

**[49:52]** Like PCM 16 or G dot 711, so it also supports different voice options, okay, like open a I voices or Azure custom voices, okay also.

**[50:10]** Our integrations okay with WebRTC for video and animations, which means we can build a video base or animated voice agent.

**[50:22]** Okay, it can also include built in noise reduction reductions and echo cancelling which improve the quality when the users speak in noisy environments. So.

**[50:39]** So over here, right, this is one Azure Live sessions, Azure Speech in Foundry tools, OK, and the foundry model. So Azure Speech is it is enable a real time spoken conversations by connecting Azure Speech foundry models.

**[50:58]** Okay, in a live sessions.

**[51:07]** Okay.

**[51:09]** So for creating a voice live agent, you enable the audio mode in the agent's playground.

**[51:18]** Okay, so.

**[51:21]** Now you can see here voice mode. This is how you can switch the agents to voice first experience. So you can configure the voice live settings for the for the agent, then create a client app that use the voice live SDK to connect to the agents.

**[51:41]** Configures the audio, hardware, inputs, and output. Okay, establish a voice live session. Monitors audio system for activity.

**[51:53]** Process events such as user's speech input and responses from the agents. So these are basically the client app perform the 5 main tasks.

**[52:07]** Okay, the application connect to the foundry agent, okay, now which basically contain instructions and tools, okay, configures audio like you know, selecting the microphone for user speech and you know speaker for the agents response.

**[52:28]** Okay, then you will start a real time voice conversations between the user and the agent. You also listen for events.

**[52:39]** As monitors audio system for activity like user speaking when the response is started or when the response completed, and then process events where the app handles the user speech input. and.

**[52:58]** Agents response in real time.

**[53:04]** Okay, so.

**[53:09]** Here, so this is the exercise for to develop a voice live voice live agent. So let's so.

**[53:24]** Okay, so create an agent, right? Then you will configure the Azure Speech Voice Live.

**[53:35]** And then use the speech to interact with the agent.

**[53:43]** Okay, use the start session button to start a conversation with the agents. Okay, then you provide Sir, you allow access to the system microphone, then the agent will start the speech sessions and listen for the input for your prompt and when the app starts.

**[54:01]** The app status is listening, you can say something like so it's similar to like how you use any other a I application. So the same can be you can create your a I applications by for speech by using the Azure Speech.

**[54:20]** Voice Live.

**[54:22]** OK, so similarly creating a creating a client application.

**[54:36]** It connect does your voice live to the agent is ledge audio processing.

**[54:42]** Configure the sessions and start the audio system.

**[54:49]** Process your events.

**[54:52]** Now this is the complete functions for client application.

**[55:09]** Okay, now once you run it, okay, so here.

**[55:15]** Begin the conversation with agent by asking questions, okay?

**[55:20]** Listen to the response and then continue the conversations. And also you can interrupt the agents to ask the new questions.

**[55:29]** Yeah.

**[55:34]** So this is exercise to develop a voice live agent.

**[55:45]** Okay.

**[55:56]** How can we log each and every interaction with agents, model, AI services, and monitoring?

**[56:06]** Each and every interactions log, okay.

**[56:11]** So let me.

**[56:26]** Let's go to the agent we have.

**[57:11]** Okay, now this is where you can.

**[57:17]** Okay, once you go to your agents, right, you can see Chris, right? And then you can see the conversations ID. Now for I haven't much conversations over here, right? We just have conversations like how, right? And basically this users get you output. How can I help you today?

**[57:37]** Right, as you make the conversation, so you can you can see the log of it over here in this space.

**[57:46]** Clear.

**[57:46]** And anything with regards to monitoring this services, like do we need to enable something for doing a monitoring of this services apart from logging?

**[57:55]** Yes, basically you would be using separate tool, okay, which is application inside resource. So that resource would be used to monitors the your a I, a I agents and then you'd be able to see like token, total token uses or evaluations, schedule evaluations. and.

**[58:16]** Other other metrics you would be able to view from here. So you need to enable it like once you connect. So from here application site resource, you click on create, right? And from here also you can directly create.

**[58:31]** Or if you have any existing, you can also link to that and then you'll be able to monitor because the application inside is basically which captures like all those metrics out there and provides you over here in this you know dashboard.

**[58:47]** Okay, yeah, thanks.

**[58:51]** Okay, so let's take a question one. Okay, what are the 2 authentication method supported by the Voice Live API?

**[59:18]** Okay, and it is generally, generally basically Azure Azure language speech we talk about or Azure Azure speech Azure speech foundry tool. so.

**[59:38]** Right. So what are the basically 2 authentication method?

**[59:46]** Yes, that's true. That would be your Microsoft Intra and the API key. Perfect. Question number 2: How do you configure and test the VoiceLife agents interactions in the Foundry portal?

**[1:00:16]** Okay, so if you go to playground and if you see...

**[1:00:22]** Right, voice mode.

**[1:00:28]** Okay.

**[1:00:31]** Hello, let's allow the microphone. Hello.

**[1:00:44]** Yes, I want to know what's the weather today in London.

**[1:01:07]** Wait, okay, this including the sound, actually, I think sound was missing out there, right? So now over here, so see right, all the interactions I had here, right? So I'll say, okay, I think now you can hear.

**[1:01:26]** Hello.

**[1:01:30]** Hello, it's great to connect with you. How can I help today? If you have any questions or need information, just let me know.

**[1:01:38]** Okay, I want to create an agents which can speak right how I can how can how can I create it in the Azure Foundry?

**[1:01:52]** Let me take a quick look.

**[1:01:54]** Here's a detailed guide on how to create a speaking, voice-enabled agent using Microsoft Foundry, formerly Azure AI Foundry, since the term Zero Foundry seems to be a mis.

**[1:02:08]** Okay, all right, so that's over there.

**[1:02:14]** Okay.

**[1:02:18]** Is it was not audible to you?

**[1:02:23]** No, it was. This is the first time.

**[1:02:32]** Okay, first time it was not okay, perfect. Okay, question number 2, audio answer. Okay, option C. Yes, that's true. Enable the voice mode in the agents playground. Okay, now next one, question number 3.

**[1:02:58]** How can you stop audio playback when a user interrupts the voice agent?

**[1:03:12]** How can you stop audio playback when the user interrupts the voice agents? You cannot. The user must wait for an agent to finish. That's not true. Now you have 2 options here: handles the input audio preferred speech started event, or you'll reset the voice live sessions and clear the conversion straight.

**[1:03:31]** That's also does not fit in, right?

**[1:03:35]** Yes, that's true. It's a option B, right? You handles the input audio buffer speech started event okay in your application code.

**[1:03:50]** Okay, so we talk about the language, Azure language, Azure speech. So now lets talk about translate text and speech with Microsoft Foundry. So we are talking about Azure, Azure Translate.

**[1:04:10]** Okay, as your translate for both text and text and speech are there. Okay now.

**[1:04:21]** So in today's global applications, so user may speak or write in different language. So the translation service helps AI applications communicate with the user regardless of their language.

**[1:04:37]** So text translation basically it convert the written text from one language to another language, right? So for example, this can be used for multilingual websites or maybe used for customer support system, okay, or maybe for document translations.

**[1:04:58]** Maybe for global business applications, so the AI agents can automatically automatically detect the source language and then translate the content okay to the users preferred language.

**[1:05:13]** Okay, so and then we have a speech translation. Speech translation basically goes one step further, instead of translating the written text, right, it translate the spoken language. Okay, let's say customer speak in one language, the system perform.


### Speech translation  `[1:05:34]`

**[1:05:34]** multiple steps there like convert the speech to text and then translate the text into another language and then convert convert that translated text backs to the speech. Okay, so this enable a real time multilingual conversations.

**[1:05:52]** Okay, so if you see here, right here.

**[1:05:59]** So, Azure Translator in Foundry Tool, okay, so it is used for multilingual translations for both your text document, right? And Speech Azure Speech in Foundry Tool, it provides multilingual speech translation, okay.

**[1:06:18]** For speech to text and speech to speech.

**[1:06:25]** So Azure, Azure Translator.

**[1:06:30]** Okay, for multilingual text and document translation and Azure speech as we discuss it basically when the user inputs or outputs it is needed in a spoken language, so it use the.

**[1:06:51]** Speech to text and speech to the speech translations. So speech to text translation means like when the users speak in one language, okay, the service basically translate it into the.

**[1:07:09]** Text.

**[1:07:12]** Okay, in another language in the text. So it basically first recognise the speech, right? And then it translate into, let's say, English.

**[1:07:25]** Okay, speech is speech to speech translation.

**[1:07:30]** OK, speech to speech translation. So here the user speak in one language, OK, and then system basically responds with the translated speech in another language.

**[1:07:44]** Okay.

**[1:07:49]** Now translate text with the Azure Azure Translator. Now for this you would need.

**[1:08:00]** Okay, translate text with the Azure Azure Translator. So you'll connect to the endpoints right endpoints using the Microsoft Foundry resource or regional translator endpoint and then credentials which can be Microsoft Foundry project API key or authentication token.

**[1:08:17]** Okay, then after that, right, you'll use the text translation client.

**[1:08:24]** Okay, so that basically communicate like it's basically which communicate with Azure translator and perform the translations related operations. So to perform the task, okay, get supported language.

**[1:08:40]** Okay, for EN is basically for English, okay, translated, translated text. Okay, so first is it basically perform 3 things out there, 3 tasks. First one is okay, it detect the language.

**[1:08:56]** Okay, detect the language.

**[1:09:01]** The get supported languages it detect the language second translate text. Translate text is basically where it translate like for example this one. Okay, so this is a Japanese, Japanese text it basically translate into.

**[1:09:21]** English.

**[1:09:23]** Okay, and also.

**[1:09:27]** Transliterate the text.

**[1:09:30]** Okay, so translating, so it's basically transliteration means like.

**[1:09:39]** It keep the pronunciation is keep the pronunciation, but keep change the writing style. Okay, so this is the this is Japanese, and when you translate it, it is basically pronounced as the Konichiwa.

**[1:09:57]** Okay, so this means it's not translative, only the script changes.

**[1:10:04]** Clear. So because of the translation, okay, anyone who is not native Japanese speaker, okay, can would be able to speak Japanese. Okay, so it just it keep the same pronunciations, but it change the writing style there.

**[1:10:24]** So that it would be easy for any ones to pronounce this word over there.

**[1:10:31]** Okay, so clear. So this is the developers, right? They would need an endpoint. So this is the endpoints, that's the key, that's the authentication token, as they can use a key or a token and then right use the text translations client.

**[1:10:51]** Using it, you can it can performs get supported language, translate text, and translate rate text clear.

**[1:11:03]** Okay, now when it is coming to translating, so previous was basically translating the text with the Azure translator. Okay, now you are translating the speech with this Azure speech.

**[1:11:16]** Okay, so same here, connect to the API, you got the endpoints, you got the, you need the credentials out there, okay. And over here you create a speech, speech translations config.

**[1:11:36]** Okay, so.

**[1:11:40]** This object for the connections, so you will create this for the for the connection and then use a translation.

**[1:11:49]** Then user translations recognise the object for the translations operations.

**[1:11:56]** Okay, so this would the speech translations config. It will store basically the end points, the authentication information, then what is the source language, what is the target, you know, translation, translation language. Okay, so you need to define what is the what is the source language, okay, like let us say.

**[1:12:21]** For Hindi, it's like EN. For English, it's an EN.

**[1:12:27]** Right, so this basically tell the Azure speech exactly what translations task to perform, okay? And then second one is the translation translations recognizer object, okay, that perform the actual translations. So it basically.

**[1:12:46]** Listen to speech from micro, microphone or audio file. It recognises spoken board. It basically translate them into the target language and then return the translated text.

**[1:13:06]** Okay, so it could be used in many, many scenarios out there, like maybe you have international customer support center, the customer, okay, the customer in Germany basically speak in German, the support agents only understand.

**[1:13:25]** English or German speech, basically it's translate, you know it will like this German speech.

**[1:13:39]** Just a minute, what happened?

**[1:13:42]** Okay.

**[1:13:50]** Allow me a minute.

**[1:14:13]** Okay, I lost the tip of the writing pen.

**[1:14:23]** Okay, let me.

**[1:14:26]** Let me use the mouse.

**[1:14:33]** Okay.

**[1:14:35]** All right, so these are basically the 2 objects, okay, this objects for connections and other one is a translation operation.


### Synthesizing translations & text-to-speech  `[1:14:46]`

**[1:14:46]** Now synthesising the speech translations. Now we have 2 things over here. One is the event based synthesis and second one is a manual synthesis.

**[1:15:00]** OK.

**[1:15:03]** Now the 2 approach, what is the difference in between these 2 approach? So even based synthesis, this is the simpler and more automated approach and it supports one to one translation, right? Means one source language and one target language, right? Let's say one the speaker speak in Spanish, right? And.

**[1:15:25]** The target language is English. Okay, so that bas that's basically like event based event based synthesis out there. Specify desire voice in the translations config. Okay, desire desire voice you will.

**[1:15:43]** Basically define in the translation config and then use the synthesising events to retrieve the audio audio stream. Okay, so is the is the translations happening as your raises the synthesising event?

**[1:16:03]** It says like think of this events as a notification saying that okay, the translated audio is ready, okay. And then we can create the event handler that listen for that event, okay. And inside the event handler, we use the result dot.

**[1:16:22]** Get audio, okay, to basically receive the audio by the stream.

**[1:16:29]** Okay, so this is what happened in the event based synthesis. Now in a manual synthesis, right? It is used for multiple target languages like now for example, let us say your source language is in English and target language could be France, Spanish, German, okay.

**[1:16:49]** So.

**[1:16:51]** Now over here, in this scenario, the automatic synthesis is not supported. Okay, we follow the 2 separate step, okay, translate to text and then use text to speech API to synthesise each translations in the result.

**[1:17:11]** OK.

**[1:17:13]** So.

**[1:17:17]** This is basically what we do in a manual synthesis.

**[1:17:23]** Okay.

**[1:17:26]** So that's the difference between them and there is again the hands on.

**[1:17:34]** Right, which is translate text and the and the speech.

**[1:17:40]** So first you will translate the text in a speech, okay? And then these are basically the libraries like Azure Translator client library for Python, so you can see based on the language. So there is SDKs available for.

**[1:17:59]** A speech and the Azure translator. so.

**[1:18:08]** Azure Translator in the Foundry Foundry tool in the portal, get the application defined from the GitHub, create text translations application.

**[1:18:27]** OK, so you define basically the target target language, choose the target language, create a client using endpoint and credentials.

**[1:18:36]** Then translate the translate the text, enter the text to translate and depending on the so for example.

**[1:18:52]** We should detect the source language and translate to the text to the target language.

**[1:19:00]** Okay.

**[1:19:02]** Right, this one create a speech translations application. So here it's using the speech okay Azure Azure speech to basically nowhere you define over here like friends Fr, Spanish, Hindi, right? So that's basically the target.

**[1:19:21]** Target target languages.

**[1:19:25]** Okay, and you're basically finding different voice out there, right? For friends, you will be using this voice so and then translate the user user speech. So you speak and it will get you output in the target languages out there.

**[1:19:44]** So when prompted, follow the instruction, sign in and then once you run it, the program should translate it into. So when prompted, say something loud right and the program should translate it to the language specified in the code right and print and speak the translation.

**[1:20:10]** Yes.

**[1:20:14]** How to how it manage the accent in the same language? so.

**[1:20:25]** Just a minute, you can define the accent as well. Just give me a second.

**[1:21:32]** Okay, so now from here you can choose.

**[1:21:35]** Okay, so text to speech voice so you can choose from the from this list out there and you can define like text to text to speech voice. So this is what do you define over here like if you go to.

**[1:21:55]** This.

**[1:21:59]** Okay, so now you can define over here the over the voices.

**[1:22:06]** OK, so for different accent out there.

**[1:22:13]** Right, so you can see Arabic, Oman, Arabic, Morocco, right? You can see same language but different, different accent.

**[1:22:30]** Let me share this link so you can go through this.

**[1:22:37]** And also, right, you can find all of this is there in your lab environments. All the instructions for accessing its outside your lab environments, you can refer this link.

**[1:22:54]** Okay, clear.

**[1:22:58]** Alright, now lets take a few questions and we will go for break. Question one: What function of an Azure Translator text translation client object should you use to convert the Chinese word?

**[1:23:17]** Okay, to English word. Hello.

**[1:24:17]** Okay, let's see.

**[1:24:27]** So what function of Azure Translator Text translation client object should you use to convert the Chinese word to the English word?

**[1:24:37]** Is it get supported language, translate, or translitrate?

**[1:24:53]** Okay, option B.

**[1:24:57]** Okay.

**[1:25:01]** Translator text translator client object.

**[1:25:05]** OK, so text translation, translation client object, so it is a translate question number 2.

**[1:25:23]** So what? Sorry, where is?

**[1:25:29]** Is it? Is it? Yeah. So what functions of Azure Translator, Text translation, client object should you use to convert the Russian word in Cyrillic characters to spacibo in Latin characters? So now understand like you're basically.

**[1:25:49]** yes, that's true. Okay, translatorate.

**[1:25:57]** Okay.

**[1:25:59]** So, transliterate.

**[1:26:04]** Question Question number 3.


### Knowledge check — speech  `[1:26:09]`

**[1:26:09]** Which Azure Speech SDK object should you use to specify the language in which you want the speech translated translated?

**[1:26:21]** Speech config, audio config, or speech translations config.

**[1:26:42]** Okay, so less participation.

**[1:26:47]** Yes, everyone.

**[1:26:50]** OK, give it a try.

**[1:26:53]** And ask if you have any question.

**[1:27:08]** Okay, so its option B guys, its B okay, not C basically C, C is basically used.

**[1:27:19]** C is used for the audio config right where we take the we take the like microphone, we define microphone or audio file over here.

**[1:27:32]** Okay, so you need to specify the language in which you want the speech translated, so we go for this one. Okay, speech config is basically where you would provide the end points and the keys right to connect to that service.

**[1:27:47]** OK.

**[1:27:51]** Okay, so that's that's completes this module, module number 3, and now what we left here is module number 4. We will take a 10 minutes break and coming back right, we would be exploring module 4, okay.

**[1:28:09]** Nowhere we would be focusing on now previous, previous we have focus on text, text and language okay and computer speech correct. So now we will be focusing on computer vision and informations extraction. So these 2 workloads we will be exploring coming back.

**[1:28:31]** Could anyone share attendance link, please? Yeah, share.

**[1:28:37]** Can you share the attendance link in the chat?

**[1:28:41]** Okay, I'll run the timer. Okay, 10 minutes quick break and I'll see you after.

**[1:39:46]** Okay.

**[1:39:51]** Okay, let me reshare the attendance URL.

**[1:40:43]** Sorry.

**[1:40:53]** Okay, so I hope you guys are back. Let's get to our...


## Module 4 — Extract Insights from Visual Data  `[1:41:02]`


### Introduction — Module 4  `[1:41:02]`

**[1:41:02]** Next module, module 4.

**[1:41:19]** OK, so.

**[1:41:22]** Now previously we have.

**[1:41:26]** We have discussed on language, okay, like text analysis and speech.

**[1:41:37]** Okay, translations nowhere we will understand how we can extract the insights from visual data in Azure. So basically we will be working on the.

**[1:41:52]** Images and Images and videos, okay, images, videos, then you have invoices, documents, PDFs, okay, so will be this module will be revolve around this different task. so.

**[1:42:13]** So we will focus on computer vision first and then informations, informations extraction.

**[1:42:22]** So develop a vision enable generative BI application.

**[1:42:29]** Okay, Vision enable generative AI application. So we will be discussing the vision capable models, okay, which are basically known as the multi model AI model.

**[1:42:43]** OK, now if you see traditionally the language models could only understand and process the text, OK, but now the modern AI models they can work with both text and images simultaneously.

**[1:43:03]** OK, so here the terms basically come again and again, which is a multi modal. Multi modal means the model can understand multiple types of data, whether it is a text, whether it is a images, whether it is a audio, or whether it is a video.

**[1:43:20]** OK, so we'll be focusing on the text and image input in this case.

**[1:43:27]** Yeah.

**[1:43:30]** Just give me a second.

**[1:43:33]** Hey.

**[1:43:37]** I lost tip of my writing pen.

**[1:43:41]** Allow me a minute.

**[1:44:20]** OK, finally I have found it.

**[1:44:26]** Thank you. so.


### Vision-capable (multimodal) models  `[1:44:53]`

**[1:44:53]** Okay, so using a vision capable model, vision capable model. Okay, so multi multi model model for text and image data. Now there are 3 common ways to interact with the vision capable model. Okay, one is the...

**[1:45:11]** Text formed. OK, here the user provides only the text.

**[1:45:17]** Okay, for example, like explain how photosynthesis work, okay, and the model generate the text response, right? Next is the image prompt. The user provide only an image, right? So for example.

**[1:45:39]** The user uploads an image of a plant, okay, and ask like what plant is this?

**[1:45:48]** Okay, the model analyse the image and then provide the information, okay.

**[1:45:57]** Nowhere multi model prompt.

**[1:46:01]** Okay.

**[1:46:04]** So.

**[1:46:07]** Multi Modal prompt means it basically supports different input and different output. So like text images, okay, maybe.

**[1:46:22]** Videos OK, an output would be like text, images, and videos.

**[1:46:31]** Okay.

**[1:46:38]** So typically a multi modal prompt for vision based input include multiple parts. Okay, for example a text part and an image part.

**[1:46:53]** Okay.

**[1:46:55]** Nowhere how this can be useful. For example, is you can see over here, OK, you upload the image of fruit, right? And then you ask to you ask here like what desserts could I make with this?

**[1:47:13]** Okay.

**[1:47:16]** It can be used in retail industry, right? Retail industry where the customer can upload the product of the image like a product, they can upload picture of the shirt and they can ask like do you have similar product?

**[1:47:36]** The I identify the product and recommend what are the matching items.

**[1:47:43]** Okay, or maybe lets say in healthcare, the medical staff, they can upload an X Ray X Ray image and then ask for the observations.

**[1:47:58]** Okay, like maybe you can provide the prescriptions out there and then you can say, okay, just provide the summary or explain this prescriptions in a simple, simple manner.

**[1:48:16]** Okay, and similarly, it could be like manufacturing where the workers upload the image of the equipments and they can ask, like, okay, is there any visible damage? Okay, so the model identify the defects and then the...

**[1:48:36]** The team basically can work on that.

**[1:48:41]** So similarly, insurance for example, so the customer can upload the accident photo and ask the ask for the damage assessment.

**[1:48:54]** And the AI basically helps to categorise and summarise the visible damage.

**[1:48:59]** OK, now there are so many use cases of using the multi model for the text and image data.

**[1:49:08]** Now we have talked about the chat completions API and response API previously. OK, now lets see for how this is used for image based prompt. For image based prompt, OK, you load the image. So this is you're loading the image, right? fruit.

**[1:49:28]** Dot JPJ, you are creating the URL, okay, data URL.

**[1:49:36]** And whenever you calling an API, so client dot chat dot completions dot create model messages in the messages you provides with the user user content.

**[1:49:51]** Okay, user content, like what can I make? Okay, this user content, okay, which consists of text and image URL.

**[1:50:04]** OK, so you provide your text and image URL to your model.

**[1:50:08]** OK, and then you get the response. Same response response dot choice dot message dot content in response a I API. OK here.

**[1:50:24]** Client or response input.

**[1:50:28]** Roll.

**[1:50:30]** User in the type input text. OK, what can I make an input message in input image is image URL? So that's how basically we provide right when you're using the chat competitions API or the response API.

**[1:50:50]** Okay.

**[1:50:52]** So basically, the both a Pi can analyse image and they can generate the response, okay, but response API is it provides more, it's a modern and provides you simplify development experience.

**[1:51:10]** Okay.

**[1:51:13]** And also one more thing here.

**[1:51:18]** Page 64, okay, the API communicate using the text based formats, right? Text based formats like the, so the binary image, the image data must be converted into the text representation right before it is transmitted.

**[1:51:40]** Okay, so that's over here, what's basically this is doing over here. Okay, so it need to be converted into text representation before. Okay, so you can say base 64 is like a way of packaging an image into the text so it can travel safely inside the API request.

**[1:52:01]** Okay.

**[1:52:05]** Clear.

**[1:52:17]** Is there any way to recognise image is generated by AI using AI?

**[1:52:24]** Yes, there are basically there are algorithmal right through which you can also recognise whether that image is generated by the A I or it is actual image. Okay, there is one I will share the reference link.

**[1:52:45]** OK, but here we are talking about like generating the image, OK, not generating image. Here we will talk generating image as well, but here we are talking about layer multi modal right, which basically lets you provide both the text and image right and ask anything related with the image.

**[1:53:05]** OK, now this is an example of using the address API for image based prompt. OK, so here we provides the image, right? And we ask like what desserts could I make with this? So the fruit in this image is dragon fruit. Here are some received.

**[1:53:24]** Recipes that you can try and then it will give you the recipes of the so it recognise the image right and right so you can see here how does it relate the text with the image.

**[1:53:40]** Okay.


### Analyze images — Chat Completions & Response API  `[1:53:42]`

**[1:53:42]** Similarly, this is an example using the Chat Completions API for image based prompt. The fruits in this image is in the orange and you can use it to make orange juice, orange sorbet, and melt mard it.

**[1:54:02]** Okay, so let's see this model from the boundary, right? Let's go to the discover.

**[1:54:15]** Discover Discover and let's go to the model model and let's so fine tuning, not fine tuning.

**[1:54:43]** Okay, for example, the models which we have already we have deployed GPT GPT High 4.1.

**[1:54:53]** 4.1 Okay, now we go to this chat completion and then if we see for benchmark, right, so here we can also see what is the.

**[1:55:07]** Input and output.

**[1:55:11]** Just a minute here. Yeah, so you can see here. OK, input type, input type is a text, an image and output type is a text.

**[1:55:22]** Okay, so we have already deployed this. We'll go to build and.

**[1:55:28]** Let's go to deployment CBT 4.1, let's go to the playground, okay.

**[1:55:37]** Go to the playground and now people find information. So here you can see attach file. So from here I can go and I can attach over here any.

**[1:55:54]** Let's say fruit.

**[1:56:07]** So along with this, what is what this what is this image of and?

**[1:56:18]** What can we make with this?

**[1:56:34]** Okay, it says this is an image of mango, right? And if I show you basically this image, so you can see this is a mango, right? And with mango you can make a variety of delicious foods and drinks.

**[1:56:53]** Okay.

**[1:56:57]** Yeah.

**[1:56:59]** So.

**[1:57:04]** Sorry.

**[1:57:28]** OK, so developer Vision enable chat app.

**[1:57:33]** OK, so over here you will deploy a model like GPT 4.1 OK which we have already and then you can test it like we have OK so I can search for here what results could I make with this fruit so let me.

**[1:57:53]** Let's go there.

**[1:58:03]** Okay, perfect.

**[1:58:07]** And.

**[1:58:10]** And similarly, you can create a client application, okay?

**[1:58:15]** So gets application file from the from the GitHub. And over here using the open OpenAI endpoint.

**[1:58:26]** And you also provide the image, right image of the fruit.

**[1:58:36]** Yeah.

**[1:58:37]** Okay.

**[1:58:39]** Then you'll write a code to submit the URL based image image prompt. Okay, so image image URL, then you provide share right input input text is basically what the user provides and then along with this we are providing image image URL.

**[1:58:58]** So this is providing then once you sign in, once you run it and then when you say OK, so just some recipe that include this fruit OK then it will.

**[1:59:17]** OK, it will review this and you can modify the code to upload a local image file as well.

**[1:59:23]** So you can upload Sir local local image by using this code.

**[1:59:34]** Okay, so what is this food? What recipe could I use it in?

**[1:59:41]** Okay.

**[1:59:43]** So this is.

**[1:59:48]** Okay, this is basically your image.

**[1:59:55]** Okay, image based prompt, okay.

**[2:00:12]** Question one.

**[2:00:17]** Just give me a second, let me share one link.

**[2:00:22]** Reference link and then I will display the questions in the chat.

**[2:00:39]** Just a question, do we have a reference that highlights the difference between AI 102 and AI 103? What's the new parts in the AI 103?

**[2:00:53]** AI 103, you are talking about what?

**[2:00:59]** The previous exam AI 102 and the current one AI 103. Do we have a reference where to see the difference? What's the new?

**[2:01:05]** okay.

**[2:01:10]** Okay, what's the changes out there, right? Okay, just let me see right if I can get to you. There is basically the articles. Just give me a second.

**[2:01:15]** Yeah.

**[2:02:18]** Okay, so I found one where I am sharing the in the chat. So here it's basically talk about like what's what has changed the key difference between 2.

**[2:02:48]** Here I'm also sharing.

**[2:02:51]** A part of the...

**[2:02:54]** No.

**[2:02:57]** Apart from the document.

**[2:03:00]** And.

**[2:03:56]** Okay, and also I'm sharing one more blog from the Microsoft Foundry.

**[2:04:04]** Okay, this is quite old, just a minute.

**[2:04:35]** Okay, so give me give me some time over here. I read once the article over there where you can recognise the images right that generated by the AI by using the AI itself. Okay, so let me.

**[2:04:53]** But now I'm just sharing back the screen.

**[2:05:01]** Okay, and let's take questions.

**[2:05:05]** Okay, question number one.


### Knowledge check  `[2:05:11]`

**[2:05:11]** Which kind of model can you use to respond to the visual input?

**[2:05:47]** Okay, yes, everyone agree.

**[2:05:51]** What kind of model can use to response to visual input? Yes, that's a that's a multi model model which take the various various inputs, right? Visual input is one of them. Question number 2.

**[2:06:11]** How should you submit? How should you submit a prompt that ask a model to analyse an image?

**[2:06:43]** Yes, everyone agree. Yes, that's true. You will submit the prompt that contain a multi part user message, right? Both text content and the image content. Perfect question number 3.

**[2:06:56]** How can you include an image in a message as URL or as a binary data, only as a URL for an online image, OK, or only as a binary data?

**[2:07:28]** Yes, that's true. That's as a URL or as a binary data. Okay, now let's talk about here next generating images and videos. Okay, so as we have discussed.

**[2:07:47]** But generate EVI is basically.

**[2:07:51]** It's a type of AI which is capable of generating the new content, right? And right, image and video is one of them.

**[2:08:03]** So now.


### Image & video generation  `[2:08:06]`

**[2:08:06]** In the previous we have seen that how it understand the image right now, we'll understand how it create an image with the AI, OK.

**[2:08:17]** So using we can deploy the image generations models right there are various image generation models are there is a model which take the you know text prompt as a input and then convert it into you know into a image. So you provide this as an input to the model and.

**[2:08:36]** It create the new image. Okay, so here you said create an image of a squirrel on a skateboard, right? The model understand you know what's what the squirrel look like, what the skateboard look like, and then also like how to.

**[2:08:56]** Combine them into a realistic or artistic image. Okay, then it generate the completely new image that has never existed before. So this capability is called basically text to image generation, text to image generation.

**[2:09:22]** Okay, and for this we have GPT images as a model we have flux 0.1 context Pro. Okay, so this is which is being used over here, right? And you have given a prompt here and it will generate the image. Okay, so.

**[2:09:41]** There are various models available in the Azure AI Foundry, okay, and that can be used over here. So, as a developer, simply you deploy the models and you interact with it through the API. Now, next one is...

**[2:10:00]** Testing in Azure A Foundry Playground, okay, in the playground, so you can select an image size. Okay, so you can, you can, you can select the size of the image over here, right? You can see.

**[2:10:15]** Okay, so different like you can create images for portrait image or landscape image. Okay, second is attach a reference image. So if you have any reference image out there because some model supports image to image generation.

**[2:10:34]** Okay, so instead of generating from the text along, we can provide source image and we can provide the additional instructions. Okay, now for example, lets say you upload the image of a car and then you ask like, okay, convert this car into a futuristic cyberbunk style. The model uses the updated.

**[2:10:56]** The model use your the image which you uploaded, right? So it will use it as a reference and then it will generate a transform transform version of that image. Okay, so you enter you if supported and require right, you can also attach a reference image.

**[2:11:18]** Wow, that's basically for image to image model and enter a prompt describing the desired image.

**[2:11:26]** Okay, now for example over here, okay.

**[2:11:32]** So.

**[2:11:34]** Now it will basically.

**[2:11:36]** It will generate an image from the text prompt. So you define your model. Okay, you provides the prompt.

**[2:11:43]** Okay, and you provides over here the in a number of images, the size of the images.

**[2:11:52]** Okay, and to save the generated images, you're using base 64 again, so you define the image.

**[2:12:05]** Okay, and then it will be saved with the image.png.

**[2:12:12]** Okay.

**[2:12:19]** Okay, similarly, what we can do, we can also create a, we can generate the video, okay, video generating model. So some generative AI models can create video from video scene from the text prompt, okay, for example.

**[2:12:38]** Sora 2 is a model that can create a generative that generate realistic scenes from the text formed reference images or by remix remixing existing videos. You can deploy and use the Sora 2 model in Microsoft Foundry project as well. OK.

**[2:12:59]** So this video generating models are models that create a short videos right based on the instructions you provide.

**[2:13:10]** OK, so when you say OK, create a video of a squirrel on a skateboard, so the model basically understand what the squirrel look like, what the skateboard look like, how the motion work and how scenes evolve overtime.

**[2:13:30]** Then the model basically generate the video showing you the squirrel riding the skateboard okay rather than just creating a static image. So this is basically known as the text to text to video.

**[2:13:49]** Generation.

**[2:13:53]** Okay, then along with this, okay, so let's take now if we talk about like where this can be used in real life, real world.

**[2:14:07]** So this can be used in marketing and advertisement, right, where companies can create promotional videos without filming it, or maybe used for e learning where educational organizations can generate training content, right? It could be used for entertainment media where.

**[2:14:28]** the film studio they can generate the storyboard or concept scene okay. Similarly, product demonstrations, gaming, right and various other industries can use the video generating models.

**[2:14:46]** Now generate videos from prompt, okay?

**[2:14:51]** So for.

**[2:14:55]** For effective video prompt, okay, describe a shot for storyboard, including the details. So you have to provide the prompts in details there, right? So you have to, you have to provide over here what would be the camera, camera framing.

**[2:15:14]** Okay, the width medium or the close up, okay, you need to describe the subject descriptions with a distinct distinct tip details, actions described in small steps, lightning, colour palette, and the.

**[2:15:34]** And this style.

**[2:15:37]** Okay, now for example.

**[2:15:41]** For example.

**[2:15:43]** In the 90s 80s, sci fi film style, a medium close up shoot at an eye level, captures a young young woman standing at the edge of the rain socks rooftop. Okay, she takes 2 steps, 2 slow steps forward, pause and.

**[2:16:02]** Turn her head back to look over her shoulder. So we describe all the scenes over here: neon pink, blue light. Okay, billboard here, right? The colour palettes and anchors are electric bulb, hot pink, and still grey.

**[2:16:29]** Okay, so for example, here you see, okay, you're using the Sura 2 model, right? And you provides here a prompt a robot waiter in a restaurant.

**[2:16:42]** Okay, so this the A I basically take this prompt and generate a short video showing the Vinod robot serving the customer in the restaurant environment.

**[2:16:55]** Okay.

**[2:16:57]** So if we take a look here, create and create create the video generations job. So model the client dot videos dot create Sora 2 from you provide the size and you provides like how long you want the clip off.

**[2:17:15]** Okay, poll for completions.

**[2:17:18]** Okay, poll for completions. So nowhere you're basically waiting for the completions of the video. Okay, once the video is completed, right, then after that you will download when the video gets completed.

**[2:17:41]** Okay, so it video generation is much more computationally intensive because the A I model must build a scene, generate hundreds of frames, right? It has to maintain those consistency, create a realistic motions, okay.

**[2:18:00]** And then render the final video.

**[2:18:03]** So, because of this, the video generation basically it run as a asynchronous job.

**[2:18:10]** So the request start a job and return the job ID.

**[2:18:16]** Okay, it return the return the job ID, which is your like video ID. Okay.

**[2:18:27]** And then after that.

**[2:18:30]** Okay, you will basically once the once the video status change to completed right then you will be downloading that video.

**[2:18:42]** Okay, clear.

**[2:18:47]** So lets see this exercise before we get into the knowledge check the image and videos. So for image and videos, so we need to go to the discover. Okay, so.

**[2:19:11]** I have, let me go to the build. I have already deployments for 4.1 for example. Okay, now I'll ask it to create an image. Okay, create and create a create an image.

**[2:19:32]** An image of.

**[2:19:35]** Fish.

**[2:19:36]** Serving.

**[2:19:39]** And the fish eating fish.

**[2:19:47]** In a.

**[2:19:54]** Best friends.


### Generate images with AI tools (demo)  `[2:20:05]`

**[2:20:05]** Okay, now see there, here's the prompt you can use to generate your desired image with the AI Arts tool.

**[2:20:18]** Okay, so it is basically getting you okay that you can do this, but it is not generating that image. Okay, please enable a image generation tools or use use this prompt in an image generating apps.

**[2:20:33]** Okay, so it is good 1i can take this prompt good prompts out there. Let lets deploy, lets go to the discover, and then here we will go to model models.

**[2:20:54]** And we'll go to inference task. Okay, we'll go for image, image generation, right? Image to text, we'll go for.

**[2:21:08]** Text to image. There are 5 models okay for text to image. So GPT image to GPT one 1.5, flex to image to image, text to image.

**[2:21:23]** Okay, so let me use this one GPT image one. Let's see benchmark is not there. Okay, let's see. I may deploy.

**[2:21:37]** It has been deprecated, okay.

**[2:21:47]** This must be the updated one.

**[2:22:01]** Okay, generate an image to get started. Okay, so from here we can.

**[2:22:08]** See and let me okay.

**[2:22:14]** Let me provide the prompt.

**[2:22:36]** So from here you can provide the size, the quality.

**[2:22:44]** Okay, and also.

**[2:22:48]** Some parameter, the image.

**[2:23:02]** So while it's generating the image.

**[2:23:06]** Okay, now we have given the descriptive scene over there.

**[2:23:36]** Okay.

**[2:23:55]** Okay, so we have one more models here, right, which is for video generation, Sora 2.

**[2:24:03]** And okay, let's.

**[2:24:06]** Right, you can see 2 videos are there.

**[2:24:11]** But I did the same same text prompt. Okay, this is the another one.

**[2:24:19]** Okay, and let's do one thing. We will just try to create a video.

**[2:24:31]** With the aquatic theme decor under, the last face is wearing a Iglesias while the small face is on the plate. Okay, Gun is like a moody is playful and a cotton is okay, perfect.

**[2:25:16]** Hey.

**[2:25:19]** Alright, so here we go.

**[2:25:23]** Okay.

**[2:25:27]** So this generated images there. Let's go download this.

**[2:25:40]** Okay, looks really good.

**[2:25:44]** Right, okay, let's see the video one as well.

**[2:25:49]** And okay, still generating the video. I think it's done now. Okay, now let me play this.

**[2:25:59]** Okay, perfect.

**[2:26:17]** Okay.

**[2:26:23]** So this is perfect.

**[2:26:26]** Okay, I hope guys this is clear to everyone. Do you have any question here?


### Knowledge check  `[2:26:42]`

**[2:26:42]** OK, let's take the question. OK, knowledge check question one. You want to find a model in a Microsoft Foundry to generate image. Which interface tasks should you filter by?

**[2:27:19]** Yes, everyone agree with option A.

**[2:27:25]** Yes, that's text to image.

**[2:27:28]** Okay, clear.

**[2:27:31]** Question number 2.

**[2:27:34]** Which OpenAI API can you use with the image generation model?

**[2:28:02]** So this is for sure, okay.

**[2:28:06]** Yes.

**[2:28:08]** It's image guys, right?

**[2:28:16]** Okay, so next, so that's about image and video generations. We are using the Microsoft Foundry models. Okay, now let's understand analyse image with contained understanding, okay.

**[2:28:36]** So we are going to understand, we are going to discuss on content understanding.

**[2:28:41]** Okay, now it is basically one of the powerful multimodal multimodal.

**[2:28:51]** Capabilities.

**[2:28:54]** Available in Azure AI Service.

**[2:29:03]** OK, so before we have seen how AI models can identify objects in an image and answers questions about the image contain understanding. Take this step further, OK, instead of simply recognising like what what's in an image.

**[2:29:24]** It basically extract the.

**[2:29:27]** It extract meaning.

**[2:29:33]** Context.

**[2:29:37]** Okay, relationships.


### Content understanding — structured info from visual content  `[2:29:42]`

**[2:29:42]** And the structure information okay from the visual content.

**[2:29:51]** Okay, so.

**[2:29:56]** So, for example, lets take an example of image image analysis, okay, where image analysis simply say, okay, like lets say you provide this picture, so it will say, okay, I see a table, a coffee cup, and a notebook, but contain understanding basically.

**[2:30:16]** Says this appeared to be a work workplace desk setups, someone is working on remotely. Okay, so you basically gets a depth out there like content understanding. When you are analysing the image with the content understanding, you are not basically getting like, okay, what's there?

**[2:30:36]** But also the meaning, the context, the relationships, and the structure information.

**[2:30:44]** Okay, so it seems like okay, it is understanding it rather than it is basically simply detecting the objects, what's objects in the image. So content understanding is basically the ability of a I model to process the.

**[2:31:04]** Process the visual. Process the visual.

**[2:31:10]** Content to process the visual content and convert it into a meaningful structure information. Structure information okay that the application can use. I will repeat again.

**[2:31:30]** Contain understanding is a is the ability of a I models to process the visual process visual content. Okay, now not only the visual content actually.

**[2:31:42]** Right, we will talk about here, but in this we are analysing image only with the content understanding and then it will convert it into meaningful structure information. Then that can be used in the applications. Okay, so right for example.

**[2:32:02]** Okay, for example, let us say you have the image out there, right? You provide the images, so contain understand, understand what the objects are, okay, how they are related to each other, right? What activity is occurring or what is the overall context of the scene?

**[2:32:21]** OK.

**[2:32:24]** So this is basically the difference between right analysing image with the models and with the content understanding, okay.

**[2:32:37]** So what is Azure Contain Understanding in Foundry tool? Okay, so Azure Azure Contain Understanding basically.

**[2:32:51]** It is a multi multi modal AI service that can analyse multiple content type. Okay, multiple content type like images, documents, forms, audios, videos, and extract the important informations automatically from them.

**[2:33:12]** Okay, so it is able to not only able to analyse the images, but also documents and forms like audios, videos.

**[2:33:23]** Okay, so in images it could be like, lets say, product image, medical images, vehicle damage image. Okay, so it can identify the relevant information and then convert them into the structured data. Getting it similarly documents and form, so it will be able to analyze like invoice.

**[2:33:45]** Okay, insurance claim, text form contracts.

**[2:33:51]** Okay, and it would be able to extract the various fields in this like invoice number, or maybe customer name, amount, date.

**[2:34:02]** Audio.

**[2:34:05]** Right, it could be able to analyse like customer call, okay, meeting recording interviews.

**[2:34:13]** Right. And it can basically process the information and provides you like what are the key topic discuss, what is the customer sentiment, what is the, it provides structure, summaries, videos, right? So simply it will, it can be used for security footages or.

**[2:34:33]** In a product demonstration video, training videos, and a I can analyse the scene, the activities, the events occur within that video.

**[2:34:45]** OK, so over here, this is the overall process, right? The user provides image, documents, audio, and videos OK to the Azure content understanding, right? And it will basically this Azure content understanding uses the analyzer. OK, you can think of this analyzer.

**[2:35:05]** Okay, it is basically it is an AI power.

**[2:35:12]** AI power export.

**[2:35:16]** Expert train to understand the specifics type of content. So the analyzer basically examine the content and it extract the relevant informations and the output become the structured data.

**[2:35:32]** Okay, in the JSON format, so you have images over here and or maybe let's say you have a invoice, so it would basically extract like what is the invoice, invoice number, the vendor amount, or total amounts.

**[2:35:51]** Okay.

**[2:35:54]** Clear, so it's a air power information instructions and this analyzer could be could be prebuilt or custom analyzer. So prebuilt analyzer are basically which are ready to use analyzer for common business scenario, like for example, invoice processing is common right in every industry.

**[2:36:16]** Receive analysis is common. Okay, Journal document processing is common. Okay, so for this there are basically a prebuilt analyser that you can use and you don't need to train, you don't need to train for specific for this kind of.

**[2:36:35]** Business scenario, okay, so this can be used immediately without training then.

**[2:36:42]** Custom Custom Analyzer.

**[2:36:46]** Basically, where you have your documents in a unique documents formats like maybe lets say a logistic company may have a custom shipping form and hospital may have the specialised menu medical form which is not common right in all the hospitals out there or maybe manufacturing company have a unique you know inspections report.

**[2:37:07]** In this situation, the developers can create a custom analyzer, okay, tailored to their business need, right? And then they can use that analyzer, okay, with the documents there they want to analyse.


### Schema training & image analyzer  `[2:37:27]`

**[2:37:27]** And next one is a single and few shots schema training.

**[2:37:33]** Okay.

**[2:37:35]** Now understand the traditionally machine learning require hundreds or thousands of training examples.

**[2:37:46]** Right, we need to provide like thousands of like images, thousands of documents, thousands of people face okay to train any kind of models there. Now, Azure Contain Understanding this significantly reduce this effort, okay.

**[2:38:03]** Now.

**[2:38:05]** Developers can provide like one or few examples and define the structure they want to extract.

**[2:38:14]** Okay, so suppose we upload purchase order and then we'll specify over there like what are the basically things we want to extract.

**[2:38:24]** So we upload the purchase order and then you specify, okay, supplier name, order number, total amount, delivery date.

**[2:38:34]** So the service learn the schema and then it can apply to the similar documents without extensive training data sets. This will speed up the development.

**[2:38:48]** Okay.

**[2:38:50]** So.

**[2:38:52]** Lets say this is the insurance company.

**[2:38:55]** Who received thousands of claims everyday.

**[2:38:59]** So each claims could have claim form, vehicle photographs, audio statement, or maybe any supporting documents. So without AI, employee need to manually review everything.

**[2:39:17]** With Azure Contain Understanding, okay, the documents are analysed automatically, the vehicle damages images are processed automatically, audio statement are summarised, you know, key claim information is extracted.

**[2:39:34]** And the final output becomes structure output that can be sent directly into the business system.

**[2:39:40]** Okay, so this save a significant time and reduce the manual effort. Okay, so these are basically some of the advantages of using the Azure content understanding right for images, documents, forms, audio.

**[2:40:00]** Video.

**[2:40:02]** Now, for example, let's take this analysing images with content understanding.

**[2:40:09]** Okay, so this is basically when you upload this image and even if you see this image is not clear actually.

**[2:40:20]** Okay.

**[2:40:22]** We can see the train status stations with the train moving at a high speed and people working on the platforms.

**[2:40:32]** Now the traditional image recognition system simply identify the train, the people, okay, the platforms, the lightning, okay, or signboard.

**[2:40:47]** Okay, so although that the information is important, like because basically what's there in the image, but it does not provide much context. Now, Azure Container Understanding it goes beyond the object detection.

**[2:41:04]** OK, so it basically tell you what is actually happening in this image. So the image shows a busy underground train station platform with a train bypassing at a high speed, creating a motion blur effect. Several people are walking along the platforms, some appearing blur due to the motion.

**[2:41:23]** The station has a curb. Okay, there see what it has noticed with a visible metal framework and lightning. Okay, a digital sign was above the platform indicates the train arrive. Did you notice that?

**[2:41:42]** Did you notice this?

**[2:41:46]** Okay, so this kind of this kind of context your contained understanding provide.

**[2:41:57]** Okay, it is understanding it, understanding the activity. The training is moving, the motion blur indicates speed, right? People are working alone, they are working along the platforms.

**[2:42:14]** Okay, so this is this provides more, more, more value and.

**[2:42:22]** Now over here, same analyzing images with contained understanding, how this is basically done.

**[2:42:32]** So it provides the image.

**[2:42:36]** OK, use one or more training images to define the schema.

**[2:42:41]** To define the schema for the custom analyzer. So you're creating the custom analyzer now.

**[2:42:49]** OK, you use training image and you define the schema in the.

**[2:42:59]** In this, you can basically have, in this schema, you want description, you want tag, you want animal type.

**[2:43:09]** Okay, animal type or environment.

**[2:43:13]** Ok.

**[2:43:17]** So.

**[2:43:19]** Now then here right use the contain understanding API to run analyzer and generate the results. So first you gets a container understanding client submits an image file through the analyzer. Okay, client dot begin analyzer.

**[2:43:39]** Then get result from the poller and then display the result which is in the JSON format.

**[2:43:46]** Okay, which will basically show you all this information, descriptions and tag and any other field that you want, right? You would be able to get that.

**[2:44:04]** Okay.

**[2:44:07]** So, for example, this one image image analyzer, okay, image analyzer, and over here you provide the image, the this provide the description, it provide you the tag.

**[2:44:23]** Okay, the person is sitting on the purple couch with their leg crossed, right? You see, and you can also view this result right in the JSON format.

**[2:44:39]** Okay, so let's give a try analysing the image with the content understanding. So I'll go back here and.

**[2:44:52]** Lets do the same you have in your.

**[2:44:56]** And so on.

**[2:45:10]** Okay, so these are the hands on like developer vision enable chat app, generate image with AI, generate video with Shora in Microsoft Foundry, and analyse image with the content Azure content understanding. So Microsoft Foundry project create a storage account storage.

**[2:45:29]** Storage account create an image analyser in the Azure content understanding.

**[2:45:35]** So for Azure Container Understanding, we have a separate studio. Okay, Container Understanding Studio. So let's.

**[2:45:47]** Continue understanding, right? And we would need Azure Blob storage because your you would be using this to store.

**[2:46:00]** Your images, so let's go for portal.com.

**[2:46:23]** Okay, let's search for storage.

**[2:47:21]** Okay, validation fail, it's already taken, so just to make it unique, I'll just keep everything default.

**[2:47:37]** And let's go click on create.

**[2:48:13]** Okay, so the deployment is complete. Let's go to...

**[2:48:19]** Resource.

**[2:48:21]** And.

**[2:48:27]** Okay.

**[2:48:30]** Okay, and over here.

**[2:49:00]** Save image download. Okay, done. Alright, so once.

**[2:49:09]** Okay, now we are in the...

**[2:49:12]** In this portal, sorry, as your content understanding, let's sign in to get started.

**[2:49:31]** Sorry, will be difficult.

**[2:49:36]** Yeah, default directory.

**[2:49:51]** OK, so get started with content understanding, you can try common prebuilt analyzer on your data, right? So these are some common analyzer data, right? So layout, OK, document field, invoice. So when you click on this.

**[2:50:35]** Okay, now you can see here there's a sample sample invoice, okay, we are trying the pre built analyzer. Okay, so we have we have analyzer already right and we are just using that analyzer and we can run the analysis over here, right? Even you can drag and drop the.

**[2:50:54]** File here, okay. And then when you run the analysis, okay, now this is where you can get the result.

**[2:51:15]** It is running the analysis on the invoice.pdf.

**[2:51:34]** Taking a while.


### Build an image analyzer application  `[2:51:50]`

**[2:51:50]** OK, so you can also create an image analyzer application. So prepare the application configuration. And then write the code to analyze image and generate the descriptions about that image.

**[2:52:11]** OK, we'll test through the portal. It's taking a while.

**[2:52:22]** Okay, let's go for audio search image.

**[2:52:28]** Okay, I'll see there, right? I'll just go browse profile. Let's go here.

**[2:52:58]** Okay, now you can see here for this it shows you right a summary. The image shows a majestic male lion sitting in a tall grass in a there is a single tree in an expense, expensive flat horizons under the emphasising the vastness of the natural.

**[2:53:18]** Have it yet, right? Did you see there, right? And if you want to see the results, okay, so this is the output.

**[2:53:33]** And also you have a code samples as well.

**[2:53:43]** Okay, so you are getting that somebody out there.

**[2:53:55]** Okay, so same same you would be performing over here.

**[2:54:00]** Okay, creating an image analyzer in the so you can not only for image so you can see over here right videos as well, right? If you see image search, okay, audio search, call centers, okay, document search, video search, you will go over here. That's basically a flight simulator.

**[2:54:21]** Let me run this sample.

**[2:54:29]** Okay, so.

**[2:54:40]** Yes, guardrail would be applied right to the image and video generation model.

**[2:54:59]** So.

**[2:55:04]** OK, good voice is better to have good data. To achieve life, we build a universal TTS model based on 3000 hours of data. We actually accumulated tons of the data so that this universal model is able to capture the nuance of the audio and generate a more natural voice for the algorithm.

**[2:55:25]** What we liked about cognitive services offerings were that they had a much higher fidelity and they sounded a lot more like an actual human voice. Orlando Ground 9555, requesting the end of pushback.

**[2:55:44]** Okay, now you can see here this video opens with the flight simulator logo alongside the Microsoft Azure AI branding, right? So you have basically the summary of the video, we can find code results and the field.

**[2:56:02]** Okay, and if you want to build it right so see over here built right and you can create a extract, contain and field with the custom schema or classify and route with the custom categories.

**[2:56:34]** Okay, so nowhere you can choose a template start from the scratch, image analysis, document analysis, invoice. Okay, so from here, like you see there, we have a schema, all right, by default we have a schema so I can save this.

**[2:56:56]** Right, and I can make the changes out there, right? So from the I can create a schema for my no invoice and what I want to extract from it. I can define over here, I can add a new field.

**[2:57:15]** Okay, so.

**[2:57:19]** Provide the different data type.

**[2:57:24]** So.

**[2:57:26]** So this is what we are extracting. This is the schema, okay? Once you have the schema, then we build the analyzer, okay, with this schema and then we use this analyzer for it is like you are training all your own models, you decide like what.

**[2:57:44]** Things you want to, what field you want to extract from that form, OK? And then after that, what do you have a schema? With this schema, you build an analyser, OK? And then you use that analyser to extract all those field from like any new similar kind of documents.

**[2:58:05]** Okay, clear.


### Knowledge check  `[2:58:09]`

**[2:58:09]** So let's take questions here. Question number one.

**[2:58:14]** You want to find a model in Microsoft Foundry to generate image. Which inference task should you filter by? Oh, it's same. Just a minute.

**[2:58:29]** OK, so this is similar to the previous one which we have taken. OK, so this is here and next one is analyse documents with content understanding. It's same like you see, use the content understanding to analyse documents in form and retrieve a specific field value. For example, extract key data value from the invoice to automate payment process.

**[2:58:39]** Sister.

**[2:58:53]** So analysing documents could be use. I will just give you one scenario. Let's say you need to get reimbursement, right? In you want to get reimbursement. and.

**[2:59:11]** You upload the invoice, as you upload the invoice, the system basically extract the invoice numbers, right invoice date and the total amount, right? And then it will basically check with the it extract that from your you know receipt and then it check with the company policy and if.

**[2:59:30]** That's within the company policy, then it will automatically process the reimbursement.

**[2:59:38]** OK, now if you see this traditionally, someone was have to manually type this information in the system like invoice number, vendors name, invoice date, a total amount. OK, now with analysing documents right with this content content understanding.

**[2:59:59]** OK, continue understanding, we can do that quite easily. We have also seen like analysing videos, OK, we can use this to summarise the conference call, determine sentiment of the recorded, recorded customer conversations, we can extract key data from the telephone messages and so on.

**[3:00:21]** Analyzing audio, analyzing video, extracting key points from the video conference recording, summarize presentations, detect and presence of specific activities in the security footages.

**[3:00:33]** OK, we have to create an analyzer, right? So for this, you have to create a Microsoft Foundry project. You have to define the contain understanding schema for the information that you want to extract. This can be based on the contain samples and analyzer template, then build the analyzer based on the.

**[3:00:52]** That completed schema and then use that analysis to extract or generate the field from the new content.

**[3:01:00]** This is the whole process out there. Is it clear, guys? This is clear to you?

**[3:01:13]** Okay, alright.


### Hands-on — content understanding (documents)  `[3:01:20]`

**[3:01:20]** Okay, so this is hands on where you will use as your content understanding to analyse documents, analyse slides, analyse audio, analyse the video.

**[3:01:31]** Okay, we will take a 10 minutes break here and coming first, coming further right, we will proceed further.

**[3:01:42]** Thank you.

**[3:12:14]** All right, okay, yes, let's proceed further. Extract information from a multi multi model content.

**[3:12:26]** So.

**[3:12:29]** I know this is...

**[3:12:32]** This is basically the hands on hands on lab. Okay, so.

**[3:12:40]** So you what do you do is basically first you'll try a prebuilt analyzer in the Microsoft Foundry, right? And then you will you will set up Container Understanding Studio for custom analyzer and then you extract information from the invoice documents, right? So now this is what you do define the schema for the invoice analysis.

**[3:13:02]** Right, once you define that schema and then after that you will build and test an analyser for the invoice, okay, and then you extract information from the okay. The next one is like information from the slide slide image.

**[3:13:22]** Okay, build and test and analyzer, then extract information from the voicemail, audio recording, right? And for this also, you'll build and test the analyzer. First, you create a schema. So this is where you basically specify the caller, okay, you want to get summary, you want to get actions, right?

**[3:13:43]** Call back number if there is any alternative contact where you want to get all those is from the audio audio analysis, right? And yeah, so similarly extract information for video video conference recording. So you want to get summary, you want to get participants OK, participants name SlideShare.

**[3:14:04]** Share slides and assign actions.

**[3:14:09]** So I'm sharing this link.

**[3:14:12]** In the chat.

**[3:14:18]** Okay, so let's proceed further. Okay, prepare to use the content understanding API.

**[3:14:27]** Now to use the container Azure Container Understanding API. So you to create a Foundry project right and.

**[3:14:39]** Okay, authenticate via entire ID or the contain understanding endpoints and API key, and to find your credentials via the code, use the Microsoft Foundry SDK with Microsoft Inter ID to automatically retrieve the connections detail for your project. Same what we have been doing so far. Okay, now also you can define your schema and you can create the analyser.

**[3:15:01]** By using the content understanding API. Okay, so this is what it shows over here.

**[3:15:13]** OK, so define define your schema and create the analyzer. So here you define the define the field that you want to right extract so like the contact name, email address, right and so on. So you specify the base analyzer and generate.

**[3:15:35]** Dev model to use send the send the schema to the client to create the analyzer, okay.

**[3:15:45]** And over here, these are basically key components of their base analyzer, ID, field schema, models. Okay, so you define your schema and then you create the analyzer and then further, then after that you analyze the.

**[3:16:04]** Analyse the content now once you have the analyser, okay.

**[3:16:09]** OK, now that you have created the analyser and you have defined the schema, next step is using the analysis to process the real content. OK, so this is the complete workflow of analysing content and retrieving the structure result. Authenticate to your client, OK, begin analysis.

**[3:16:29]** Providing the analyzer name and the URL or binary data, okay? So through this input, you provides actually what you want to, what you want to process, okay?

**[3:16:45]** So then you are going to retrieve the results right and then extract the content from there. OK, so for example contact.

**[3:16:55]** Contact name, right, and the email address. So you can see over here this is the value we are getting from that analyzers which we have created. Okay, so analyzer is as like trained employee creating an analysis like training that employee on you know what informations to look for. Analyzing containers like when we give that employees new documents or.

**[3:17:17]** Ask it to extract the informations that we care about, okay?


### Develop a content understanding client app  `[3:17:26]`

**[3:17:26]** So develop a container understanding client application. There's a lab for this. OK, so let's take the questions from the container understanding.

**[3:17:39]** Okay, question number, question number one.

**[3:17:47]** Question number one: What kind of AI solutions is Azure Content Understanding designed to help you build?

**[3:18:27]** So, Azure Container Understanding is designed to build a analyzer that extract information from the documents, right? And what information you want from the document you can define with the help of the analysis schema.

**[3:18:42]** Correct. Question 2.

**[3:19:09]** Yeah.

**[3:19:11]** So, which graphical tool should you use to create an Azure Content Understanding project?

**[3:19:22]** OK, as you contain understanding project, remember I've taken you to the you know this page over here right now, this is where we have created the created the project and then we can basically.

**[3:19:38]** Now we can basically create our project here. So you see it shows you the project here.

**[3:19:45]** OK, we can also see the analyzer list once you once you have a schema and then you build the analyzer and then that analyzer can be view from here.

**[3:19:56]** OK, so welcome to the Azure Container Understanding. This is a studio bring together Azure Document Intelligence and advanced LLM based multi model capabilities for extracting information across structure and under structure content.

**[3:20:12]** So the right answer is yes, that's true. That's option number 3.

**[3:20:21]** Okay, what happened guys? The number of participants are less now participating on the quiz.

**[3:20:32]** What should you define for the informations you want to extract from content?

**[3:21:00]** Okay, so yes, so everyone says this schema, right? That's true. Okay, perfect.


### Module 4 — last topic  `[3:21:11]`

**[3:21:11]** Okay, so now let's move to our last topic of module 4, and after this, we will go for, I will give you some tips and tricks if you are, you know, if you want to prepare for the AI 103 exam and you want to give it.

**[3:21:31]** To validate your knowledge and being certified okay as a AI apps and a I agents developer and also how you can basically then further I will take your queries and any questions any.

**[3:21:50]** Doubt you have and then we were gonna wind up the sessions.

**[3:21:56]** Okay.

**[3:21:58]** So we talk overs here.

**[3:22:02]** Sorry.

**[3:22:05]** Okay, so let's talk about here, create a knowledge mining solutions with Azure AI search. Okay, now see organizations they generate enormous amount of information everyday, okay, and this informations.

**[3:22:26]** Can be in different formats and locations. It could be PDF documents, it could be Word files, it could be email, scan forms, databases, or in the blob storage websites. Okay, the challenge is that the organization.

**[3:22:48]** Organization process the process the valuable information.

**[3:22:53]** Okay, but much of the much of the informations remain hidden inside those unstructured content, and employees often find they spend a lot of time searching for the informations rather than using it.

**[3:23:11]** So this is where right Azure AI search come in.

**[3:23:17]** Okay, now creating a knowledge mining solutions. What do you mean by knowledge mining solutions? So this is basically knowledge mining solution is nothing but it is a processing, it is a process of okay discovering.

**[3:23:35]** Discovery.

**[3:23:38]** Extracting.

**[3:23:41]** Okay.

**[3:23:43]** Enriching.

**[3:23:46]** Okay.

**[3:23:48]** Organising.

**[3:23:52]** And.

**[3:23:56]** Looks clear.

**[3:23:57]** Searching.

**[3:24:02]** Information.

**[3:24:04]** Form.

**[3:24:06]** A large collection of data.

**[3:24:15]** Okay.

**[3:24:17]** So, knowledge mining is process of discovering, extracting, enriching, organising, and searching information from a large collection of data, right? So that's basically the issue with the issue with the organization is that they basically generate huge amount of information everyday.

**[3:24:38]** Okay, and the you find that informations when needed out there, right? So you can think of it like creating an intelligent digital librarian, okay? Instead of manually opening hundreds of documents to find an answer, Azure AI Search can.

**[3:24:57]** Automatically analyse the content and help user find exactly what they need within the second.

**[3:25:05]** Okay, enough, let me give you an example. Okay, so lets say company has let lets say 5, 5000 or 5 5,00,000 documents.

**[3:25:18]** Okay, which is stored in the SharePoint and Azure storage. Okay, so this is basically documents there now.

**[3:25:28]** Employee ask, okay, show me all the contracts.

**[3:25:33]** Expiring within next 90 days.

**[3:25:39]** I want to guess basically all the contracts expiring within the next 90 days. Now, without the knowledge mining, someone may need to do this to locate that informations, okay, find out basically all the documents, right, all the contracts which is going to.

**[3:25:59]** Expire within next 90 days with Azure AI Search. Okay, the answers to this questions can be found instantly.

**[3:26:11]** Okay.

**[3:26:13]** Got it.

**[3:26:15]** So there is a basically process how basically the Azure AI search work. Okay, so.

**[3:26:30]** Okay, basically there are 4 major stages. Okay, how is your AI search work? There are 4.

**[3:26:40]** Mazer.

**[3:26:42]** Stages first one is connect to the data source.

**[3:26:52]** Right, so Azure A Search basically connect to the data source where the data is stored, okay, so as Azure Blob Storage or maybe SharePoint, SQL Database, Cosmos DB. Okay, so it's like gathering all the valuable information. That's the first steps.

**[3:27:12]** Second step is basically indexing.

**[3:27:17]** Indexing. Okay, so Azure AI search basically create an index. Okay, so it's like it's similar to the index at the front of the book or at the back of the book.

**[3:27:32]** Okay, so instead of reading every documents right every time.

**[3:27:37]** Okay.

**[3:27:42]** So instead of reading every documents every every time.

**[3:27:47]** Azure basically create a searchable structure that allow the information to be retrieved quickly. So that is indexing. So it will basically create a index like the index of the book.

**[3:28:02]** Okay.

**[3:28:04]** Then the 3rd one is basically 3rd steps here is it will basically a I enriched.

**[3:28:12]** And AI enrichments. So what happened is this here the AI basically add the intelligence, okay, like you have documents and you want to extract the contract, you know, which is expired 90 days out there.

**[3:28:26]** Okay, so using the Azure Azure AI, we can automatically extract the text from the scan document. We can basically extract the key phrases, we can identify entities like people, organizations, locations, or we can generate summaries, we can translate the content.

**[3:28:47]** Okay, so AI enrichments automatically, automatically.

**[3:28:55]** Enrich okay, it enrich the documents okay by the Azure AI.

**[3:29:02]** Clear.

**[3:29:04]** And then comes the 4th one, which is basically search.

**[3:29:09]** And.

**[3:29:11]** Search and discovery.

**[3:29:15]** Source in discovery. Now once the index is built and the it is enriched, the user can perform an intelligent search.

**[3:29:26]** Okay, so for example, lets say when you search for invoices from Contoso over $5000, so as you a search understand the query and it will return the relevant results instantly.

**[3:29:43]** Okay, and now just think about how it can be used in law forms, law forms like with millions of documents where the lawyers need to find a specific contract, okay, or a specific court cases.

**[3:30:03]** Okay, so instead of manually reviewing those files, Azure AI search can identify the client name, okay, contract date, okay, legal entities.

**[3:30:15]** Okay, so maybe for healthcare like hospitals, can they store patients record, medical report, research paper.

**[3:30:25]** So we can basically doctor can search like patient diagnose diagnosis with diabetes and hypertension's like in 2025. So Azure AI search basically retrieve this relevant information quickly.

**[3:30:42]** So clear the 44 major 4 major stages out there connect to the data source, indexing, AI enrichment, and search and discovery.

**[3:30:53]** Clear so.

**[3:30:59]** Okay, what is Azure AI search?

**[3:31:03]** OK.

**[3:31:05]** So, it is a Microsoft enterprise search and knowledge discovery platforms. Key capabilities in intelligence indexing, it indexes documents and data from a range of sources, including images. AI enrichments use AI skills to enrich the index data and vectorizations. It also supports the.

**[3:31:26]** Agentic workloads.

**[3:31:29]** Okay.

**[3:31:31]** So.

**[3:31:34]** Is basically intelligence indexing before the user can search information as your a search create an index. Okay, a enrichment. We talk about factorizations is basically it is converting your content into factor embedding.

**[3:31:54]** Okay, so instead of searching only for exact keyword, the Azure AI search can understand the semantic meaning. Okay, means if the user searches for employee benefits, okay, Azure can also find documents discussing the health insurance or leave policies or retirement plan.

**[3:32:15]** Okay, even if those exact words were not in that, were not there in the document.

**[3:32:24]** OK, so this semantic semantic understanding is what enabled the modern AI assistant and agentic application. So if you see what is the core application, so enterprise search, right, so powering the websites and apps. to.

**[3:32:45]** Find informations fast rag for generative a I, right? So for rag also be used as your AI search, OK, grounding LM prompts, knowledge mining, OK, tuning massive documents libraries into data assets for analytics.

**[3:33:04]** OK, now this is the same OK, extract text from extract data from with an indexer. OK, here indexer extract data from the data source. Document cracking basically retrieve the text contained from the from the source OK and enrichment pipelines.

**[3:33:24]** Build Jason's representations of each index documents, okay, and the field for each documents can be extracted from the source or it could be generated in the enrichment pipeline with the with the AI enrichment and the result is a index containing all the index document.

**[3:33:47]** Okay, so indexer, you can think of indexer as a automated data data ingestion and processing engine.

**[3:33:55]** OK, where let us say organization has thousands of documents stored in the blob storage, instead of manually uploading each documents into a I Azure AI search, the indexer automatically connect to you know those sources and read the content, you know process it and prepare it for searching.

**[3:34:14]** Okay, then comes to the enrich the extracted data with this AI skills. So you have a built in skills where you use the AI services to detect the language that the text is written. Okay, if I want to find all the documents which is written in a particular language, so I would need a you know AI service which detect the language.


### AI Search & document search  `[3:34:34]`

**[3:34:34]** Detecting and extracting places, locations, other lets say maybe I want to find all the documents where the place is mentioned is London. Okay, so here we are basically going to use this built in skills of extracting places and likewise so PLL extracting text from image, generating captions, multi modal image and text vectorizations.

**[3:34:55]** Customer skills, which is where basically you implement the custom logic to return the field based on the input. So I can write the custom logics over here and I can say, OK, just count the number of count how many times the particular word appear in the document.

**[3:35:15]** Okay, so that basically implement custom logics to return field based on the input often refer around the services like Azure language.

**[3:35:27]** OK, and then further right search and index. So now each each index field can be configured as a field. OK, field that identify the unique key for index record searchable.

**[3:35:42]** Okay.

**[3:35:44]** Now index, when we create an index, we configure each field with a specific capability, okay, that determine like how it can be searched, filtered, sorted, okay, retrieval. So we can basically refine all of this out there and based on that we can search, we can filter, we can sort them.

**[3:36:06]** And then finally, right, we also like after we extract extract informations, then we need to persist it.

**[3:36:19]** Okay, now we extract it and then we can store this one in the knowledge store. So knowledge store is basically a place where Azure ASR save all of its valuable informations okay, which is discovered during the enrichment process.

**[3:36:39]** So instead of keeping that information only inside the search index, the Azure can persist that in the Azure storage so that other application and services can use it. So you can store the projections in the Azure Azure storage and we here we have the first format is object.

**[3:36:58]** Which is which are basically stored as a decisions document okay table for relational schema for extracted field okay, similar similar to your data database table okay, if thousands of invoice are processed, Azure can create rows and column containing those invoice detail.

**[3:37:21]** File is basically.

**[3:37:24]** File is extracted images like Azure may extract images, scan pages, or other any embedded content. So it is basically used to persist that.

**[3:37:38]** Okay, so create a knowledge mining.

**[3:37:46]** So exercise.

**[3:37:51]** OK, create a mining mining solutions here. First, you will create the Azure storage. OK, then you will create and run an indexer, right?

**[3:38:04]** We will You will upload the documents first. You will create a Azure AI search resource, create a storage account, and then upload the document to the Azure storage, and then you create and run an indexer.

**[3:38:20]** And then you can search the index.

**[3:38:24]** OK, like this where you can search, OK, and then it will basically get you the output out there. Like for example, you get this time there is also only the file name and any location mentioned in there. OK, so you can see this is like what's output you'll be getting out there. So you can create a search client application.

**[3:38:46]** Prepare to use with Azure AI Search SDK.

**[3:38:52]** So I'm sharing this link.

**[3:39:03]** Okay, for the over for the data.

**[3:39:11]** 2 will get ****** vectorized in gets store.

**[3:39:19]** Real time data.


## Q&A, Feedback & Closing  `[3:39:30]`


### Open Q&A  `[3:39:30]`

**[3:39:30]** Okay, so lot a lot of questions are there. Okay, so now first thing a I search is only for document search. Yes, it is mainly for document search, but document means like it can also contain an image. For example, let's say you have documents which contain an image.

**[3:39:31]** Yeah.

**[3:39:49]** OK, so with the help of the AI skills, we can also extract the with the OCR, we can extract the text from the images because maybe lets say that image contain some information that you would basically want to extract and which basically help you to find the information. So yeah, mainly for mainly for the document search, but also we can leverage it to the data.

**[3:40:12]** Database data 2, okay, we can connect to databases as well.

**[3:40:20]** Okay.

**[3:40:22]** So.

**[3:40:25]** Also, where will the dog get vectorised?

**[3:40:30]** Vectorise data gets stored. Okay, so vectorise data basically gets stored in the Azure Azure AI search only.

**[3:40:42]** Okay, as your AI search, can it work for the real time data?

**[3:40:52]** Or real time data.

**[3:40:55]** I mean, kind of a chat or anything that which gets frequently changing or if it is very dynamically getting changed in the background. So for an example, you mentioned that AI search can be accessible with a DB, which means if the DB is getting changed with the data's.

**[3:40:55]** I need to.

**[3:41:16]** Will it still work or every time it needs to get a trigger point to again understand the change and again vectorise it and update it in AI search, AI search storage and then it will accommodate it?

**[3:41:16]** Right.

**[3:41:29]** It's.

**[3:41:32]** I understand completely, as I know, basically it is not for the real real time, okay, because every time like it basically have there it has to do the indexing of their like if there is a new contents being added to the database or documents.

**[3:41:50]** It has to do those indexing out there, but I need to check on this for the real time, okay, to confirm, right, it is not for the real time data, okay.

**[3:42:06]** And index need categorizations and store separate yet. So you can basically like you know you can process those indexes out there, right? You can store the projections in the in the Azure storage.

**[3:42:24]** How big it can deal data considers and how the cost consumptions work here, OK.

**[3:42:28]** Just to know the limitation on AI search, you mentioned that data is getting stored at the AI search. So how much, how many documentation it can hold or is it data volume will be a measurable quantity in terms of limitation and then how the cost consumption is being used on this?

**[3:42:47]** Okay, lets see the latest documentations out there because it's keep changing out there. Now we can see service limits in the Azure AI search. So we have over here.

**[3:43:01]** Depend on the pricing tier, so we have free basic and the standard so we can see here, okay, it's basically.

**[3:43:12]** The smallest scale and is engineered for multi tenant last for small indexes, 3000 indexes per service subscriptions limits.

**[3:43:23]** Okay, service limits for each of them partition storage. So here we can see all the limitations out there. So index, index limit for each of the different different pricing tier like free basic.

**[3:43:42]** Right, S1, S2, S3.

**[3:43:46]** Okay, and for the pricing, this is for the indexer limits.

**[3:43:54]** Its getting varied based on like what we are doing, indexing, what we are vectorising. Does it vary for each shows like that?

**[3:44:04]** It very for basically it has a like whenever you create a your a search, right, you have to choose the pricing tier, okay? And there is a different different cost for the each of the pricing tier, different features, different pricing.

**[3:44:26]** Okay.

**[3:44:29]** And if you see the pricing.

**[3:44:39]** So Azure AI search pricing and if we scroll down, so we can see the...

**[3:44:45]** Over here pricing so you can see.

**[3:44:53]** So its not based on the consumption, it is based on the sub like what we are subscribing or based on subscription, the cost will be calculated even though if we are using so much limitation of files getting added to it, it is based on subscription per month, it is getting cost, it is not on the consumption like how models we used to.

**[3:45:15]** Like tokens, but cost is getting added, right? So that is handled in a different way, and this is handled in a different way. It is not on the consumption, rather it is on the subscription. I understand from this way. Is it correct? Okay.

**[3:45:28]** Yeah, yes, mainly it is on the subscriptions out there like okay, there's the tier actually, but there are some cases out there right where basically it based on the compute type. Okay, so.

**[3:45:47]** Right, for example, up to 9 units per service. So this is what you are getting maximum out there, but mainly it would be on the pricing there. But there are basically some other features, right, which might basically cost you extra. OK, now for example, let us say this one, OK.

**[3:46:07]** So over here per million tokens, right? First, 50,000,000 token free per month, okay? And after that, so this is a different, different cost out there. So even even if you see this one, okay, customer entity look up skills, document cracking, and then also you can take a look here, okay?

**[3:46:25]** The FAQs out there, OK, so there is a standard cost as well as there is a variable variable cost out there depending on the product and the feature.

**[3:46:36]** Okay.

**[3:46:39]** So I'm pasting that this link as well.

**[3:46:48]** Okay, so.

**[3:46:52]** Okay, let me take this question. Is there any place where we can write logic where model can be selected dynamically based on the consumption required for a prone to optimise or because something like one agent is multiple model and yeah, so there's a basically concepts of model routing. Okay, so model routing basically lets you.

**[3:47:14]** Basically, it automatically decides like what based on your prompt, it will automatically decide which models would be right for your cases. So if you see go to the model catalogue, let me take you there, right? There is a model routing.

**[3:47:33]** Okay, I'll just go for document model.

**[3:47:38]** Routing in Azure AI Foundry. Okay, so you can read over here more on this model model router for Microsoft Foundry. So it is a trained language model that intelligently routes your prompt in real time to the most suitable large language model. Okay, you deploy the model router like any other foundry model.

**[3:48:01]** Okay, so it is similar to how you deploy any other like we have deployed many models out there GPT, you know Sora and other transcript model. So it deliver high performance while saving on the cost, reducing latencies and increasing the so it will automatically decide you know based on if it is a complex like your.

**[3:48:19]** Your prompt is a complex, so it will basically choose the model right with more reasonings.

**[3:48:27]** Okay, sorry, I'll share the link. And similarly, if the prompt is simple, like simple prompt, then it will choose the, it will automatically gets you the output from the like the small models out there, right, with less, less cost model.

**[3:48:46]** Clear.

**[3:48:51]** Okay, so just minute.

**[3:48:57]** Right, so this was basically last topic. I'll take few more minutes before we get started. Just give me a second guys here. I have one more meeting. I'll just.

**[3:49:51]** Alright, okay, fine. So guys, I'm yeah, this is done. I'm done with.

**[3:50:00]** This one, this was the last last module out there, right? Model number 4, okay. and.

**[3:50:09]** Okay.

**[3:50:12]** One more Q&A session to be planned next week as we need times to go over each. Yes, so we can you can basically ask for revised sessions. Okay, revision session so you can ask your training coordinator, sorry, spokesperson to arrange one revised.

**[3:50:33]** Revised session, so we have that revised sessions out there so that you can basically perform all the labs and then you have any doubts, any concern, then you can basically ask in that revi revision sessions. It would be for like 2 or 4 hours session.

**[3:50:52]** Okay, so guys, I'm sharing my email ID is there in the LET portal, right? So I'm sharing with you.


### Course feedback  `[3:51:05]`

**[3:51:05]** A feedback URL. Okay, so please.

**[3:51:09]** Share your feedback.

**[3:51:12]** Where we can practice for the A I103 exam. OK, this is completely new exam, so you will not get practice sets that's not mature yet because still the exam is not live, but as it basically gets live, then you started getting the.

**[3:51:31]** Practice test out there.

**[3:51:35]** In Microsoft, Microsoft Learn used to provide the practice test out there, but it is not available for this AI 103. You can basically because it is something you know lot of things are similar to AI 103, you can refer the practice test for the AI 102 and also there are basically various online you know online sources you can.

**[3:51:54]** You can get practice test.

**[3:51:59]** Do we have any code for this training for the timesheet?

**[3:52:05]** Have any code for this training for times sake? I'm not getting your question. Code, I mean voucher code.

**[3:52:16]** Okay, its a I103 its a I103.

**[3:52:25]** Okay, simple.

**[3:52:28]** I'm not sure about it's TT 04. If you are talking about this course code then so 103 okay, so guys, I have shared with you link a feedback link. Okay, please share your feedback for this sessions, share your whole experience out there.

**[3:52:50]** What's your project code for timesheet filing?

**[3:52:54]** Okay.

**[3:52:59]** Project code, I'm not sure about.

**[3:53:05]** Okay, it's internal KPMG code. Okay, alright.

**[3:53:15]** Okay, done guys.

**[3:53:21]** Okay, one one more meeting is scheduled for me actually, so I just need to go and take that meeting. so.

**[3:53:38]** so last, please use this feedback survey right and provide your feedback. And if you have any questions out there, you can always reach out to me on the mail and also right if your attendance is not marked you know for you know previous like let's say.

**[3:53:57]** 2 or 3 days, okay, just mention the day, okay, and your name and day, okay, for which the attendance is not marked, okay, and I will manually mark it from the system.

**[3:54:13]** OK, so what you have to do, you have to say OK, your name, right? Lets say Sumit, right? And attendance is not marked. For example, lets say day 2, right, comma day 4, OK, like this.

**[3:54:26]** Okay, and I will mark it manually from the back end because a lot of you are facing the you mark attendance, your it shows mark at your end, but it is not showing on my end. Yes, that's great Ranjit, right? So likewise, okay. And only if you have attend, right? Because we.

**[3:54:46]** Have the teams basically used to keep record of like when you have joined, when you have left. Okay, so only if you have attend the sessions for each day, okay, just mention this way. Okay, so.


### Closing remarks  `[3:55:01]`

**[3:55:01]** Yeah, so guys, I just need to, I just need to go and because I have another bt schedule. I wish you all the best. If you have any queries, questions, so feel free to use my email ID, right? And please do make sure like you provide your feedback.

**[3:55:21]** There is a survey link I have shared in the chat. Okay, yeah, so I mean this was basically instead of like 30 hours of 32 hours of training, right, we just have 15 hours over here. So it means like you have to put on more times for performance hands on.

**[3:55:40]** Right, I was only able to get you through the overview what's there in this course and the columns, right? And take you through the portals and show you basically where those services are available. But yes, to basically be confident, right, you need to perform those hands on.

**[3:56:00]** Perfect. My mail ID is in a let in LET portal, right? So I'm also sharing over here.

**[3:56:09]** I am sure. What do you think then that after how much time that LET portal access will be resolved because the certificate will also be there now?

**[3:56:18]** By.

**[3:56:20]** Correct, correct, correct. By today or tomorrow?

**[3:56:25]** Okay, I will keep tap on it, right? And yes, the 33 of you are facing the history. I am keeping tap on it right by today or tomorrow, right? If you are not getting it right, you can just drop me a mail.

**[3:56:26]** Okay, thank you.

**[3:56:38]** Okay, in case.

**[3:56:43]** Okay, so guys, I'm just yeah, thank you. Fine, fine, thank you everyone. I'm just leaving for now.

**[3:56:44]** Okay.

**[3:56:53]** Thank you.

**[3:56:56]** Thank you everyone for joining. Thank you.

**[3:57:05]** Thank you.
