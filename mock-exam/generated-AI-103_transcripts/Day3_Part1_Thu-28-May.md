# AI-103T00: Develop AI Apps and Agents on Azure — Day 3 (Part 1)

- **Date:** Thursday, 28 May 2026 (12:30–16:30 IST)
- **Trainer:** Shova Kant Sharma (Microsoft Certified Trainer), Koenig Solutions
- **Recording:** Day 3 — Meeting Recording (Part 1 of 2, SharePoint Stream)
- **Length:** ~3:59:59  ·  **Captions:** 1146

> Transcript captured from the on-screen auto-generated captions for personal study. Captions are machine-generated (Microsoft Stream) and may contain errors. Section headings were added at the points where the trainer moves to a new topic; the caption text itself is verbatim.

## Contents

- `[0:00]` Recap — Module 2 (AI Agents)
  - `[0:44]` Recap of Day 2
  - `[19:39]` Revisiting agents built yesterday
  - `[40:57]` Review & troubleshooting
- `[1:02:36]` Module 2 (continued) — Agent Framework & Orchestration
  - `[1:02:36]` Agent workflows & human-in-the-loop
  - `[1:05:20]` Core components of a workflow
  - `[1:30:49]` Develop agents with Microsoft Agent Framework
  - `[1:41:15]` Hands-on lab — Agent Framework
  - `[1:47:42]` Orchestrate multi-agent solutions
  - `[1:53:31]` Sequential & handoff orchestration
  - `[2:01:52]` Hands-on lab — multi-agent solution
  - `[2:08:42]` End of Module 2 & break
- `[2:20:56]` Module 3 — Natural Language Solutions
  - `[2:20:56]` Introduction — text analysis concepts
  - `[2:24:26]` Sentiment, language detection, NER & PII
  - `[2:30:48]` Text Analytics API
  - `[2:36:05]` Demo / lab — text analysis (Python)
  - `[2:57:56]` Text analysis lab — review
  - `[3:01:07]` Text analysis agent with Azure Language MCP server
  - `[3:23:38]` Speech — speech-capable models
  - `[3:32:33]` Speech-to-text
  - `[3:41:05]` Text-to-speech
  - `[3:47:45]` When to use speech models vs Foundry speech service
- `[3:50:30]` Q&A & Wrap-up

---


## Recap — Module 2 (AI Agents)  `[0:00]`

**[0:03]** For you to performs the hands on, okay, so hands on is it's very, very important. The hands on exercise out there to reinforce the learning, right? What we are discussing in the session, okay, so until and unless you not try by yourself, right, you not experiment by yourself, right?

**[0:26]** You not remember it for long. Okay, so lets.

**[0:34]** Let me share to open my slides. Let's go through the topics.


### Recap of Day 2  `[0:44]`

**[0:44]** Okay, so yesterday we started with module 2, okay, we started with the AI agent in Microsoft Foundry.

**[0:54]** Let's have a quick recap and then we'll proceed with other topics from module 2 and then we'll switch to module number 3.

**[1:11]** All right, so.

**[1:17]** So yesterday we started with the AI agents in module 2. Okay, in first topic we...

**[1:27]** We learn how to develop an AI agents with Microsoft Foundry and Visual Studio Code. OK, we understand the AI agent. OK, what is AI agents? We understand the flow, right? And we explorer these 3 components in the.

**[1:48]** In the AI agents, LLM instructions and the tools, correct? Then further, we understand why agents are useful.

**[2:02]** Okay, also we have taken some AI agents use cases, okay, for personal productivity, for research, for sales, for customer service, right? So these are some example of AI use cases, AI agents use cases we understood that.

**[2:22]** What is the typical development workflows? Okay, so you connect to the Foundry project, right? And then you create an AI agents, you configure the agents' instructions, you add tools, you test your agents in the playground, right? You iterate on the design, and then you deploy the agents to the productions. and then.

**[2:40]** Finally, you will integrate into the application so that the consumers can start your users can start using it, right? So you can integrate your agents into various applications, whether it's website, mobile app, in your teams, in CRM.

**[3:01]** Okay, we talk about the required resources, we talk about what are the optional resources.

**[3:08]** Then we understood.

**[3:12]** Basically, to development approach, okay, creating your AI agents in Foundry using Foundry portal.

**[3:22]** OK, which is a visual web based interface and Visual Studio Code, which is a developer centric. OK, get friendly.

**[3:31]** Okay, where you can controls the version controls and you have basically the code first development approach.

**[3:42]** Right then, knowledge check done, then we talk was here indicates the custom tools, custom tools in your agents. We understood why to use the customs tool through this through this example of.

**[4:00]** Agents asking about the weather conditions in a ski ski resort, right? So options for implementing the custom tool, right? So we have custom functions, Azure functions, open API specifications, and Azure.

**[4:19]** Logic app. So these are 4 options for implementing the custom tools.

**[4:25]** Then exercise, labs and knowledge check.

**[4:30]** Okay, then we talk about the MCP tool, okay, how to integrates an MCP tool with Azure A I agents. So we understood what is model context protocol right and how model context protocols help is used in your.

**[4:50]** AI agents, okay, how it basically solves the challenge, you know, where you have to build a separate custom indications, you know, for each tools.

**[5:03]** And how the MCP server basically provides standard standard way for your a I agents to connect with like with many tools and data sources.

**[5:17]** Correct. Not only for the tools, but also the data sources.

**[5:24]** We understood integrates agents tools using MCP server and client, right? MCP server, MCP client, and agent.

**[5:34]** And then hands on lab knowledge check.

**[5:38]** Okay, next one is built knowledge enhance a I agents with the foundry IQ. So we understood the rack, the concepts of rack, okay, and we understand the difference difference between the simple agents and.

**[5:59]** Rack power agents.

**[6:02]** Okay, then we explorer the foundry Foundry IQ.

**[6:08]** Okay, which provides a centrally managed knowledge base for your agents.

**[6:14]** Okay, so it basically auto index.

**[6:17]** Right, whenever a new documents is basically added to the data source, right? It is auto index, it continuously sync and.

**[6:27]** know it is accessible to any.

**[6:30]** Any authorised agents and this Foundry IQ can be used by various agents out there. Okay, so it basically helps agents answers the company specific contextual informations.

**[6:49]** So configures database data sources, right? It could be we have 3 options here.

**[6:56]** One is your index.

**[6:59]** Second, direct, and 3rd is the real time.

**[7:05]** Okay, then over here we talk about configures the retrievals with foundry IQ, how you can create an effective instructions, you know where you need to specify the 3 critical behaviour okay to use to retrieving with the foundry IQ.

**[7:25]** Okay, and then hands on lab, the knowledge check, okay.

**[7:31]** Now lets talk about here, integrate your agents with Microsoft 365. Okay, now Microsoft 365 has already a Microsoft 365 Copilot.

**[7:46]** Correct.

**[7:48]** So there are various applications in Microsoft 365. The idea of integrating your agents with Microsoft 365 is basically what we want is to, we want to connect the agent to Microsoft 365.

**[8:07]** So the user can access it from their from their tools, okay, the tools they already use everyday, like for example, Teams, okay, Microsoft Teams. So for example, lets say you created an HR assistant agents, okay.

**[8:28]** And you want to make that HR assistant agents into the teams, okay, where the people, where the employees can basically ask questions about, leave policy, the benefits or expenses, expenses, rules, okay, policies.

**[8:50]** Okay, so the benefits over here is that the user do not need to open a separate custom application. They can interact with agents directly inside their normal work environments.

**[9:03]** Okay, and also.

**[9:07]** Right, understanding the agents agents' application.

**[9:12]** Now over here, Microsoft, if we...

**[9:22]** Give me a second. Okay, lets go to.

**[10:27]** Okay.

**[10:47]** So.

**[10:49]** Incognito M 365.

**[11:17]** Okay, so this is the dummy account. I think this is expired now.

**[11:49]** Okay, let's take a one from the lab.

**[12:02]** OK, so don't have.

**[12:08]** Okay, it does not have lab on in indicating the agents with Microsoft 365. Just allow me a minute here.

**[12:28]** I'll just take one credentials out there.

**[13:06]** Okay.

**[13:18]** Okay, so I will be using a dummy accounts to sign into the Microsoft 365 Copilot. Okay, now understanding the.

**[13:32]** Understanding the agents agents applications. Okay, now when we publish the agent, what happened is the Microsoft Foundry it create an agents applications resource, okay, which basically has a dedicated invocations URL.

**[13:52]** Okay, it means it provides you a stable endpoint that will remain consistent as you update your agents agents versions. Like even if you update your agents versions later, the URL remain the same, so the application integration does not break. Okay, then this app agents applications resource also provides the agent.

**[14:14]** Agent identity OK, it means the agents will get its own identity OK on Microsoft, a distinct Microsoft intra identity, it is separate from your development project. OK, so this basically help you to secure, you know, secure the.

**[14:35]** Access.

**[14:37]** Okay, to authenticate.

**[14:41]** Authentications and the permission.

**[14:48]** Permissions OK when the agents connect to the Microsoft 365 or other enterprise resources. OK, so dedicated invocation URL agents identity and as well.

**[15:04]** Okay, as well the user data isolations it means one user input and interactions they are not available to other other users. Okay, for example, if one employee ask like ask the...

**[15:23]** HR agents about the salary or leave informations, another employee cannot see that conversations.

**[15:34]** Okay, so agent agents application resource.

**[15:39]** Give the publish agents a dedicated invocations URL.

**[15:45]** Okay, secure identity with the agents agents ID, Microsoft intra identity for the agents and then isolated users data, okay, which basically make it suitable for productions and Microsoft 365 integrations.

**[16:10]** Okay.

**[16:14]** Next step is publish your agents, OK, so the user can access it OK through Teams or Microsoft 365.

**[16:25]** Now, first thing we need to do is we need to select your agent's version.

**[16:31]** Okay, then you have to start publishing process.

**[16:37]** Okay, from the Microsoft Foundry, right? And the 3rd thing is basically you have to configure the Azure Bot service. Okay, Azure Bot service. This is basically which which help expose this you know agent okay as a chat.

**[16:57]** Pod experience so that can be used in the teams and other channels. So it is using this Azure port service.

**[17:10]** It is using Azure Bot Service, okay, through this, okay, it exposed the agents okay to the teams and Microsoft 365.

**[17:21]** Then the 4th one is complete the metadata, okay, which means like agents, agents name, okay, descriptions, icon for the agents, okay, who is the publishers of this agents, right? Any privacy policy or any terms of use.

**[17:41]** Right, you basically define the metadata for the agents, okay, which you're publishing from your Microsoft foundry, okay, through the Azure bot service.

**[17:55]** Okay, and then after this, okay, now this is the metadata, for example, name, descriptions, icon, okay, publishes, informations, privacy policy, term of use.

**[18:08]** Okay, and then after this, you have to choose your public scope.

**[18:13]** Okay, public scopes. Now there are basically 2 scope over here: share scope and organization scope.

**[18:20]** Okay, in share scope, agents appear under your agents in the store and it is available immediately. Best for testing and small team organization scope is basically the agents appear under built by your organizations in the store and it require the admin approval.

**[18:40]** And it is basically best for productions deployment.

**[18:44]** So you basically have to choose the public scope, whether it is a share scope or organization scope.

**[18:51]** Okay, and then finally, right, you prepare and optionally download the packages.

**[18:59]** Okay, the packages.

**[19:03]** Okay, and this package is basically used to use for the deployment and distributions.

**[19:11]** Okay, so this is basically the process of publishing your agents, right? Selecting the version agent version, then start the publishing process.

**[19:25]** Configures your bot service, OK, complete some meta data, choose your public scope, and prepare and optionally download the.

**[19:35]** Packages. So if we.


### Revisiting agents built yesterday  `[19:39]`

**[19:39]** Go to our previous agents we have created yesterday.

**[19:43]** Let's go to the previous one. Let me see if I can.

**[19:49]** Get here resource.

**[19:56]** Okay, so it's not available.

**[20:02]** Resources are not available, so let's exit.

**[20:14]** Okay, so.

**[20:18]** Let's go to the agents which we have created.

**[20:27]** Okay, so yesterday we created here this IT support agent.

**[20:34]** Okay, so for this agents, we provide the instructions, we define the tools, right? and.

**[20:45]** OK, now once here, right? So this shows you the different versions. OK, version one.

**[20:53]** Okay, version 2 and the version 3 which is right now which is which is the active one. Okay, you can also compare your versions, you can show all the version history, you can delete the current version, right? And then you have this option to.

**[21:12]** Publish.

**[21:14]** Okay, so to publish and you can see here you're getting here this is the active version, okay, version 3 and this is the this is the endpoint, okay, this is the endpoint and then you can see publish to Teams and Microsoft 365.

**[21:33]** Okay, so still this is in preview. So here this is basically where you define your agent's name, descriptions, sort description, descriptions, right? Then you configure your Azure Bot service. Okay, so.

**[21:54]** First, we need to have the bot service. So now if you see that the subscriptions does not register use namespace over here bot service. So if we take a look here, bot service.

**[22:10]** And if we if you go here, OK, if I try to create it.

**[22:17]** Okay, then.

**[22:21]** Microsoft is your bot. Okay, so you would not be able to create in the subscription because this is not registered in your subscription. If we go to try to click on create right and you provide the information over here, bot handlers right and other information out there, it will throw an error.

**[22:42]** We go to the subscription.

**[22:45]** OK, we go to subscriptions and we'll go to this setting and you can see the resource provider.

**[22:55]** Resource provider, I look for the bot bot service. Okay, now you can see the bot service is not registered with my subscription and because of which we are getting this error, it says the subscription is not registered to use the namespace Microsoft dot bot service.

**[23:14]** Okay.

**[23:17]** So we are going to go here and what we have to do is we have to select it and then register it. So once you register it, then with your subscription, then you would be able to create the bot service resource okay in your subscription.

**[23:37]** So it provides here this details, the author, the developers, right and then developers, websites, term of use, privacy statement. OK then right, we need to fill it and then basically go to the next one where you have to.

**[23:57]** Once you complete the metadata, then you choose your publicity scope, okay? And then you will be able to basically gets the package, okay, which would be installed in the tombs in the teams. and.

**[24:16]** Microsoft 365.

**[24:20]** Okay.

**[24:48]** Okay, now this is basically the hands on, hands on how to deploy the agents to the Microsoft teams and Copilot. Okay, now.

**[25:02]** So if we scroll down over here, right? So what you're gonna do is you're gonna build the agents with the instructions and grounding grounding data, right? So this is the instructions you provides to your agents. You are an enterprise knowledge assistance for Contoso corporations, your role, okay.

**[25:21]** And then you download this IT security policy right and remote work policy, right? And then you will upload this file to the tool, okay? And then right, you will test the agents in the playground.

**[25:41]** Okay, after that, you are going to publish to the Microsoft team. Okay, so when you publish your team, publish to the team, the Foundry portal automatically create an Azure bot service, okay, it generate a team app manifest, okay.

**[26:01]** Package app icons and configurations and then provides a down downloadable app packages. So this is what you have to provide: app name, OK, short description, full descriptions, developer names, all this information. Then you create an app icon, OK, then after that you publish from the.

**[26:21]** From the portal.

**[26:26]** Okay, so here you publish from the portal, publish to teams, then configures teams app detail, basic informations, developers informations. So all this app scope, app icons, right? And then deploy to the team, okay, deploy to the team and then.

**[26:46]** Right into individual scopes or organization scope, right? Then select submit and your agents is now available in the teams. OK, then the people would be able to use agents from the teams.

**[27:17]** Okay, so now you can see here is your bot service. Okay, now once we have enabled it, we have registered it so we can see the status here. Now the bot service is registered with my subscription.

**[27:32]** What services register with my subscriptions so we can view over here. Let me provide here.

**[27:42]** Okay, short description.

**[27:50]** Okay, let's give it his name, Enterprise Knowledge.

**[27:54]** Agent, sorry.

**[28:00]** Let's keep your IT IT support agent assistant for company policies.

**[28:09]** Full description.

**[28:14]** Okay, then developer name.

**[28:44]** Okay, so direct publish, you can publish your agents directly from the AI Foundry or you can download and customise the agents benefits and then side load it in the teams. So you have both options over here. You can download the zip file here.

**[29:03]** And then you can installed into your team applications. So available immediately, just you people in your organizations. It required the admin approval. Okay, so Microsoft 365 admin will review the request and assign access. So just me and then we click on.

**[29:24]** Click on Publish.

**[29:32]** Okay, so your agents is now available in the Microsoft 365 Copilots Agent Store and in your Teams.

**[30:06]** Okay, so.

**[30:10]** I need a Microsoft 365 tenant right to use the agents which we have created this one. Okay, so what we can do is...

**[30:22]** is.

**[30:27]** When we go over here, next publish option, we can go download and download the right teams app dot zip and then we can install this in the teams applications.

**[30:43]** Okay.

**[30:55]** Okay, so that's basically how we create the agents in the portals. Okay, we add the knowledge with the file search, publish to the Microsoft team, publish to the Microsoft 365 Copilots, and update the publish agent.

**[31:16]** Okay, clear case.

**[31:28]** Yes.

**[31:30]** OK, so from where we will get this PPT OK, this slides are only for Microsoft certified trainer, but whatever I'm covering, everything is available in your Microsoft Learn profile. OK, so once you log into your micro once you.

**[31:49]** Okay.

**[31:52]** Let me help you with the getting your courseware actually where you can find the content for the AI 103, right? It is always available in Microsoft. You just have to search for AI 103 like certifications for Microsoft. So when you search over here.

**[32:11]** Right, you can see course AI 103, so the right, you can go through the Microsoft learn contents are available, you know, free of course over here. OK, so this is the link for each of the modules that we gonna cover.

**[32:38]** So will it create a new versions whenever we publish it?

**[32:45]** So basically, you choose the versions, okay? So you basically create different versions and then you publish it, okay? So whatever the, whatever the final versions you have, you publish it so that it can be used by other team members in the teams and Microsoft 365.

**[33:05]** Okay, so this is one second is right to get this to add this course into your Microsoft Learn profile, okay, you have to go to your LED portal, okay, login into the LED portal right using your official.

**[33:24]** Email ID.

**[33:28]** Right.

**[33:31]** And then?

**[33:53]** Okay, now once you have once you have login, right, you have to choose your course. If you have opted for multiple, okay, choose your course over here and then go to courseware, click on the courseware.

**[34:09]** Okay.

**[34:11]** Once you're in the on the course where you can see, okay, click here.

**[34:21]** Okay, and then you have to sign in with your Microsoft Learn profile account.

**[34:33]** Okay, then you will get some pop up, right? And then you have to redeem this key. This is achievement key, achievements, your achievement key, okay, achievement code. So you have to redeem it your Microsoft Learn profile once you redeem it.

**[34:50]** Okay, once you redeem it, then if you go to view profiles and then if you go to the courses, so you would be able to see this course here, develop a I apps and agents okay in Azure. So you'd be able to see that course there and you can go through that course. Now it's the same content that you have in Microsoft learn.

**[35:10]** OK, so you'll find the same contents out there like you can see.

**[35:15]** Sorry, not this one. I'm just showing you.

**[35:20]** You know how you can get this, so it will be for AI 103 in your case.

**[35:27]** Clear.

**[35:32]** From where we can get this HTML doc which you're using alongside the PPT. Okay, so this our I'll share the link.

**[35:44]** So here we go, okay.

**[35:49]** See for second module, develop AI agents in Azure. Okay, so these are the hands on exercises. Build AI agents with portal and Visual Studio, use custom functions, okay, extend agents with model context protocol tool, indicates an AI agents with foundry IQ or deploy agents and so on, right? So this is the all the hands on for second module.

**[36:16]** Okay, so kindly go and redeem your achievement code, right? And once done, just give a like here. So we will wait 2 minutes and once done, we will proceed further.

**[37:01]** The link is blocked. Okay, so you can try with your with your mobile.

**[37:08]** OK, ready meeting in your Microsoft learn profile.

**[37:12]** And then you can go through the contained over there.

**[39:28]** Yes, turn everyone.

**[39:56]** Hey, hi Shubham, your name is Shobha, right? Sorry, I'll just...

**[40:02]** Yeah, yes, your audible result.

**[40:02]** Hello, am I audible? Okay, so in case if you face any issues during the lab, then how we should troubleshoot actually even after following the instructions.

**[40:15]** Actually, this labs are well tested, okay, so if you're following the instructions closely, as you're following closely with the instructions strictly, you will not face any kind of issues out there, right? But is still if you have issues out there.

**[40:34]** At then that time you can take the screenshot of it, right? And you can send an email to me. My mail ID is always there in the LET portal. And also after the session is over, if you need any help out there, there is a help desk out there right after training help desk.

**[40:53]** So you can take the screenshot of it and then you can send to them, right? Try to no way.


### Review & troubleshooting  `[40:57]`

**[40:57]** Okay, so just one quick review. Sorry to interrupt you, just one quick review. So yesterday I was trying to performing Lab 9 and I was trying to create the knowledge base inside Microsoft Foundry IQ portal actually. So that time at the time of creation, it was just giving some error related to some API compatibility or some API preview things.

**[41:09]** Mhm.

**[41:16]** I couldn't capture, but I was not able to proceed further for the lab at the time of creating that knowledge base. So maybe I will recreate that issue or if it is reoccurring, maybe I will share with you there, OK?

**[41:27]** Yes, sure, alright.

**[41:29]** Yeah, so your email is there, right? In that portal, we will drop that error. Okay, sure. Okay, yeah.

**[41:32]** In LET portal, yes, it is there, it is there, okay.

**[41:39]** Okay, so guys done right. I hope you gets the course where in your Microsoft Learn profile. Okay, now let's proceed further and let's take this knowledge check question. Okay, question number one.

**[41:53]** What Azure resource does the foundry portal automatically create when you publish your agents to Microsoft T?

**[42:15]** Okay, just we have 45 response.

**[42:32]** Okay, so yes, that's true. That's Azure bot service. Okay, now this is basically the service which is host, which is used to host your agent.

**[42:46]** Okay, next one. What is Microsoft Work IQ? So we have heard about Microsoft Work IQ.

**[43:12]** Microsoft Work IQ.

**[43:15]** This is a new term, right, in Microsoft.

**[43:20]** What do you think? It is a machine learning model for workspace analytics or is it CLI&MCP server that connect agents to Microsoft 365 data or a replacement for Microsoft Teams, Visual Studio Core extension for building agent?

**[43:39]** Okay, everyone says it's B, right? Yes, that's true. Microsoft Work IQ is a CLI and MTP server that connect your agents to Microsoft 365 data, right? So every everything in your Microsoft 365 out there, right? Whether it's an email, whether it's a.

**[44:00]** Teams conversations, whether it's like the hierarchy in the organization, so it can really make the context out there okay with the Microsoft Work IQ, okay, like similar to similar to we have in Foundry, we have Foundry IQ.

**[44:19]** In Microsoft 365, right, we have the work IQ.

**[44:25]** Okay, through the work IQ, you can connect to all the data in the Microsoft 365.

**[44:34]** Okay.

**[44:37]** So we will take a short break, 1010 minutes break, and then we will understand how to build an agent driven workflow using the Microsoft Foundry.

**[44:49]** Okay.

**[44:59]** Big 10 minutes break. I'll see you after 10 minutes. Thank you.

**[56:20]** Alright, I am back. Okay, so lets proceed further.

**[56:29]** Built agents driven workflow using Microsoft Foundry. Okay, now if you talk about workflow, okay.

**[56:42]** So in normal applications, the workflows are fixed. OK, so they're basically like step one, step 2, step 3.

**[56:56]** Okay, but in agent drivens workflows over here, the agents can understand the user request and decide like what information is needed. Okay, it choose the right tool. it.

**[57:15]** Performs the action and then return the final result.

**[57:22]** Okay, so for example, let's say employee ask.

**[57:28]** Employee ask the.

**[57:34]** Employees, the agents like plan my business trip to Bangalore next week and prepare a expense estimate.

**[57:46]** Okay, so the agents basically it follow the workflow like for first it will understand the request, it check the travel policy, right? Then it use the tool okay or a Pi to check the hotels and flight.

**[58:05]** Right. And then it will apply the conditions like company, company rules, okay, like budget limits.

**[58:15]** Okay, it ask the users any clarifications if needed. Okay, like for example, here when I say plan my trips to Bangalore next week, okay, so maybe it will ask like, okay, what's the exact date actually?

**[58:34]** Okay, so it basically generate the travel plan X estimated, expense estimated.

**[58:43]** Okay, or maybe it create a booking request or maybe approval approval flow.

**[58:52]** OK.

**[58:55]** So.

**[58:58]** In agent driven workflows, this is, this is smart workflows, okay, which can be created by using the Microsoft Foundry.

**[59:11]** So this is how the workflow look, right? What do you what do you see over here? We can create this kind of workflows out there. Okay, so workflow is nothing but it's basically the visual sequence of the steps, okay, that basically define like what happened next and.

**[59:30]** So instead of writing everything in the code, we can design this process using the connected node. These are basically the various connected nodes out there.

**[59:42]** OK, and each node basically perform a specific task here.

**[59:46]** So rather than writing code, you define a sequence of steps using a visual declarative approach that describe what said, what should happen and when it allow the platforms to manage the executions and the state.

**[1:00:04]** Okay.

**[1:00:06]** So these are basically connected node actually. So node performs specific functions. Some node invoke the agent, right? For example, over here, this node basically invoke the student agent. This node basically invoke the teacher agent, okay, while other evaluate conditions.

**[1:00:26]** So this node basically check the conditions, OK, some manage the data some or communicate with users. OK, so together this node form an execution path that determine like how the request move through the system.

**[1:00:45]** OK.

**[1:00:47]** So.

**[1:00:50]** There are various nodes and each nodes has their own specific function.

**[1:00:57]** Okay, for example, here this is a set variable node. Okay, then this is call agents, teacher, teacher agents, set variables, then the conditions, okay, then there's a end node, there's a send message node, this is a go to node, so move to the.

**[1:01:17]** Next note.

**[1:01:20]** Okay.

**[1:01:23]** So.

**[1:01:26]** Workflows basically allow you connect the agents, okay, tools, conditions, actions in into a structured process.

**[1:01:40]** Okay, so without writing the complex orchestration code.

**[1:01:48]** Okay, so you can build a a I driven business automations without complex orchestrations code.

**[1:02:00]** So there are basically a workflow pattern.

**[1:02:04]** Okay, one is the sequence here.

**[1:02:07]** Now in sequential, as you can see right here, steps basically run in a fixed order like step one, step 2, step 3, and then the output and each steps basically it pass its results to the next step.

**[1:02:25]** Okay, the output of a step 2 would be the input for step 3.

**[1:02:29]** Okay, so this is useful for predictable processes.

**[1:02:34]** Okay.


## Module 2 (continued) — Agent Framework & Orchestration  `[1:02:36]`


### Agent workflows & human-in-the-loop  `[1:02:36]`

**[1:02:36]** Then next one we have is a human in loop. Okay, here the workflow pause for human approval or input before continuing. It balance the automations with oversight.

**[1:02:53]** Okay, so here it started and it will wait for the approval. Okay, if the once the approval is given, only then it will continue okay to the next step.

**[1:03:06]** Okay, so for example.

**[1:03:11]** So let's say you are creating an agents for requesting the leave. Okay, so now the you have basically an approval. You need the approval of the manager. So manager must approve it your leave okay before it is.

**[1:03:30]** Before you basically a leave is provided to you, right? Or you get an email confirmation.

**[1:03:37]** Okay, so this kind of workflow patterns is used when decisions involves risk or any compliances, approvals, or any financial impact right where you need the human in the loop.

**[1:03:53]** Now the 3rd pattern is basically a group chat.

**[1:03:57]** So in group chat, what happen is there are basically a multiple specialised agents those collaborate dynamically.

**[1:04:06]** Right, they control the SIFT based on the context, allowing the agents to build on each other's output.

**[1:04:15]** Okay, so for example, let's say you have one agents which is used to analyse the data, right? Another agents basically to check the policy, okay? Or maybe another agents that basically write the final response.

**[1:04:32]** OK, so you have a orchestrator basically which coordinates between this, this specialised agents. So these are basically useful for complex tasks like where you have different agents, they contribute their expertise.

**[1:04:54]** Okay, so it's like a group chat over there like you multiple agents come in, specialised agents come in right and take the decisions okay and gets you the final output.

**[1:05:11]** OK, so these are the basically the workflow pattern, sequential, human in loop, and group chat.


### Core components of a workflow  `[1:05:20]`

**[1:05:20]** Moving further, what are the core components of the workflow?

**[1:05:26]** Okay, now they're basically executor.

**[1:05:31]** Edge and the event. So these are the 3 core components of a workflow.

**[1:05:37]** Executors, these are basically the main workers in the workflow.

**[1:05:42]** Okay, these are basically which performs the actual work. So each executor receive input, perform actions, and pass the output along. Okay, it is driving the workflows towards its goal. So executor can represent the AI agents or a custom logic component.

**[1:06:02]** It is clear.

**[1:06:04]** Okay, so like one executor may lead the customer request, another may check the company policy.

**[1:06:12]** OK, another major generate the final response, right? These are basically the executives are basically they represent the AI agents or custom logic component.

**[1:06:23]** These are basically the main they perform this performs actual task. Then there are basically edge.

**[1:06:31]** Okay, now this basically decide like how the workflow move right from one executor okay to another executor. It is like it control the path of the executions. Okay, like traffic police.

**[1:06:51]** Okay, so then we have here there are different type of edges like direct, conditional, switch case, fan out, and fan in. Direct means one executor feed directly into the next in the sequence. Conditional means triggers only when a conditions is met, otherwise skipped.

**[1:07:10]** Switchcase means.

**[1:07:12]** Okay, it route the route the route to different executors based on the predefined conditions.

**[1:07:20]** Okay, so it route the workflows to different path based on the conditions fan out, it sends the single message to multiple executors simultaneously.

**[1:07:31]** OK, fan in means it combine the messages the result from multiple executors into one final step.

**[1:07:40]** Okay.

**[1:07:42]** So this is the next component. Then comes the events. So events are basically the these are nothing, but these are the signals generated during the workflow executions, okay. And this basically help to track like what is happening inside the workflow, okay, for example, workflow start events.

**[1:08:03]** Workflow output events, workflow error events, executor invoke events, executors complete events, request info events.

**[1:08:13]** Okay, for example, whenever an external users login, okay, and this is basically when the executive finished the work, this is when the executive start the, you know, processing the task, right, and so on.

**[1:08:27]** Okay, clear. The executor is basically which performs the which do the work, okay, which performs the task, okay. This basically decides the flow, okay, and it will basically help you understand like what is happening okay in the workflow.

**[1:08:47]** Okay, so together these 3 components help you build.

**[1:08:52]** A structure and a reliable AI workflow, okay, which can be which can be traceable.

**[1:09:04]** Clear.

**[1:09:09]** OK.

**[1:09:12]** So build a workflow in Microsoft Foundry.

**[1:09:16]** Okay, let's go through this.

**[1:09:23]** Exercise OK, build a workflow in Microsoft Foundry now over here.

**[1:09:33]** So in this exercise, you will use the Microsoft Foundry portals to create the workflow. Workflows are UI based tools that allow you to define the sequence of actions involving the A I agents. You'll create a workflow that helps resolve customer support request. OK, and this is the workflow overview.

**[1:09:53]** Right, and to create a work workflow, right, you first create your agent.

**[1:09:59]** Okay, you create your project first, right? And then...

**[1:10:04]** Then create a customer support tries workflow.

**[1:10:09]** So for this.

**[1:10:22]** Okay, now once you are here right in the in the agent section, just next to the agent, you can see workflows.

**[1:10:32]** OK, delete the existing one, enter the workflow name.

**[1:10:54]** Okay, so workflow helps you to automate task and streamline the processes.

**[1:11:01]** Okay, so you can start, you can see over here sequential, human in loop, and the group chat. So we'll be starting with the blank.

**[1:11:10]** Okay, and then we'll set the name.

**[1:11:17]** Which is a support ticket.

**[1:11:33]** Let's provide the enter the workflow name.

**[1:11:43]** OK.

**[1:11:54]** OK, now.

**[1:11:57]** Now after this.

**[1:12:02]** Just a minute here should be the name. Okay, sorry, this is the name will give.

**[1:12:27]** Let's see for.

**[1:12:31]** Renaming it.

**[1:12:34]** Swint.

**[1:12:38]** Okay, let's delete the workflow. Go back here.

**[1:12:48]** OK, let me create new one blank workflow and.

**[1:13:03]** Save.

**[1:13:06]** Save it.

**[1:13:22]** OK, so now we are getting the user user interface out there. Now this is where we will be creating the workflow, right? And what is the workflow over here, right? That we need to collect the incoming support ticket, right? So work workflow start with the predefined arrow customer support ticket.

**[1:13:41]** Support customer support issue.

**[1:13:45]** Okay, each items in the array represent individual support tickets submitted to the contour so pay process tickets one at a time. Okay, classify each tickets with an A I agent. Okay, so nowhere comes the in the workflow we will be using the A I agents which will decide basically what that ticket is all about.

**[1:14:05]** Right, it is for billing, okay. The issue is basically classify the ticket regarding the billing technical or general okay along with the confidence score. So it handles the uncertainty with the conditional logic, right? If the confidence score is below a define.

**[1:14:24]** Threshold the workflow recommend additional info for that ticket.

**[1:14:30]** Okay, route based on issue category. So billing issues are flagged for escalations and removed from an automated resolution path. Technical and general issues continue through the automated handling. Okay, so if there is any billing issues out there right that would be flagged for escalations.

**[1:14:50]** OK, and that basically it is removed from the automated resolution part.

**[1:14:55]** For technical and general issues, right, it will go through the automated handling. Okay, then generate a recommended.

**[1:15:00]** How is the confidence score getting creative? Just to understand. How is this confidence score getting creative?

**[1:15:05]** Sorry.

**[1:15:12]** Do we have any place we have a logic behind the confidence to creation?

**[1:15:12]** OK.

**[1:15:20]** It is basically by the A I agents actually the model this model has been trained. So whenever it make the predictions out there when it is classified. So how confident is that whatever it is basically getting you like whether it is a billing, whether it is technical or general, so it will tell you basically how confident is that model.

**[1:15:41]** That this ticket is basically for billing or technical or general. So this confidence score basically depend on the model itself.

**[1:15:52]** Okay, it is on the model model itself and these are basically the pre trained models, okay. And to increase this confident, right, if you want to increase this confident out there, then we have to train our own models out there like, you know, providing, providing more, you know, data for.

**[1:16:12]** Training with similar kind of classifications.

**[1:16:19]** Okay.

**[1:16:21]** Okay, now for example, I'll just give you an example of, let's say.

**[1:16:28]** We have 3 fruits.

**[1:16:34]** Apple, orange, and banana.

**[1:16:38]** OK, So what I did I use I'll have taken a number of here. Let me go to yeah.

**[1:16:49]** Okay, so lets say.

**[1:16:56]** You have 3, you have a fruits, you have taken 10 images of mango.

**[1:17:03]** 10 images of banana and 10 images of, let us say, orange. OK, so you take this images and you train your AI model. OK, now once you have your model, OK, now what you do is.

**[1:17:22]** Right, you provides the image of mango now.

**[1:17:27]** Okay, and while training the data, the mango, the image of the mango, most of the image of the mango were yellow.

**[1:17:37]** Okay, now what happen if you provide similar like yellow yellow mango, right? So the confident of the model would be high. Okay, let us say 98%, okay, that's basically the probability out there. So it is a 98% probability that the...

**[1:17:56]** this image of a mango mango, okay, this image of a mango, this fruit is basically this image is a mango. Okay, so it will classify it as a mango, 98%.

**[1:18:13]** Okay, so mango 98%, orange 2%.

**[1:18:22]** Got it. Now what happened? Instead of yellow, right? You this time you have basically yellow and green.

**[1:18:32]** Yellow and green or red, yellow and red. So mango has basically some part yellow and some part red. So now what happen is if you provide this to the model, OK, then the model the confident for the model, the confident score of the model will reduce to like 95 now.

**[1:18:52]** Okay, 95 and maybe for orange it will increase to 5%.

**[1:19:02]** Getting it now what I have to do, okay, for my this scenario, I have to basically train this, train this model with all the different kind of mango, right? Different variety of mango, different colour, different shape of.

**[1:19:21]** Mango right? I have to collect like thousands of mango images, okay. And when I train it, so now I provide any type of mango, any variant of mango. So it will able to, it is more confident, the model is more confident to predict.

**[1:19:41]** OK, that this image is of mango.

**[1:19:47]** Okay.

**[1:19:49]** So now same over here like a I agents, right? You're using the A I agents, okay. And this A I agency is using the A I models, okay. So that models basically give you the confident confidence score and then you'll basically.

**[1:20:08]** Sets the threshold.

**[1:20:11]** Okay, and then based on that threshold, right, you can lets say for example, okay, there's something like I want for medical, so I need high confident models out there like the model should be able to provide high confidence score, okay, but if I am basically using it for general.

**[1:20:29]** Applications where I need to detect various products in the industry right then maybe like I am not, I don't want the high confidence score in that scenario.

**[1:20:44]** Okay, is it clear the confidence score?

**[1:20:51]** Yeah. Thank you.

**[1:20:54]** OK.

**[1:20:58]** So this is basically the workflow overview, right? And to make this workflow right, Microsoft Foundry basically provides you okay this UI interface. Okay, now you started over here, right? And then let's go here. Okay, so next we will set a variable.

**[1:21:17]** Support ticket. So we'll click on node, right? And you can see over here like agent. You can call the agents in the workflows to complete the task. You can set variable, reset variable, pause value and converting like one type to another, right? You can control the flow here.

**[1:21:39]** With the conditions, OK, maybe somewhere you need to send the message, OK, message users with the reply or ask a questions straight from the users and then end the workflow. So sets a variable.

**[1:21:58]** Then you sets the variable new variable should appear, give the variable name support ticket so which is.

**[1:22:10]** Support ticket.

**[1:22:15]** OK, let's give the value so the value would be this one.

**[1:22:24]** Okay. and.

**[1:22:34]** Okay, so API return 403 error when creating invoice, but our API key hasn't changed. Is there a way to export all invoice as a CSV?

**[1:22:46]** Twice for the same invoice. That's right, my customer is also saying to receive. Can someone fix this? Okay.

**[1:22:57]** Great. And then further we can go and we can create a for each node to process each support ticket in the array.

**[1:23:08]** Okay, then we invoke any agents to classify the.

**[1:23:14]** Dikhe.

**[1:23:21]** Okay, nowhere when you configure that, you need to configure the agent setting, right? You pro you select the parameters, okay, like temperatures and top P.

**[1:23:40]** Then you'll add a response form it.

**[1:23:43]** Okay, so this would be the response out there. Category, category response out there.

**[1:23:52]** This is basically the format.

**[1:23:55]** And then you provide the instructions to your agents.

**[1:24:00]** OK, classify the user problem descriptions into exactly one category from the list below. OK, and also provides the confidence score from zero to one.

**[1:24:02]** Hello.

**[1:24:06]** Yeah.

**[1:24:11]** OK, billing.

**[1:24:15]** Technical.

**[1:24:17]** General.

**[1:24:19]** OK, and important rules over here.

**[1:24:22]** Okay, so questions about exporting, viewing or downloading invoice are general, not billing. Billing only applies when money was charged, refunded or paid incorrectly.

**[1:24:36]** Okay.

**[1:24:38]** Then over here you will provide the input, set the input message field to local dot current ticket variable and then save the agents output message as create a new variable name. OK, tries output text.

**[1:24:55]** Then you will add here handles the low confident classifications right where you have confident greater than 0.6 recommend additional info for low confident tickets.

**[1:25:11]** Okay, then you route the ticket based on the category. So based on billing, you will escalate billing issues to the human support team. Then for generate response. So over here you provide this to your agents again.

**[1:25:31]** Okay, so this is the resolutions agent resolution agent. So we provide instructions, your customer support resolution assistant for Contoso pay guidelines. It provides tone output.

**[1:25:45]** Right.

**[1:25:47]** And then you can previews the previews the workflows.

**[1:25:51]** Right, okay.

**[1:25:56]** So, Copilot says thank you for reaching out right reaching out about this one. This error typically indicates a permissions or access issues. Please ensure that your ABI key has been has the necessary permissions for invoice creation and that your request is being sent to the correct end points.

**[1:26:16]** If the issue persists, try regenerating your API key and updating it in your indication to see if that resolve the issue problem.

**[1:26:25]** Correct. And then you can use your workflows in your client applications. So you create a client applications by using Visual Studio and then you will integrate this workflow into your applications. Right here you define over here.

**[1:26:44]** Right, you specify the workflow over here, OK, Contoso customer support trials workflow that you have created connecting to your project. OK, first you will be creating to the project project endpoints OK in the dot ENV variables and you install libraries here.

**[1:27:03]** Define the Python code and then after that you can test it in your client applications as well.

**[1:27:16]** Okay.

**[1:27:20]** So also let me share this.

**[1:27:40]** Okay, let's.

**[1:27:46]** For the module one as well. Okay, sure.

**[1:27:51]** For model one, let's go to.

**[1:28:05]** Okay, so these are basically for the module one, right? All the exercises.

**[1:28:24]** Okay, now lets take questions. 2 questions are there. Which type of node in a Foundry workflow is used to invoke an AI agent? Is it logic, logic node, it is an agent node, or it is a data transformations node?

**[1:29:02]** Yes, okay, yes, that's agent note, right? So if your workflow need and need to invoke any agent, then you use the agent note out there. Okay, question 2.

**[1:29:21]** What node type would you use to handle multiple items in a workflow without duplicating the node?

**[1:29:31]** Multiple items in a workflows if else for each or send message node.

**[1:30:06]** Okay, yes, everyone agree with the B right for each node. Okay, so you will use the for each node, let's say, when you need to process like multiple items like, you know, one by one without creating separate repeated.

**[1:30:27]** No, if you have 100 customer feedback message instead of creating 100 separate agents node, you use for each node and you look through the each feedback and then you process them one by one.

**[1:30:47]** Okay.


### Develop agents with Microsoft Agent Framework  `[1:30:49]`

**[1:30:49]** Now let's talk about here develop and a agents with Microsoft Agent Framework. Now, Microsoft Agent Framework is basically the developer framework.

**[1:31:00]** Okay, it's a...

**[1:31:04]** Developer.

**[1:31:06]** Framework OK, which is used to build an AI agents.

**[1:31:13]** Air agents by writing code.

**[1:31:20]** Okay.

**[1:31:23]** So, Microsoft Agent Agent framework.

**[1:31:30]** You can say...

**[1:31:37]** It basically helps the developers to provides the code based, code based structure.

**[1:31:47]** To build the agent.

**[1:31:55]** Okay, now for example, let's say you want to build a travel assistant.

**[1:32:02]** Agent.

**[1:32:04]** OK, travel assistant agents now using using Microsoft agent framework, we can define the model.

**[1:32:13]** We can define the instructions.

**[1:32:16]** Okay, we can define tools, we can define the workflows.

**[1:32:26]** Okay, so you can use for models like you will use the GPD models or any other foundry, Microsoft Foundry models, you provide the instructions, tools like calling the MCP tool or any APIs.

**[1:32:46]** Okay.

**[1:32:48]** So you have basically the controls over here with the code, you have the complete controls into your agent, yeah agents.

**[1:33:01]** Okay.

**[1:33:05]** Now we have also known as the Azure Azure Foundry.

**[1:33:11]** Agent service.

**[1:33:17]** Okay, so Azure Foundry Agent Service, it is basically a managed service. Okay, managed managed platforms by Microsoft for hosting.

**[1:33:30]** For hosting.

**[1:33:32]** Deploying.

**[1:33:35]** Scaling.

**[1:33:38]** Securing.

**[1:33:41]** And.

**[1:33:43]** Monitoring your agents.

**[1:33:50]** Okay, so this is basically a Microsoft Foundry agent service. So behind what we have previously the agents we which we have built right, that is basically on the Azure Foundry agent service which is hosting which is used for deploying.

**[1:34:09]** Right, it is managing all this scaling, security, monitoring your agents.

**[1:34:15]** Okay, now by using Microsoft agent framework right developers can build their agents right through code and they can host this agents okay in the Microsoft Foundry agent service.

**[1:34:32]** OK, so this is basically used to build to build your code in, build your agents in code, right? And then you can basically deploy and run your agents in the Azure Foundry Agent service. Is this clear?

**[1:34:52]** Now, Microsoft Agent Framework, what are the core component?

**[1:34:57]** One is the agent itself.

**[1:34:59]** Okay, it's basically the main main AI worker.

**[1:35:04]** Then.

**[1:35:06]** Right, agent consistent interface enabling multi agents orchestration supports function calling, multi turn conversations, structure output, and streaming responses out of the box. So it receives the input, you know, use the model, right? Follow the instructions, call the tools.

**[1:35:27]** And return the final answer. The second core component of agent framework is the chat provider.

**[1:35:36]** Okay, chat provider abstraction for connecting to AI services under a common interface. All providers are interchangeables through the base agent abstractions.

**[1:35:52]** So.

**[1:35:54]** Basically, chat provider connect the agents to the AI model service.

**[1:36:02]** Okay, so they basically act as a abstractions layer so the same agents logic can work with different model provider. You can connect the agents to Azure Open A I or you know any other you know models, Microsoft models or.

**[1:36:20]** Lama without rewriting the full agents logic.

**[1:36:25]** Okay, so it abstract for connecting to the AI services.

**[1:36:31]** Then we have a functions tools, right? These are basically the custom functions that your agents can call, right? Then extend the agents capabilities. Built In tools, these are ready ready made use ready made tools okay provided by the service.

**[1:36:50]** Ready to use without additional configuration. Conversations managements is basically this manage the conversations history where it and the sessions context. So for persistence conversation context across multiple interaction, so conversation managements components is used.

**[1:37:11]** And then the workflow orchestration, this basically helps to coordinate the complex task which involves like multiple, multiple steps or multi agents, multi agents collaborations, human in loop supports the agents can hand off the task or participate in.

**[1:37:31]** Group conversation, so such kind of scenario, the work workflow orchestrations in is used.

**[1:37:41]** Okay, so Microsoft Agents, basically these are components which is used to create your agents out there, okay, to build your agents using Microsoft Agent framework. These are the components for this agents, chat providers, functions tools, built in tools.

**[1:37:59]** Right conversations management and the workflow orchestration.

**[1:38:06]** Okay.

**[1:38:10]** Now create an AI agents. What is the process here? Okay. What are the steps to create an AI agents using Microsoft agent framework? Okay.

**[1:38:26]** So first, you create a Microsoft Foundry project. Okay, so you're creating an EI agents with the Microsoft Agent framework with Microsoft Foundry. So you create a Microsoft Foundry project, okay, then you will add the project connection string to your Microsoft Agent.

**[1:38:46]** Framework application code.

**[1:38:50]** Okay, so your Microsoft Foundry project basically it contains the models, agents, okay, tools, resources, okay, then you add the project connection string to the agent framework application code.

**[1:39:10]** You will set the authentication credentials with the Azure CLI credentials, okay, which is used to access the foundry project, okay, you will use the Azure CLI credentials, connect to your project client.

**[1:39:30]** With the Azure OpenAIResponseClient class.

**[1:39:36]** Okay, so it will create a project client using Azure Open a I response API class and then right you will create an agent instance with the client okay instructions and tools that you want to use.

**[1:39:58]** OK, so you have client instructions, tools, you can configure the behaviour.

**[1:40:11]** Okay, so this is basically the steps of creating an AI agents using Microsoft Agent framework in Microsoft Foundry.

**[1:40:21]** So these are same like built in tools, we have code interpreter, file search, okay, and the web search. We have talked about this custom functions tool, okay, custom functions tool. These are the functions that you can create in your own application code.

**[1:40:41]** OK, by defining the Python functions and decorating it with the tools decorator, create your tool by defining a regular Python functions with proper type annotations and pass your custom functions to the chat agents during creations using the tool parameter. So once the tools are registered, the a I agents automatically select and orchestrate the.

**[1:41:02]** Appropriate tool based on the user request without requiring the human manual interventions.

**[1:41:11]** OK.


### Hands-on lab — Agent Framework  `[1:41:15]`

**[1:41:15]** So this is the hands on lab, okay, to develop the Azure A I agents by using the agent framework. So first here you will install the Microsoft A I toolkits, foundry toolkits in Visual Studio code. Then you will deploy the model, okay.

**[1:41:35]** Then you will clone the starter code repository and you write the code for an agents app, right? And then you run the app. So if you go here.

**[1:41:48]** To double up the so this one agent framework.

**[1:42:00]** Yeah, develop Azure AI chat agents, the Microsoft Agent Framework SDK.

**[1:42:06]** Okay, so deploy a model, right? Then clone this starter code repository.

**[1:42:13]** Right, install the required SDKs.

**[1:42:20]** Right in the from the requirements dot txt.

**[1:42:24]** And then further, right, you are using the agent framework right from agent framework, import tools agents as your open AI response clients, right? And then you're creating a tool functions for the email, email functionality.

**[1:42:41]** Okay.

**[1:42:45]** And then you're creating a client and initialise an agent, okay, with the tools and instructions. So this is where you provide the instructions to your agents, then you provide the tools.

**[1:42:58]** Okay, so you create a client.

**[1:43:05]** OK, here you provides your deployment name, project, project endpoint. So you're taking this from.

**[1:43:14]** You're taking this from your dot in V in V file out there, right? Then use the agents to process the expense data.

**[1:43:25]** And you can test it submits an expense expense claim.

**[1:43:31]** Okay, the agent should have composed an email for the expense claim based on the data that was provided.

**[1:43:38]** Okay.

**[1:43:46]** Okay, so this is how to develop a Azure A chat agents with the Microsoft Agent framework.

**[1:43:55]** Okay, let's take 2 more questions here.

**[1:44:01]** Would there be questions for writing code in the exam? Yes. So there would be some of the questions. Okay, now for example, over here, okay, some of the questions would be over there like, okay, for example.

**[1:44:20]** Just give you one example.

**[1:44:26]** Okay, so maybe in right in exam, so this part would be missing. So you have this piece of code.

**[1:44:35]** Right, you have this piece of code, okay, and this part would be missing out there. Or maybe you have tools here and then, right, this part would be missing. So you have scenario, okay, you have a scenario and then this part would be missing out there and then you have a drop down here and you have 33 or 4 options.

**[1:44:55]** From the drop down and you have to choose one.

**[1:44:59]** Okay, so you don't need to write the code, but yes, so understanding of the this code is important. Understand understanding of this is important so that you would be able to fill up like whenever you getting something like okay, some part is missing over here. For example, if this is missing from here.

**[1:45:18]** Right, and then you have given like 34 options, so you'd be able to select the right options from the drop down.

**[1:45:26]** Okay, but you don't have to write code on in the exam.

**[1:45:32]** Okay, let's take question one.

**[1:45:36]** So what are the key steps to create a Microsoft Foundry Agents using the Microsoft Agent Framework?

**[1:46:18]** Okay, let's see. Yes, that's true.

**[1:46:23]** Okay, so Azure AI agents client, right, which connect your code to Microsoft Foundry Agent service, then instructions, which basically is used to define the behaviour of your agents.

**[1:46:41]** Okay.

**[1:46:44]** With instructions and tools and agent threads, which is used to store the conversation state and messages, correct?

**[1:46:54]** Question number 2.

**[1:46:57]** Which component in Microsoft Agent Framework manages conversation state and store messages?

**[1:47:18]** Simple, right?

**[1:47:20]** It's a agent threat, right? Agent threat manages the conversion state. It is store the message exchanged between the user and the agents, so the so that the agents can continue the conversations with the with the context.


### Orchestrate multi-agent solutions  `[1:47:42]`

**[1:47:42]** OK, next one is orchestrate a multi agent solutions using the Microsoft Agent framework.

**[1:47:49]** Okay, multi agent solutions means like multiple specialised agents work together to complete a task. Okay, so you have a agents first specialised task there and you have a.

**[1:48:08]** Complex, you have a complex task which requires multiple agents to work together, right, and provides you the output.

**[1:48:20]** Okay.

**[1:48:22]** So.

**[1:48:24]** Multi Agent solutions. Now, for example, let's say.

**[1:48:30]** Shoa, sorry to interrupt you. I have one doubt actually, sorry. So it is regarding our agentic development kit actually. So the way we build the agent right using the code base. So do we need to run that particular code every time like in our application or just one time?

**[1:48:34]** Mhm.

**[1:48:50]** Activity to build the agent using as the agentic development kit like.

**[1:48:57]** Agentic Development Kit.

**[1:48:59]** like our development framework, agent framework.

**[1:49:05]** Okay, Microsoft agent framework you mean, right?

**[1:49:08]** Right, correct.

**[1:49:10]** Okay.

**[1:49:12]** Microsoft Agent Framework.

**[1:49:16]** Okay, what happened is basically now once you once you develop right in your development machine and then after that you are going to basically host it.

**[1:49:28]** Okay, you will host in the Microsoft agent service, okay? And then you make the peoples available to you, okay? So it is like if you have to run on your machines, then you have to start it, okay? And then it basically goes in loop where it basically asks for the prompt.

**[1:49:49]** Until you exit there, right? If you perform the hands on lab, okay, there also you have done that, right? You run it once, right? And it goes on like user user prompt right until we stop the we stop the code.

**[1:50:04]** So is there any way to publish this entire code base to that agents? Sorry, to Microsoft Foundry Agent service? Like do we need to do any extra step after testing and building that agent locally?

**[1:50:18]** Yes, to make it available, right, you would need to basically host it in the agent framework.

**[1:50:31]** Sorry, in Microsoft agent service.

**[1:50:37]** Okay, so there should be some command that we have to execute or maybe we have to create some package artifact and we have to run some command, right? I believe it is like a dockerization or something we have to do it.

**[1:50:48]** Yes, yeah, it would be, it would be something like you can do using the like toolkits. Okay, so like for example, you can use Foundry toolkits similar to that you have a toolkits through which you can directly create and then you can host it.

**[1:51:09]** In the Microsoft agent service.

**[1:51:12]** Okay, yeah.

**[1:51:17]** Okay, thanks. thanks.

**[1:51:18]** Yeah, you're welcome. Okay, so now basically, previously we were talking about like a single agents, right? So we're talking about single agents, right? This agents to do this thing, this agents to do this things, right? And agents, basically, we talk about instructions, we talk about tools, we talk about knowledges.

**[1:51:37]** Right. But if you have a complex task, right, then comes the multi multi agent solutions, OK, we use multi agents orchestrations when the task is complex and it need a different skills.

**[1:51:57]** Okay, so how you gonna manage right to how you gonna manage the coordination between those agents, you know, or how you gonna combine the a I agents' functions and workflows?

**[1:52:11]** So Microsoft Microsoft Agent Framework basically provides you the workflow, workflow orchestrations to connect the agents and tools together.

**[1:52:24]** Okay.

**[1:52:26]** So now you can see this pattern here. Okay, this is a concurrent orchestrations.

**[1:52:34]** OK, concurrent orchestrations means multiple agents work at the same time in parallel instead of like one by one. So run the task in parallel, independent agents execute simultaneously, then results are merged at completions and this is optimised for the speed.

**[1:52:53]** Speed.

**[1:52:57]** Okay, so the user basically give one input, right? The same input would be sent to multiple agents.

**[1:53:07]** Right, each agents work independently.

**[1:53:11]** Connect and then the collector basically it gathers all the agents output and then the final results is created from the combined responses.

**[1:53:26]** Okay.


### Sequential & handoff orchestration  `[1:53:31]`

**[1:53:31]** Then next one is sequential orchestration. Okay, now here.

**[1:53:39]** The agents work one by one in a fixed order.

**[1:53:44]** User given the input agent A, agent one process it first, then output of the agent one goes to agents 2, output of agents 2 goes to agent 3, and then final result is produce.

**[1:53:59]** Okay.

**[1:54:02]** So maybe lets say this is agents for summarising the documents, this may be agent for translating the translating the summary, or maybe this is to basically QA agents which check grammar, accuracy, or completeness.

**[1:54:20]** Okay, then comes the group chat orchestrations. Group chat orchestrations is basically it means like multiple agents can work together in a share conversations like a team. Okay, so you have a group chat manager here, okay, the user.

**[1:54:40]** User give the give give the input, okay, the group chat managers receive the request and then this basically decide right which agent should respond next.

**[1:54:55]** OK.

**[1:54:57]** So.

**[1:54:59]** Then basically it this agent, the agent discuss, share ideas and they can build on each other response.

**[1:55:11]** Okay, and then the final final result is basically produce.

**[1:55:20]** OK.

**[1:55:23]** Say user ask, like, okay, should we launch this new product next month?

**[1:55:29]** Okay, so here basically you have various agents like marketing agents, engineering agents, and finance agents.

**[1:55:38]** Okay, so marketing agents now the group chat basically involved marketing agents checking campaign campaign readiness, customer demand, engineer agents basically check the product readiness, okay, any technical risk, the financial agents basically check for the budgets. and.

**[1:55:59]** And revenue then human basically they can like this is for review and approving approving important decisions. So the group managers control the conversations and decide who should speak next.

**[1:56:14]** Okay.

**[1:56:16]** And then provides the final result.

**[1:56:21]** Okay, so based on the discussions out there from the various agents out there.

**[1:56:29]** OK, now this is useful when the problems need multiple expert opinion.

**[1:56:37]** Okay, when the agents need to collaborate dynamically, okay, and you need brainstorming or reviewing things before.

**[1:56:51]** Before something taking decisions.

**[1:56:55]** OK, for brainstorming and synthesis, common conversations control shift dynamically.

**[1:57:05]** Clear.

**[1:57:07]** The next one is a use handoff orchestration.

**[1:57:11]** In han of orchestrations means...

**[1:57:15]** So here one agents transfer the controls to another. OK, clear the ownership per stage.

**[1:57:24]** Okay, let's say user give inputs to the agent A. Agent A handles the request initially, right? And let's say if the issue is technical, the agents A basically hand overs to the technical expert, which is agent B.

**[1:57:43]** And if the issue is related with billing, so it will basically hand overs to the agency for the billing issue.

**[1:57:52]** Okay.

**[1:57:55]** So and then.

**[1:57:58]** Right. And then the this basically the right selected specialise agents basically complete the task and result return the result.

**[1:58:11]** OK, clear.

**[1:58:17]** OK, now next thing, next one, next orchestrations and I guess this is the last one. So this is the magnetic orchestration. So magnetic orchestration is used for the complex open ended problems where we cannot define a fix you know, step by step workflows in advance.

**[1:58:39]** Okay, now generally, like the previous normal orchestrations we talk about, right, we define the flow like step one, step 2, step 3, right, and finish. But in magnetic orchestrations, the agents can self organise, they decide like what to do next based on the task, the progress of it.

**[1:59:00]** And the result.

**[1:59:03]** Okay, its.

**[1:59:10]** Collaborations, no fix existing solvers agents are self organised for complex over ended problems. Okay, now for example, the user give a task okay then orchestrator basically it create or update the.

**[1:59:28]** Task.

**[1:59:30]** Pleasure.

**[1:59:32]** Okay.

**[1:59:34]** So, task leisure basically track right fact to look up, fact to drive, educated guest assist task plan.

**[1:59:48]** Okay.

**[1:59:51]** So then comes over here, this is task ledger and then there is a progress progress ledger which check like what's the progress out there, like what's the what's progress has been made, whether the agents are stuck, okay, what are the next step should be or what should what should be done or who should speak or.

**[2:00:12]** What is the next speaker? Okay, next speaker instructions. Is progress being made?

**[2:00:19]** Okay, does the system basically keep on checking is the task completed?

**[2:00:24]** If yes, then it will return the final answer. Okay, if no, then it continue.

**[2:00:31]** Okay, task completed, yes. If no, okay, what's the progress being made?

**[2:00:39]** Right, it observe the agents, the agents work based on orchestration instructions, observes and act based on the orchestration instruction.

**[2:00:52]** Okay, now for example, magnetic orchestrations could be, lets say, the user says, analyse the customer feedback, identify the major issue, compare with the sales trend, and recommend the product improvements.

**[2:01:11]** Now the task is not simple. The system may need to inspect the feedback, summarise the complaint, compare with the sales data, maybe to it should ask with another agents to analyse the trend or may use an agents to.

**[2:01:29]** So just improvements, okay, or revise the plan if results are incorrect, right? So this is where the magnetic orchestrations are useful.

**[2:01:40]** Okay, so it basically allow the agents to plan, act, check progress, and adjust their approach until the task is complete.


### Hands-on lab — multi-agent solution  `[2:01:52]`

**[2:01:52]** Okay, so for multi agent solutions, there's a hands on lab, right? So this way you will develop a multi agent solutions with Microsoft agent agent framework.

**[2:02:07]** So you would start here with creating an AI agents with the framework.

**[2:02:14]** And over here.

**[2:02:17]** You're creating the agents like 3 agents out there, one is summariser, one is classifier, and one is the actions. Then you will create a sequential orchestrations here.

**[2:02:34]** Okay, so build a sequential orchestrations so workflow equal to screen shell, screen shell builders, add the following code, run and collect the output, add the to under the display output display output.

**[2:02:52]** Put and then you test it, right? So you can see over here, right? So you'd be getting over here this is the users like user feedback and then it summarise it, right, it classify it and it perform the actions. Okay, so 3 agents which is used over here, 3 agents sequentially first is summarise it, it classify it.

**[2:03:16]** And then it performed the action.

**[2:03:26]** OK, let's.

**[2:03:32]** Why do we need different agents? Cannot we have only one agents train on all?

**[2:03:42]** That would be, that would be difficult out there, right? Now, basically, we whenever we create an agents, we create an agents for a specialised task, okay, like my HR agents or my finance agents.

**[2:04:02]** Okay, so they are specialised for that particular task out there and sometime we have the complex work right where basically we need this agents to talk together right now. It is similar to like how in organizations we have different role.

**[2:04:24]** Okay.

**[2:04:26]** Now.

**[2:04:28]** Single Single agents agents are basically for specialised task, right? We don't create single agents for everything out there, and that would also be quite challenging when.

**[2:04:48]** When you have one one single agents, if something goes wrong, right, the complete it basically gets complete complete shutdown there, okay? But in case of in case of when you have multiple agents out there, right? So there is less chances out there because even if one agents fail.

**[2:05:07]** Right, other agents are working in this one. So it's similar to like how you have monolithic applications and you have micro micro services.

**[2:05:23]** Okay.

**[2:05:29]** Okay.

**[2:05:31]** Good question, thank you. Question number one, what are the steps? What is the first steps in Microsoft Agent Framework Unified Orchestrations workflow?

**[2:05:57]** Orchestration workflow.

**[2:06:08]** Okay, so most of you say is option A and some of you say option B.

**[2:06:18]** Ok.

**[2:06:20]** First steps in the Microsoft Agent framework unified orchestrations workflow.

**[2:06:38]** Okay, it's option B guys.

**[2:06:41]** Its option B, you define the agents and you describe their capabilities, okay?

**[2:06:53]** Basically, the framework must know, right, what which agents are available, what each agents can do, right, what tool each agents has, and when each agent should be used.

**[2:07:10]** Only after defining the agents, you can choose the orchestration pattern, right, and start the execution.

**[2:07:22]** Got it.

**[2:07:27]** Question 2: For brainstorming and collaborative problem solving among multiple agents, which orchestration pattern is most suitable?

**[2:08:03]** Turn everyone. Okay, we have mix over here. Most of you says A and that's true.

**[2:08:16]** Yeah, so group chat orchestration, so for brainstorming and collaborative problem solving among multiple agents. Okay, the group chat is used.

**[2:08:29]** Okay, so it's basically more on the collaborations and brainstorming, so it should be the group chats out there.


### End of Module 2 & break  `[2:08:42]`

**[2:08:42]** All right, so we have done here module 2, okay, we will take a short break, 10 minutes. Coming back, we will starting with module number 3, okay, and we will get into the language, natural language processing, and speech.

**[2:20:26]** Okay.

**[2:20:32]** OK, so yes, let's proceed further. OK, give me a second.

**[2:20:45]** Okay, so.


## Module 3 — Natural Language Solutions  `[2:20:56]`


### Introduction — text analysis concepts  `[2:20:56]`

**[2:20:56]** Okay, so let's proceed to our...

**[2:20:59]** What you 3?

**[2:21:12]** Yes, so I have the.

**[2:21:27]** Okay, so for module, this is the learning path. Okay, for module first, this is the learning path. For module second, this is the one. Okay, so now we can explorer here.

**[2:21:41]** Module Module 3.

**[2:21:57]** Okay, so the next module is develop natural language solutions in Azure.

**[2:22:04]** Okay, so here we would be focusing on the text and language.

**[2:22:13]** Text and language and computer speech.

**[2:22:18]** Okay, so this 2 workloads, we'll be focusing on this.

**[2:22:24]** Okay.

**[2:22:27]** So analyse text with the Azure Language in Foundry tools, right? Remember we have talked was the Foundry tool, right? Foundry Foundry tools and we have discussed the language in Foundry tools, speech, translator.

**[2:22:46]** Contain understanding, okay. and.

**[2:22:52]** So first we'll be exploring this tool, analyze, analyze text with Azure language in the foundry.

**[2:23:00]** Okay, so here Azure language will be exploring as your language in the Foundry tool.

**[2:23:09]** Okay.

**[2:23:12]** So.

**[2:23:15]** Basically, we will be focusing on natural language.

**[2:23:20]** Processing.

**[2:23:24]** Okay, so natural language processing, right? And in this specific part, we will be analysing the text.

**[2:23:36]** So.

**[2:23:38]** Assured Language.

**[2:23:43]** OK, now when we give a text to the Azure language, so it can answers questions like what language this text is written in.

**[2:23:55]** Okay, what language? So if you see there, okay, this is the Azure language.

**[2:24:01]** And when we provides here the text OK to this.

**[2:24:08]** Azure Language.

**[2:24:10]** Okay, as your language in the foundry too.

**[2:24:16]** So it will answer like it can answers like what language the text is written in.

**[2:24:24]** Okay.


### Sentiment, language detection, NER & PII  `[2:24:26]`

**[2:24:26]** Is the sentiment of this text positive, negative, neutral?

**[2:24:35]** What are the...

**[2:24:37]** Like this is.

**[2:24:40]** Sentiment.

**[2:24:43]** What are the important keywords or phrases?

**[2:24:49]** Okay.

**[2:24:51]** Or are there any people, places, or dates, products, organizations in this text?

**[2:25:03]** Okay, or does the text contain the sensitive personal information like person name, account, okay, email address, or phone number?

**[2:25:15]** OK, so for example, let's say a customer right.

**[2:25:21]** I visited Contoso Bank okay yesterday. I visited the Contoso Bank in Mumbai yesterday. Their staff was helpful, but the mobile apps was very slow.

**[2:25:37]** So, language Azure Language basically can analyse this text and it can return like what this text is return in. Okay, what is the sentiment of this?

**[2:25:51]** Okay, it's a mixed statement because it has a positive like the staff is helpful and it has negative because the mobile app are very slow.

**[2:26:06]** Okay.

**[2:26:07]** So the it will be mixed, it will be English and entities. In my statement, when I say I visited bank, so the entities would be like Contoso Bank, which is an organizations.

**[2:26:27]** Okay, then Mumbai, Mumbai is basically the location.

**[2:26:36]** Okay.

**[2:26:42]** Or yesterday, it's basically the date. Okay, so this is basically known as the entities name entity recognition.

**[2:26:55]** Okay.

**[2:26:59]** So.

**[2:27:01]** It provides you a prebuilt model for language detection, name, entity recognition, and PLL detection. This is prebuilt, prebuilt model okay that can analyse the text and extract the useful information automatically.

**[2:27:18]** Clear. I hope this is clear. Language detections, name entity relation and PLL detections. Okay, this identify the sensitive informations account, maybe lets say credit card informations or phone numbers, email address.

**[2:27:36]** OK.

**[2:27:42]** OK.

**[2:27:44]** So using the text analytics API.

**[2:27:50]** Okay, first we need to connect to the API.

**[2:27:54]** And for this, we require an endpoints and credentials. So here.

**[2:28:02]** Basically, the endpoint is the URL of the Foundry resource.

**[2:28:09]** OK, and credentials is the Microsoft Foundry project EPI key or Microsoft intra ID.

**[2:28:19]** Okay, so it basically support both.

**[2:28:22]** So you can either use a Pi key, this is secret key generated from the foundry project, OK. And basically the applications it can send this a Pi key, OK.

**[2:28:41]** So let's say this is a developers and developers want to use this text want to use this.

**[2:28:53]** Azure Language right for lets say language actions, name entity recognition or PLL detection. So they can basically make a call okay using the text analytics client. So it supports both like SDK and API to this endpoint.

**[2:29:12]** OK, in the foundry, so use the text analytics clients to call the appropriate functions for your task.

**[2:29:23]** Okay, so we use the text analytics client.

**[2:29:29]** Okay, and this client is available in Azure SDK, okay, and it helps you to call the correct functions for the task and in the request you send one or more text documents.

**[2:29:47]** Okay, and then we will basically gets a response a task specific collections of the result. So if you want to detect language, we will call the language detection function. If you want to extract the entities, we will be called the you know, name entity recognition function, okay.

**[2:30:07]** With the request, if you want to detect personal informations, we call the PLL detection functions.

**[2:30:14]** OK, and in the request, we basically contain one or more text documents that you want to analyse, and the response basically give your task specific collections.

**[2:30:27]** OK.

**[2:30:29]** Right, use like one one per documents.

**[2:30:33]** Okay, clear.

**[2:30:38]** Yeah.

**[2:30:41]** Okay.

**[2:30:45]** So how to use this?


### Text Analytics API  `[2:30:48]`

**[2:30:48]** Text Analytics API, so let's get to.

**[2:31:16]** Okay, now first we have to create a Microsoft foundry project, get the application file from the GitHub.

**[2:31:26]** Okay, and then we have to configure the application by installing the library and then we'll add the code to connect to the Azure AI language resource.

**[2:31:39]** OK, Azure Air language resource. So creating a client using the endpoint which is the foundry endpoints right and the credentials. So here in dot in V you provides with.

**[2:31:58]** So if you see there, right, this is application configuration file.

**[2:32:07]** Okay, and.

**[2:32:19]** Okay, now this is the code to detect the language.

**[2:32:23]** Okay, a underscore client dot detect language right and then the document.

**[2:32:31]** Right, then similarly add the code to extract the entities a dot client dot recognise entities okay a I underscore client dot detect language and similarly right a I client dot recognise PLL entities.

**[2:32:49]** Okay, and when you observe the output, you will basically able to identify. So there are basically some documents in the file itself.

**[2:33:09]** Okay, let's give a try because it does not take much time. So we already have a Microsoft Foundry project. Okay, and...

**[2:33:22]** Let me download this.

**[2:33:25]** Application file from the GitHub, so use the Visual Studio code.

**[2:33:43]** Let's go to view command palette, git clone.

**[2:33:51]** You come on palette, gear clone.

**[2:33:56]** Yeah, and then we'll enter a language. This will download the lab file.

**[2:34:11]** It's taking a while.

**[2:34:25]** If something is wrong, is it?

**[2:34:32]** Open again the Visual Studio code.

**[2:34:44]** Okay, so.

**[2:34:46]** Let's go to view command palette, get clone.

**[2:34:54]** Can you get some box here?

**[2:34:57]** Come on.

**[2:34:59]** Okay, it came over there, right? Git clone. Yeah, so you just enter.

**[2:35:08]** And.

**[2:35:16]** Come on.

**[2:35:49]** History name.

**[2:35:52]** Cancel.

**[2:35:59]** Yeah, it seems.


### Demo / lab — text analysis (Python)  `[2:36:05]`

**[2:36:05]** Okay, now we are getting here. Okay, so let's go to the maybe desktop AI 103 and select the repository. So it's gonna download that lab file.

**[2:36:20]** OK, I'll say open here.

**[2:36:24]** That's perfect. Okay, so we have the instructions, lab files, and we can see analyze analyse text, text analysis. We can see the foundry endpoint, so we'll provide foundry endpoints here. Then we have this review text here like you can see.

**[2:36:44]** This is the text reviews reviews text over here. This is what we are going to analyse using the Azure Azure language.

**[2:36:57]** Okay, so.

**[2:37:00]** OK, text analysis. Sorry, yeah, this one. So once this is done, right then after this.

**[2:37:14]** We'll get to the Python select interpreter.

**[2:38:17]** Okay, dependency is to install, so it will be a I.

**[2:38:25]** Yeah, language.

**[2:38:53]** Creating the environment.

**[2:39:10]** So it's installing the library, right? So what do you see here? You can install this way you can install requirements dot ext.

**[2:39:40]** Still installing the right, we can view from here requirement dot.

**[2:39:47]** Ext.

**[2:39:53]** So let's go to text analysis.py when an indicated terminal.

**[2:40:04]** Close this. OK, so now we have the Python, Python environments to work and now we will go to analysis dot Py. So we'll get some will import the namespace here.

**[2:40:16]** Let's provide the namespace Azure dot identity import default Azure credentials Azure dot IAI dot text analytics import the text analytics client okay and.

**[2:40:33]** Okay, so we are going to open this file, reviews file, reviews folders, and then we will basically go through them.

**[2:40:41]** Next thing we need to create a client using the endpoints.

**[2:40:48]** OK, so creating the client using the endpoint and over here the endpoints we need to provide it in the ENB. There's a Foundry endpoint, so there's a project resource name.

**[2:41:12]** The project endpoint.

**[2:41:20]** Let's save this perfect. Let's go to text analysis. So now we have a we have created a client using the using the endpoint right which is a underscore client and then we'll call this method to get the language.

**[2:41:38]** So.

**[2:41:40]** Copy this.

**[2:41:45]** Okay, and also for getting that credentials, we need to login. So first let's get the.

**[2:41:53]** Let's add the code too.

**[2:41:56]** Okay, let's basically see what's there in the in this one. So we'll read it through the code. Okay, read it through the code and we'll use the command easy login to login to the Azure portal. So we'll save this changes.

**[2:42:52]** That's right. From here, you get some options to login.

**[2:44:03]** There's issue with my studio code. Let's give a try again.

**[2:45:13]** Okay, slow.

**[2:46:58]** I'm gonna try the other way.

**[2:47:05]** Which is their environment is created, but...

**[2:49:03]** You can kill the terminal and you can create new terminal and try again maybe.

**[2:49:09]** Yeah.

**[2:49:30]** Okay, itself, I think there's a issue with my...

**[2:49:35]** Okay.

**[2:49:39]** Okay, let's give a try here.

**[2:49:42]** Once more try.

**[2:49:45]** Some issue with my Visual Studio.

**[2:49:49]** Code and so we have all sets here just we need to create environments to run the Python. So let's go here selector.

**[2:49:59]** And then we have, okay, let me.

**[2:50:03]** Let me create new one.

**[2:50:06]** And.

**[2:50:08]** Okay, space.

**[2:50:32]** Okay, perfect. Now we are in the environment.

**[2:50:36]** Right in environment, so let's go back here.

**[2:50:41]** We already installed the libraries and other things out there. and.

**[2:50:47]** OK, we need to log in easy log into the portal.

**[2:50:57]** So usually you should basically get a pop up over there to sign into the Azure and you need to authenticate by signing with your Azure credentials.

**[2:51:13]** Okay, yeah, so this is what we we're not getting previously out there, right? so.

**[2:51:23]** That sign in once you sign in right then it retrieve your tenant subscriptions for the selection. That's how you authenticating your you know your terminals to basically on the Microsoft foundry.

**[2:51:37]** On the Azure and select your subscriptions, right? That's the subscription that I'll be using. Perfect. Next here, let's go, let's run this.

**[2:51:57]** Okay, so now when you run it, right, so you can see here this is it read the file. So what we have to do is basically for each of the reviews, each of the reviews, we need to get the language so you can see over here. Okay, so we are not sure which language is this one. Okay, so we will basically use the this.

**[2:52:17]** This service to gets language to detects the language. So for this, we'll be adding here the get.

**[2:52:28]** Get language and whenever you're working with Python, keep take care of those indentations. OK, so we call this methods detect language OK and for the documents that we.

**[2:52:45]** We're going to upload the text file.

**[2:52:50]** Let me go and let me run this.

**[2:53:04]** First, let's save this.

**[2:53:07]** Then try again.

**[2:53:17]** Okay, unauthorised access token is missing, invalid audience is incorrect or have expired. Okay.

**[2:53:26]** So it is not able to call the call the service, so let's again go for easy login.

**[2:53:54]** Access token is missing.

**[2:55:10]** Should capture the token.

**[2:57:14]** OK.

**[2:57:16]** So it is not able to authorised into my Microsoft Foundry.

**[2:57:29]** Okay, let me take a look here when you start with the hands on. Okay, so once we once the authorization is done, right? That's basically the code over here for the authorizations. If we go to the right, this one.

**[2:57:48]** I think.

**[2:57:53]** Okay.


### Text analysis lab — review  `[2:57:56]`

**[2:57:56]** No taxation. So this is the one text analysis lab reviews requirements text analysis. So we've already created a client here right with the default default Azure credentials. Now this is what it will capture those tokens whenever you use the easy logins.

**[2:58:15]** And then it will use for all the requests that you're gonna make through over here. Okay, so I'll take a look into this like once, well, that's not.

**[2:58:29]** Troubleshoot over here because it's gonna take a while. Okay, so let's proceed further. So this will basically gets you the detected language, okay? And then also this next one right it will it is used to.

**[2:58:48]** Gets all the entities that has been detected in the text. This will give you any if there is any personally identifiable information like the name, address, phone numbers, all of this you can get from there.

**[2:59:06]** Okay.

**[2:59:15]** OK, thank you. I can see there are some recommendations.

**[2:59:22]** OK, so let's go for question number one. OK, how should you create an application that analyse news article and extract the key, extract key peoples, places, and dates that are mentioned for indexing?

**[3:00:01]** Okay, option C.

**[3:00:05]** Option C and that's true. Use Azure language in foundry tool to extract name entity. Okay, clear. Question number 2.

**[3:00:20]** You want to publish?

**[3:00:23]** Extracts from customer testimonials on a website. You need to remove personal detail from the text before publishing it. What should you do?

**[3:00:56]** Okay, option A. Yes, use the Azure language and foundry tools for fine and redact the PLL entities. Perfect.


### Text analysis agent with Azure Language MCP server  `[3:01:07]`

**[3:01:07]** Okay, now lets talk about here, develop a text analysis agents with the Azure Language MCP server. Okay, text analysis agent with Azure Language MCP server.

**[3:01:24]** Okay, now we have already talked about the AI agents.

**[3:01:29]** Okay.

**[3:01:32]** Now over here, what is Azure Language MCP server? Now Azure Language MCP server it exposed the Azure Language.

**[3:01:44]** Language capabilities.

**[3:01:48]** As a tool, As a tool that your agents can call.

**[3:01:53]** Okay, so through the MCP, right, Model Context Protocol.

**[3:01:58]** As you discussed, it provides a standard way for your agents or your A applications to connect with external tools, correct? Okay, so this just give me a second.

**[3:02:15]** Okay, so this basically get this can be offered through the Azure Language MTP server. So this Azure Language capabilities can be get get through Azure Language MTP servers for your agents, so you can make a text analysis agents with this.

**[3:02:34]** Okay, for example, maybe you want to create an agents which analyse the customer feedback and tell the sentiment what are the key peoples or what organizations or it whether it contain any personal informations.

**[3:02:54]** Okay, so.

**[3:02:57]** Azure Language MCP server, how does it how does it work? Okay, so agents AI agents use the Azure Language Mp servers to analyse the text. The user sends the prompts to the agents.

**[3:03:10]** Right, the agents basically determine the task, okay, to be performed.

**[3:03:16]** OK, and then the agent checks the available MCP tools to find the best match. Then agents call the selected tools through the MCP server, passing the relevant input text.

**[3:03:31]** Okay, so agents MCP server, MCP client MCP server. Okay, now MCP server process the request using the appropriate Azure language capability and then return the result. Then the agents combine the results into.

**[3:03:51]** Natural language response for the user.

**[3:03:57]** Okay.

**[3:03:59]** So.

**[3:04:02]** This is basically where the agents can use MCP server. Okay, through the MC server, they can call the appropriate Azure language capabilities, right, which is Azure language in the Foundry tool.

**[3:04:18]** Yeah.

**[3:04:21]** So here we can see, okay, using the Azure Language MCT server, first you have to create an agent.

**[3:04:29]** Okay, and then?

**[3:04:33]** Then we need to add the Azure Language MCP server tool.

**[3:04:38]** Okay, so for this we can see the tool catalog and in tool catalog we can see Azure Language in the Foundry tool.

**[3:04:51]** Okay, and then we will select the Azure Language in Foundry tool. So this will allow your agents to use the Azure Language capabilities like language detections, name entity, or PLL detections, right? And then we'll specify the agents instructions to select the tool.

**[3:05:12]** When appropriate.

**[3:05:14]** OK, this is important because we need to guide the agents on when to use the tool. OK, now for example, you can say you can give instruction saying like, OK, when the user ask to analyse text, detect language, or extract entities, use the Azure Language tool.

**[3:05:34]** OK. And then 4th is basically test the agents in a playground.

**[3:05:41]** Okay, where you can give a sample prompts, okay, then after that you can build a client applications that uses the agents. Okay, once the once you test it, you can connect the agents to the real applications.

**[3:05:58]** Okay.

**[3:06:02]** So if you go to the agents here, let's go to my...

**[3:06:08]** Agents, let's go to the build.

**[3:06:12]** Okay, so let's go to build and we have this, let's say.

**[3:06:17]** IT Support Agents and if we scroll down here, so...

**[3:06:26]** If we take a look into...

**[3:06:31]** Just a minute tool, right? And then you can click on this options, okay, browse all tools and then in the.

**[3:06:40]** And.

**[3:06:42]** Catalog right, you can see.

**[3:06:47]** Or we can search for.

**[3:06:52]** As your...

**[3:06:56]** Language.

**[3:07:03]** As your language.

**[3:07:06]** In Foundry 2, OK, so the MCB server enable AI agents to access as your language, right? Let me click on create.

**[3:07:16]** Okay, name remote MCP server endpoints foundry foundry resource name.

**[3:07:33]** EVS authentications, so enter the value foundry resource name.

**[3:08:44]** Let me take from the instruction.

**[3:09:10]** Okay, so let's provide this, create the language, right? And helping by analyzing the analyzing the text.

**[3:09:20]** So let's create an agent.

**[3:10:02]** 4.1 instructions.

**[3:10:06]** Then.

**[3:10:09]** Let's save.

**[3:10:11]** And let's ask here.

**[3:10:19]** Yeah.

**[3:10:22]** Let's make the foundry tool connections.

**[3:10:26]** Perfect. So it's there and.

**[3:11:18]** Okay, unique name for you too and remote MCB server endpoint.

**[3:11:31]** Okay, so it is not changeable then parameter.

**[3:11:43]** Authentication key based and API key.

**[3:11:49]** Yeah, once you update the parameter, then MCB server endpoint will automatically adjust that, so you can enter the value of project here, yeah.

**[3:12:05]** Value of the project.

**[3:12:13]** Okay.

**[3:12:16]** I think this is the foundry resource name that we can find in Azure portal. This is not a project name.

**[3:12:24]** Yeah, it's a foundry resource name. Actually, when you provides over here, that's gets added over there. So foundry resource name is this one.

**[3:12:37]** Just a minute, let me see my foundry to source name. I will go to right this one and the project name is a I development process 01. This is the one and this is the foundry project.

**[3:12:57]** And this is basically the foundry resource name, correct? So we'll I'll just copy from here and let me go and provides.

**[3:13:08]** Here, so foundry resource name.

**[3:13:14]** Okay, it's added, but let's see.

**[3:13:28]** Okay, actually this is the issue, right? So right, if you see here, if the key base key base authentication disabled by the policy in your Azure subscription, right? You can use the intra ID authentication to connect the agents to the Azure language service.

**[3:13:48]** OK, let me go click on connect.

**[3:13:53]** Okay, now this is basically the language Azure Language in Foundry tool which is added as an MCP tool, right?

**[3:14:03]** Okay, and then after that, right, we will basically modify the instructions.

**[3:14:14]** OK, you are an AI agents that assist users by helping them analyse text OK, use the language Azure language tools to perform the analytics task.

**[3:14:24]** Okay, and let's go ahead and let's save.

**[3:14:28]** And then over here.

**[3:15:04]** Data action. So there's some issues with authentication failed when connecting to the MCP server. Usually, it will prompt like approve of the language tool, but so we need to approve. You need to do it as because the prompt ask for 2 distinct it didn't ask over here.

**[3:15:42]** Okay, so now if we take look here.

**[3:15:53]** What counts as PLL?

**[3:16:07]** Specific date locations.

**[3:16:15]** Placeholder.

**[3:16:21]** Okay, so PLL replaced with the generic.

**[3:16:30]** With the generic placeholders here.

**[3:16:34]** Okay, and then here you're getting the legend for the reactions. These are basically the PLL detections.

**[3:16:47]** OK, so review the response which should identify any personally identified information in the article about the founding of the Microsoft and create a versions of the article with the this informations redacted, right? So this is what we are getting the output here once it is started using that too, OK.

**[3:17:06]** MCP Azure language MCP server.

**[3:17:11]** Clear.

**[3:17:13]** Okay.

**[3:17:22]** Can we use one model across multiple agents? Yes, you can use.

**[3:17:28]** Right, so you if you see for all the all the agents I've created over here, I'm using the same model.

**[3:17:36]** Okay, I'm.

**[3:17:36]** So do.

**[3:17:38]** So do they share any contextual data like across the agent or the learning happened only at the agent level, not at the model level like the instruction and the data we provide right at the agent level? Does it share across the model or not?

**[3:17:56]** Or sorry, does it across, does it share across the agent or not? Like if you use same model?

**[3:18:04]** No, it should not do it. Okay, that's not there, but I just need to check with the documentations. Okay, let me check this one as well, okay, with the agents one. And one more thing as over here, this course is like, it is a new course recently launched out there.

**[3:18:27]** Right in March, okay, so that's why I'm taking times over there to verify with the documentations out there even a lot of things is changing in the platform itself, right? So what are you what are you seeing right now? It's a new foundry portal. Okay, now before this there was basically other other portals out there if you.

**[3:18:47]** If you turn off this right, it will take you to the old foundry foundry portals, OK. And also lot of things out over here is the preview, OK, which means like things can go wrong over here because there's a preview and it's not used in the productions.

**[3:19:06]** Right, until it become public and generally available. Okay, so let me see that with the good questions here. Okay, let me go, let me go through and I'll let you know.

**[3:19:11]** Okay.

**[3:19:23]** Sure.

**[3:19:55]** Okay, so that's a good question. Thank you.

**[3:20:04]** Okay, let's take this.

**[3:20:11]** Question one.

**[3:20:14]** Okay, what is the primary role of the Azure Language MCP server?

**[3:20:23]** Is it?

**[3:20:29]** Okay, let's make it fast. We have, we have just 20 minutes out there, right? And we have 2 or 3 more topics to cover today.

**[3:20:41]** Okay, so yeah, that's true to expose Azure Language text analysis capabilities as MCP tools for the agents, right? Question number 2.

**[3:20:54]** How does an agent determine which Azure language MCP tools to call when processing a user prompt?

**[3:21:22]** Option B, yes, that's right. The agents may match the prompts, match the prompts to tool descriptions okay received from the MCP server.

**[3:21:34]** Okay, and then it will basically determine like which languages or MCP tools to call when processing the user prompts. Okay, next one here is developer speech capable speech capable generative a I applications.

**[3:21:51]** Okay, so speech capable model in Microsoft Foundry models. Okay, so here we are basically going to discuss how we can build and generate EPI application that can understand the spoken input and also response using speech. Okay, so normally.

**[3:22:11]** Whenever we are interacting with the AI apps, we are using the text, OK, but in speech capable AI applications, the user can speak naturally and the applications can also reply in the right voice. OK, so this create a more natural experience like you're talking to the virtual.

**[3:22:32]** Assisting.

**[3:22:34]** Okay, so.

**[3:22:38]** It basically there are 3 main path, right? First is speech to text, okay, converting the user spoken audio into the text, right? Second is generative A I models like once the spoken inputs become text, the application send it to the model. Okay, so this is like as your open a I model.

**[3:22:57]** And the model understand the request and generate the response. And then 3rd is basically text to the speech right after the a I models create the answer and the text format the Azure speech can convert that text you know response back to the spoken audio. Okay, so it is like.

**[3:23:16]** User speech, there was a speech to text, converts the audio to the text, then generate TBI models, create the response, right? And then text to speech converters basically, you know, it basically converts to the voice and then user basically, you know, gets the output.

**[3:23:36]** A spoken output.


### Speech — speech-capable models  `[3:23:38]`

**[3:23:38]** OK, so we have a specific speech capable models in the Microsoft Foundry model.

**[3:23:46]** Okay.

**[3:23:48]** So here you can filter and search for a generative AI model that can transcribe the spoken speech to text.

**[3:23:58]** OK, generative AI model that can synthesise the text to speech.

**[3:24:05]** Okay, so if the user says book a meeting with the sales sales sales team tomorrow, so the speech to text model convert the spoken sentences into the text.

**[3:24:21]** And then the AI applications or the agents can understand the request and take the actions. Okay, so if we take a look into the foundry, go to the discover, and then if you go to the model model catalog, right, and if you see based on the...

**[3:24:42]** Capability. Sorry.

**[3:24:51]** Okay, audio, audio generation.

**[3:24:57]** Okay, text to speech audio generations. So these are basically for audio.

**[3:25:04]** Audio generation.

**[3:25:15]** Okay, we also have models specifically for the text analysis. so.

**[3:25:21]** See model for text analysis, text classifications, okay, text generations, text to image, okay, text to speech, 4 modules for the text to speech or speech to speech to text. So if you see there are 6 model for speech to.

**[3:25:41]** Text here.

**[3:25:44]** Okay, speech to text.

**[3:25:49]** Okay, automatic speech recognition, speech to text. Okay, so these are these are all the all the models are there. These are basically the speech capable model in the Microsoft Foundry model.

**[3:26:02]** OK, so you can filter and search for generative a model that can transcribe speech to text and generative a model that can synthesise the text to speech.

**[3:26:18]** Using speech capable generative AI model.

**[3:26:23]** Okay, now for example, there are basically...

**[3:26:28]** Microsoft Foundry resource okay foundry model we have GPT 4O transcribe GPT 4O DTS.

**[3:26:39]** Okay, now.

**[3:26:43]** There are 2 main type of the speech models, okay? The first one is a transcriptions model, okay, which is this one.

**[3:26:53]** So this model basically it take the binary audio data.

**[3:26:59]** Right as a input.

**[3:27:01]** Okay, which means like actual audio, audio data, audio file, audio stream, okay, then model basically convert that speech into the text.

**[3:27:18]** Okay, then second is basically the speech synthesis model, which is like GPT 4 or TTS. So this model work in the opposite directions. So it take the text prompt as input and it basically responds the.

**[3:27:36]** Output as a audio.

**[3:27:40]** Okay, clear. So these are basically the 2 different type of models out there: transcriptions model and speech synthesis models out there. Okay, so transcription model convert audio to the text while speech synthesis model convert text into the audio and together they.

**[3:28:00]** They allow the developers to build a natural voice based generative AI applications in the Microsoft Foundry.

**[3:28:29]** So, is speech capable generative AI model?

**[3:28:34]** Okay, deploy a model so GPT 4O mini TTS okay and then GPT 4O mini so you'll deploy the speech generation model and speech recognition model okay then gets the application file from the GitHub.

**[3:28:54]** Right, and then you will create a speed generation app.

**[3:28:59]** Speech Generations app.

**[3:29:19]** You provides your input as my voice is my.

**[3:29:24]** Passport.

**[3:29:34]** Okay, so the code generate the requested speech and save it in a file, okay, and the code should also play the generated audio file.

**[3:29:47]** Thanks.

**[3:29:51]** So this one right, my voice is my password. So you converting the text to the speech out here, okay, for speech recognition.

**[3:30:03]** Okay, then you're creating a speech transcriptions app.

**[3:30:18]** Okay, file type is the audio audio file and over here.

**[3:30:27]** Okay, the code submits the output audio files to the model for transcriptions and then display the result.

**[3:30:37]** Okay.

**[3:30:39]** So the code also play the audio file.

**[3:30:45]** So here you're using basically there's both models out there for the speech to text or text to speech, both speech synthesis synthesis model, okay, and the.

**[3:31:02]** Speech, speech synthesis, speech to text, and text to speech.

**[3:31:14]** Okay, next let's take a look here. Questions.

**[3:31:21]** Question one.

**[3:31:26]** Okay, which model can you use to generate the text from speech?

**[3:31:35]** Text from your speech.

**[3:32:23]** Right, did you see there? Okay, so GPT 4O mini transcribe, so the option C is correct.


### Speech-to-text  `[3:32:33]`

**[3:32:33]** Okay, so if you see here, okay, there is basically speech to text model. So for a speech to text model, so out of that options, right, you can see we have the GPT 4O mini transcribe.

**[3:32:49]** Okay, that's the option C GPT 4 or mini transcribe. Now, what which model can you use to synthesise the speech from text? So previous was basically speech to text and this is text to speech.

**[3:33:10]** Question 2.

**[3:33:15]** If you see there, this was speech to text and let's see text to speech. We have 4 models for text to speech, so you can see okay, GPT 4O mini TTS, GPT 4O mini TTS.

**[3:33:34]** Okay, so option B is correct. Perfect.

**[3:33:40]** OK.

**[3:33:43]** Clear, so we can use those models out there right for the for our speech whenever you want to create an applications which enables like speech capable if you want to create a speech capable generative AI application.

**[3:34:03]** Then you will use those 2 models out there.

**[3:34:09]** Okay, next one is create a speech enable app okay with Microsoft Foundry.

**[3:34:17]** Speech enable app.

**[3:34:20]** So here we are talking about the Azure Speech in Foundry tool, similar to Azure Language in the Foundry tool, we have Azure Speech.

**[3:34:31]** Okay, Azure speech, so Azure speech in Foundry. So this is basically used for speech to text. Okay, Azure speech is basically used for speech to text, transcribe the spoken audio.

**[3:34:51]** Okay, text to speech, synthesise this speech.

**[3:34:56]** Voice Live, which is basically real time conversational speech interactions, and speech translation, which means multilingual translations.

**[3:35:07]** So it basically support.

**[3:35:10]** All of this now when we say voice live.

**[3:35:15]** Okay, speech interactions, the user can speak naturally and the system can respond quickly in a conversations like experience.

**[3:35:30]** Speech translation is basically, for example, if the user is speaking in Hindi.

**[3:35:37]** So the app can translate and responds in English or any other language.

**[3:35:45]** So for this also right connect to the API right as your speech API using the endpoint. Nowhere you would need the Microsoft Foundry resource okay or global or regional endpoint.

**[3:36:02]** And credentials would be either the project API key or Microsoft intro ID.

**[3:36:10]** Okay, so there and then you'll create a speech config object. Okay, so you'll create a speech config object.

**[3:36:22]** Okay, so you can think speech config object as a proxy object that basically store okay, it store the connections detail for your speech API.

**[3:36:37]** Okay, it basically contains the informations like the end points okay and authentication authentication matter.

**[3:36:49]** Okay.

**[3:36:51]** So if you want to build a voice assistance, the application use the Speech config to connect to Azure Speech and then performs the operations like whether it's converting user's speech to text or converting the a I response to from text to speech.

**[3:37:10]** Okay, or translating the spoken language or real time voice conversations.

**[3:37:21]** Okay.

**[3:37:24]** So now if we take a look here, speech to text.

**[3:37:29]** So here it basically start with the...

**[3:37:34]** Speech Config.

**[3:37:37]** Okay, the application uses SP's config. Okay, it contain basically the endpoints and authentications detail.

**[3:37:47]** Okay, then audio config audio config basically it.

**[3:37:54]** Right, because you need a audio, right? And that basically where you audio could be microphone, right? Or it could be a file, an audio file, or it could be direct microphone. The audio is coming from the microphone.

**[3:38:14]** OK.

**[3:38:16]** So the process start with the connections to this Azure speech.

**[3:38:23]** Okay, and then applications need an audio input source.

**[3:38:30]** This is configured using the audio config.

**[3:38:34]** And then over here the application create a speech recognizer object and this object will basically this will combine the speech config and audio config and then it will basically call the recognise async method.

**[3:38:53]** So this method basically it listen, it listen to the audio and then it basically give the recognitions result. So here in the results, it include durations, okay, like how long the audio was.

**[3:39:14]** Okay, how long the audio was offset basically where the recognised speech started. Okay, properties, you know, it provides additional metadata about the speech. Okay, region whether the recognitions.

**[3:39:33]** Succeed or not. So this is the reason for the result, okay? And the text transcript is basically what is the final like in the voice you will say hello, right? So voice you say hello. So here text would be hello, the output would be the text.

**[3:39:54]** Speech to text.

**[3:39:59]** Okay, so you can see the reason over here, this reason in the reason, it could shows recognised speech. If the speech was successfully converted to the text, okay, it will gets you the speech, you know, recognise speech, no match.

**[3:40:18]** The audio was received, but speech could not be recognised.

**[3:40:24]** Then cancel if the operation failed or it is cancelled.

**[3:40:33]** Okay.

**[3:40:35]** So for example, if the user says please check my order status.

**[3:40:42]** Okay, the Azure speech written the transcript with the text. Okay, please check my order status text.

**[3:40:57]** Okay, clear.


### Text-to-speech  `[3:41:05]`

**[3:41:05]** Now, similarly for text to speech, for text to speech also the process start with the connection using the speech config.

**[3:41:16]** Okay, which in this object you provides the connections to Azure speech, then audio output config, right? Basically, this decides like the generate speech speech should go where like it should be coming out from the speaker or it should be saved in a file audio file.

**[3:41:40]** Then speech recogniser object this will use this speech config and audio output config okay and then it will basically call the speak async speak speak text async method. This method send the.

**[3:41:59]** Text to the Azure speech and then it will return. The Azure speech will return the spoken audio.

**[3:42:08]** OK, and then over here, right, the result basically consists of the audio stream.

**[3:42:16]** Okay, properties, region, and result ID.

**[3:42:23]** OK, so the audio stream is basically this one. This is the main one, other properties and regions like in the regions for result synthesizing audio completed or cancel. OK, if the speech was origin, if the speech was generated successfully, then it will gets you region as synthesizing audio completed.

**[3:42:42]** Or if the operation is failed or cancelled, okay, then it will get you the cancel.

**[3:42:53]** Okay, I will just take 2 more minutes here. Space synthesis markup language now using this SSML, what we can do is we can basically control how the text is converted in the speech like speaking style, okay.

**[3:43:12]** Or any pauses silent. So in the speaking style, right, I can make it sound cheerful, sad, or excited. Okay, so how do you want like what is the style you want? Speaking style you want that you can define with the help of a SSML.

**[3:43:33]** Right, for example, here, okay, we define over here style equal to cheerful, then positive silence, phonemes, phonetic pronunciations, okay, prosody say as like how do you want your numbers to write narrate addresses.

**[3:43:53]** Okay, you can tell the systems how to read dates, numbers, time, okay, or inserts, recorded speech, or background audio. You can use different voice in the same response.

**[3:44:08]** So, for example, you can define the voice name.

**[3:44:14]** Okay, and the method used is basically the speak SSM async, okay, and then SSML string.

**[3:44:25]** So this means instead of sending the normal text, we send the SSML string to the Azure speech. Okay, so where we are telling it okay what voice name okay like how to.

**[3:44:41]** If there is any like how to pronounce this, okay, tomato, okay, or we want some silence, we want some speaking style. So all of this we can configures with the SSML.

**[3:44:59]** Okay, all right. So yeah, so with this is all for today, right?

**[3:45:09]** So the labs you need to performs, there are many labs, okay, lots of lots of hands on for you to try out. So what you would be doing here is...

**[3:45:25]** You have to complete till yesterday it was till 9.

**[3:45:31]** Now you'll go for 101112131415.

**[3:45:39]** Yes.

**[3:45:41]** 16.

**[3:45:44]** 17.

**[3:45:51]** Okay.

**[3:45:57]** Okay, till 15, guys, recognise and synthesise the space. Okay, so perform till 15.

**[3:46:16]** Okay, let me see for Swathi.

**[3:46:22]** Okay, so guys, we have done right. If you have any questions, any queries, you can stay. Otherwise, we have done for the today. And thank you, thank you so much for joining today's sessions. I will see you tomorrow. So tomorrow would be the last day for this. As I told you, that this is a fast paced training, right? So we don't have time to perform as hands on.

**[3:46:42]** And in do practice in the session itself. So you have to perform right everyday. You have to perform the certain labs out there. So perform till 15 and I'll see you.

**[3:46:55]** What is the native language for the LLM model? There is no native language for LLM model actually.

**[3:47:04]** Okay, in fact, in fact, LLM model does not understand the text, okay, it only understand the numbers. so.

**[3:47:15]** What we do is basically we use the tokenizers and we convert those words into the numbers so that your models can understand it, right? Because ultimately if you see, it is a computer, right? So everything is number like zero and one for it.


### When to use speech models vs Foundry speech service  `[3:47:45]`

**[3:47:45]** Okay, when to use speech models or Foundry speech service? That's good question, sir, now.

**[3:47:55]** you can use both of both of them, right? That's good question.

**[3:48:03]** Now, if you want to large language model for the speech, okay, then you will basically go for this. Like if you want more advanced, okay, your what you want is like you not basically want to convert text or speech out there, but you want to do more things out there.

**[3:48:23]** And you want to generate something new, right? So then you will basically go for those speech models, okay, those speech models, foundry foundry speech models, right? Beyond those simple task. But if you have just like speech to text and text to speech, then you will go for foundry speech services.

**[3:48:43]** Okay, these are pre trained models and that were uses that were used previously when the Foundry speech models were not there.

**[3:48:54]** Okay.

**[3:48:56]** Beyond just converting speech to text or text to speech, you can go for Azure Foundry speech model.

**[3:49:03]** And one more thing, like if you want to create any AI agent solution based on the speech services, then we definitely go for the speech model only, right? If we plan to do something with respect to AI agents, correct?

**[3:49:17]** It's also depend on the cost actually, right? If you go for a speech model, then cost will be high. If you go for foundry speech service, the cost will be less, right? If your requirements could be fulfilled with the you know, speech service, go for speech service. That's the first thing, right? If not, then you can go for the like a speech model.

**[3:49:20]** Okay.

**[3:49:38]** Okay.

**[3:49:39]** Okay, so for every agents that you gonna create, is basically cost is involved over there, right? So in terms of like costing, yeah, foundry service fees you should go for and right, if needed, then you go for the speech model.

**[3:49:56]** sure.

**[3:50:02]** Okay.

**[3:50:05]** All right, perfect. So guys, if you have any questions, so feel free to ask. So we have done for today. Thank you everyone.

**[3:50:15]** Let me see attendance.

**[3:50:18]** So I think on the first day I had some set of questions and you have made a note on those. Any chance that we can discuss on that?

**[3:50:28]** Yes.


## Q&A & Wrap-up  `[3:50:30]`

**[3:50:30]** Yes, there were few questions out there. I do remember and I also have my notes there. I have answered few of them yesterday, right? Sorry.

**[3:50:42]** Okay, then I will do the sessions, then I will go through that video session. I missed to check that, right? So if it is already covered, then I can go through that session.

**[3:50:53]** Okay, few of the things we have covered yesterday, right? And also tomorrow, tomorrow I'll just basically go through them once again out there so that if you miss out there, right, so we can go through them.

**[3:51:08]** Calling, yeah.

**[3:51:10]** Okay, let me see first Swati the attendance.

**[3:51:15]** Can you also please check my?

**[3:51:19]** Okay, just give me a second.

**[3:51:39]** Yes, I can see I can see Swathi your there is only one okay 3 actually just a minute.

**[3:51:51]** So Swadeep Pandey, okay.

**[3:51:54]** Hello, sorry, I just want to ask a question if you don't mind.

**[3:52:00]** Yes.

**[3:52:02]** Yeah, I just want to ask, how long do we have access to the labs before it's been taken off?

**[3:52:09]** You have 6 months.

**[3:52:12]** Okay.

**[3:52:12]** Okay, so you have access to the lab 6 months once you redeem the training key within the session.

**[3:52:20]** All right, thanks.

**[3:52:23]** So I have one quick quick. How long do we have access to the recordings of training?

**[3:52:25]** Yes.

**[3:52:30]** It would be 15 days. You can see LET portal, right? You will see the exact number of days out there. Okay, I guess it is 15 days.

**[3:52:34]** Okay.

**[3:52:37]** Okay, can you please post the link of that portal? Somehow I lost that in the chat.

**[3:52:44]** Okay, just let me see.

**[3:52:54]** If anyone has that link, okay, I got it.

**[3:53:02]** There you go.

**[3:53:07]** Swati Swati, your attendance is not marked for today. I can see it is marked for marked for yesterday, not for first day as well.

**[3:53:20]** Actually, I was present and I did mark my attendance on day one and today as well.

**[3:53:25]** Okay, fine, no worry, I have marked it for today and on the first day.

**[3:53:30]** Okay, thank you. thank you.

**[3:53:32]** It is also not showing in my case. Sumit the side, yes.

**[3:53:36]** Summit right, I can see your first day, second day, and today's Sumit Kumar. Sorry, Sumit Kumar Singh, right? Okay, yeah, it's not marked for today.

**[3:53:46]** Sing.

**[3:53:49]** Right.

**[3:53:53]** I have marked it for today.

**[3:53:55]** Okay, thank you.

**[3:53:56]** So still, you guys are facing the same issues out there, right? You're marking attendance, but it's not marked in the at the back end, correct?

**[3:54:05]** Yes.

**[3:54:05]** Correct.

**[3:54:06]** Yeah, it's not minus.

**[3:54:07]** Okay, Rishikesh, let me see for Rishikesh.

**[3:54:18]** Hey.

**[3:54:21]** Okay guys, you can go through the LET portal right and refresh it. You can see your attendance marked for each day from there, okay? And if it is not marked here, Rishikesh, it is done because I cannot check like you know all of your attendance out there. So you can see from LET portal and you think that, okay, I marked it, but it is not reflecting over there.

**[3:54:41]** Then you can let me know.

**[3:54:43]** Okay, so here let's say Deepak, I'll see for Deepak.

**[3:54:53]** Yes, I can see it's marked for day one, day 2, day 3, not for day one.

**[3:55:02]** I'm not sure whether you have marked on the first day or not.

**[3:55:06]** Yeah, but I had it.

**[3:55:10]** Okay, fine, as the smart over there you can view. Yes, it's.

**[3:55:14]** Okay, thank you.

**[3:55:22]** Okay, it's marked for it's showing for 2 days on the LED portal, but it's marked for...

**[3:55:29]** It is marked for 3 days I can see, so you can refresh once LED portal. Okay, it is marked for 3 days, so maybe it is taking a while.

**[3:56:03]** Okay, sure.

**[3:56:09]** Correct, so I am marked.

**[3:56:18]** Or.

**[3:56:28]** So let me see for.

**[3:56:39]** Okay, Disha, you have to wait a while. Let me see if there's any information from the team.

**[3:57:06]** Okay, that is no.

**[3:57:11]** Not getting.

**[3:57:15]** Okay, so still it's circulating out there with the different team.

**[3:57:23]** Okay, let me see for Vivek RN.

**[3:57:37]** Okay, it is not marked for today. I will just mark for today and for first day it is not marked for Aryan.

**[3:57:51]** OK, are you were there on the first day?

**[3:58:03]** Yeah, sure. I was pressing for first day as well.

**[3:58:04]** okay.

**[3:58:06]** Perfect, perfect. Yeah, I have marked it.

**[3:58:18]** Also, one more thing Shova, as I am not able to access LET portal for this course, so my attendance is also not showing to you. or.

**[3:58:30]** Actually, your name is not showing your complete. I mean like you cannot, I cannot see your name out there right in the system itself, right? So at least like even even if someone mark for one day, okay, can you try to use any other device and try to mark your attendance?

**[3:58:45]** MM.

**[3:58:52]** Because it is working for everyone because the name is reflected here. Once you mark your attendance and if the name is entered into the system, then you have access to the LED portal.

**[3:58:52]** Oh.

**[3:59:06]** Okay, I was using my mobile phone only for the attendance.

**[3:59:12]** Okay.

**[3:59:14]** Or should I use my personal mail account?

**[3:59:19]** No, mail mail would be the same. It is your corporate corporate email ID, right? Which is you choose. Okay, so the team is team is looking actually. Okay, let me once I get update, I will let you know I have already forwarded your name.

**[3:59:37]** Okay, to the team, okay, they might add you or they will basically tell like what you should do. So you have to wait till tomorrow. Okay, so by tomorrow, I will let you know basically whether they will add your name or you have to do something else.

**[3:59:59]** Okay, sure. Thank you.
