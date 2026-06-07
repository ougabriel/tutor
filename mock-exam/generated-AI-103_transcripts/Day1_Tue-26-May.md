# AI-103T00: Develop AI Apps and Agents on Azure — Day 1

- **Date:** Tuesday, 26 May 2026 (12:30–16:30 IST)
- **Trainer:** Shova Kant Sharma (Microsoft Certified Trainer), Koenig Solutions
- **Recording:** Day 1 — Meeting Recording (SharePoint Stream)
- **Length:** ~3:41:49  ·  **Captions:** 1201

> Transcript captured from the on-screen auto-generated captions for personal study. Captions are machine-generated (Microsoft Stream) and may contain errors. Section headings were added at the points where the trainer moves to a new topic; the caption text itself is verbatim.

## Contents

- `[0:00]` Introduction & Course Overview
  - `[0:00]` Session start & housekeeping
  - `[2:32]` What we'll cover
  - `[4:18]` The four modules & day-wise schedule
  - `[5:10]` Microsoft Learn profile & course materials
- `[12:00]` Module 1 — Develop Generative AI Apps in Azure
  - `[12:00]` Introduction to Module 1
  - `[26:31]` Planning & preparation
  - `[26:52]` What is Microsoft Foundry? (resource, project, models, tools)
  - `[34:20]` Azure portal — creating a Foundry resource & project
  - `[54:57]` Foundry Toolkit for VS Code
  - `[1:02:52]` Principles of Responsible AI
  - `[1:18:43]` Recap & knowledge check
  - `[1:26:10]` Selecting & deploying models
  - `[1:41:59]` Lab environment walkthrough
  - `[2:14:15]` Select, deploy & evaluate a Foundry model
  - `[2:51:48]` Knowledge checks
  - `[2:55:39]` Develop a generative AI chat app
  - `[3:30:43]` Knowledge check
  - `[3:32:56]` Develop generative AI apps that use tools
  - `[3:40:37]` Wrap-up

---


## Introduction & Course Overview  `[0:00]`


### Session start & housekeeping  `[0:00]`

**[0:04]** Okay, so I've started recording this.

**[0:08]** So the hands on hands on sessions you have to perform right after the session. Okay, I hope this is clear to everyone because it is a 4 hours each day. So we will be covering the concept demonstrations and today I will basically take some times to get you around the lab environments, right? and.

**[0:27]** Perform some one, one or 2 labs OK from the from our first module, OK, so that you basically get comfortable with the lab lab environments.

**[0:40]** I request everyone's to be on mute.

**[0:46]** OK.

**[0:49]** Yeah, thank you everyone. Okay, so let me start with my introduction. My name is Shoa Khan Sharma and I am a Microsoft certified trainer. I have more than 9 plus years of experience in various Microsoft technologies. I am specialised in.

**[1:09]** Microsoft Azure Cloud Platforms and Microsoft Power Platforms. So mainly in Azure cloud platforms, I work on Azure development and Azure A I.

**[1:24]** I am certified, I am certified Azure Developer Associate. I am a certified Azure AI Engineer Associate. Now this is basically from the previous AI 102 Azure Data Scientist Associate. I am certified in various Microsoft Power Platform certifications.

**[1:44]** Power BIT Analyst, Associate Power Platform Functional Consultant, Power Platform Developer.

**[1:52]** So over here now for a I10103, it is still in beta phase, right? So I have appear for the exam, okay. And since it is a beta, right? So once the exam will be live, okay on June, so you will be getting the.

**[2:11]** I will be getting the result on June if you are taking the beta exam out there, this is still in beta, right? So other other live exam, basically you will get the result immediately. So I have taken the AI 103 few weeks back.

**[2:29]** Okay.


### What we'll cover  `[2:32]`

**[2:32]** So now moving further.

**[2:34]** Okay, let's talk about...

**[2:39]** What we will cover, OK, so this is basically for the software developers right who want to build an AI infused application that libraries the Microsoft Foundry. So topics in this course includes like developing generative AI apps.

**[2:58]** Okay, building AI agents and solutions that implements knowledge connections or tools in your agentic applications.

**[3:07]** Okay, so although this course will basically mainly focus on...

**[3:17]** Main focus would be on the A I apps and A I agents. OK. Also, it will cover the concepts regarding the multi models, like multi models capabilities and understanding of the complex content.

**[3:33]** So this is design for software engineer, okay, concerned with building, managing, deploying AI solutions that leverage the Microsoft Foundry.

**[3:44]** OK, so they are familiar. This is basically what is the prerequisites, familiar with the Pythons right and have the knowledge on using a P I's and SD Ks to build agents and generative AI solutions on the Azure.

**[3:58]** OK, so on the Azure, the service basically we're gonna talk about is a Microsoft Foundry service. OK, we'll talk about this, what this Microsoft Foundry is all about and how basically we can use the Microsoft Foundry to build the AI solutions on the Azure.


### The four modules & day-wise schedule  `[4:18]`

**[4:18]** The modules that we gonna cover here are the topics that we gonna cover. There are 4 modules we will be covering module one. Okay, so day wise, this is the module. So today our focus would be to learn how to develop a generative AI apps. So tomorrow, right? So you must.

**[4:38]** You must be, you must be hurting this term like AI agents or Agent AI. So tomorrow we will learn how to develop an AI agents on Azure. That's day 2. Then we will learn how to develop a natural language solutions on Azure.

**[4:56]** And the 4th module is extract insights from visual data on Azure.

**[5:04]** Okay, so these are the 4 modules that we gonna cover each modules, you know, each day.


### Microsoft Learn profile & course materials  `[5:10]`

**[5:10]** Now coming to next one, get the most out of your Microsoft Learn profile.

**[5:17]** Okay, so to sign into your Microsoft Learn profile, you can go to learn.microsoft.com and then sign in with your in a personal Microsoft account.

**[5:30]** OK, so if you don't have a Microsoft loan profile, create your Microsoft loan profile. Now this Microsoft profile can be used to verify, track, and share your training and certification progress and accomplishments all on one platform.

**[5:48]** So in this Microsoft loan profile, you can claim your achievement code.

**[5:52]** Okay, this course, so I'll let you know from where you can access the achievement code. For this course, you can redeem that achievement code in the Microsoft Learn profile, you can access your course material, you can track the progress on your learning activities, you can share and verify your Microsoft certifications, you can download and print transcripts and certificates.

**[6:13]** You can manage your upcoming activities in certification exam, so if we let me share the link in the chat.

**[6:25]** OK, so there we go. And from here, if I click on the profile.

**[6:38]** Okay, now this is a Microsoft Microsoft Learn profile. Okay, then you can see over here you can manage your transcript, your achievements, your training, your courses. Like if you go to the achievement, achievement.

**[6:57]** Okay, so here you can redeem your code. Okay, you can see all your courses. Once you redeem your code, you can see your courses, you can see the learning path. Okay, you can go through each modules here.

**[7:15]** OK, and you can redeem your code here. So once you click on this, it will ask you to enter your achievement code and once you redeem your code out there, the course appear over here. Like if you see course, so it shows you the course over there like Developing Solution from Microsoft Azure or Microsoft Power Platform Developers.

**[7:37]** Okay, likewise.

**[7:44]** Let me.

**[7:47]** Let me share the link.

**[8:08]** Okay, so from where we will get the code to redeem you will get tomorrow. I will let you know that's basically from LET portal. You will be getting access to your code from the LET portal, okay, which you will get access tomorrow.

**[8:27]** Okay, so moving to next year, access your course material, right? All the course content is available on Microsoft Learn, so right, its easy 103. So we will go through this content together and as the course progress, okay, I will basically advise you on which modules to review.

**[8:46]** Right, so all this modules that we gonna cover in this sessions are available in the Microsoft Learn, right? And each day we will be covering the certain modules are there, right? I'm going to give you the reference links for the same so that you can go through them, OK? And also this course includes the lab exercises, OK, there are detailed.

**[9:06]** Exercise instructions which are included in lab environments, so to basically get the hands on experience on developing an A I apps and agents on the Microsoft Foundry.

**[9:24]** Okay, also you can go for AI 103 exam.

**[9:31]** Right.

**[9:34]** You can become a Microsoft certified on the Azure AI apps and AI agents. Okay, so 92% of the certified IT professionals feel more confident in their abilities after earning the certifications.

**[9:53]** Okay, so can validate your technical knowledge on developing an a I apps and a I agents okay through the exam, taking the certification exam on the A I103 and Microsoft role based and specialty certification require the annual renewal.

**[10:12]** Right, it means you need to update with the latest latest content and then you need to give the assessment, okay, in through the Microsoft LUN, you need to give the assessment to renew your certificates, right? Like you know, for example, you renew your driving license, you renew.

**[10:31]** Any other source like your passport. So similarly, you also need to renew your Microsoft certifications right annually, okay. And for this, you just have to pass the assessment given in the Microsoft loan, which is free of course, right? You do not have to pay when you renew your certificate, but.

**[10:52]** When you appear for the certification, that's where you would need to pay, right? And if your organization is providing you the vouchers, you can redeem your vouchers and can give the certification exam.

**[11:05]** Okay, so I will talk about more on the certification part on the 4th day. Alright, once we complete our all the content for the A I103, I will take you through the my exam experience right for the A I103.

**[11:24]** I have taken the beta exam, okay, by June it will be available. The exam like regular exam would be available by June and you can appear for the that a I103 exam.

**[11:42]** Okay, so that's the introduction about the course and the schedules and Microsoft Learn profile. Yes, any question guys before we get started with the topic?


## Module 1 — Develop Generative AI Apps in Azure  `[12:00]`


### Introduction to Module 1  `[12:00]`

**[12:00]** Now we will be taking the first topic, the first module of this course.

**[12:12]** All right, all good. Okay, so lets get into the first module. So right, so we have 44 modules here, right? And can see I have 4 slides with me that we will go through each of them right each day. So lets start with day one.

**[12:38]** Okay.

**[12:41]** Now the first module we will take today is develop generative A I apps in Azure.

**[12:52]** Develop generative AI apps in Azure.

**[12:57]** Now lets talk about the artificial intelligence workload, right? I am sure like everyone know what is artificial intelligence and what is generative AI. Okay, now when it is come to the artificial intelligence workloads, okay, workloads are basically.

**[13:14]** Different type of task that the AI system can perform.

**[13:20]** OK, so this is basically group into different areas like generative AI and agent, OK, text and languages, computer speech, computer vision, information extractions. OK, so these are basically different.

**[13:39]** Areas, okay, different areas in the artificial intelligence. Okay, now for example, like generative AI and agents, these are basically used to create new content, right? New content, new images, new.

**[13:59]** Text, okay, or maybe new code.

**[14:04]** Okay.

**[14:06]** Text in languages. This basically about.

**[14:14]** Text and language.

**[14:17]** Like sentiment analysis, translations, summarizations, key phrase extractions. Okay, computer speech, right? It include like speech to text or text to speech or speech translations, speaker recognition.

**[14:36]** Computer visions, okay, this workloads is mainly on like detecting objects, reading text from image or identifying faces, information extractions, okay, this is basically extracting the meaningful information from the documents like forms, invoice.

**[14:58]** Okay, so extracting like invoice number or maybe date, vendor name, total amount.

**[15:09]** Okay, and at the bottom, okay, we have a machine learning. So machine learning is the foundation behind this many AI workloads.

**[15:21]** Okay.

**[15:25]** So.

**[15:27]** Artificial intelligence workloads are basically these are categorised into the 5 different areas: OK, generative AI and agents, text and languages, computer vision, computer speech, computer visions.

**[15:46]** And informations extractions.

**[15:49]** Okay.

**[15:53]** So our focus would be on generative a I. So today our focus would be on generative a I. So we will be basically going through all of this, all of this areas in the artificial intelligence, okay. But today our focus would be with generative a I. Tomorrow we will be focusing on agents.

**[16:13]** Right. And then remaining, remaining 2 days are there, right? We will be focusing on text and languages, computer visions, okay, computer speech, computer visions and information extraction. So we'll be exploring all of these areas of artificial intelligence workloads. Clear now, proceeding further with generative AI.

**[16:36]** Okay, now what is generative AI?

**[16:47]** Generative AI.

**[16:52]** Yes, anyone would like to answer what is generative EVI?

**[16:58]** Just creates the content, maybe text or images or act like an smart assistant for us.

**[17:08]** OK, yes.

**[17:12]** Okay, thank you, Dinesh. Yes, Disha, you want to answer?

**[17:19]** Yeah, generative AI are the applications which can create new content, like we can create or generate text, emails, reports, codes, or summaries, everything from that.

**[17:36]** Correct.

**[17:48]** Okay, so Swatish is when it is all about creating new data based on the knowledge base, okay, creating or generate hallucinations or info based on the LLM, right? Yes, one point LLM, which is basically your large language model.

**[18:07]** Okay.

**[18:10]** So what is generative AI? Generative AI is basically that it is a type of artificial intelligence that can create new content.

**[18:24]** Okay, based on the based on the input or the prompt.

**[18:31]** Input.

**[18:34]** Or prompt prompt given by the users. Okay, so if you talk about like we have a traditional AI.

**[18:43]** Right. So traditional A I basically they were mainly used for they are used for analysing the data. OK, they were basically used for classifying the informations or they were mainly used for making the predictions out there.

**[19:03]** OK, making the.

**[19:07]** Prediction.

**[19:12]** Correct.

**[19:14]** So.

**[19:16]** Traditional AI, okay, and then comes the generative AI. Generative AI basically can generate something new.

**[19:24]** OK, so this new content can be your text, can be images, can be code, can be audio.

**[19:38]** OK, and can be videos.

**[19:46]** Okay, so this basically creates new content, right? Now, for example, if we ask AI system to write an email okay to a customer.

**[20:00]** Apologizing for the delay, the generative way I can create a complete professional email.

**[20:07]** Okay, to the customer.

**[20:10]** OK, if you ask to summarise the documents right, it can read the content and it can generate this short summary. If you ask like to create a Python code to connect to a database, right, it can it can generate a sample code.

**[20:27]** Okay, now this generative AI basically.

**[20:32]** This generative AI.

**[20:36]** It uses the...

**[20:39]** Large AI model.

**[20:43]** Okay, which is basically known as the LLM.

**[20:49]** Which is stand for large language model, correct? Now this large language model are basically trained on a is a trained on a huge amount of data.

**[21:06]** Correct. So from that huge amount of data, they learn the pattern. OK, they learn the pattern in the language, they learn the pattern in the structure, the context, the meaning.

**[21:21]** Right. So once they learn from the patterns in the data which we have provided, So now when we basically give a prompt to this large language model, the model basically make the prediction it basically predict and generate the most suitable.

**[21:42]** Response, okay, based on what it has learned.

**[21:47]** So it is also making the predictions out there, right? So basically it gets like the and then it make the predictions out there, cat.

**[21:56]** Okay, then it make the prediction next board like the cat is then it make the predictions out there playing okay because it has learn it has learn basically we have provided data okay where basically it learn that okay, what is the relations between the the and cat?

**[22:18]** What is the relation between each or playing? So various words out there, lets say dog, okay, lets say catching. Okay, so basically this model has learn what's the relationships out there okay between the cat and.

**[22:36]** Is What is the relationship between cat and the cat and dog? Okay, cat and catching or catching or playing.

**[22:47]** Okay, and basically based on the prompt, it will give you the response, right, which is like making the predictions for the next word, okay, and generate the output.

**[23:01]** Okay, so now this large language models are basically trained on a huge amount of data, right? And basically, these are basically the organizations who would train on this large amount of data.

**[23:20]** Right, and provided you as a model.

**[23:24]** OK.

**[23:26]** So provided use the model.

**[23:31]** Fine, so these are basically known as the foundation model.

**[23:36]** Now, these models are basically good for, because this is a train on a his own data, they are able to you give the prompts and they are able to get you response out there, right? But to make the most out of this model, right, if you ask something related with your organizations inform, organizations data, lets say maybe if I go to.

**[23:57]** Lets say ChatGPT, okay, which is using a GPT model, correct? So ChatGPT is an applications, right? And it is using a GPT model, correct? So when you ask to the you know the GPT model, right, what is the you know what is the...

**[24:16]** Travel policy in my organization.

**[24:23]** Okay, what is the policy? What is the travel policy in Contoso?

**[24:28]** Okay, sir, I want to ask.

**[24:33]** I want to basically ask information related to my organization, so this would not be able to provide you the appropriate response out there, right? That's basically come over here that we can basically use this model and we can provide our own.

**[24:50]** Organizations enterprise data.

**[24:54]** Right, so that now the next time when I ask questions to this model, okay, what is the travel policy in Contoso right? It will get you the appropriate response out there.

**[25:10]** Okay, so one point is that the generative AI.

**[25:16]** It basically it does not think like a human, right? It generates the response based on the patterns and probabilities.

**[25:24]** Okay, so that is why we must design a good prompt.

**[25:30]** Provides the model with proper grounding data.

**[25:35]** And evaluates the response, provides it with the safety filter, and monitor the solutions.

**[25:45]** Okay.

**[25:50]** So over here, basically will not be going deep dive understanding the generative AI or large language models or transformer model transformer architecture, which is behind for large language models. Okay, we would be basically focusing.

**[26:11]** On the AI solutions on the Azure. Okay, how to develop an AI solutions on the Azure, correct?

**[26:17]** Right.

**[26:19]** Take care.

**[26:22]** So we'll be starting here with I think someone is on mute there.

**[26:22]** Ha.

**[26:28]** Alright, thank you.


### Planning & preparation  `[26:31]`

**[26:31]** OK, so first lets understand planning. Before we started with developing an A solutions in Azure, first we need to plan and prepare.

**[26:42]** Okay, we need to plan and prepare to develop the AI solutions on Azure, so let's go with this.

**[26:50]** Okay.


### What is Microsoft Foundry? (resource, project, models, tools)  `[26:52]`

**[26:52]** So first, let's start with the Microsoft Foundry.

**[26:57]** Now, what is the Microsoft Foundry? Microsoft Foundry?

**[27:01]** So.

**[27:02]** Sorry, anyone has a question?

**[27:10]** Okay.

**[27:12]** So what is the Microsoft Foundry? Microsoft Foundry?

**[27:16]** Is a unified platform for building the AI apps and agents okay on the Azure.

**[27:26]** Okay, so it basically it gives the developers one place where they can create.

**[27:37]** They can test.

**[27:40]** They can deploy and they can manage manage the AI solutions.

**[27:48]** Clear.

**[27:50]** Okay, now in Microsoft Foundry, okay, we have basically the Foundry Foundry resource.

**[28:00]** Okay, Foundry resource. So, Foundry resource in Azure, it provides compute, storage, model delivery, and other services.

**[28:10]** So first we have the Microsoft Foundry Foundry resource.

**[28:17]** So you can say the main container okay is called the Microsoft Foundry resource okay. And this basically provide the back end capabilities which is required for a I development okay, which is like your compute storage.

**[28:35]** Your model delivery and other connected services.

**[28:41]** Okay, then comes the Microsoft Foundry project under under your Microsoft Foundry resource, we have a Foundry project. Now, Foundry project are basically this isolated workspace, okay, work environments for your apps and agents development.

**[29:00]** Okay, so for example, one project can be created for customer support chatbot or another project could be created for the HR policy assistant. Okay, another another project could be created for invoice processing. So if the project is an isolated workspace where the...

**[29:20]** Team can build a specific AI application or the agent.

**[29:25]** Clear. Then in a project you work with the model.

**[29:33]** OK, these are basically the AI model, the large language model.

**[29:38]** So you can choose and you can deploy the model from an extensive model catalog.

**[29:46]** Okay, and this language model, I mean this models can be used for language understanding, for reasoning, for code generations, for conversations, for summarizations.

**[30:01]** Okay, then next is basically agents.

**[30:06]** Hey, model, right?

**[30:10]** Now this models Microsoft Foundry provides you a model catalog, okay, where you can choose the models not only offered by the Microsoft, but also from OpenAI, from other various 3rd party vendors.

**[30:29]** Okay, and you can deploy that model and you can use in your applications. Next is agents.

**[30:40]** Okay, agents, basically you can create and manage agents that use the model for language and reasoning.

**[30:48]** Ok.

**[30:52]** So you can in the project, you work with the model, you work with the agents.

**[30:58]** Okay, then comes the tools. Now, AI agents is basically they are the AI assistants. They are not only for conversations, but they are also able to perform the, they are also able to perform the task.

**[31:17]** Okay.

**[31:19]** Now next is the tools. Now what is the tools? Tools basically it lets connect your agents okay to perform the actions and access the information. Now your AI agents or your models basically would be using the tools.

**[31:39]** Okay, it basically allow your agents to perform right actions like maybe, for example, calling a function or accessing the database.

**[31:50]** Okay.

**[31:53]** Then comes the knowledge. Okay, knowledge means this is used to manage the data source access for the agents so that they have the information they need to.

**[32:07]** Okay.

**[32:09]** So it could be, lets say, knowledge could be your product manuals.

**[32:11]** Okay.

**[32:16]** Right, could be company.

**[32:19]** Company policies.

**[32:22]** Could be PDF, could be the SharePoint files, okay, or could be your indexed enterprise.

**[32:35]** Enterprise data.

**[32:40]** Okay.

**[32:43]** So in simple word, Microsoft Foundry, okay, basically it provides the platform.

**[32:52]** Microsoft Foundry resource provide the Azure infrastructure.

**[32:57]** Okay, it provide the infrastructure, then Microsoft Project, Microsoft Foundry Project, it provide the workspace, okay, where we can build the AI apps agents using models agents.

**[33:17]** Tools and knowledge.

**[33:21]** Is this clear to everyone?

**[33:27]** Yes.

**[33:28]** Yes.

**[33:30]** Okay.

**[33:31]** So.

**[33:34]** Let me take you to the Azure portal.

**[33:39]** Okay, now you can directly you can go to portal.azio.com.

**[33:50]** Okay, and let me sign in with my Azure account.

**[34:04]** Okay, now this is Azure portal.

**[34:08]** Okay, now in this Azure portal, we can basically create a resource, right? You can deploy the resource here. So it shows basically if we go to all services.


### Azure portal — creating a Foundry resource & project  `[34:20]`

**[34:20]** All services so you can see we have a different categories. Okay, we have basically all the services for analytics. It give you the list of all the services for analytics for compute. Now let's say maybe you want to deploy a virtual machine, you can go and simply click on this. you can.

**[34:40]** Choose the right, you can choose from here. You can select like the virtual, you can provide virtual machine name in which region you want to create virtual machines, right? What image you want to use, okay, what image you want to use, Windows, Linux.

**[34:59]** Right, Ubuntu server, so you can specify what should be the size, okay, username, password, site, so you can provide this information and you can create your virtual machines, right? And then you can use that virtual machines for your users. Similarly, right, you can see containers, databases, so these are all services for DevOps.

**[35:20]** Right, and so on. So if you go to the a I plus machine learning.

**[35:25]** AI plus machine learning. So you can see Azure AI plus machine learning platforms, Azure AI service plus API, okay, industry machine learning solutions. Now you can see under this you can see Microsoft Foundry, okay, you can click on this Microsoft Foundry, right? And then from here you can.

**[35:46]** Create a foundry resource, create a foundry resource over here and under this right you can see use with foundry. Okay, Foundry, AI, Hub, Azure, Open AI, AI search and if you click on more services now it shows it give you the list of.

**[36:06]** Now these are basically known as the foundry tool. Okay, these are known as the foundry tool. Now these are basically the previously it was known as the AI services before that it was known as the cognitive services.

**[36:22]** Okay.

**[36:24]** So from here we can go, we can create a resource. Now we can also search from here to create a Microsoft Foundry so I can search for.

**[36:36]** Microsoft.

**[36:40]** Foundry. Once you click on this, it will take you to the same page. Now from here, create a.

**[36:47]** Create a foundry foundry resource, right? You will provide this information to create a foundry resource from here, right? And in that foundry resource, right, you can create a project.

**[37:00]** Okay, now whenever you are working on the Microsoft Azure platforms, you need the subscriptions. Without subscriptions, you will not be able to create any of this any of the resources on the portal. So you need to have your account first. Okay, once you have account, you should have a subscriptions like.

**[37:19]** I have the subscription which is Visual Studio Enterprise subscription. So this is subscription, okay, this the billing is basically on this subscription, right? As of now, I have spend over here like ₹850, okay.

**[37:39]** As you consume the resources, as you deploy resources and you consume it, the amounts basically gets deducted from your credit card which is associated with the subscription.

**[37:52]** Now, because I am an MCT, so I have this Visual Studio Enterprise subscriptions where I gets like around 12 to 13 key that can that I can spend like for my training and demonstrations.

**[38:07]** Okay, so let me go here. So any resource you deploy that would be basically associate with the subscription, right? And the amount basically gets deducted from the subscription.

**[38:24]** Now our target would be the Microsoft Foundry.

**[38:29]** Okay, so or I can go to aiai.azio.com.

**[38:38]** Okay, now it will take me to the Microsoft Foundry. So it's an AI app and agent factory.

**[38:46]** Okay, so it's never been easier to build, optimise, and govern AI apps and agents that understand your business context, deliver the business impact. So our unified interoperable AI platforms enable developers to build faster, smarter okay while organizations gain.

**[39:07]** Feed wide security and governance in a unified portal. So this is Microsoft Foundry, right? Microsoft Foundry, the portal which we talk about. It's a unified platform for building your A I apps and agents. It's a A I apps and agent factory. Let me go click on sign in.

**[39:30]** Let me sign here. You need to sign in with the Azure account which has a subscription.

**[39:37]** OK.

**[39:39]** So now we are here. Okay, so sign in, sign in is done. Okay, now what do you see right now? Okay, now from here you can see an options to create an agent. Okay, you can explorer the latest model, right? These are these are basically the language model.

**[40:00]** OK, so you can see this these are the these are the last language model generative AI models. OK, so from here we can go to full model catalog.

**[40:16]** Okay, and as of now you can see here that there are 463 models are there, right? You can see these are these are all the models available out there. Okay, now this is a older interface. Okay, this is a old interface.

**[40:35]** Okay, so previously we use this in a I 102, now we have a new user interface. So to enable the new user interface, okay, we will just click on this option, this toggle button for new foundry. This is a old foundry.

**[40:54]** Okay, the user interface is different. Okay, so we will basically because Microsoft would be switching to the new one, so we will go for the new foundry, right? We will switch to the new foundry.

**[41:09]** OK, now select a project to continue. OK, so we have you can see where I have already created 2 project. OK, these are the 2 projects. So let me create a new project for this demonstration. Let me define my project name. I will say.

**[41:28]** AI Foundry.

**[41:35]** A foundry.

**[41:42]** From the project.

**[41:46]** OK.

**[41:48]** So I've given my project name.

**[41:52]** Right, and you will see that's my project name. A new project name would be created and then for your project, what you need is the Microsoft Foundry resource. So along with for project, it will create an Azure, it will create a I foundry project resource, okay.

**[42:11]** Remember we talk about here, OK, Microsoft Foundry, Microsoft Foundry resource and in the Microsoft Foundry resource we have a Microsoft Foundry project. So we'll be creating this foundry resource will be created in and then in that foundry resource will have the project.

**[42:33]** Now on which subscription? So you need to select the subscriptions. If you have multiple subscription, you will choose one subscription then resource group. Okay, if you have like I have already a I103 training resource group, I can use that resource. I can select this resource group.

**[42:54]** Or I can create a new resource group.

**[42:58]** Yes, Rajat, you had a question.

**[43:01]** Hi, so I have just small doubt, so can't we select the existing foundry resource here while creating a project?

**[43:09]** Here we don't have an option.

**[43:13]** Okay, once if you have all existing foundry resource, so you can go to that foundry resource and then you can create a project over there.

**[43:22]** okay.

**[43:22]** Okay, you need to be inside that resource foundry resource, okay? And then you can create a project. But here what I'm doing is basically I'm creating a project from the scratch okay by a.sio.com. So it does not does not give the options over here, although the location is same, okay, but you can choose here.

**[43:44]** Which under which resource group you want to create this? Under which resource group you want to create this foundry, Microsoft Foundry resource and your project?

**[43:53]** So Shoma, one question quick question. If I'm creating a project and attaching this foundry as a service, will it be like where will I get the cost? It is on demand or it is just on the deployment?

**[43:54]** Okay.

**[44:11]** Okay, now costing basically depend costing would be on the deploy models actually.

**[44:21]** OK, now once you once you create this and then you started deploying models and then when you consume the model, so depending on like what's kind of deployment you do with the model.

**[44:34]** Okay, it could be token based or it could be compute based. So based on that, okay, the bill will be calculated.

**[44:46]** Got it.

**[44:47]** Okay, so it is basically on the on the infrastructure, this basically which provide the infrastructure, right? So we are not paying for the infrastructure over here, but we are paying on how what you consume actually.

**[45:03]** Okay, so it basically abstracted everything is abstracted over here, okay, so that we don't need to focus over there like the computer resources which is used behind like what is the compute power used, what is the RAM we use, right? We don't have to worry about it. We only pay for, like for example, the token we which we're gonna use.

**[45:26]** Okay.

**[45:27]** So now.

**[45:29]** Let me go click on create.

**[45:33]** So what does it do? It will basically, since I haven't created a new resource group, it will automatically create that new resource group, right? And I will show you my old one. So if I go to my resource group, right, I have existing resource group. Now you see this is my existing resource group and this is the just resource group which is created.

**[45:53]** So if I go to new resource group, it is empty right now because it is in process of the deployment. Okay, you are almost ready to create and deploy AI solutions. So it is setting up the project. So that's why you see it is empty. So if I go to my AI 102.

**[46:12]** Right previous resource group. Then you can see I have my foundry. This is my foundry resource and then you can see I have my foundry project. Okay, I have another another foundry resource here, right? And then I have the another project over here.

**[46:31]** Okay.

**[46:37]** So let's see here. Okay, now you see there your Foundry resource is created, right? And in that resource, right, a project would be created.

**[46:47]** And then once the project is created, which provides you the workspace, okay, isolated work environments for your app and agent development.

**[47:08]** Okay, so now this is done. We are inside the project now. Okay, build and deploy your A I solution faster safe. So here you can go through this and let me close this. We're not creating agents now we'll be creating agents tomorrow.

**[47:28]** Okay.

**[47:30]** Right, so now we are inside the project. Now this is where we are going to basically create agents and the AI app. OK, now this is where inside in your project we will be working with models, agents, tools, and knowledge.

**[47:51]** Now, Foundry tool. What is a Foundry tool? These are basically ready to use Azure AI capabilities.

**[48:03]** Ready to use.

**[48:05]** Azure AI.

**[48:11]** Capabilities.

**[48:13]** Okay, so basically these are the services, okay, these are the Azure Language service, right? Azure SP Service, Azure Translator Service, Azure Document Intelligence Service, and Azure Contain Understanding, right? So now Microsoft has basically defined them as a foundry tool.

**[48:36]** Okay, so instead of building everything from the scratch, we can use this tool for language, for speech, for translations, okay, where you need like a speech recognition and synthesis, where you need a natural language processing and text analysis is needed, okay, where you need multilingual text and document translations, where you need.

**[48:58]** To create an application for translating the text from one language to another another language, or maybe you want to performs like complex document processing and extractions, like for example, to read invoice or receive or form, OK.

**[49:18]** Extract the structure informations from the invoice like the invoice number, the invoice date, the customer name. You want to extract this informations okay or Azure Container Understanding in Foundry tool. Basically, using this you can analyse.

**[49:37]** You can analyse different type of content like whether it is a text, whether it is a images, whether it is a audio, okay, video, okay. So we would be exploring this Foundry tool in the coming modules, module number 3 and 4, okay, where we basically will be working on this your.

**[49:57]** language service, Azure speech service. Okay, so this were basically this were basically the pre trained models by Microsoft before generative AI, okay, which were basically used to perform like this kind of task out there now because of.

**[50:17]** Once the generative AI has come.

**[50:22]** So Microsoft basically these are basically known as the right. If you recognise okay at the starting, these were basically known as the cognitive cognitive services. These were known as the cognitive services. Later on, Microsoft changed the rebrand. It is the Azure.

**[50:41]** A service, right? And now the Microsoft rebrand it is the Foundry tools. So these are nothing but these are basically a pre trained models by Microsoft, okay, which was basically done previously when generative A was not that you know does not.

**[51:01]** It was not there and where people need to perform speech recognizational synthesis, they use basically the Azure speech. If people need to do some translations like language translation, they use the Azure translator, okay.

**[51:19]** Now once we have this generative AI, these are basically the services which are now known as the Foundry 2.

**[51:30]** Okay, so Foundry 2 provides a prebuilt a I capabilities that can that can be connected with your a I apps and your agents to make them more powerful, more practical, and enterprise ready.

**[51:50]** Clear.

**[51:55]** Okay, next coming here, developers, tools, and SDK.

**[51:59]** Okay, now what are basically the tools in SDK developers can use to build the AI apps and agents on Azure?

**[52:15]** Okay, in tools, what do you need? You need a Microsoft Visual Studio code.

**[52:22]** Right, Micro Microsoft Visual Studio Code. OK, now this is basically the this is the main tool. OK, this is the.

**[52:32]** This is developer tool which is used to write, test, debug, and manage the AI application code.

**[52:42]** Correct, and inside inside the Visual Studio Code, we can use Microsoft AI Toolkit extension. It basically helps the developers to work with the like AI models.

**[52:57]** OK, prompts.

**[53:00]** Agents.

**[53:04]** Okay, and they can directly deploy from here, okay, to the okay, they can deploy from here the into the production environment.

**[53:18]** Okay, another important tool is basically the GitHub Copilot. So it basically helps the developers write code.

**[53:26]** Okay, to write fast quote by using the copilot.

**[53:35]** Okay, so it basically have developers write code by suggesting like code functions, explanation, fixes while they are working.

**[53:45]** Okay, and for example, let us say if the developer is building an AI chatbot, the Copilots, the GitHub Copilots can help generate sample Python code, you know, to call model endpoints or to connect to the Azure services.

**[54:00]** Okay, so you will get all of this in your lab environment. Okay, so let me open the Visual Studio.

**[54:12]** Visual Studio Code.

**[54:18]** So I am in the Visual Studio Code now. Okay, then what you have to do is you have to go to the extension.

**[54:29]** Let's go to the extension extension and then you need to install the Foundry.

**[54:36]** Foundry 2.

**[54:42]** Foundry AI 2.

**[54:51]** Okay, then you can see here Foundry toolkits for Visual Studio Code.


### Foundry Toolkit for VS Code  `[54:57]`

**[54:57]** Okay, toolkit for Visual Studio Code. Now if we click on this, okay, so we have installed the Foundry Toolkit for Visual Studio Code. So Microsoft Foundry Toolkit is a new name for the AI toolkit. Okay, so it is a Visual Studio Code extension that help you build.

**[55:16]** A I Agents quickly with the built in access to Microsoft Foundry, Microsoft Foundry resource for model deployments, agents, managements, and more without leaving your Visual Studio code. So you don't need to go to the visuals, the foundry portals and deploy the models over there.

**[55:37]** Or test your models using the playground so you can do all of this okay with the Foundry Toolkit for Visual Studio Code.

**[55:47]** Okay, so using with Microsoft Foundry Toolkits, you can discover and evaluate model from providers including Microsoft Foundry, Foundry, Local, Anthropic, Open AI, GitHub, Google, NVIDIA, and run model model locally with ONSX and.

**[56:06]** Pulama build, test, deploy AI agents, manage Microsoft Foundry resource, right? So once this is installed, if you go to the foundry over here, foundry tool and then if we have to basically go and we have to log in here.

**[56:25]** Okay, so we have login over here from here you can choose it shows.

**[56:31]** OK, you can see here models. OK, this is the project summit support agent project. So if we go here and let me change in the Microsoft, so if you see.

**[56:46]** Summit support agents project one. Okay, now if I go to build and if I go for the deployment.

**[57:01]** Okay deployment. So here we can see we have 2 model okay GPT 4.1 and text embedding.

**[57:18]** Loading the model.

**[57:34]** So, how did you connected that? I think probably I missed it. My bad. How did you connect it to your Arjun?

**[57:41]** Okay, so here you just need to sign in into your Microsoft Azure platform.

**[57:47]** Okay, so from here once you have right for example.

**[57:55]** Let me show you if I can.

**[57:58]** OK, show me the subscription.

**[58:05]** Omri 2.

**[58:06]** Thank you.

**[58:12]** Ethical.

**[58:27]** Okay, now from here you will get some options to sign in. Okay, and once you click on that option, then you have to provide with the credentials of your Azure, your Azure credentials, and then right, it will give you this options here. And this is from where you can also go and you can see the model catalog. So whatever you.

**[58:49]** Performs over here like through the through the portal. Like if you go to the Microsoft Foundry, for example, this like I want to find the models, I click on this right, it will take you me to the model catalog right where I can view all of these models and I can deploy over here. The same thing I can do from here.

**[59:09]** Like find the right model for your AI solutions. It shows the popular models. I can basically filter it by, you know the different hosted by right and I can deploy to the Microsoft foundry from here. Similarly, if you have your existing existing model you are my resource, it will also load that model. It is not showing right now, just give me a second.

**[59:43]** Switch project.

**[59:47]** Let me switch to the project which we just have created.

**[59:53]** I think we created the AI Foundry project, right? So I'll just switch to this.

**[1:00:00]** OK, so once I switch to this product, if I go to model, OK, it shows me no models deployed. OK, now if I want to create a new models, I can deploy the model from here, right? Or.

**[1:00:15]** Right, you can see here it shows like models, prompt agents inside your project, right? So you can manage all of this like tools, knowledge, evaluation, okay, connected, connected resources.

**[1:00:30]** So now let me go back. Okay, so I have my project.

**[1:00:36]** Okay, so I have my project, let me go to the home. So this is I'm on the home, right? So for your project, this is the API key and this is the project endpoint. Okay, so along with this, you have Azure Open AI endpoint. So you have 2 endpoints here, okay, you can connect to your Microsoft Foundry.

**[1:00:58]** Using this 2 endpoint, now the first thing.

**[1:01:04]** In the project, OK, we are going to basically find the model, OK.

**[1:01:20]** OK, so we basically have in incoming slides, we will be talking about how to choose the different models out there. I will take this part over there. OK, so as of now, you need to understand the tools as developers you would need. OK, what you need is a Microsoft Visual Studio code, right? And then.

**[1:01:39]** Microsoft AI toolkit extensions, GitHub Copilots, okay. It basically helps you to write code by using the Copilot, okay. Then comes the SDK, okay, SDK, so SDK, Microsoft Foundry SDK, Open AI SDK, Microsoft Foundry.

**[1:02:02]** Tools SDK, right? For example, language and text analytics analysis, speech, okay, translator, document intelligence, and content understand side. So all we talked about this Microsoft tool previously. So to basically consume and use this services, right, you need the SDK for that particular.

**[1:02:23]** Tool.

**[1:02:26]** Okay, so this is what you need it as a developers out there and the lab environments has the Visual Studio Code. You just need to install over there like the SD Ks and other things right as you progress with the hands on you would be installing them.

**[1:02:50]** Okay.


### Principles of Responsible AI  `[1:02:52]`

**[1:02:52]** Now let's talk about the principle of responsible AI.

**[1:02:57]** Okay.

**[1:02:59]** Now what is principle of responsible A I? OK, responsible A I means building and using the A I system in a way that is safe.

**[1:03:13]** Okay, which is fair, which is secure.

**[1:03:19]** And which is transparent and accountable.

**[1:03:27]** Okay, A I is very powerful and with great powers basically comes the great responsibility and it is a responsibility of the developers who basically develop the A I apps or the A I agents. Okay, then they must have to make sure.

**[1:03:47]** It is used responsibly.

**[1:03:50]** Okay, so the first principle is the fairness okay means your AI system should treat all user fairly and should not create bias or discriminatory, you know discriminatory issues.

**[1:04:08]** Okay, for example, the loan approval or recruitment screening agents, okay, it should not, it should not unfairly favour or reject people based on gender, age, locations, or the background.

**[1:04:29]** So the A system should treat all user fairly. Second is reliability and safety. A system should work correctly and safely under different conditions. Okay, so for example, if you build a medical assistance or customer support board, it should provide a reliable response.

**[1:04:51]** And avoid any misleading suggestions or any harmful suggestions.

**[1:04:57]** Correct. The 3rd is basically privacy and security.

**[1:05:03]** OK, the AI system must protect the user data and sensitive business informations. OK, like customer personal detail, financial data, OK, or company document should not be exposed or misused.

**[1:05:20]** Next one is inclusiveness. The AI system should be designed for everyone, including people with different abilities or language or accessibility need.

**[1:05:34]** Okay, for example, that can be included like speech to text okay or screen reader support or multilingual supports it make the a I solutions more inclusive. Transparency users should understand.

**[1:05:55]** that they are interacting with the a I. Okay, so it means like the chatbot should clearly indicate that this is an a I assistant, and it will not be always perfect out there, right? So you will see out there like if you go to any.

**[1:06:12]** Any AI applications, right? You will see at the bottom there is like the output should be check because the sometime it could generate the wrong output, wrong result.

**[1:06:28]** Okay, so it has to be clarified by the person. So transparency, accountability, the organizations and developers are responsible for how the AI systems are designed, deploy, monitors, and improve. Okay, so it means the AI system, if lets say AI system give.

**[1:06:48]** Incorrect or harmful output. There should be the human basically who would be accountable for that. So there should be an accountability for the AI system.

**[1:07:03]** Okay, so responsible A I ensure the A I solutions are not only powerful but also safe, also ethical, okay, it also trustworthy.

**[1:07:20]** Okay, and useful useful for all users.

**[1:07:29]** Clear.

**[1:07:34]** Okay.

**[1:07:37]** So, in this exercise, you will create a foundry project, okay, like how I have shown you, deploy and test a generative a model. Okay, lets do one thing. so.

**[1:07:55]** So we have a project. Okay, next what we gonna do is we are going to deploy the model here. Okay, so to deploy a model, now you can basically see over here this option, find models, okay.

**[1:08:14]** Or you can go to Discover.

**[1:08:17]** OK, from this stop you can go to discover.

**[1:08:22]** And then you can basically see discover what's possible. You can view all the models from here.

**[1:08:30]** Right, it will take you to the model model catalog.

**[1:08:34]** OK, now here where you can see you have 117 available in my project and if I click on this all models so you can see all models 11,374 models are there.

**[1:08:51]** Right available in my project, I have 117 and now we can basically go through them. I want to deploy the GPT.

**[1:09:05]** Let's deploy the same order which you can also deploy in your lab environments, GPT 4.4.1.

**[1:09:14]** Okay, we'll deploy the GPT 4.1 and we'll test it. So you can see all the GPT models here, right? There are 40 models from open AI. These are all the open AI models.

**[1:09:28]** Right, so this is GPT 4.1 for chat completions and responses, right? You can see this is GPT real time which is for audio generations, right? Text to image, image to image. So chat completion, response, audio generations, right, so speech to text.

**[1:09:47]** OK, so these are various models. So we'll just click on this GPT 4.1.

**[1:09:54]** Okay, now from here, okay, we have basically the this is a model card. This is a model card. Actually, it provides the informations about the model and it basically help you to understand.

**[1:10:10]** the model capabilities, its limitations, its use cases, and it basically helps you to determine if they are suitable for your requirements, like the pricing.

**[1:10:22]** Okay, so pricing is based on the number of factors including deployment type and the token used.

**[1:10:29]** Okay.

**[1:10:30]** So deployments.

**[1:10:34]** Okay.

**[1:10:37]** So I have existing one like I've already deployed this models are there.

**[1:10:47]** Benchmark.

**[1:10:51]** Responsible, Responsible AI okay licenses.

**[1:10:58]** So this is basically known as the model car. Now after this to deploy this model, okay, we'll click on deploy, right? We have 2 options over here, okay, default setting and custom setting. So when you set the default setting.

**[1:11:17]** Okay, you are setting to the global standard and default quota. Here you have basically more controls on the infrastructure, sets your own SKU, quota, PTU, spillovers or guardrail. So for now, we will be keeping on the default.

**[1:11:40]** So the deployment is done. Let me go to here.

**[1:11:47]** Okay, so it basically that's a name. So already if you see in Microsoft, okay, sorry.

**[1:11:57]** I just go for new project, the project which we have created.

**[1:12:02]** Okay, yeah, this is the project which we have created as of now. We don't have any model, so deploy a base model.

**[1:12:12]** Search for GPT.

**[1:12:16]** 4.1

**[1:12:22]** Click on deploy.

**[1:12:25]** Default setting.

**[1:12:28]** Deploying the model.

**[1:12:30]** Right, the model has been deployed and it will navigate you the playground. So if you click on the deployment, now you can see here the model is deployed.

**[1:12:40]** OK, so along with this right, we can see on the left hand side the target URI, the key OK to connect to this model and this is the code sample.

**[1:12:54]** Code sample, okay, we have basically 2 api completions API and the response API that we will be discussing in a while. Okay, so you can choose the option from here, which API you want to use, right? and.

**[1:13:12]** So it is there and you can open in a playground. So if you click on this, so this will open this model in a playground, OK? And then you can see here, OK, on the left hand side, this part. So this is where you can provide, Sir.

**[1:13:26]** Lock.

**[1:13:31]** System instructions.

**[1:13:33]** Okay.

**[1:13:34]** Okay, that's the model GPT 4.1 you can provide here the instructions which is also known as a system system prompt. Okay, so here we'll say okay you.

**[1:13:50]** You are and.

**[1:13:54]** Assistant.

**[1:14:00]** Yeah, assistant that can.

**[1:14:06]** Provide.

**[1:14:09]** Information.

**[1:14:14]** And advise.

**[1:14:20]** About.

**[1:14:22]** A I software.

**[1:14:29]** Development.

**[1:14:32]** Okay.

**[1:14:33]** So this is the instructions we have provided and now over here, this is the chat window.

**[1:14:40]** Okay, this is the chat window and in this chat window, we can chat with the model.

**[1:14:47]** Okay, so I'll say hi.

**[1:14:56]** Okay, how can I assist you with the software development software development today? Okay, so now we have provided it a role saying that, okay, you are an AI assistant that provide information and software developments, let us say.

**[1:15:17]** I'll say, tell me.

**[1:15:20]** Tell me.

**[1:15:22]** 3.

**[1:15:25]** Key.

**[1:15:28]** Consideration.

**[1:15:31]** Or.

**[1:15:33]** Working with.

**[1:15:36]** The large.

**[1:15:42]** Language model.

**[1:15:47]** Or.

**[1:15:49]** AI application.

**[1:15:59]** Element.

**[1:16:02]** Okay, so let me ask you.

**[1:16:12]** Okay, so it provides a response here. Here are the 3 key considerations when working with the large language model: So data privacy and security, performance and scalability, ethical considerations, and bias mitigations.

**[1:16:30]** Okay.

**[1:16:36]** Sorry.

**[1:16:38]** So this is build. OK, just next to the build we have operate.

**[1:16:49]** Okay, now this is where you can monitor your project. Okay, here you can view alerts, you can monitor the agents performance, quotas, and you can manage the resource.

**[1:17:07]** Okay, discover basically where you can discover like all the models available. Lets go to the home now. Once you are in the home, right, then you can basically see.

**[1:17:25]** Okay, API key project endpoint and Azure AI endpoint.

**[1:17:33]** Okay, even we can go to.

**[1:17:38]** Operate, we can go to admin.

**[1:17:45]** So it will show you like all the project. So we can navigate to a particular project.

**[1:17:55]** From here, OK, and you can see for this project, this is the endpoint.

**[1:18:03]** Okay, subscription ID, other information.

**[1:18:07]** Other informations can be view from here.

**[1:18:12]** If you want to go for the parent resource for A Foundry, this is the parent resource.

**[1:18:20]** Okay, now you can see there you have the endpoint, okay, and the API key, okay. So this is what we would be needed to connect to this, you know, foundry resource, okay.

**[1:18:39]** Right, okay.


### Recap & knowledge check  `[1:18:43]`

**[1:18:43]** So what we have done, we have created the foundry project, we deploy and test the generative AI model, we identify the project endpoints and the keys, correct? And we also have explorer the Microsoft Foundry extensions okay in the Visual Studio for the Visual Studio code.

**[1:19:02]** Okay.

**[1:19:04]** Now proceeding further, let's go for the knowledge check. Okay, so what do you have to do?

**[1:19:23]** Okay.

**[1:19:25]** How do we get the AI quota for our subscriptions to work with the AI workloads? OK, you can basically request for the quota. OK, if you don't have you know, AI quota for your subscriptions, right, you can request for the quota.

**[1:19:47]** Question number one.

**[1:19:52]** Okay, what you have to do is there are 3 questions. Okay, so I am going to basically display the questions and you have to type the you just have to answers like option A, option B, or option C. So A, this is the A Azure portal, which web portal should you use to work with assets in?

**[1:20:14]** Microsoft Foundry project, Azure portal, Microsoft Copilot, or Microsoft Foundry portal? OK, let me know on the chat.

**[1:20:24]** Is it option A, B, or C?

**[1:20:37]** Yes.

**[1:20:41]** Okay, Microsoft Foundry project. So the right option is it's a Microsoft Foundry portal. Okay, so Microsoft Foundry portal is basically where this is where the developers basically work with the foundry.

**[1:21:00]** Project models, agents, tool, knowledge, deployments.

**[1:21:08]** Okay.

**[1:21:10]** Azure Portal is basically used for creating and managing Azure resources.

**[1:21:16]** Okay.

**[1:21:18]** For creating day to day, creating and managing Azure resources, but the Foundry portal is basically where the developers work with the.

**[1:21:31]** Yeah.

**[1:21:33]** AI solutions.

**[1:21:37]** Next is question number 2.

**[1:21:46]** Which component of Microsoft Foundry provides a prebuilt service for common AI task? Foundry tools, Foundry models, or Foundry IQ?

**[1:22:13]** OK, so question number 2, all of you says OK, A or some of you think that its a B. OK, so what is the correct one? Its a A actually OK, which is a foundry foundry tool. OK, the foundry tool is basically which provides a.

**[1:22:34]** Ready Made a I capabilities or a prebuilt services for common a I task. Okay, now for example, language for speech for translator, okay, document intelligence and so.

**[1:22:51]** Boundary models are basically these are the large language models.

**[1:22:56]** Okay, these are the large language models.

**[1:23:00]** Okay, which is used for your AI applications and your AI agents.

**[1:23:07]** Question number 3.

**[1:23:13]** Which extension should you use in a Visual Studio Code to work with the Foundry project?

**[1:23:32]** Okay, everyone agree with the C? Yes. So now it is basically Microsoft Foundry Toolkit. Okay, Foundry Toolkit extension. As you can see, this is a foundry foundry toolkit, right? And just right now, let me refresh it.

**[1:23:56]** OK, now did you see we have deployed this model right in this project? So it shows that model over here, right? And lets say I want to test this model in a playground.

**[1:24:09]** Okay, so from here you can see right, you can view the deployment info, deployment information here, right? You can see the endpoint information like there's a target URI and keys, right? And also I can open playground. Let me click on this playground.

**[1:24:29]** OK, so model is loading. You can provide the system prompt.

**[1:24:34]** Right, you can also provide other parameter from here and then right I can. Use this like let me say hi.

**[1:24:53]** Today, okay, provide instructions with the relevant context to guide the system response out there.

**[1:25:00]** Okay, so I will say you help.

**[1:25:05]** People planned.

**[1:25:09]** Your help.

**[1:25:12]** People.

**[1:25:22]** Okay, let me ask.

**[1:25:30]** Okay, right, I am just asking the same like hi, how, hello, how can I help you today? Now see hi again. Are you planning a trip or looking for travel advice? Let me know how I can help, right? Do you see the response changed based on what you provide in the system prompt?

**[1:25:49]** You can basically, you don't have to switch to the Microsoft Foundry portal. You can basically, as a developer, you can use the foundry toolkits right and use your Visual Studio code.


### Selecting & deploying models  `[1:26:10]`

**[1:26:10]** Okay, so guys, over here we will be taking before we jump to the next topic. Okay, nowhere we will understand how to select, how to deploy, and how to evaluate the Microsoft Foundry models. So before we talk about this topic, we will be taking 10 minutes break. So let me start the time here.

**[1:26:31]** Right, if you have any questions, feel free to drop in the chat.

**[1:26:37]** And just start the timer. I'll see you after 10 minutes. Thank you.

**[1:37:15]** Okay, so I'm back. Okay, let me.

**[1:37:21]** Let me see.

**[1:37:25]** Okay, when do we get the lab access to Microsoft AI Foundry? Okay, so.

**[1:37:33]** To is I'll share with you the...

**[1:37:37]** Lab environments.

**[1:37:46]** Lab access.

**[1:37:52]** Okay, guys, can you check? Are you able to mark your attendance?

**[1:38:19]** Yes, everyone. Okay, I think the issue is resolved now.

**[1:38:25]** Okay.

**[1:38:38]** Okay, just give me a second.

**[1:39:02]** Okay.

**[1:39:14]** Okay, attendance link. Okay, first let me share with you the lab access detail. Okay, so.

**[1:39:33]** OK, so here I'm sharing. Yeah, I'm sharing the lab details.

**[1:39:46]** OK, and also let me show you.

**[1:39:50]** How you can access along with this? Let me share with you the attendance URL.

**[1:40:05]** Okay, so here's the attendance URL.

**[1:40:20]** Attendance link is not accessible right now also.

**[1:40:27]** Okay, could you could you try to use any other device because I think it's working for most of them.

**[1:41:04]** Okay.

**[1:41:09]** Okay.

**[1:41:22]** Okay, so let me share my screen, let me paste the QR code again.

**[1:41:42]** What is the training key? Yeah, training key is there in the chat.

**[1:41:48]** If you see at the top, there's a training key.

**[1:41:53]** Okay.


### Lab environment walkthrough  `[1:41:59]`

**[1:41:59]** Okay, so now let me walk you through, let me share my screen and walk you through the lab environments.

**[1:42:16]** Alright, so first thing what you have to do is you have to navigate to this URL, OK, GSI Don dot GSI dot learn on demand.net. Let me paste here.

**[1:42:34]** Okay, click on sign in once you click on sign in.

**[1:42:39]** Yes, everyone, please pay attention.

**[1:42:42]** So then you have 3 options here. Okay, I am demonstrating like how to get access to your lab environments, how to redeem your the training key. So you get 3 options out there. Okay, go for the Microsoft account. If you are using your corporate machines, maybe you know you are not allowed to use your personal personal account. So in that case.

**[1:43:03]** Go for the intra ID where you'll use your corporate ID.

**[1:43:08]** Okay, use your corporate ID for intry ID for Microsoft account, use the personal one. So I'm going to use the personal, so let me click on this Microsoft account.

**[1:43:20]** Okay, the process would be same. Let me sign in with my personal so.

**[1:43:30]** Okay, now once you have sign in, okay, in your case it would be blank and then you can see like in my training, we don't see this options to redeem training key, click on my training. Once you click on my training, you can see this options redeem training key.

**[1:43:50]** So copy the training key.

**[1:43:56]** Okay, so this is basically for the lab. So click on this and click on redeem training key. Now once you click on this.

**[1:44:08]** Okay, then you can see over here right basic informations right Microsoft end user license agreement. So right now you don't see an options to launch your lab. Okay, once you click on view agreement, click on agree.

**[1:44:26]** Click on agree.

**[1:44:29]** Right, once you click on agree.

**[1:44:37]** Okay, just a minute guys.

**[1:44:40]** Just give me a second.

**[1:45:02]** Okay, I am not sure for this error. Are you getting this error on the intro ID or the Microsoft account? Okay, so if personal Microsoft account does not work, then use your corporate corporate ID.

**[1:45:18]** Okay, one more thing here guys, just give me, give me a second here before you redeem the training key. Okay, just give me a second.

**[1:45:32]** There are basically 2 batches.

**[1:46:22]** Okay, guys, wait if you don't use the training training key. Okay, don't use the training key as of now.

**[1:46:30]** OK, just click on sign in and don't use the training key. I'll let you know which training key you need to use.

**[1:46:53]** Okay, alright guys, use this training key. Okay, I'm just providing you the training key and also I'm modifying.

**[1:47:08]** Okay, if you have already redeem it, okay, let it be.

**[1:47:13]** OK, if you haven't redeemed the training key, use this training key.

**[1:47:18]** Okay, use this training key. Now what happened is basically there are 2 sessions okay going simultaneously for the a I103. So that's why you know it shows if you have redeemed the previous training key, it will basically ask you to wait for you know 4 hours.

**[1:47:39]** Okay, but once you redeem with this training key, right, you basically get the access immediately. You don't have to wait for 4 hours. You have the access to the lab environments immediately. Okay, so let me share my screen.

**[1:47:56]** Okay, now once you once you have redeemed training key, right, and then once you click on view agreement, then you can see the interactive labs, okay, and you can see the number number of labs out there. So overall you can see we have 22 labs.

**[1:48:13]** OK, 22 labs that you will be performing for the 4 modules. So here you can see you have 10 attempts. OK, so once you click on launch, this is your first lab.

**[1:48:28]** Click on launch.

**[1:48:30]** It will take 3 minutes okay to build your lab environments and then it will be available for you to perform the hands on.

**[1:48:43]** Okay, I have already redeemed the training key. Okay, no worry, you just have to wait over here like for 4 hours, okay. After that, you can see this button available to you and you can launch your lab if you have already redeemed the previous training key.

**[1:49:03]** Okay, I have already remade. Okay, rem the training key.

**[1:49:10]** Okay, I am able to do with personal Microsoft account. Personal Microsoft account worked personal accounts not working as well. Okay, if personal is not working, go for intra ID, okay.

**[1:49:24]** Can you share the logging details again? I'm sharing the instructions again.

**[1:49:38]** Okay, all right, let me take some questions.

**[1:49:49]** Okay, let me take the questions.

**[1:49:55]** Okay, first is done, right? When do we get lab access to Microsoft AI Foundry? So now you have access to your lab, okay, and you can launch and you can perform them. So every every time you have to login with the same same credentials. Okay, second is what is how this is different from using Microsoft.

**[1:50:17]** Copilot Studio to build an agent.

**[1:50:20]** Okay, now basically the difference is based on the based on the target users, the level of control, and the development style. So AI Foundry is mainly basically for the developers and AI engineer.

**[1:50:42]** Who want to build a custom a I apps and agents with more control, whereas Microsoft Copilot Studio it's mainly used for business users and makers who want to build the agents faster using the low code tool.

**[1:51:00]** Okay, so both can be used to built in agents, but the difference over here is basically low code and the Microsoft AI Foundry is basically for the developer, right? Where you need a deep customizations, you want advanced model control, you want.

**[1:51:07]** Yes.

**[1:51:19]** More custom applications, indications, okay. If you want to go beyond like what is available in the Microsoft Studio, because Microsoft Studio is basically sorry, Copilot Studio is basically used to build the agents like where you need fast, you want to speed, you want low code developments, right?

**[1:51:39]** Without extensive, basically for the maker. So the Copilot Studio is basically for makers, okay, who want to quickly want to build an AI agents without extensive programming knowledge, okay. And the kind of controls you need more controls over the orchestration, the AI models.

**[1:52:01]** Okay, then for that you'll go for the Zero A Foundry.

**[1:52:07]** OK.

**[1:52:10]** Then next is once we deploy model and if we need to use it in the project, what control we have over that pre trained LLM model? Like how do we evaluate hallucinations, guardrails, validations? What happened when the model versions gets updated or retired?

**[1:52:31]** Okay, if we need to use this in a project, what control we have over the pre trained LLM model?

**[1:52:38]** Work control. OK, now you don't have control on the internal model weight, OK, unless you fine tune the model, but you can control the application layer around the model. It means you can control like how the model is.

**[1:52:58]** Prompted, what data it can use, what tool it can call, okay, how it answers, how it answers are evaluated.

**[1:53:08]** Okay, about safety checks and things before and after the response. Okay, so you basically you can control the prompts and system instructions, you can control the model parameters, like you can control settings of like temperatures, maximum tokens.

**[1:53:29]** Okay, other various parameters you can control grounding, okay, like grounding data like you which data source you want to connect to. Okay, so all of this you can do on the application layer. you can.

**[1:53:47]** You can control, but you don't have a control over the internal model weight.

**[1:53:57]** What happened when the model versions get updated or retire?

**[1:54:01]** Now when model versions get updated and retire, basically you have options out there like do you want to like for example when you deploy when you deploy your model. So you have basically settings like 3 settings you have okay you have auto update or.

**[1:54:22]** Default versions, manual update or current versions. So it means if you enable auto update so your deployment can move to the newer, newer default versions.

**[1:54:39]** Okay, whenever there's a new updates about the model, so automatically right your solution basically use the latest model.

**[1:54:48]** Sure, just Shari, to stop, if you can just bring it in the screen and help us in these questions, I think would be more clear.

**[1:54:59]** Okay, sure.

**[1:55:02]** Lets do one thing, I will take this questions, okay, lets discuss on this later. Okay, first let me take through the content, okay, what we are supposed to cover, and then I will take a look into I will cover that later. Okay, so I hope everyone done with the lab access.

**[1:55:24]** All good with lab. Let me quickly walk you through the lab environments, OK, and then we'll get into our next topic. So once we are here.

**[1:55:34]** Okay, once you're here, so you'll see once you launch your lab, so you'll get over here. First thing you need to log into your virtual machine. So for this.

**[1:55:48]** Use the use the password given here or you can go to the instructions. You can see to sign in into your Windows. Once you there, you can see your Visual Studio Code. This is there. Okay, now scroll down, go to next. Okay, read the instructions over here carefully, go to next.

**[1:56:07]** Right, and the first lab is basically prepare for an AI development project. Okay, so it take approximately 30 minutes. Okay, overall time is like 56 minutes.

**[1:56:21]** Okay, so you have basically one one hour, okay, one hour to perform this is a maximum maximum time after that. Okay, this labs gets closed.

**[1:56:33]** Okay, so once this is done, so every every time you launch, okay, that's a new instance of the VM, it will not save any progress.

**[1:56:43]** OK, so every every time you launch the lab, like for example, if you launch this lab, OK, or even if you launch this lab later, like once you complete once, if you relaunch it again, so it will be new instances out there.

**[1:56:58]** Okay, new instances, it means like you the nothing would be save over there. Okay, so it is basically some hints on where first you will be creating a Microsoft Founding project and these are the instructions that you would be following.

**[1:57:16]** OK, like for example, it says OK, web browser, open the web browser.

**[1:57:22]** Okay, this is a web browser on the VM, right? And then go to ai.azure.com, okay?

**[1:57:31]** Right, and then click on sign in. The credentials that you gonna use here right is provided here. You can see the credentials and the password, and you can access this on the resources tab as well. Once you navigate to the resources, then from here right you can see this username.

**[1:57:51]** And justice, you have to click on this icon keyboard icons, which will automatically copy and paste in the.

**[1:58:00]** Your VM and you need to use tab here.

**[1:58:06]** Temporary access pass, click on sign in.

**[1:58:10]** Okay, if you use the password then you might need to perform some multifactor authentication. So let me click on sign in.

**[1:58:21]** OK, so done, right? We are inside the foundry foundry portal. OK, we are inside the foundry Microsoft Foundry and then from here you will click on new foundry.

**[1:58:32]** Alright, you can see there.

**[1:58:36]** Okay, explain the advance options if so new project options, then create a new project with the project name. So you have to provide the same project name as given over here. So we'll be creating a new project.

**[1:58:49]** So new project. So from here, create a new project.

**[1:58:57]** And then here you'll be providing this project.

**[1:59:06]** Okay, and follow the instructions if you write. For example, if you try to, for example, let me go click on create.

**[1:59:25]** Okay, did you see it give you an error?

**[1:59:29]** Okay, you are getting failed to create resource project resource was disallowed by.

**[1:59:36]** The lab, okay, so because the policy right, you have to stick with the name, same name given in the instructions, you have to strictly follow the instructions there.

**[1:59:50]** OK, like for example, what I missed previously, create a new project.

**[1:59:56]** And then it was the project name. I have to give the same project name.

**[2:00:04]** OK, and then you can see here foundry resource it same right subscription, then resource group, I have to select the resource group one. So there is already a resource group. So I have to select this resource group. If there is any other resource group right, then it will throw an error because the policy.

**[2:00:25]** OK, and then select any of the AI foundry recommendation. OK, so I'll just keep us to let me click on create, then wait for so as you perform it, like click on this.

**[2:00:39]** Click on this check box.

**[2:00:41]** OK, select create, wait for your project to be created. When it's ready, the project home page will open.

**[2:00:48]** Okay, likewise you deploy and test the model.

**[2:00:53]** Okay, view the Foundry resource and project endpoint.

**[2:00:59]** OK, then install the Microsoft Foundry tool extension for Visual Studio.

**[2:01:05]** So it has already a Visual Studio Code. So for example, start a Visual Studio Code, then navigate to the extension, then search for Foundry toolkit.

**[2:01:22]** Foundry toolkit for the VSU record install.

**[2:01:33]** Okay, so then in the Foundry Toolkit pane, explain Microsoft Foundry resource and set the default project by connecting to Azure and select the foundry project you created previously.

**[2:01:48]** Okay, so this is what you will be doing like after you perform it, right? Clean up and then you can go and you can end.

**[2:01:59]** You can make a full screen by clicking on this option. This will make the full screen so you have more space to work. You can also right, increase or decrease the size of the instruction instruction pane.

**[2:02:16]** Okay, sometime because of internet if it's...

**[2:02:21]** You know, there's issues with...

**[2:02:25]** The it's lagging or it's not reacting, so you can always go and you can click on reconnect.

**[2:02:35]** Reconnect options.

**[2:02:39]** Okay, reconnect again. It will ask for the password.

**[2:02:49]** Okay, and once you have done right, you can click on end and then click on end my lab and mark it as complete. So you have to complete this okay within that hour which is given over here. Okay, that's the maximum maximum time you have, although each lab will take like.

**[2:03:09]** Depending on different labs has different.

**[2:03:14]** Time OK, this exercise take approximately 30 minutes. OK, this VM would be available to you for like 4049 minutes, 49 minutes is remaining. After that, it will close automatically. Once you have completed it, click on this and end my lab and mark it as complete and click OK.

**[2:03:37]** Okay, how would you rate this lab? Okay.

**[2:03:42]** Thank you and provide you.

**[2:03:45]** Done. Okay, so now you see we have 9 attempts remaining. Each lab can be launched 10 times and the validity of lab is basically for the next 6 months.

**[2:04:03]** Okay, so the validity is for the next 6 months.

**[2:04:11]** Okay, clear. Let me see if you have any questions here.

**[2:04:19]** Resource creations blocked by policy. Okay, now there's some issues out there may be related with the region.

**[2:04:30]** It is most likely with the region. Okay, central US instead of central US, go for East US 2 or.

**[2:04:42]** Sweetened. So it's just a minute, let me get the.

**[2:04:51]** Second.

**[2:05:02]** Just a minute, I'll give you the foundry list.

**[2:05:29]** Okay, so Foundry is currently available in the following Azure region. Okay, so you can select from this region. I usually keep it default and it's usually East US 2 in my case.

**[2:06:02]** Actually, I have tried couple of them on that list, but doesn't looks like it's not working.

**[2:06:14]** Okay, can you quickly share the screen?

**[2:06:20]** Yeah.

**[2:06:29]** See my screen.

**[2:06:31]** Yes, okay. Can you retry once? Let me see. Okay, close this. Close this.

**[2:06:41]** Okay, just a minute. Close this.

**[2:06:46]** Go to the Microsoft Foundry homepage.

**[2:06:58]** Okay, start from scratch. Okay, open a new tab, close this Microsoft foundry. Okay, lets go for yeah, close the previous one, go for ai.azure.com.

**[2:07:11]** Okay, guys, everyone, because most likely you would face this challenge.

**[2:07:16]** Okay, you will you'll get this challenge.

**[2:07:21]** The moment I open it comes with this page, so but looks like the project name is not matching, so I should be using my own project name, correct?

**[2:07:35]** No, you need to use this project name which is given here like project in the instructions, give the same project name in the instruction.

**[2:07:44]** No. So you see this, the project name is ending with 334, but it is saying 334-7854. So this is defaulting some other project name.

**[2:07:59]** Can you change? Can you change that?

**[2:08:01]** Yeah, so if I just delete this one and fill it up with the new the one as it is given there, then resource found your resource seems okay. Subscription I only have one which is auto selected resource is also one so.

**[2:08:02]** Yeah.

**[2:08:21]** Is coming default to Sweden Central. Lets say if I do East US 2, yeah, I tried actually multiple centrally.

**[2:08:33]** Okay, now what happened is resource creation for the project blocked by policy.

**[2:08:43]** Okay.

**[2:08:46]** Next page of the instructions shows which project name. Okay.

**[2:08:54]** Just a minute.

**[2:08:57]** Mhm.

**[2:08:58]** Can you close this?

**[2:09:02]** Rishikesh.

**[2:09:04]** Say something next page of the instruction shows which project name, okay.

**[2:09:13]** Can you go to portal.azure.com once?

**[2:09:17]** In the new tab.

**[2:09:19]** Go to portal.azure.com.

**[2:09:27]** K.

**[2:09:32]** This is coming outside of.

**[2:09:37]** Yeah, use insights your VM.

**[2:09:38]** So.

**[2:09:40]** This is coming outside of it.

**[2:09:41]** Close. Yeah, close this. Okay, now go for portal.sio.com here.

**[2:09:52]** OK, just want to check if the resource is already created.

**[2:09:58]** So portal.azure.com.

**[2:10:17]** Okay, can you click on the resource book?

**[2:10:22]** And then navigate, there's a resource drop down.

**[2:10:26]** Mhm.

**[2:10:27]** Click on this.

**[2:10:32]** OK, can you click on the resource group one?

**[2:10:40]** Okay, as of now there is no resource, its empty. Okay, yeah, open, go to that a dot hotel.sio.com.

**[2:10:53]** Go to the previous one.

**[2:10:56]** The Foundry.

**[2:10:59]** Click on create project.

**[2:11:05]** Okay.

**[2:11:09]** Yeah, keep the project name.

**[2:11:31]** Mhm.

**[2:11:32]** Resource group is fine. Project is also fine. Sweden Central is also fine.

**[2:11:41]** Just a minute.

**[2:11:44]** Can you can you is there is options to can you untoggle this one, set up the recommended resource?

**[2:11:57]** OK, then click on create.

**[2:11:57]** Yeah.

**[2:12:23]** Yes, creating, I think.

**[2:12:26]** Okay.

**[2:12:28]** Okay, let's let's wait here. Do let me know if you still have any issues out there. Okay, that there only the options like there was toggle button. I think because of that you're getting this issue.

**[2:12:42]** But why is that any reason? Why is that toggle or that button was stopping any or is anybody else facing the same thing?

**[2:12:55]** I think Rishikesh basically says something next page of the instruction shows which project should be given. Okay, actually the interface you're getting like while creating the project, okay, that's different from me. When I when I did that, I didn't get that toggle button out there.

**[2:13:17]** okay.

**[2:13:20]** So other basically can.

**[2:13:24]** If anyone getting that toggle button out there, right? So basically what you have to do, you have to turn off and I'll also take a look into that.

**[2:13:35]** Okay, set up recommended resource. Okay, set up the recommended resource. Okay, so basically what you have to do, you have to strict with what is given in the instructions. Okay, the resource group, the project name, everything has to be same otherwise, there would be issues with the creating.

**[2:13:53]** Resources and your project.

**[2:13:56]** OK, lets proceed further.

**[2:13:56]** Yeah.

**[2:13:58]** Thanks. Yeah, it's working now, okay.

**[2:13:59]** Yeah, okay.


### Select, deploy & evaluate a Foundry model  `[2:14:15]`

**[2:14:15]** Okay, so guys, let's proceed further, select, deploy, and evaluate the Microsoft Foundry model.

**[2:14:29]** Okay, so explorer the model catalogue foundry model sold directly by Azure. Okay, now what is the playground? Okay, what do you see? Sorry, just a minute, its not the one. Okay, first you have to explorer the model catalogue.

**[2:14:49]** Okay, foundry model sold directly by the Azure, like for example, open a I models and more. It is built directly through the Azure like you basically would be paying through the subscriptions out there. Okay. And then we have foundry model okay from partners and community. Okay, now these are the models from the trusted.

**[2:15:09]** 3rd parties okay and purchase from the models provider. So maybe you need to go and you need to get the subscription separate subscription for those models out there okay for the models from the other 3rd parties out there now for direct model so direct model.

**[2:15:29]** By Microsoft, okay, it would be basically built directly through the Azure subscription.

**[2:15:35]** Next is you can search and filter by OK curated collections, model capabilities, source, inference task, fine tuning support, and industry. Now whenever whenever you go to your model, like for example, find model.

**[2:15:52]** Okay, now from here, right, you can select over here like based on different collections, okay, it is direct from the Azure, right? So these are basically direct from the Azure, from Foundry Lab, from Hugging Face, from fire fireworks on Foundry and based on capabilities for fine tuning.

**[2:16:12]** Reasonings.

**[2:16:15]** Okay, a tool calling right based on the different sources.

**[2:16:20]** Sources like for example, model from meta.

**[2:16:27]** Now there's 22 model from Meta, okay, similarly anthropic. So there are basically 7 models from the anthropic. So you can select from the source based on the inference task, okay, based on fine tuning tuning methods.

**[2:16:48]** Okay, and based on the industry like for manufacturing, there is no such model for retail.

**[2:16:59]** Consumer goods.

**[2:17:03]** Okay.

**[2:17:07]** Industry, okay, specifically for industry as of now.

**[2:17:13]** It doesn't have cannot find the models out there where so basically based on the different you can filter the models okay, you can search and filter the models by model capabilities, the source inference, fine tuning support and by the industry out there.

**[2:17:32]** As you can see here.

**[2:17:36]** OK, next thing is select the model using benchmark.

**[2:17:43]** Okay, select the model using the benchmark.

**[2:17:48]** So you can compare some models out there like that's for sure. Like before you go ahead and deploy deploy your models, right? You want to basically identify like you have basically lets say 405 100 models out there, then how you would select the appropriate model for you.

**[2:18:08]** Okay, so what you can do is you can click on the compare model, okay, view leadership board, okay, if you go to compare model.

**[2:18:20]** Okay, so you can basically have a comparisons.

**[2:18:24]** Okay, you can have a comparisons between the model.

**[2:18:29]** Okay, based on quality, safety, estimated cost, throughputs, input, output.

**[2:18:36]** Context endpoints supporting features. So you can see through here comparison between GPT 5 and GPT 4O. Let's remove it. I just want to compare 2 models. Let's say I want to compare another model which is let's say.

**[2:18:56]** Let's say this model.

**[2:18:59]** Okay, so for this we don't have metrics for any models to see the metrics we can go for search for GBT for example 4.1, this is what you will be using most of the time. Okay, then we can go and we can click on the benchmark.

**[2:19:19]** Okay, now this are the benchmark. This is a quality index, okay, latency, okay, benchmark cost, safety, throughput.

**[2:19:32]** Okay, if you scroll down, so it shows you the comparing similar models benchmark, so you can compare, compare models over here. So this is showing you for the this particular benchmark for this particular model, right? and.

**[2:19:50]** To compare some models, we can go and we can compare from here.

**[2:19:55]** Right.

**[2:19:59]** We can have a comparison between this, right, based on quality, okay, quality quality index, higher is better safety, okay, attack success rate, lower is better, throughput output tokens per second, which is higher is better, and the cost, which is USD per 1,000,000 token.

**[2:20:18]** Lower is better.

**[2:20:20]** Okay, now this is basically how we can compare like in a column to compare it with the graph, we can go click on the view leaderboard.

**[2:20:35]** We can go to leaderboard and you can see over here based on quality, safety, throughput benchmark. So we can see from here, OK, which has the highest quality which GPT 5.5 and Cloud Opus 4.4.6.

**[2:20:53]** 4 -6 OK this one from here you can choose which models you want to compare like for example I just want to compare like GPT 5.5 and the model which we are going to use is GPT 4.1 here OK and I will click on compare compare models it take you to the previous.

**[2:21:12]** One. So here from here you can navigate or you can also scroll down okay over here and you can choose like the models that you want to compare like for example 4.4.1 mini okay and 4.1 GPT 4.

**[2:21:32]** Okay, first let me remove all of them and only select GPT 4.1 and GPT 4, right? Okay, so now you can see the comparisons actually.

**[2:21:45]** Okay, so GPT 4.1 it has the lowest cost, correct? But also the quality index if you is lowest one, if you see it has the highest quality index but also the cost is higher.

**[2:22:06]** So, most attractive quadrant is this space over here, and you can compare the quality against the benchmark cost. You can compare the quality against the throughput.

**[2:22:20]** Okay, so in this case, this is the best. You can compare it against the safety, quality against the safety.

**[2:22:31]** Okay, so in this case, GPT 4.1 is good in terms of like safety and quality.

**[2:22:39]** Okay so attack success rate lower is better so it's lower so it's fall in the most attractive quadrant is this and you can choose from here the models that you want to compare.

**[2:22:52]** Okay, you want to compare the models, you can choose from here.

**[2:22:57]** Right, and then also you can see standard harmful behaviour, right? Contextual harmful behaviour, copyright violations. So you can see metrics for different different category for coding, okay, accuracy rate.

**[2:23:15]** For general knowledge.

**[2:23:19]** Okay, so accuracy is basically is highest of this model for question answering okay for groundness. So based on various various metrics, you can see this over here.

**[2:23:34]** Okay, you can explain it.

**[2:23:41]** OK, so you can select the models using the benchmark.

**[2:23:55]** Then next one is deploy the models to the.

**[2:23:59]** Endpoint.

**[2:24:02]** Okay, now deployment type. Whenever you deploy the models, you gets an options the on the this one deployment type. Okay, so depending on different region, okay, it will be these are the various options are there: global standards, global provisions.

**[2:24:21]** Global badge, okay, data zone standard, data zone provisions.

**[2:24:29]** Data zone batch standard regional provisions OK developers OK for fine tune models evaluations only.

**[2:24:40]** So, global standard for general workloads and highest quota.

**[2:24:45]** Where you need a predictable high throughputs.

**[2:24:50]** Global batch basically for large A Singh jobs.

**[2:24:55]** And if there is basically some compliances regarding with like data zone compliances.

**[2:25:01]** Like Europe, US.

**[2:25:04]** Okay, data zone and predictable throughputs.

**[2:25:09]** Regional compliances and low volumes, regional compliances and throughputs.

**[2:25:15]** So these are the various one. By default, we keep the global standard for general workloads and highest quota.

**[2:25:22]** What is highest quota?

**[2:25:28]** Highest quota means you will be getting the maximum.

**[2:25:34]** Like for example.

**[2:25:40]** Every Azure regions basically have some quotas limit.

**[2:25:45]** OK, like the number of tokens.

**[2:25:50]** Okay, when you deploy your models okay for that particular region, okay, so you basically gets a quota for that region.

**[2:25:59]** And if you set the global standard, you will be getting the highest quota for that reason. Okay, so they would not be. I mean, like what happened is like when once the quota limit is reached, okay, it will basically throw an error. So whenever you make a query, so it will says the you are out of the quota limits.

**[2:26:19]** Okay, so we can basically request for more quotas out there, but by default, global standard basically gets the highest quotas are there.

**[2:26:31]** Where do we get to know their the highest quota? As in when we are deploying a model, selecting this deployment type, do we know which highest quota or the number of tokens which to be confused consumed to set a limit or to know the limitation?

**[2:26:51]** Yes, you do here like you can see tokens per minutes rate limits, OK.

**[2:26:56]** Okay, so 16300 is the max ice quota as such.

**[2:27:01]** Correct.

**[2:27:03]** Correct, correct for this particular regions and for this particular deployment type. So it depend on the regions as well like which regions you are deploying it.

**[2:27:03]** Okay.

**[2:27:15]** OK.

**[2:27:20]** Give me a second here.

**[2:27:29]** Okay, so next one is evaluates the model performance.

**[2:27:36]** Okay, now for example, let's say you deploy a models like, but how we can evaluate whether the AI models is giving a safe or useful response before using it in the productions? Now there are basically 2 main ways to evaluate the model performance. One is the manual evaluations.

**[2:27:56]** Okay, second is the automated evaluations. In manual evaluations, we test the model responses directly in the playground.

**[2:28:08]** OK, so playground is basically where you can play with the models. OK, it allow us to enter prompt and basically check like how the models responds. OK, and we can also compare the model side by side. Let us say, for example, you have 3 models are there, 2 models are there, and you want to compare them for the same prompt.

**[2:28:27]** What is the output you are getting out there? OK, so we can ask the same questions to different models and then compare which response is more accurate, complete, and useful.

**[2:28:41]** OK, so here manual, you can compare the model side by side and it is helpful for early testing because the human can basically judge the quality, tone, reasoning, and relevance.

**[2:29:03]** OK, so for example, if you are basically building a customer support chatbot or agents, we can manually check whether the answer is polite, correct, or align with the company policy.

**[2:29:17]** OK, second option is a automated evaluation. Nowhere we use the synthetic data sets or your own data OK to evaluates your model.

**[2:29:30]** So it is at a scale.

**[2:29:33]** Right. And instead of checking the response manually, we can test like hundreds or thousands of the prompt automatically.

**[2:29:44]** Major responses based on the standard metrics. OK, so automated evaluations, major responses using the standard metrics. This metrics can include like accuracy, relevance, groundness, OK, safety, completeness.

**[2:30:04]** Okay, so for example, if you are building a document based assistant, we can test whether the model answer only from the provided documents and does not hallucinate.

**[2:30:19]** Okay, so evaluations help us identify the weakness before the deployment. So if we see here, okay, let's say first, for example, you have, let's go to the playground for let's go to build.

**[2:30:35]** And over here, let's go to the deployment and from here I can click on this 4.1.

**[2:30:50]** Okay, now from this playground right, I can chat right, I can go to the compare compare model option and then lets say I was I'm using GPT 4.1, GPT 4.1 and I want to test it with like GPT 4.1 mini.

**[2:31:10]** Okay, so now it is deploying this model GPT 4.1 mini. Okay, now you can see here.

**[2:31:19]** Okay, this is GPT 4.1 and this is GPT 4.1 mini okay and over here.

**[2:31:39]** Yes.

**[2:32:22]** Okay, so you can, this is the manual evaluations, right? Okay, where you can basically just the quality, the tone, the relevance reasonings, right?

**[2:32:37]** Okay, based based on your scenario, like for what purpose you're basically using this model, right? And then you can choose the best models to use in your applications.

**[2:33:02]** Okay, so we this is automated evaluation, so we don't have the evaluation found for this, but let's see, I'll just take a AI development project. Okay, now you can see over here we have this evaluation, okay, which is shown as the status of last run.

**[2:33:20]** Complete it.

**[2:33:25]** Okay, and over here now you can see here GPT 4.1.

**[2:33:31]** Okay, so.

**[2:33:35]** So you can see groundness 100% like for 40 prompts, there are for 40 prompts, you can see okay, the response we are getting is 40 out of them. 40 responses like groundness. This is what the customer satisfaction, coherence, deflections rate.

**[2:33:54]** Violence, self harm, in Narayan attack.

**[2:33:59]** Right, so we can basically.

**[2:34:02]** Evaluates on based on different metrics out there by automated evaluations.

**[2:34:11]** Okay, now same can be done for other models.

**[2:34:18]** Okay, other models which is deployed and then basically we can choose the models to deploy.

**[2:34:26]** OK, so manual evaluations help us inspect the model response directly, while automated evaluations help test the model quality at a scale. And for this, we can basically uploads the data sets, right? We can, we can upload the data sets.

**[2:34:48]** Like with the prompts or we can also generate the prompts out there, okay, within the automated evaluations.

**[2:35:00]** Can we just go back on the automated evaluation just to understand one more clear, how do we do that in terms of achieving the automated evaluation after the deployment?

**[2:35:17]** Okay, you mean this automated evaluation? So we'll click on create here.

**[2:35:19]** Yes, yeah.

**[2:35:23]** Yeah.

**[2:35:24]** Okay, now for example, you want to evaluate the model. Okay, choose your model for example. Okay, now I want to evaluate like GPT 4.1 mini, right? Next one is right data. Okay, so over here what we can do is we can generate the synthetic generations.

**[2:35:28]** Mhm.

**[2:35:43]** Okay, we can generate the generate the prompt. Okay, question will be automatically generated for each target when you submit the evaluations or if you have any existing data sets or if you want to import the chat completions. Okay, so you can also upload over here, like for example, I have this one.

**[2:36:05]** Okay, you can upload the new sample data.

**[2:36:20]** Okay, now for example, here you can see this data sets. Okay, these are the query actually the query I'm flying to Paris, New York next time. So this is related with the travel.

**[2:36:37]** OK, so for example, here I'll say generate the synthetic generations name of the new data sets.

**[2:36:49]** Demo.

**[2:36:52]** New data set OK 4.1 number of rows we'll keep here, let's say.

**[2:37:00]** Keep 10.

**[2:37:02]** And.

**[2:37:05]** OK, you will provide describe the data that you want to generate.

**[2:37:20]** Create.

**[2:37:24]** Create a prompt.

**[2:37:50]** Okay, or I'll just take.

**[2:37:54]** Just give me a second.

**[2:38:01]** Let me check the prompt from.

**[2:38:04]** Lab files.

**[2:38:27]** OK.

**[2:38:39]** Okay, so we'll basically create here.

**[2:38:43]** Prompt create various travel related questions and include some contained safety and security test.

**[2:38:50]** Okay, prescription for the data sets you can provide and then click on confirm.

**[2:39:15]** We will keep it default.

**[2:39:23]** I think and in developer.

**[2:39:26]** Okay, so we are basically creating, we are providing a system prompt. Okay, you are helpful travel assistant that provide accurate, detail, and practical travel advice to help user plan their trip.

**[2:39:41]** Okay, so let me save.

**[2:39:45]** Okay, now then you will basically choose the criteria. So what do you have first, right target model, right data, which is synthetic data we are basically generating from the AI, okay, that will be used to evaluate your model, okay, then we configure the model, right?

**[2:40:04]** And then we select the criteria over here. OK now.

**[2:40:10]** OK, for example, let's say quality, groundness, coherence, relevant, fluency, OK, safety, OK, customer satisfactions and deflections rate. And then once we set over here, we'll provide Sir valuations name demo EVL evaluations.

**[2:40:31]** Okay, and once we click on submit.

**[2:40:37]** Okay, so it will basically evaluates based on this different parameters and metrics.

**[2:40:50]** Okay, now once the evaluation it will take a while here it's in progress. So once we get the output so we can evaluate right 2 models over here we have done for the GPT 4.1 previously right and for the same number of over here we keep it 10. For the previous one there were 40.

**[2:41:11]** Prompts OK and it will basically gets you the results and based on that we can choose like which models to go further.

**[2:41:20]** Okay, so this is just to help us make a decision on which model to use it for our purpose.

**[2:41:30]** Yes, for your use your scenario. Okay, so it basically helps you to evaluates like the which model should you go for.

**[2:41:30]** And it was.

**[2:41:33]** Okay.

**[2:41:39]** It will not select consider that we have a model deployed and in a real time if we are using any using that model. For an example, I'm building a chatbot and through that chatbot, I'm using this LLM. Will the prompt or whatever the users are prompting in real time data, the prompts and response, all these are being.

**[2:42:04]** Captured and evaluated somewhere just to track for this subscription for this project.

**[2:42:10]** Upon using of this model, where exactly this gets evaluated or to track it?

**[2:42:10]** Yes.

**[2:42:20]** Yes, this would be this would be done out there. Just a minute, let me.

**[2:42:29]** You mean at the runtime, right? When people started using your applications, right?

**[2:42:32]** Yeah, the real time.

**[2:42:34]** Yes.

**[2:42:38]** The one which you have shown is kind of we are providing the data sets as synthetic way of providing the data set. But what if the real time upon the real time usage, the user prompts or response on keyboard iteration, all these have been also been a real time use case, right? So will they be able to track it and evaluate its performance?

**[2:43:01]** Or any other criteria.

**[2:43:06]** Okay, just a minute.

**[2:43:32]** Okay, actually more than evaluations over here. It's basically more monitoring here, right? You can see here in the in the operate section. Okay, now this is where you can monitors and you it give you the alerts.

**[2:43:49]** Okay, estimated cost, agent success rate, token users. Now these are the various things that you can monitor.

**[2:44:00]** Let me see if we can, I can find anything related with the real time evaluations, okay? But as of now, this is basically where we can monitors like what's happening with our agents and solutions.

**[2:44:18]** Yeah, this is different from the valuation, right? Like this is on monitoring. So just thought to understand from the evaluation standpoint, will it be a real time data on the valuation picture, will it be covering or not?

**[2:44:20]** Correct, correct.

**[2:44:32]** Okay, let me do my research and I will let you know tomorrow.

**[2:44:37]** Sure, yeah.

**[2:44:45]** OK, so this is next exercise here. OK, select deploy and evaluates the model. OK, so in this exercise you will explorer the models in the catalog, OK, compares the models using the model leadership board, leaderboard, right? And then you deploy the models.

**[2:45:05]** You compare the models in the model playground, and you evaluate the models with a synthetic data sets. OK, now this is your...

**[2:45:14]** We go to the lab environments, is the lab number 2.

**[2:45:27]** Yeah, this is the lab number 2. Explore models and evaluate the performance. Okay.

**[2:45:39]** Okay, let's take few questions from this topic.

**[2:45:51]** Question one.

**[2:45:57]** Me.

**[2:46:04]** Sign in with the personal Microsoft personal personal and entry is not allowed.

**[2:46:20]** Okay, so if you are facing issues with both Microsoft personal Microsoft and your corporate, okay, then you have to switch your device. Okay, use the use the personal device if you are not able to use both of those options.

**[2:47:07]** Okay, that's good questions, Rishikesh, who is calculating this values attack success rate.

**[2:47:15]** Who is doing the benchmark test on mobiles and will this come across multiple platforms?

**[2:47:24]** Okay.

**[2:47:29]** I just need to check on this, okay?

**[2:47:37]** Let me go through my research, okay, on this benchmark and I will let you know tomorrow, right, who exactly basically do this benchmark testing.

**[2:48:00]** How do these models understand the filters on data like the default there was option we are selecting while deployment default option like if we need to do the customization on it, how do we do that?

**[2:48:19]** Okay, customizations, I'll talk about this tomorrow. In tomorrow, tomorrow sessions, I'll talk about the customization part.

**[2:48:27]** Okay.

**[2:48:30]** OK.

**[2:48:34]** If you're getting this things out there, okay, that's network issues, okay, you can basically click on the options to reconnect, right? If that does not solve the issues, close the lab and relaunch again.

**[2:48:52]** Yeah.

**[2:48:53]** Okay, let's go for question number one.

**[2:48:58]** Which model benchmark indicates the model ability to process prompt and return comprehensive responses quickly?

**[2:49:21]** Okay, like quality index, cost, throughputs, the model's ability to process prompt okay and return a comprehensive responses quickly.

**[2:49:37]** So, like a speed.

**[2:49:41]** Which which model is P Which model is faster?

**[2:49:50]** Okay, so we have mix here, most of you says.

**[2:49:56]** See.

**[2:50:00]** And that's basically the correct answer. OK, now super basically it measure like how fast.

**[2:50:12]** A model can generate output.

**[2:50:20]** Okay, usually it's basically a tokens per second.

**[2:50:27]** Okay, like we have a kilometre per hour, right? That's basically like how we measure the speed. Okay, so similarly, right token per second, okay, higher throughput means.

**[2:50:45]** The faster response.

**[2:50:48]** Okay, now for example, if you're basically creating a real time chatbot, for example.

**[2:50:57]** Okay, definitely what you want to do is like you want peoples to people's to get faster responses.

**[2:51:07]** OK, then basically you will go and choose the model which has the highest throughput.

**[2:51:15]** OK, and you have to balance them actually, right? Not only just go for the highest throughput, but you also have to consider the cost. You have also have to consider the quality.

**[2:51:26]** Okay, so there should be a balance between all this benchmark, okay, and that's where you can basically compare through the leaderboard and you can conclude like which one to use. Question number 2.


### Knowledge checks  `[2:51:48]`

**[2:51:48]** Which deployment type in Microsoft Foundry is best for general use while offering the largest quota?

**[2:52:05]** Remember, we talk about the largest quota, which of this deployment type offers the largest quota?

**[2:52:23]** Yes, that's true. That's B, which is global standard.

**[2:52:30]** Question 3.

**[2:52:35]** Now, which evaluations metrics measures the linguistic correctness and natural language quality?

**[2:52:45]** It is fluency, groundedness, or relevance.

**[2:52:51]** Okay, linguistic correction, correctness, and natural language quality.

**[2:53:01]** Okay.

**[2:53:02]** Which evaluations metrics?

**[2:53:08]** Okay, so we have CA.

**[2:53:20]** Okay, now grammatically, right? Which which metrics basically it measure are the responses grammatically correct? Its natural, okay, or easy to read.

**[2:53:39]** Groundness, relevance, or fluency?

**[2:53:43]** Its option A guys, okay, fluency, okay, fluency. So relevance is basically how like whatever you have asked, okay, you are getting the responses like how relevance to that.

**[2:54:02]** OK, if I am asking something about like lets say soccer, OK, so how relevant it to basically what I have asked?

**[2:54:13]** Okay, groundness means like okay, is it basically the response is coming from like what I have offer is the data data knowledge?

**[2:54:22]** Data knowledge, okay, is the response is basically right coming from this like the data knowledge. So that's basically groundness like is my response is groundness to the data data source. Okay, so fluency is basically we check whether the response is.

**[2:54:43]** Grammatically correct.

**[2:54:46]** Okay, it's naturaler, natural language. Okay, natural.

**[2:54:52]** Okay, all right, yeah, thank you everyone for participations. Okay, the next thing is okay, what we have done here is now we have understood. Let me go to portal. Okay, now we have understood how to basically go, how to basically go to Microsoft.

**[2:55:12]** Foundry and create a project, how to deploy the model, how to test models, okay, how we can compare between like various models, how we can deploy it, after deploy how we can test it, right now the next thing is right comes the developer part where I need to use this model into my client applications.


### Develop a generative AI chat app  `[2:55:39]`

**[2:55:39]** Okay, client application. So develop a generative, develop a generative AI chat app with the Microsoft Foundry.

**[2:55:50]** OK, so explorer with the model playground, right? So it provides an interactive interactive model testing against platform.

**[2:56:01]** Okay, so where basically you can like developers can deploy models, they can try to deploy models before using them in the real applications. So in the playground, you can send the prompts to deploy model and see the response in real time, correct? You can also adjust the settings like.

**[2:56:21]** Temperature and maximum token.

**[2:56:24]** Okay, basically what does the temperature do? Temperature basically is used to control the creativity.

**[2:56:33]** Okay, so if you have higher temperature, like which will be zero to one, okay, if the if you set one, it means you are basically it give more like your model will give more creative responses. But if we kept the temperature as zero, so it will basically give you a...

**[2:56:55]** Predictable answers, right focus and predictable answers.

**[2:57:00]** OK, similarly, maximum token basically using this, we can control the maximum length of the model response. OK, now you don't want your users to get long paragraph like every every time in a prompt, OK, they ask something they're getting the.

**[2:57:19]** long paragraphs are there, you want to keep it short and simple. OK, so to the point. So that's basically where right you can set the maximum length of the like token token maximum token length.

**[2:57:36]** OK, add system message to customise the model behaviour, right? This is basically the instructions and system system message is the same. Now through this, we can define how the model should behave.

**[2:57:50]** Okay, we can tell but the model is like you are an assistant that help people find information, you are a helpful customer support assistant, and you answers people questions professionally.

**[2:58:03]** Okay, so you can basically...

**[2:58:07]** Guide or you can say you can provide the instructions that how does the how does the models respond? Okay, so experiment with different models and configurations, right?

**[2:58:25]** Then also from here, you can view the code samples, okay? You can view the code samples based on a Pi whether chat completion or response api okay in different programming languages, both with rest and SDK.

**[2:58:47]** Okay, so Playground basically allow you to experiment with different models and configurations and it show you sample code that you can view code samples you know based on the A Pi type or programming language whether they want to use the.

**[2:59:05]** Rest or REST API or SDK.

**[2:59:10]** Okay, and then they can basically move to the development.

**[2:59:17]** Okay, now when it's coming to choosing the endpoint and SDK.

**[2:59:23]** Okay, we have to endpoint here.

**[2:59:30]** Foundry project and Azure OpenEx. Give me a second.

**[2:59:37]** Okay, so we have Foundry project endpoint.

**[2:59:42]** OK, when you want to work inside the Microsoft Foundry project.

**[2:59:48]** Okay, and it uses the Microsoft Foundry SDK authentication is basically done with the Microsoft Intra ID. Okay, and the chat API is basically responses API.

**[3:00:07]** Okay, and it is best for foundry specific capabilities with OpenAI compatible interface for foundry direct model.

**[3:00:18]** The next one is Azure Open AI endpoint.

**[3:00:23]** It is used when you want to directly call the Azure Open AI models okay using the Open AI SDK authentication can be done using Microsoft Intra ID or API key.

**[3:00:40]** Okay, and this basically support both response and chat completion API.

**[3:00:49]** And this is best when the developers wants the latest OpenAI SDK models and features with the full OpenAI API surface.

**[3:01:07]** OK, so you can see over here the examples. OK, so.

**[3:01:15]** A I project.

**[3:01:17]** Client default Azure credentials. Okay, endpoint which is a Foundry project endpoint.

**[3:01:28]** Then open AI clients equal to open AI. So this is using the Azure Open AI endpoints with the A Pi key okay and the Azure Open AI endpoint.

**[3:01:45]** So the same we can see over here for our project, that's the project endpoint. OK, that's a foundry endpoint, foundry project endpoint, and this is the Azure Open a I endpoint.

**[3:02:02]** Okay.

**[3:02:11]** Now when it's come to the chat API, we have response API, right? We have response API and we have a chat completions API.

**[3:02:23]** So what's the difference here?

**[3:02:26]** Chat completions with the response API. Chat completion API. The state management is on the client side and developer store and sends the full message array.

**[3:02:39]** Whereas Response API is a server site, API store the thread automatically.

**[3:02:48]** Usually, when it's a system prompt, this is how the format you provides your prompt in.

**[3:02:56]** OK, so in chat completion API, you provide here role, OK, like system, then you provide the contain, then role user, OK, then provides the content.

**[3:03:09]** Whereas in a dedicated in response API, you have a dedicated parameter which just provides the instructions, you just write the instructions, and then you provides the instructions to it.

**[3:03:22]** So.

**[3:03:25]** Here, payload per request grow with the conversations length. So it means what you have to do is you have pre you have conversations, right? And then in new conversations, you have to also provide the previous conversations.

**[3:03:39]** Okay, then again you have to provide like in the new conversations, you have to provide the previous conversations out there.

**[3:03:49]** Okay.

**[3:03:51]** So.

**[3:03:54]** Whereas here is a constant, so only the latest input plus an ID. Okay, now for example.

**[3:04:15]** OK, one more thing here is this chat completion API, OK, it is a older API, OK.

**[3:04:23]** Okay, and it is the it is the whitelist widely used API pattern.

**[3:04:30]** Sorry.

**[3:04:32]** Just a minute.

**[3:04:35]** Hit marker, okay, whereas the response API is the newest one.

**[3:04:40]** Okay, this is the newest one. so.

**[3:04:47]** Okay.

**[3:04:51]** So if you come to the chat completion.

**[3:04:57]** EPI.

**[3:04:59]** So here the developer sends a list called as message.

**[3:05:06]** Okay, list. So inside this, we define the role.

**[3:05:14]** System.

**[3:05:22]** Content.

**[3:05:25]** And then we will say like you are a AI assistance that help people, you are a travel agent, okay, you are helpful assistance.

**[3:05:35]** Like this, okay, then next one here you define role.

**[3:05:41]** Okay, then this is the user user prompt.

**[3:05:46]** Okay, then content.

**[3:05:50]** And then you'll basically ask over here, OK, let's say what is.

**[3:05:56]** As your AI foundry.

**[3:06:04]** Okay, this one, this is chat completion API where you basically developers provides the they send the list call as message. Okay, where you basically provides the system prompt and the user prompt.

**[3:06:22]** And here the developer is basically responsible for managing the conversation history.

**[3:06:28]** Okay, so let's say if someone asks again, like let's say if you want to ask again.

**[3:06:39]** Right, new questions out there, okay.

**[3:06:45]** So we must add the new user message, okay, as with the previous one. So we have to keep the previous like what happen is like when you basically do this, so the...

**[3:07:03]** The model basically responds like user. Okay, role is basically...

**[3:07:12]** Assistant.

**[3:07:15]** Okay, and then it basically provides the content out there. So if you ask over here, okay, what is the Azure Foundry? And then if you ask like, okay, what can it do?

**[3:07:27]** So in this case, you have to also pass on the previous, okay, you have to keep the previous assistant response out there.

**[3:07:37]** So the conversion state is managed on the client side.

**[3:07:41]** Okay, whereas in case of your response API, okay, it will be something like this.

**[3:07:54]** OK, instead of manually managing full message array, so we can basically sense the latest input.

**[3:08:04]** Over here, it will be like response.

**[3:08:09]** OK, and you just provides over here the instructions, so you define instructions right and then input.

**[3:08:21]** Okay, so let's say you are a helpful assistance and in inputs you'll say, okay, what is Azure Foundry?

**[3:08:30]** Okay, and if you want to basically keep the conversations out there, right, so you just have to provide over here the.

**[3:08:42]** You just have to provides the last response ID.

**[3:08:51]** Okay.

**[3:08:53]** So here the API basically manage the conversations continuously, more easily.

**[3:09:00]** OK, and it which means the conversations state is managed on the server side.

**[3:09:07]** OK, so if we take a look at difference here, OK, that's what it says, state management. So client has to basically manage, developers has to store and sends the full message array here, server side API store the thread automatically.

**[3:09:25]** This is the...

**[3:09:28]** Older chat based api. OK, this is the new unified API.

**[3:09:34]** But how does it understand the whole context? Like in the older version, we know like we can save the conversation history up to and we can have a limited limitation on the conversation history like top 10, the last 10 histories can be shared as a context. But in response API, when it comes to the conversation ID, we are.

**[3:09:53]** Sending it and I we don't know like how does it track only last conversation will it be tracked or will it have the whole context? How do we understand that?

**[3:10:06]** Okay, it will basically track based on the ID, like whatever the conversations you have previously. Okay, so it will keep track of the with the help of this ID, actually like this ID.

**[3:10:23]** That ID was store only the last conversation.

**[3:10:23]** So it is basically known as the...

**[3:10:29]** Response ID.

**[3:10:33]** So actually what happened is like everything is basically like this ID contain all the conversations out there.

**[3:10:43]** Okay, not just the last one, okay, the previous what it refers to the previous one that also contain the previous one. So it's like a chain.

**[3:10:54]** For every individual users, when they start a thread, it will store any single ID, the whole context at the service side.

**[3:11:05]** Yes, it will, it will keep on in the for example.

**[3:11:15]** If you see here, just a minute, let me see if I can give you example.

**[3:11:24]** OK, so this is basically how we define out here.

**[3:11:30]** Okay, so now you can see the difference here. Okay, this is chat completions API, this is response API, okay.

**[3:11:41]** So it basically keep over here like you provide the instructions this way input input text here previous response ID equal to the last response ID.

**[3:11:51]** Okay, whereas here you provides the complete like the role system context like user okay completions models.

**[3:12:04]** Right, and then it basically use conversations message dot append role assistant assistant message.

**[3:12:13]** So this last response ID, that's a new property introduced on the response API to track it.

**[3:12:20]** Yes.

**[3:12:25]** Okay, and it this is going to be there like which model does it support or it will be there across all the models?

**[3:12:40]** In terms of understanding.

**[3:12:40]** It.

**[3:12:42]** so basically if we take a look here, okay, it will support all of them, okay? All the response response A Pi is basically all the models in the Foundry project, okay? The chat completions, okay, this is basically for open A I.

**[3:12:48]** All the models, okay.

**[3:12:56]** Okay.

**[3:13:02]** Okay, it's supposed for the OpenAI SDK Azure OpenAI.

**[3:13:05]** Mhm.

**[3:13:12]** Okay, now for example, if you see over here using the response API, okay, it is using response API, enter the prompts. Okay, what is the machine learning? Machine learning is a type of okay. After that, you ask over here, okay, can you give me an examples? Okay, certainly a simple example of this one. So.

**[3:13:32]** It is because of this one. It track the response for the next turn.

**[3:13:40]** Okay.

**[3:13:42]** Now, if you take a look here, this is an example using the chat completions API. Okay, what is Microsoft found? When was Microsoft found it right and who founded it? Okay, so over here, this is the chat completions a Pi is out there. So initial system message, then you loop until the user.

**[3:14:05]** Want to quit, then add the user message, get completions.

**[3:14:12]** OK assistant message then add the assistant message out there conversations messages dot append role assistant contain assistant messages.

**[3:14:30]** OK, so we have this exercise, create a generative AI chat app. In this exercise, you will create a Microsoft Foundry project, deploy a model, get the endpoints and keys, and create a client applications to chat with the model.

**[3:14:49]** So now we have already deploy a model. Okay, let's go to the project and over here we'll go for.

**[3:15:01]** The.

**[3:15:03]** Okay.

**[3:15:09]** Let's go for just minute Python.

**[3:15:18]** Okay.

**[3:15:32]** Just give me a second order.

**[3:15:53]** Okay, so we have chat app dot py.

**[3:16:00]** Okay, so this is Python Python script here and over here we have we have to provides the.

**[3:16:10]** Okay, open AI endpoint.

**[3:16:15]** OK and the deploy model which is GPT 4.1 and if I want to connect to the models which we have just deployed.

**[3:16:35]** A Foundry project.

**[3:16:39]** 01 and here is your open AI endpoint.

**[3:17:11]** Okay.

**[3:17:13]** And the model.

**[3:17:23]** OK, GPT 4.1.

**[3:17:31]** OK, so first we need to install all the libraries over here in requirement dot txt. OK, so this is the libraries that you need to be you need to install.

**[3:17:44]** Do you say this?

**[3:17:44]** Then.

**[3:17:47]** Right, okay, now first we will connect to the connect to the foundry.

**[3:17:55]** Right, so over here it will take the Azure OpenAI endpoints and the token.

**[3:18:00]** GPI key.

**[3:18:21]** Okay, instructions input previous response ID stream true. Okay, so this is basically for the for the stream streaming response out there. So you'll see stream equal to true. I'll show you in a while. So tool app let me.

**[3:18:40]** Open integrated terminal.

**[3:18:47]** Okay, now can you tell which API is being used here?

**[3:18:52]** Is it the chat completions API or is it the response API?

**[3:18:57]** Is on the response.

**[3:18:58]** Response API.

**[3:18:59]** In response.

**[3:19:00]** Correct. So this is a response API. Okay, now we define over here instructions and input, right? And this one basically this keep the track of the previous conversations out there. So if we remove that, right, every conversations would be a new conversations out there.

**[3:19:20]** Okay, so let me.

**[3:19:21]** But then one step and on the same thing, I just want to get it clarified. Like how do we track this last responsibility of the session get closed? Like for an example, a user tries to create a problem and then they were chatting and the session gets closed and if they are coming back.

**[3:19:39]** To the same chat, and if they are trying to make any prompt in the same chat, will we be able to track this last response?

**[3:19:48]** No, this is for the same same session.

**[3:19:52]** This only works for the same session.

**[3:19:52]** This would be for the...

**[3:19:54]** Yeah, correct, correct.

**[3:19:59]** Okay, so over here, let me run this.

**[3:20:17]** Yeah.

**[3:20:47]** Okay, where is Tesla located?

**[3:21:20]** Okay, now it is able to relate with the previous one. Okay, it does not have a single one.

**[3:21:28]** And state one by the shareholders. So you'll see here, right?

**[3:21:35]** Take you to the...

**[3:21:39]** Live experience.

**[3:21:43]** It's.

**[3:21:45]** So here, prepare for the AIAI development project, right? Then compare, generate, create a generative AI chat. OK, so now what you're gonna do is this is basically the same instructions you have in your lab. OK, first you gonna deploy a model, right? And then you'll create a...

**[3:22:06]** Client application to chat with the model.

**[3:22:09]** Okay, create it right. So here you will you'll download lab files, okay, these are ready made lab files that you need to download to your local folder and then you'll prepare the application configurations, right? And then you installs the.

**[3:22:30]** Requirements library is right in the in the requirement dot txt, right? And then first you will use the chat completions API to chat with the model.

**[3:22:41]** Okay.

**[3:22:46]** So to chat with the model and over here, right? This is basically the list that you'll provides.

**[3:22:54]** Okay, sorry.

**[3:23:03]** Okay, right. And then.

**[3:23:08]** Okay, yeah, this is what you provide here. Then over here you will be using easy login. Okay, easy easy logins to get access to the your foundry.

**[3:23:27]** Okay.

**[3:23:30]** Then next one year here, you'll be using the response API to chat with the model. OK, you'll be making the modifications over here, right? Changing the previous code with this, right? And over here, right over here, you'll test it, OK?

**[3:23:49]** When you test it, the app should response in a way that indicate it does not understand what it refers to. So the conversation context has been lost, right? And then next, here you'll add the conversations tracking, okay, with the...

**[3:24:06]** Track response. So you'll add over here previous response ID OK equal to last response ID.

**[3:24:15]** So this basically keep the context out there and you'll test it again, right? And then later on, you'll implement the streaming response.

**[3:24:26]** Okay, and then you'll use a asynchronous API.

**[3:24:30]** The last.

**[3:24:32]** Okay, so that's basically what you're gonna do in this, create a generative AI chat app.

**[3:24:39]** What is streaming response?

**[3:24:43]** Sorry.

**[3:24:44]** What is streaming response?

**[3:24:47]** Streaming Streaming means like whenever whenever we interact with any application, so it is like getting line by line, okay, you are getting the response line by line, like it seems like moving the letters are moving. So that is basically the streaming response.

**[3:24:48]** Hello.

**[3:24:57]** Okay.

**[3:25:01]** Yeah.

**[3:25:05]** Okay.

**[3:25:15]** Okay, so lets take this knowledge check again, okay, quickly.

**[3:25:27]** Okay, so always go for the response API. Okay, always go for the response API. That's basically what's used for the new applications out there, but it's also good to know how basically the chat completions API used, but you will use the.

**[3:25:47]** Response API, which is more efficient in terms of the token utilizations and in terms of the context.

**[3:25:58]** Will it not like for case to case? Will it vary right? Like for response API to save the tokens, it will be helpful when the user is on the current session. But if the user wants to continue something and if they come back once the session gets closed, then how the response API can help?

**[3:26:18]** To retain the context.

**[3:26:22]** In that case, you have to implement some some memory and you have to store the response in other other memories out there. So that's a that's a different different part.

**[3:26:35]** So still the property of sending the whole context like there in the chat completion, we have the conversation history messages to send to retain the context. But in this response API, do we have a property to send the conversation?

**[3:26:54]** Again, come again.

**[3:26:54]** You have shown me an example, right? Like code of the response API where the properties of chat completion owns the properties to add the append the chat conversation histories and whereas in response API, do we have that option?

**[3:27:01]** Mhm.

**[3:27:11]** We basically gets the ID only like whatever the conversations you have from the previous one, okay? We gets the ID from the previous, previous conversations which basically you know, keep the conversations context, okay? But that's again in the same, same sessions out there.

**[3:27:25]** I think we have.

**[3:27:29]** Exactly. So that's where my question lies. So in the chat completion, even if the session goes out, if the user wants to come back, consider that we have a cache or something memory that holds the conversation and that conversation details can be upended into the chat completion where the system.

**[3:27:49]** User role and then there is a property to define the conversation message and then send to pick up the context of it. But whereas in the response API here, do we have such options to send the data with the property message to retain the context?

**[3:28:10]** Back when the session gets closed.

**[3:28:15]** I just need to check on the sessions one, okay, because that's that's you have to implement on the developer, developer sites out there, okay, by maintaining the memory.

**[3:28:29]** Yeah, I understood that consider that we have the memory and we have maintained it. But what I am asking is, do we have a property like how in the chat completion we have a message to append? There is an option to append the message details, conversation message details, and that would retain the context of earlier history even when the session gets closed.

**[3:28:49]** But in the response API, do we have that option like how the response ID is being option for trying to get the data? Similarly, do we have option of conversation messages to be sent in that case?

**[3:29:08]** Okay, I just need to check on that. Not sure as of now. Yeah, I will check on that and I will let you know.

**[3:29:13]** Okay.

**[3:29:15]** Okay.

**[3:29:19]** Okay, just give me a second, I'll just note it down, otherwise I'll forget.

**[3:29:21]** Yeah.

**[3:29:29]** K.

**[3:29:43]** And in the chat also I have messaged some questions maybe you can consider to add that in your notes and then we can discuss tomorrow.

**[3:29:52]** Sure, yeah.

**[3:29:56]** Okay, question number one: Which endpoint offers the broadest supports for Open a IAPI with the Foundry model? Okay, so the Foundry.

**[3:30:13]** Foundry project endpoints, Azure OpenAI endpoint or Foundry tools endpoint.

**[3:30:23]** Okay.

**[3:30:26]** So it's a open for open AI API, right? So it's a Azure Open AI endpoint. Yes, that's true. So B.

**[3:30:38]** Question number 2.


### Knowledge check  `[3:30:43]`

**[3:30:43]** Which package must you install to use the Microsoft Foundry SDG in Python?

**[3:31:22]** Okay, so B&c.

**[3:31:31]** So Microsoft Foundry SDK in Python.

**[3:31:36]** OK, it's a Azure AI project.

**[3:31:50]** Okay, question number 3: Which method do you use to generate response with the response API?

**[3:32:16]** Client dot chat dot completions dot create, client dot get response ID or client dot response dot create.

**[3:32:42]** Okay, options.

**[3:32:47]** C Yes, it's true. Option C is correct. Client dot response dot create.


### Develop generative AI apps that use tools  `[3:32:56]`

**[3:32:56]** Next one is develop a generative AI apps that use the tools.

**[3:33:06]** Okay, now what are tools actually? Basically, tools.

**[3:33:14]** Provide the extra capabilities which helps your models to do more than just generate the text.

**[3:33:22]** Okay, so models use the tools to access real time informations, take actions, ground the responses in facts.

**[3:33:33]** Okay, or extend the functionality, build intelligence workflows.

**[3:33:41]** Okay, so the language models, like if you talk about this large language model, it can basically large language model, it understand the prompt and generate the response. But sometimes the model need to access, let's say, the real time.

**[3:33:58]** Informations or need to take some actions or maybe need to search files. Okay, so or maybe it need to run code.

**[3:34:11]** OK, for that we connect the tools to the model.

**[3:34:18]** OK, now for example, lets say if the person ask like what is today's weather OK, the model may not know the live weather as of now OK by itself because this is basically trained on the.

**[3:34:37]** The it has been trained right with the data, it basically knows the till the till the last cut up date it was trained on. So but if I want to ask it like okay, what is the weather now in India?

**[3:34:57]** Okay, so here it will basically if you provide it with the tool, okay, which is like web web search which find the current informations on the Internet.

**[3:35:10]** Okay, or let's say user says like, let's say, okay, let's say calculate this data.

**[3:35:19]** Okay, so or baby, analyse this data or create a create a chart.

**[3:35:28]** Okay, a pie chart.

**[3:35:30]** So over here, right code interpreter, basically it this tool basically lets your models to generate and run the code.

**[3:35:43]** Okay, so in this case it will use the code interpreter tool.

**[3:35:49]** And if the user asks questions from the company documents, right, the model can basically use the file search to find the relevant informations and give the grounded you know, response.

**[3:36:04]** Okay, so tools basically helps the models to access the real time informations, take actions, okay, ground the response, build intelligence workflows, okay. And these are basically the common tool out there. The code interpreter is basically just to generate and run the code, okay.

**[3:36:26]** Now, for example, you can provide your models to analyse a CSV file.

**[3:36:32]** Okay, or to perform some calculation, so it will generate the code, right? It will, it will generate the code and then it execute the code and provides you the output.

**[3:36:44]** Okay, web search.

**[3:36:47]** Find the current information file search functions. Okay, you can use it to call the custom functions in your applications code. Okay, maybe for checking some order status or maybe booking an appointments or creating a support ticket.

**[3:37:08]** Okay, updating the CRM records.

**[3:37:13]** Okay, so it basically allows your models to connect with external outside world.

**[3:37:21]** Now, for example, over here using the code interpreter tool.

**[3:37:27]** OK, so here response API, instructions, the models, OK and input and then we specify the tools the model can use and we have defined over here the code interpreter. So here the model received the questions, OK, it sees the code interpreter is available.

**[3:37:47]** And decide to use it to compute the answer. The code is generated and executed. So model basically write the Python code and run it inside the isolated sandbox container.

**[3:38:00]** OK, and response the return. So models basically formulates the readable answers from the code execution result, OK, not the row code.

**[3:38:13]** Okay, so for example, here, what is the square root of 16? So the response output would be this, or maybe like you provide the CSV file and then you ask it to create a trend like it is there like a trend line. So it will basically show you the trend line there.

**[3:38:37]** Second tool is basically a web search tool.

**[3:38:41]** Okay, web search tool basically.

**[3:38:44]** Like for example, what are the major, what are the 3 major announcement from the Microsoft build? So model detect need for live data based on the questions and the model find the that current real time information is needed. So web searches performs model reformulated the query and conduct a live Internet search.

**[3:39:04]** Okay, and it basically ground the response. So if search results are added as a context and the model create the response that include the URL. So you can see this is the response you are getting here 3 major announcement from the Microsoft build using the file search tool.

**[3:39:22]** So using using the file search tool, your AI models can answers questions using the uploaded documents or enterprise knowledge source.

**[3:39:34]** Okay, so over here tool is basically file search, okay, and it will create a vector store, okay, which is a managed store that hold your documents and their embedding. Then it will upload and index the documents. Now files are automatically chunk, embedded and stored.

**[3:39:54]** Ready for the search.

**[3:39:57]** Okay, then at query time it will semantically relevant passages are found and provided to the context the model answer from the answer from the document and the response is grounded in the retrieve content optionally with the chunk level creations.

**[3:40:15]** Okay, so over here when you ask, what is the maximum amount I can claim for the taxi ride? So based on the expense policy, the maximum amount you can claim for the taxi ride is this.

**[3:40:28]** Okay.

**[3:40:32]** Okay.


### Wrap-up  `[3:40:37]`

**[3:40:37]** Right, so we have basically few slides remaining from this first module. We will cover them tomorrow, okay? And I left you with the hands on on so it give you more clarity right with the hands on.

**[3:40:55]** So perform lab number one, prepare for a IAI development project. Also, let me open here.

**[3:41:08]** so perform lab number one, lab number 2, lab number 3, okay, and lab number 4, okay, so perform this 4 laps, okay, which give you more clarity out there, right? And if you have any questions, so we will take tomorrow.

**[3:41:28]** Okay, I hope everyone has an access to the lab, those who have already redeemed the lab training key.

**[3:41:34]** Aur wo.

**[3:41:37]** They will get access to the lab like after I think after a few minutes, okay.

**[3:41:49]** Alright, so let's wind up the session guys, any issues with your lab or do you have any questions, queries?
