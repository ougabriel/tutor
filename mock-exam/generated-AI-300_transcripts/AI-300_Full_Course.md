# AI-300T00: Operationalize Machine Learning and Generative AI Solutions — Full Course Transcript

- **Course:** AI-300T00 — Operationalize Machine Learning and Generative AI Solutions (Microsoft, GSI)
- **Dates:** 1–4 Jun 2026 · 4 days · night batch 21:30–01:30 IST
- **Trainer:** Pauroosh Kaushal (Microsoft Certified Trainer), Koenig Solutions
- **Captions:** ~3,026 across the captured recordings (~12h of lecture + the short cross-midnight session-close clips)
- **Source:** On-screen auto-generated captions from the Koenig LET portal / Microsoft Stream recordings (expire 19 Jun 2026)

> Caption text is verbatim but machine-generated (Microsoft Stream) and may contain transcription errors. Section headings were added by the editor where the trainer changes topic. **Note on day grouping:** this is a night batch, so each session crosses midnight; the portal files the short session-close clips under the *next* calendar day. The full **Day 4 (Thu 4 Jun) lecture was not yet published** at capture time — only the Day-3 close clip was available (recap once it uploads, ~5 Jun).

## Master Contents

1. [Day 1 - Mon 1 Jun 2026 - Module 1 ML Ops](#day-1---mon-1-jun-2026---module-1-ml-ops)  ·  1,073 captions
1. [Day 2 Part 1 - Tue 2 Jun 2026 - Day 1 session close](#day-2-part-1---tue-2-jun-2026---day-1-session-close)  ·  20 captions
1. [Day 2 Part 2 - Tue 2 Jun 2026 - Training, Tuning, Pipelines, CI-CD](#day-2-part-2---tue-2-jun-2026---training-tuning-pipelines-ci-cd)  ·  992 captions
1. [Day 3 Part 1 - Wed 3 Jun 2026 - Day 2 session close](#day-3-part-1---wed-3-jun-2026---day-2-session-close)  ·  10 captions
1. [Day 3 Part 2 - Wed 3 Jun 2026 - Module 3 GenAI Ops](#day-3-part-2---wed-3-jun-2026---module-3-genai-ops)  ·  897 captions
1. [Day 4 - Thu 4 Jun 2026 - Day 3 close - Day 4 lecture pending](#day-4---thu-4-jun-2026---day-3-close---day-4-lecture-pending)  ·  34 captions


---

## Day 1 - Mon 1 Jun 2026 - Module 1 ML Ops


- **Date:** Monday, 1 June 2026 (21:30–01:30 IST)
- **Trainer:** Pauroosh Kaushal (Microsoft Certified Trainer), Koenig Solutions
- **Recording:** Day 1 — Meeting Recording (SharePoint Stream)
- **Length:** ~3:58:04  ·  **Captions:** 1073




### Introduction & Course Overview  `[0:00]`


#### Session start & housekeeping  `[0:00]`

**[0:00]** 0:10 0 minutes 10 seconds But...

**[0:38]** Yeah.

**[0:47]** 1.

**[2:16]** Yeah.

**[2:19]** A very good morning, everyone. While the participants are joining, I'm sharing the attendance link in the chat. You may mark the attendance for today's session. Any challenge with marking attendance, let me know.

**[2:35]** We wait for a minute, so, and we'll get started with the training.

**[3:36]** Okay, please try maybe in incognito mode. We should be able to access the attendance link. Let me just cheque that.

**[3:53]** The link is working fine. Has anyone able to mark the attendance if I know?

**[5:13]** Right.

**[5:18]** Maybe if you have restrictions at your server, please.

**[5:25]** Make the VPN on or something and.

**[5:29]** Just try marking the attendance.

**[6:06]** All right.

**[6:08]** Yeah.

**[6:19]** No worries. Let me just cheque if I can share any QR code. So those who are not able to mark attendance, it's okay, right?

**[6:32]** Still, you may try with any other public network and try opening the link and the link is working. Others are able to mark the attendance. If not, let me share the QR code in some time then. Is that okay?

**[6:57]** No worries. OK, so.

**[7:01]** Yeah.

**[7:12]** So let's begin the session, right? I'll be later sharing the attendance link again, and those who are not able to mark attendance, they would be able to mark them. Okay.

**[7:31]** Not working. So what is the issue? Actually, the the I think it's the corporate network you are connected to.

**[7:42]** If I know from other, yeah.

**[7:42]** Yes, maybe. So we use a, well, in my case, I use a BDI, so maybe the link is blocked. The other course I took, they share a QR and I did the attendance in my cell phone.

**[7:59]** Okay, okay.

**[8:01]** So I'm on my personal Wi-Fi, home Wi-Fi, but I'm not able to like access the website with or without the VPN.

**[8:01]** All right.

**[8:13]** With personal, I think there should not be any issue because I'm able to open the link. Maybe we try later in some time because the link, we are able to open the link. Yeah.

**[8:27]** Okay, so, but it was not working for me for another course, so we got QR.

**[8:35]** Okay, let me just share the QR code in the chat then.

**[8:42]** Mhm.

**[9:03]** Just give me a minute.

**[9:16]** The QR code is shared in the chat. Maybe we can try opening the link using mobile.

**[9:24]** If that helps, let me know.

**[9:58]** Great. Thank you.

**[10:02]** So let's get going. Let me.

**[10:06]** Let me share my screen.

**[10:21]** All right, so I welcome everyone to this 16 hours training. So we would be spending four days and each day we would be

**[10:36]** We'll be spending 4 hours each day. So total, we have 16 hours duration. And within this duration, we would be completing this Microsoft learning path, which is the course AI 300, operationalize machine learning and generative AI solution.

**[10:55]** I welcome you all to this training session, and yeah, so before we talk about the agenda, let's have a bit of chit chat. Let me first introduce myself, and then we'll have some conversations and we'll go ahead and...

**[11:15]** Talk about the course agenda. Okay, so yeah, so I'm Doctor Pauroosh Kaushal, and I'm A Microsoft certified trainer with a PhD in artificial and machine learning.

**[11:31]** I have delivered over 150 corporate trainings related to AIML on.

**[11:41]** on different Microsoft courses like DP 100, AI 900, AI 102, then the newer courses like AI 901, including AI 300 as well.

**[11:56]** I'm also Microsoft Certified Azure AI Engineer, Microsoft Certified Azure Data Scientist, and AI Transformation Leader.

**[12:06]** Okay, so...

**[12:08]** These are a few of certifications which I have completed from the Microsoft.

**[12:15]** So my focus would be like using the Microsoft Azure.

**[12:22]** to build enterprise grade AI applications using different services, right, related to agent, related to the generative AI, machine learning, deep learning, implementing ML Ops and Gen AI Ops, right, and build a AI solution.

**[12:43]** So, that's the core expertise I have, and so that's the short introduction.

**[12:52]** All right.

**[12:55]** So, before we go ahead and talk about the course objectives, right, it would be nice if I'm able to get information. What's the role in your organization, right? What experience you carry? I would really would like to know if...


#### Audience check — Azure ML experience  `[13:14]`

**[13:14]** If you have already explored the Azure Machine Learning workspace, if you have used the Foundry portal, done some any project on it, or right, if you have explored this portal.

**[13:29]** And what are the course expectations?

**[13:33]** So maybe we can provide this information in the chat or that would be helpful or you may speak up as well. No worries with that.

**[13:46]** Yep.

**[14:00]** Try to get to know your the background so that I can just plan the rest of the sessions accordingly.

**[14:19]** Mhm.

**[14:31]** I can go Pauroosh. My name is Balu Paniker. I lead the Cloud Operations team. To answer your question, I've explored a little bit in the Foundry workspace, creating projects and then defining

**[14:34]** Yeah, please.

**[14:53]** the, what do you say, the LLMs based on what we are trying to achieve.

**[15:01]** But I'm trying to see if this course can expose more into that area and see how we can use the services available in our day-to-day job, you know.

**[15:15]** Okay, okay, all right. That's great to know. Thank you, Vaibhav. So currently, basically, we are exploring it, right? Something similar.

**[15:28]** Yeah, to some extent, yes.

**[15:31]** Okay, read.

**[15:40]** That's great. So I'm able to get.

**[15:44]** The background information, thank you, Gabriel, and...

**[15:49]** Yeah.

**[15:56]** So I see.

**[15:59]** We are a bit new to machine learning. Maybe we have experienced with Foundry, a bit of machine learning, workspace. That's good to know. Anyone who would like to share further, please post it in the chat. Yeah, that will be helping me understanding.

**[16:18]** what could be the requirements, right, and we'll tailor the training accordingly.

**[16:27]** Did.

**[16:29]** So let me go back and...


#### About AI-300 — ML Ops & GenAI Ops  `[16:42]`

**[16:42]** Great, so thank you for sharing the responses, right? And let's talk about this course, AI 300. Okay, and so we have this course split into four days, right? And each day will spend 4 hours, will...

**[17:02]** go ahead with certain concepts related to Azure Machine Learning, we'll be exploring. Then later we will talk about the Foundry portal and build a generative AI solution. So the first two days we will be focusing on Azure Machine Learning workspace.

**[17:23]** Yeah, and we would be exploring this service, Azure Machine Learning Service. We'll see how we can train a machine learning model, how we can optimise model training. Going further, we'll also talk about how we can integrate.

**[17:42]** GitHub actions, we can integrate GitHub to AML workspace, and we can build some automated pipelines, do MLOps, the machine learning operations, or we can go ahead and deploy a model using Azure Machine Learning.

**[18:01]** So these are certain topics we'll be exploring in first two days and in first eight hours. These conceptual slides are accompanied with certain hands-on labs. So I'll be sharing the instructions how we can redeem a training key, right?

**[18:21]** And later we can use the key and do the lab hands-on. Then the other two days that we have, day three and day four, we'll be focusing on Microsoft Foundry. We'll build generative AI solutions and going further, we will also see how we can optimize.

**[18:41]** the applications, the generative AI applications using Microsoft Foundry. We'll also go ahead with doing the application which is deployed, monitoring of that application will do. So we'll talk about generative AI, we'll operationalize.

**[18:59]** Gen AI applications. So these are the topics we would be covering and the learning paths. Let me take you to that link, the learning path links here. So if I go to...

**[19:13]** Yeah, 300, I must learn.

**[19:17]** Kaur.

**[19:45]** Great. So if we look at this training path,

**[19:51]** We have ML Ops as the first module and Genia Ops as the second one. So we will be exploring machine learning using Azure Machine Learning Workspace and we will make use of Foundry Portal and to build a Genia application and operationalizing those applications.

**[20:10]** So, that's the content, and as we go along, I would be sharing certain GitHub links, other resource links, as we go along with the with the concepts. OK, so that's...

**[20:27]** What?

**[20:30]** Yeah. Now let me just go ahead and share lab instructions how we can set up the labs. So later it would be a smoother transition moving from the theory to the practical sessions. So I'll go ahead.

**[20:45]** And.

**[20:52]** Please find the link in the chat with the instructions to redeem a training key. We need to.

**[21:03]** Just give me a minute.

**[21:22]** Please do not redeem training key right now. Just, I'm just checking if it is a correct URL.

**[21:36]** Because I see two URLs here and

**[21:39]** That's creating issue.

**[22:22]** All right.

**[22:40]** Please follow the instructions provided in the chat. OK, and...

**[22:48]** Then, going further, you, you would be able to.

**[22:53]** Uh, redeem the running key.

**[22:57]** So we need to go to GSI loan on demand.

**[23:26]** May I know if you are able to access the link here?

**[23:32]** I hope no challenge with that.

**[23:37]** If the corporate network has issue, maybe we switch to a personal network or maybe we try a personal laptop and redeem. Yeah, okay, great.

**[24:02]** Let's spend 2, 3 minutes for redeeming the key here.

**[24:10]** So.

**[24:15]** Yeah.

**[24:17]** Hi, Kaushal.

**[24:18]** Yeah.

**[24:19]** After marking the attendance, I can't find this course in the mic going.

**[24:27]** Okay.

**[24:29]** If you just mark the tenants, maybe you may not be able to log in, but maybe if it is immediately you are trying to log into my clinic, just wait for 5 minutes and then you try log in. Else, what is the issue you are facing if I know?

**[24:48]** I think I had a course already in this when in Azure in Azure classes. I can see that course and one more course, but this current course I can't see after marking attendance.

**[25:02]** Okay, Harshit.

**[25:05]** I submitted that twice, I thought once it's not submitted, but there's no use of.

**[25:15]** Harshad, I can see your attendance is marked, and when we go to my clinic portal there, you need to reset the password, so we are able to log in to my clinic, right? That's all good.

**[25:27]** Yeah, yeah, I already, yeah, I already changed my password.

**[25:29]** Mhm.

**[25:31]** Just to try logging out and log in and if that refreshes the page here.

**[25:36]** Yeah, sure.

**[25:38]** Let me try that.

**[25:40]** If.

**[25:45]** So the sessions are getting recorded and you can cheque the recordings also by going to my quinic portal.

**[25:55]** Right.

**[25:57]** Let me share that instruction as well in the chat.

**[26:02]** The.

**[26:10]** So to access recordings to track your attendance, you need to log into mycoinning.com. If it is your first time login, use reset your password. The default password is provided in the chat.

**[26:45]** Once you are able to log into my.com, you can see attendance tab where you can mark the attendance.

**[26:58]** You can track your attendance there as well and there is a recording link that gets generated on the next day. Yeah.

**[27:04]** Talk to you.

**[27:08]** So, you know, still on that same issue, like trying to the tools that like import them.

**[27:14]** Yeah, maybe we can we can try later on because maybe it's not updated. OK, in the break time, we may we may try looking at it again. OK, because we I can see your attendance is marked already for this course. Yeah, you may proceed with redeeming the training key.

**[27:18]** And sure.

**[27:30]** Yeah.

**[27:31]** Yes.

**[27:33]** So, then I'll cheque with that.

**[27:35]** Yeah.

**[27:51]** I hope we are able to redeem the training key.

**[28:13]** So let me share my screen. Okay.

**[28:18]** So once we are able to redeem training key,

**[28:24]** Okay.

**[28:29]** So if the site is getting blocked, it is a restriction at your end. Maybe we try on a personal laptop and we should be able to redeem branding key. So either if it is a login issue with your corporate account, you may try.

**[28:48]** You may try signing with a personal account and so if it is a login issue, you may try logging with the personal ID. This can be done and redeem training key.

**[29:01]** And if it is an issue with navigating to the site, maybe we try incognito mode or if we are able to access the link. Else we may try on a personal laptop.

**[29:24]** Great.

**[29:36]** Once we are able to redeem any key, we may note that the key has an expiration date here. So the key is valid for six months from now, right? And using this key, we can perform the labs. And we, if we can scroll down and we can find there are 11 labs we have here.

**[29:57]** and which we can perform and each lab can be performed 10 times. The maximum attempts are 10.

**[30:05]** So we can have maximum 10 attempts within the.

**[30:10]** Until the keys expired, right?

**[30:14]** We may note that.

**[30:33]** We'll spend two, three more minutes. Any challenge we have, you may share your screen also. We can just see how.

**[30:43]** Right, any challenge with redeem training key? We should be able to navigate to the site. Just try with the appropriate network and anything you would like to add, how we are able to redeem training key.

**[31:02]** using a corporate laptop, if I know. Anyone able to redeem using a corporate network?

**[31:11]** They can help others.

**[31:12]** Okay.

**[31:13]** I remember to log in you and use it in a corporate laptop by signing with my own form and personal account.

**[31:18]** Yes.

**[31:22]** Okay, with a personal account. Okay, that's great.

**[31:24]** Yes, yes.

**[31:26]** So the corporate network with login with the personal ID works well.

**[31:35]** Please try, and so let me just write.

**[32:09]** On Quinic site, we may try looking at it later, okay? Try log in again, right? Maybe during break. And if still the issue persists, I'll be raising ticket, right?

**[32:28]** Let's try resolving that issue then. I hope that's okay.

**[32:39]** All right.

**[32:41]** Thanks.

**[32:44]** So let me go back then. Okay.

**[32:50]** Sure.

**[32:55]** So do not launch any lab right now. Okay. We'll spend some time on lab performance later. Okay. I'll be providing certain demonstrations, right? And something similar, you should be able to do it in the lab as well. So we'll spend some time, a dedicated time would be there to perform the labs.

**[33:16]** So, let's first get started with the concepts, and so let's proceed then.

**[33:24]** Anything would you like to add, anyone, before we proceed?

**[33:30]** All good?

**[33:39]** Okay, nice then.

**[33:50]** Log in the app, Kaushal, if I know the app, the my portal, or it's the GSI Learn on Demand portal.

**[34:05]** If it is, yeah, we'll try later on. OK, let's see if during break, I hope key redemption and marking the attendance, it's all done for everyone.

**[34:21]** Okay, Koinik, we may try log in again. Okay, if not, still, I'll take the issues during the break.

**[34:31]** If that's all good.

**[34:47]** Alright.

**[34:48]** So, let's get started. OK, because it's going to be a quite condensed session, right, where we would be exploring MLOps, GeniaOps as well, right, in just 16 hours with the concepts related to it, the demonstration, and hands-on labs as well.


### Module 1 — ML Ops: Build & Train ML Models on Azure  `[35:08]`


#### The machine learning process  `[35:08]`

**[35:08]** Okay, so let's proceed with the first agenda, where we will go ahead and build a machine learning model on Azure Machine Learning. So what all...

**[35:23]** Services can offer, OK, helping us building and deploying A scalable machine learning solution. So, let's explore this, explore the service. So, before we look at the service AML, let's have a quick background on what is machine learning and...

**[35:42]** How we can leverage machine learning to do a certain task? OK, so machine learning, it's like it's the it's the machine which is learning from some historical data.

**[35:57]** So there is some data available, historical data available. We pass this data to an AI, to a machine learning model, where the machine learning model understands the data and it gains the ability to do a certain task. Maybe it gains the ability to

**[36:16]** Do some classification or predicting and some value. OK, this it can do so.

**[36:25]** Let's start with a simple example. Let's say that we...

**[36:33]** We have our data, right? The data which is collected. Let's say a healthcare example where we have certain features. Features could be like we have patient ID. Okay, we have the BMI of the patient, age of the person, and we are preparing a supervised data here.

**[36:53]** Where we have one of the columns, which is the target column, that is what we want the AI model to predict later on. That variable is a part of the data, the target column, so we may have certain records, certain patient records we may have.

**[37:11]** And.

**[37:13]** So each patient, there would be a BMI values, age values, and target column is either one or zero. For example, one indicating the person is diabetic. Okay, 0 indicates person is non-diabetic. So this is a simple use case where we are trying to build a machine learning model.

**[37:33]** which can predict based on the features that based on the inputs that

**[37:41]** What are the chances a patient is diabetic? So we are taking this example, like since we'll be exploring this example further during the labs as well. But the idea can be extended to any other use case. For example, we can use machine learning. We can train a machine learning model.

**[38:02]** which can predict house price given the features, the location of the house, the area of the house, for example, and it can predict a house price. It can predict stock prices, prediction of, let's say, sales values, right, for the next quarter.

**[38:20]** we can build our own machine learning model. Any other example, let's say we can build a machine learning model which predicts what are the chances the machine will fail in another five days, 10 days, in one month, so that we can optimise our maintenance schedule.

**[38:40]** So this can be done.

**[38:43]** There are machine learning models available, for example, to do the fraud.

**[38:49]** fraud detection, where there would be the transaction logs provided, fed to the model. Model will look at that transaction log and it will tell whether there's a fraud happened or fraud has not happened. So here basically we see that.

**[39:07]** We have our own data, we have a historical data, we have gathered certain data, and we want to use the data to solve a business problem. OK, business problem could be like a patient when it comes to a clinic, right? Then...

**[39:27]** Taking up the normal checkups, etc., right? The patient is checked for, like, is the features are given to the model and model will screen that whether the person is at risk of diabetes or not. OK, so such kind of ML model can be built.

**[39:46]** Right, which can assist, like, where to go with for the screening? Should it go for a diabetic use case? Should it go for the diabetic screening later on? So, we built a business problem, OK? And to solve the problem, we collect the data.

**[40:06]** We gathered the data.

**[40:10]** So that's the historical data collected. It would be including a column which is the target column so that machine learning model can use the inputs.

**[40:21]** and the target and it understands the relationship between them. Okay, so it learns on its own. So before we pass this data to the model for training, the data that we have gathered need to be prepared because the data may not be in a correct format. We need to structure the data.

**[40:41]** there would be certain columns, let's say patient ID, right, which is a redundant column because patient ID has nothing to do with what are the chances the person will have diabetes. So we may need to remove certain columns, add certain columns, do some transformations, right? So we need to do some data.

**[41:00]** preparation or data pre-processing has to be done.

**[41:05]** Once the data is cleaned, pre-processed, it is passed through the model for training, where the model understands the data, it learns the pattern in the data. So it will understand how age is related to person being diabetic, how BMI is related to person being diabetic.

**[41:24]** So it understands the trend and based on the trend we get a trained model.

**[41:33]** So train model uses a supervised data, right? And it learns the pattern. Once we are able to get a train model, we can package this model and we can deploy this model to an endpoint. So this is how.

**[41:52]** the deployment happens.

**[41:55]** Like we have a trained model, we are able to register it. We'll talk about those steps. And finally, what we do is that we have the model and we are deploying the model to a URL, to an endpoint. So the model is available at certain URL at a.

**[42:16]** server address and to consume this model, the client application. So we have our application where we provide the inputs like BMI, age, etc. We submit a request to the model so.

**[42:34]** We make a HTTP request, submit our request where we provide all these feature information to the model. Model makes a prediction here.

**[42:46]** It generate a response; the response is then returned back to the client application, so multiple client applications can interact with this model, right? The model gets the request and it provides the response back to the application, so this is the way.

**[43:05]** how we integrate the train model.

**[43:09]** right, to the client application. Once we are able to integrate our model, we can further monitor our deployment, the model that we have deployed. Since now it is taking up the real.

**[43:25]** Real-time data, real examples, right? It's taking, and we would want to know how well this model is doing, what's the model performance, how many, how much time it's taking to generate a response, right? Maybe we want to...

**[43:45]** The model which is deployed, we want to change this model, improve the model. So this all things can be done under monitoring the model.

**[43:55]** Okay, so that's the overall the machine learning business, the life cycle we have here. Okay, it's iterative in nature because like when we do the experimentation also, like if we have certain data, we train the model on that data. If the model training is not good, we may go back.

**[44:16]** Try to improve the data so that we are able to train a good model. So, there are many iterations we may need to go before we can have a model ready for deployment. Once the model is deployed, we need to monitor the deployment as well, looking for a better model or...

**[44:37]** logging the model performance, any deviations are there in the performance, then we need to.

**[44:45]** Go back, update the deployment. OK, this need to be done, so that's an overall what's machine learning process. OK, and Azure Machine Learning Service, it helps us with all the steps of building the machine learning.

**[45:03]** Solution.

**[45:05]** So the problems could be, so if you look at the machine learning life cycle, define the problem, right? So what type of problems that machine learning model can solve? Okay, it can solve a classification problem, classification in the sense like it can predict whether the person, whether...

**[45:25]** Like whether to approve a loan through a person or disapprove a loan. So we can build a classifier here. We can build a regression model where the output of the model is not a class. So in classification.

**[45:42]** The ML output is outcome is the classes.

**[45:47]** the classification output. The regression, the machine learning outcome is a continuous value. That is, let's say if it is predicting stock price, stock price could be 112, 113.

**[46:04]** Yeah.

**[46:05]** 112.1.

**[46:08]** Think that.

**[46:10]** Sorry.

**[46:24]** Just give me a minute. Yeah, I think all good.

**[46:28]** So, the problem could be a classification, could be a regression problem.

**[46:34]** It could be a time series forecasting problem, like where...

**[46:40]** We have our time series data and we are, let's say, predicting the sales forecast for the coming month. Okay. Computer vision is another workload, machine learning workload we have, where we have, where the machine learning model.

**[46:58]** can get an image and it can predict the person this is person X or it's a person Y.

**[47:07]** So we can work with images, we can work with the X data also. So for example, we have a given review of a customer and we want to build a sentiment.

**[47:22]** Analysis system which can predict the sentiment of the review as positive, negative, or neutral like that. So, these are different problems that can be solved using a machine learning model, right? So, once we have...

**[47:42]** Define the problem statement.

**[47:45]** what data is required to build that machine learning model. So here we see we need to gather the data. The data source could be anything like it could be a...

**[47:57]** It could be a DB file, it could be SQL database file, it could be...

**[48:02]** a PDF document, it could be simply a sensor output also. Okay, so it's a sensor output and which is basically logging the temperature of a given machine, right? And once we know the temperature pattern, we can pass it to the machine learning model.

**[48:22]** and it can predict what are the chances the machine will fail in another one month. Okay, so the data source, it could be like a tabular data, data in the form of rows and the columns. So we have data in a given schema, a CSV file, TSV files we may have.

**[48:43]** Data is logged in this file format.

**[48:47]** Right now.

**[48:52]** Data maybe could be a semi-structured data, right? It could be a PDF, right, which is semi-structured, right? We may want to extract the information from this, and those information then be given to the machine learning model for training purpose, right?

**[49:12]** It could be an unstructured data like images, text we have, and we can build a face recognition app. This can be built. So the data source could have a different format, right? So right now we see a...

**[49:31]** The data is in a key value pair and we then convert it into a tabular form here.

**[49:39]** In A tabular format, further, we can do go ahead and do the processing. OK, so for example, device ID is not important to make a prediction that machine will fail or not, so we may drop such columns, we may we may.

**[49:55]** make some changes with the column, like we may not need the second part and we just are in the minute part is sufficient for building a predictive model. So we may try working on the data, pre-process it, clean the data, right, and then it's ready to be passed through the model for.

**[50:14]** For training purposes.

**[50:17]** Right, so when we are working with some new data, right, when we are gathering the data, we should be building a data ingestion solution, right, where we may have a raw data available, maybe it's getting generated, maybe it's a...

**[50:36]** Temperature sensor, we then give it to the Azure Synapse Analytics, right? We can do the ETL process, extract, transform, load, right, where we extract relevant information from the raw data, transform the data, and then maybe...

**[50:55]** Load it, and we may keep it in the BLOB storage.


#### Connecting & splitting data  `[51:04]`

**[51:04]** Okay, we can then pass this data to the Azure Machine Learning for connecting the data and using the data to train the model. Okay, so right now, data ingestion solution is not the scope of this training we would be focusing on once we have the data available.

**[51:23]** in the BLOB storage, how we can connect the storage account to the AML workspace, how we can train the model, deploy the model, consume the model via certain applications. So this we can go ahead and we'll explore. Let's.

**[51:41]** Go ahead.

**[51:45]** So, here we know that.

**[51:49]** The Azure Machine Learning, it has one of the tools available, which is the designer, where we can use drag and drop approach, we can get certain components right, and we can build or train.

**[52:07]** machine learning model. Okay, so assuming that we have the data available in a BLOB storage, maybe it's in a BLOB storage, it's a data lake, for example, right? So data is available and...

**[52:24]** This data need to be connected to Azure Machine Learning, and to do that, we create certain data asset in Azure Machine Learning, so which points to the data. OK, so these are data pointers we need to create so that these data pointers can fetch the data and...

**[52:44]** Then we can use the data and train a model. So the first step is to load the data. We need to create a data asset.

**[52:55]** Okay, which is pointing to a data, a file location. Then this data to be used for the model training, we may need to do data pre-processing.

**[53:08]** So these are certain components available in Azure Machine Learning, right, which we'll be exploring further as you go along, what all other components are there and right. So it's just an overview, like a broader picture, how we can.

**[53:27]** train a model using Azure Machine Learning Designer. So we see using data asset, we are able to load the data in our Azure Machine Learning workspace.

**[53:43]** OK, use the data, do the data pre-processing.

**[53:49]** So one of the pre-processing step would be to normalise the data. Okay, so other pre-processing steps are also there. So we may use that component and use the component connect with the data source. So it outputs a pre-processed data, which is then.

**[54:09]** Pass further where we are splitting the data. So let's say we have 1000 rows of data available. We split the data into 70-30 ratio. So 70% means 700 records would be passed for training the model. And rest 300.

**[54:29]** Rose would be passed.

**[54:31]** To test the model that we have trained, because training the model is not sufficient, we need to before we go ahead and deploy the model, right? The model that we have trained. OK, this model need to be.

**[54:47]** evaluated how well the training has happened, right? So for that purpose, we are splitting the data so that model can use this new data. We test the model, look at the model performance, and if it is all good, then we may further go to the

**[55:06]** Next steps.

**[55:08]** So, overall, what is happening? We have the data available, we can do pre-processing, we split the data, we pass the training data set to a blank model.

**[55:23]** So we have a blank.

**[55:27]** logistic regression model. It's A classifier which can predict two classes or it can predict multiple classes also. Here we have this model, this algorithm available. It's a machine learning algorithm.

**[55:42]** which gets the data and we are able to train our own models. So this is a blank model. We pass training data to this model. The model understands the pattern in the data and we are able to get a trained model. So this trained model is.

**[56:02]** It has the capability to make the prediction. For example, person is diabetic or person is non-diabetic. Okay, so it can make that prediction. So that's the trained model we are able to get. To evaluate how well this model has been trained, right? We need to score the model.

**[56:21]** So, we pass our test data.

**[56:25]** To this train model.

**[56:27]** So model is looking at some new data here, the 300 rows that we have, which it has not seen before. It's looking at this data and the model is giving its prediction.

**[56:40]** So maybe for row number one, it says person is diabetic, row 2 person is non-diabetic, for example. So we are able to get the predictions. Now, these predictions are compared with the ground truth or with the target, because we know that the data that we have gathered.

**[57:01]** It has both input and the target.

**[57:05]** Even when we split the data into 70-30 ratio, the 300 rows comes with the input and its target. So we can provide the target, which is the actual values, okay, and we can compare the target with what model has predicted. So basically we can evaluate the model in terms of...

**[57:24]** Let's say certain metrics like accuracy, F1 score, etc. and see how well is my, how well my model trained and how it is behaving with some new data. So if evaluations are good, we can further follow the steps and we can.


#### Evaluate & deploy the model  `[57:45]`

**[57:45]** Deploy the model. If evaluation is not appropriate or right, we can go back. We may try changing the model. We may try.

**[57:58]** Changing the process, how we are training the model, we may try improving the data quality, right, so that if you provide a high quality data, the model which gets trained will be of good, which will be performing better, right? So, for example...

**[58:17]** If, let's say, there is an issue with data quality, let's say...

**[58:22]** We want to build a fraud detection system, right? And the data that we have has 90% of the data, which is non-fraud.

**[58:33]** and only 10% of the data we have where the fraud has happened. And if you pass this data to the model for training, since model has sufficient examples to learn from non-fraud cases, and it will learn this pattern well for non-fraud, but for fraud cases.

**[58:53]** There are limited examples the model has seen. So the model gets biassed and it may not predict fraud cases appropriately. So this is a data quality issue where in the data we don't have sufficient examples of fraud. So model could not learn that well and then model fails during the evaluation.

**[59:15]** So this may happen. So we can go back and try to improve the model training, right?

**[59:25]** And further going ahead, we can go and deploy the model, monitor the deployment, those all things can be done.

**[59:35]** I hope that's this flow is all good so far.

**[59:43]** Anything, anything would you like to add related to the machine learning basics we have covered?

**[59:55]** Any queries on that?

**[1:00:06]** All right.

**[1:00:07]** If sounds good, we can further go ahead then. So to train our own own model, right, we can choose one of the service from the provided services on Microsoft, right? So on Azure platform.

**[1:00:27]** We can see different services out there which help us building an AI solution.


#### Azure data & AI services overview  `[1:00:37]`

**[1:00:37]** Right, so we have Azure AS Services, Microsoft Fabric, Azure Databricks, and Azure Machine Learning. So these are certain services which we may use, try to leverage to do a certain task. Okay, so let's explore when to use this service.

**[1:00:57]** Yeah, yeah, please.

**[1:01:01]** Hi, so I was just thinking on the example that you gave about the fraud detection data set and how one-sided data can lead to bias in the trained model. So I was just thinking, how do we determine what?

**[1:01:07]** Mm-hmm.

**[1:01:19]** Correct.

**[1:01:21]** kind of data set should we have? Let's take this example itself. Like what should be the ratio between fraudulent and non-fraudulent cases?

**[1:01:30]** When we are trying to train a model to detect for fraud, basically fraud detection, if you are trying to train a model for fraud detection, because if we'll take more number of fraudulent cases, wouldn't that lead to overfitting?

**[1:01:46]** then how do we balance it?

**[1:01:49]** Generally, the target, it's ideal that we should be having 50-50 ratio for both the cases, fraudulent and non-fraudulent cases. So that's an ideal number. If it is, let's say 45, 55, that's also it's a fine ratio, but it should not be a very...

**[1:02:11]** a drastic difference like 90-10 or even 80-20 may not fit well, right? So there are certain solutions to such kind of issues like class imbalance issues. So this is a class imbalance issue, right, where the...

**[1:02:29]** target having examples of 1 class and it doesn't have examples of the other class. So if we, so ideally we should be having the balance, right, so that the model is exposed to all the both examples of both the cases so that it learns the pattern for both the classes.

**[1:02:49]** Right. And in real time, like if let's say we are not able to gather many examples for one of the class, there are other techniques available like SMOT is there, synthetic minority oversampling technique. Then we have other oversampling techniques are there.

**[1:03:08]** which allow us to.

**[1:03:11]** Fix the class imbalance issue. OK, so this can be done.

**[1:03:17]** Okay, using such a technique, we may try improving the data quality, okay, which creates or with synthesise some new data sets, right, and try to balance out the examples without the model getting overfitted.

**[1:03:33]** Okay, just last question. So shouldn't these kind of, for a model that is being trained for fraud detection, shouldn't the training data be reflective of real world scenario because fraudulent cases would be just a fraction of actual total transaction. Out of total transaction, fraudulent cases would just be a fraction of it.

**[1:03:56]** So, but why would we still go for 50-50-ish?

**[1:03:58]** Correct.

**[1:04:03]** Because if we don't go with such ratio, if you go with, let's say, 90-10 ratio, right, the model is getting like it gets overfit with 90%. It will learn this thing like non-fraud cases very well.

**[1:04:21]** And then it will fail detecting a fraud case later on during the evaluation. So this will happen, right? Even if you look at the confusion matrix of the model that we have trained, right? The model will be insensitive to, it will have a low precision recall for.

**[1:04:41]** fraud cases right and it will be doing very well for non-fraud cases. So we need to synthesise some more data with it will not be a duplicate row right from the real cases it would be it would be like synthetic right with.

**[1:04:59]** Yes.

**[1:05:01]** Let's say we have the original or like we have the fraud case.

**[1:05:07]** fraud data, right? On top of it, we are adding the noise so that model do not overfit on the fraud data. So we tried to create some synthetic data so that it can get some new data, new examples without model getting overfitting on the existing data. Yeah.

**[1:05:27]** So, that's what the smote does, yeah.

**[1:05:32]** Thank you.

**[1:05:34]** Great then.

**[1:05:36]** So, Kaushal, what about this and reinforcement? Are we going to cover those in this sessions in the process?

**[1:05:47]** I'm sorry, in the current process, what?

**[1:05:50]** Course, course. Are we going to cover this unsupervised learning and the reinforcement learning?

**[1:05:55]** No, no, we'll not be discussing the reinforcement learning. Actually, the focus on machine learning is of not that much. Okay, the focus would be how to build a machine learning solution on Azure Machine Learning.

**[1:06:08]** Yeah.

**[1:06:15]** Okay, so the topics like reinforcement learning will not be exploring as a part of this training. Yeah, that's not the scope. Also, talking about machine learning is not much like pre-processing steps or other, but how to use those steps, what all tools are available on?

**[1:06:23]** Cool.

**[1:06:34]** Azure Machine Learning, the focus would be more on that side, yeah.

**[1:06:34]** Yeah.

**[1:06:39]** Okay.

**[1:06:42]** Great.

**[1:06:47]** So...

**[1:06:49]** Let's explore what all services are there where we can leverage AI for use case. So we have Azure AI services.

**[1:07:01]** Now, this is a service which comes with pre-built models, so we need not to train a new model to do a certain task. There are pre-built models available, and so it's like a plug-and-play service. Yeah, so we simply create a resource.

**[1:07:21]** use a pre-tain model. We have an option to customise it a bit, but these are pre-tain models available and simply consume these models, build an application. This we can do. Okay, so we can go with Azure AI services when we want to

**[1:07:42]** rapidly from ideation phase, we want to quickly go to experimentation and then releasing a application, right? So where we want to save our time and the efforts to train a model. So since we are not training our own models, we are using a pre-trained model.

**[1:08:01]** Right, so we can use that and build our application. So, for example, we should be going with Azure AI Services, where the pre-built models can cater to our requirement. So, let's say if we have a reviews certain reviews we want.

**[1:08:21]** To use Azure AI service, right? There is a language service within it which can do the sentiment analysis and provide you the sentiment output as positive, negative, and neutral. OK, so if there is a...

**[1:08:40]** Sentiment analyzer AI model already available. Why to train your own model? No need to do that. Why to spend resources to build our own AI? When pre-build models can cater to the requirements. So this can be done using the Azure AI services and.

**[1:09:00]** It has many services within it, like language service we have, computer vision service we have.

**[1:09:07]** then content understanding service, etc. So we can use AI models and build a computer vision application. So there is a face API available. So to build a face recognition solution, we need not to train our own model. Simply use face API.

**[1:09:28]** Right, and...

**[1:09:32]** Use the face here.


#### Use cases & the AI development lifecycle  `[1:09:35]`

**[1:09:35]** and build our face recognition app. If it is a custom requirement, maybe like doing the fraud detection, et cetera, we may try Azure Machine Learning, where we need to bring our own data and train our own model.

**[1:09:52]** It.

**[1:09:55]** Then we have Microsoft Fabric, okay, where it's like A1 platform where we can do the data engineering, right, and also use that data to build a machine learning solution, so we have Fabric available where we can.

**[1:10:13]** create a Jupyter notebook, create certain scripts, PI files we can create, and we can train a model, or we can even go ahead and deploy the model as well. So we can use fabric, but currently, as for the developers are concerned, if we have a team of developers to build.

**[1:10:35]** a machine learning solution. Azure Machine Learning would be a better approach which allows which where we have a better control over.

**[1:10:46]** model training, optimising the model, deploying the models, putting into the production, etc. So currently, the Azure has more features to have a controlled AI application development as compared to Fabric. Later on, maybe Fabric can...

**[1:11:06]** Will emerge, maybe Azure Machine Learning can integrate with Microsoft Fabric. This may also happen, right?

**[1:11:14]** So we can use fabric as well, right, to build a machine learning project, but with a lesser control over the deployment process, etc. So that's Microsoft Fabric we can use. Or if we have, let's say, some big data.

**[1:11:35]** where we want to train a model and we are exposed to a large volume of the data, then we may choose Azure Databricks, which allow us to use PI Spark, use distributed computing, and we can train a model, we can handle some large data and...

**[1:11:57]** Build our own model, so, so Azure Databricks also support use of notebooks, etc., creation of PI files, use those PI files to build machine learning model. This can be done right, so, so where the data is at?

**[1:12:15]** Lost scale, we may go with Azure Databricks. OK, and currently Azure Machine Learning is the platform for developers to.

**[1:12:27]** do the app development, the AI development, testing, evaluating the model, putting the model into production, etc. So that's for that purpose, we can go with the Azure Machine Learning workspace.

**[1:12:44]** Right.

**[1:12:46]** Let's continue then.

**[1:12:51]** So once we are using, let's say, AML workspace, we are able to train a model.

**[1:12:59]** And we can deploy the model to an endpoint. So using Azure Machine Learning.

**[1:13:05]** Kaushal, sorry to interrupt.

**[1:13:05]** We, yeah, yeah, please.

**[1:13:08]** So, can you go to the previous slide?

**[1:13:10]** Yes.

**[1:13:12]** Can you explain it in Microsoft?

**[1:13:16]** I.

**[1:13:16]** Yeah, Microsoft Fabric, correct. So the Microsoft Fabric, it's again a platform, right, where we can do data engineering, okay, the ETL process and doing the data pre-processing, et cetera, along with building a...

**[1:13:36]** Data science or machine learning project, so we can.

**[1:13:41]** We can, so it's like a one platform where we can do data engineering with machine learning, right? However, machine learning would be, we don't have much control, like, for example, in case of Azure Machine Learning, right? We can configure.

**[1:14:02]** a deployment strategy like green, blue deployments and the rollback and those strategies can be implemented with more ease in Azure Machine Learning as compared to Fabric. But Fabric allows us to build machine learning project, even we can deploy.

**[1:14:21]** A model.

**[1:14:23]** Using the fabric, this can be done, so it's like A1 platform for including both data data engineering with ML projects we can do, so that's the fabric available, however.

**[1:14:39]** Even if we compare the two platforms, the Azure Machine Learning and the Fabric, if the focus is on building a machine learning model, not with the data engineering aspect, we should be preferring Azure Machine Learning over the Microsoft Fabric.

**[1:14:56]** That's how the two services are differentiated, yeah.

**[1:15:01]** That.

**[1:15:03]** Okay.

**[1:15:05]** Is that all good?

**[1:15:09]** Yeah, so for the Azure Directory team, getting the last.

**[1:15:17]** Oh, sorry, I could not hear you well. What's that?

**[1:15:19]** So, we'll be using the events.

**[1:15:23]** Yes.

**[1:15:25]** Yeah, we will be using Azure Machine Learning.

**[1:15:25]** Yeah.

**[1:15:29]** Not the fabric.

**[1:15:39]** All right.

**[1:15:43]** That's great then. Sure.

**[1:15:49]** So, we can use Azure Machine Learning, where we deploy the model, the model that we have trained to an endpoint.

**[1:16:01]** Right, so there is certain URL, and we may consume the model right, or we may integrate our model that we have deployed right to the client application, so we have the application. It could be a web application where the user come.

**[1:16:20]** provide the input features, let's say the BMI, age of the person, other features, and hit the predict button and we make a HTTP request. The request is submitted to the model, to the endpoint.

**[1:16:40]** The model here running over a compute, right? And...

**[1:16:45]** The model which we have available, the model is loaded. It makes the prediction and the response, the predictions, which is the response, is sent back to the application. So that's how we can consume a model which is deployed.

**[1:17:05]** To an endpoint, so that's a industry standard, how we can consume a model or which is deployed to an endpoint. OK, so that's how we can integrate the machine learning model.

**[1:17:19]** To do an application, OK.

**[1:17:25]** So if you talk about deployments in Azure Machine Learning, there are two type of deployments, the real-time and the batch deployments. Real-time deployment from the name, right? It's A real-time deployment. The user submits a request.

**[1:17:43]** OK, it would be processed in real time, and the machine learning model provides a response. OK, generally, for running such endpoint, running a real-time endpoint, we need a dedicated compute.

**[1:18:01]** Right, which can running 24 by 7 can handle requests from, like, which can handle maybe a high traffic and it provide the real-time predictions. Use case could be, for example.

**[1:18:21]** If let's say we want to do the fraud detection. So for such a scenario, we don't want like the results to be coming, the outcome of machine learning model to be coming later, maybe.

**[1:18:33]** We send the request in the morning and...

**[1:18:36]** Right, we obtained the result, the outcomes in the evening. So for such use cases, we should be going with a real-time predictions.

**[1:18:51]** Real-time deployments we should be going with. Okay, then we have batch predictions also. So where the use cases are there, where we don't need, where it is not a requirement to have a real-time predictions. We can go with the batch predictions where, let's say,


#### Batch scenarios & model monitoring (drift)  `[1:19:11]`

**[1:19:11]** We collected the data in the evening and we want the outcomes in tomorrow's morning. So tomorrow morning, right? So in such a scenario, we don't need an expensive compute, a less expensive compute with maybe with a shared.

**[1:19:29]** Pool, right? That kind of a compute can also be used, which, whenever it's available, it can go ahead and load the model, model provides the predictions, so, so under those scenario use cases, we can go with the batch predictions where we provide the batch of.

**[1:19:48]** input, maybe like we gathered the data throughout the day, maybe we collected 100 records. And then once we have the batch of input available, we submit the request and later we get the results, maybe the next day, right? So.

**[1:20:09]** We get a batch of inputs and that is passed and model makes the predictions for each row of the batch. So there we can go with the batch deployments. We will be exploring further the real time and the batch deployments, how we can create an endpoint.

**[1:20:28]** Deploy a model to the endpoint. OK, consuming the model, so...

**[1:20:33]** We'll go ahead and discuss it as well.

**[1:20:37]** So that's about integrating the models, right?

**[1:20:42]** looking at the types of deployment we can do using Azure Machine Learning.

**[1:20:48]** And here we have.

**[1:20:51]** monitoring the deployment. So when we are able to successfully deploy the model.

**[1:20:57]** To an endpoint, right? We need to go ahead and do the optionalizing, like we need to. We need to monitor our deployment, like how well my model is doing on real world use cases, OK?

**[1:21:17]** We should be.

**[1:21:19]** able to track performance of the deployed model like so.

**[1:21:25]** The model, when it is deployed, it gets the real use cases, real examples for which the model is making the predictions, right? So we should look at how good the predictions are. Is the performance of the model degrading over a period of time or not?

**[1:21:44]** So if it is, how much is the model accuracy? How much is its FN score? So these are certain metrics we need to log.

**[1:21:53]** for our deployment, right? And maybe like if the metric falls below a certain threshold, right, we should be automating certain triggers. So maybe like accuracy falls below 85% of our model, okay?

**[1:22:12]** We may want to retrain the model on some new data, on some updated data, so that we provide the latest deployment, and that deployment works well, right? So, if that kind of a metrics fall below a certain threshold, we may make use of certain.

**[1:22:32]** integration like we can have a GitHub integration.

**[1:22:38]** OK, with our AML.

**[1:22:42]** Workspace, where if the threshold falls, if the if the metric falls below a certain threshold, right, we can trigger an action, we can trigger a GitHub action, right, and this will try implementing CICD.

**[1:23:03]** continuous integration where we would be able to fetch some new data, retrain the model.

**[1:23:11]** And after model is retained, we are able to get the new model. We can do continuous deployment and we can further go ahead and deploy the model as well. So we should be able to set retraining triggers with integration with GitHub, right?

**[1:23:31]** We can build certain automated pipelines.

**[1:23:36]** Right, for doing CICD, the continuous integration and continuous deployment can be done.

**[1:23:44]** So continuous improvement or integration like training a new model or we may have some new data and training the model on that and further use that model and deploy that model. Okay, so that we should be able to set.

**[1:24:02]** We should be able to look at the data drift also when we are monitoring our deployment. Okay, so let's say we trained a diabetic porter.

**[1:24:14]** Right. This model is trained on a data set where one of the column is age and let the age range be 40 to 60. So the model is trained on such age group and it can predict person is diabetic or not. Later on, we

**[1:24:34]** Deployed this model.

**[1:24:37]** OK, once the model is deployed, it is getting the real-time examples right for prediction and this data.

**[1:24:48]** has the age feature and for that it is making the prediction. And here the production data is.

**[1:24:57]** having the age group between 20 to 30.

**[1:25:00]** So we see that the model is trained on another data distribution and it is then used or consumed on another data distribution. So if there are any changes in input distribution or target distribution is changing, right, model will not be performing well because it is trained on something else.

**[1:25:22]** And getting tested on something else, so it's a scenario if we should be able to detect, so we should be able to detect the data drift. Okay, if the drift or the change in the data distribution is significant, we may go ahead and deploy or...

**[1:25:42]** Retrain the model on this new data distribution, right, so that the model works as expected, so...

**[1:25:51]** Detecting the data drift, and based on that, we may trigger, we may have some retraining triggers that can be added.

**[1:26:00]** Concept ref could also be there. So concept refs are nothing but the relationship between the feature and the label if it is changing. That is the input. Let's say we train the model on a data where age is there and target is person being diabetic. So they have certain relationship which is learned by the machine learning model.

**[1:26:21]** Right, so the training data has.

**[1:26:26]** some other relationship than the data which is there in the production. So that relationship is changing the right. There's a concept drift and model trained on something and it is tested on something. So this should not happen. Maybe like let's say we trained a model.

**[1:26:46]** Uh, let's say we we have a model.

**[1:26:50]** Which can understand an X-ray, and it is making up diagnosis.

**[1:26:58]** Okay, for a disease, maybe for, let's say, pneumonia or let's say, right. Then, so there is some data and model trained on that. Okay, so there was some relationship between x-ray image and the person suffering from a disease or not. Later on, maybe after a month or two.

**[1:27:18]** OK, or maybe after 5 to 10 years, right? The disease pattern changes, right? There is a concept drift, the X-ray, which is the feature.

**[1:27:31]** And the disease, right?

**[1:27:34]** The signature pattern is getting changed, right? So the model that we have trained is no longer good, right, on the new data. So the model needs to be retrained. So if there is a concept drift, feature label, relationships, if they are changing, we should be able to detect that drift and...

**[1:27:55]** Make changes in our model accordingly.

**[1:27:59]** That we should be able to do.

**[1:28:02]** If let's say some new data is coming, we want to train the model on that, right? That such pipeline should be built so that the pipeline should be detecting presence of new data and it would trigger retraining the model and continuous deployment. So, for example.

**[1:28:22]** If we are building a machine learning model which predicts the sales for the next month.

**[1:28:27]** By using...

**[1:28:29]** Daily data, so.

**[1:28:32]** If let's say it's predicting the sales value for the month of January, and when the January passed, right, we now have the month of February and we have the data available of January, which can be used to make the predictions for the month of February. So as the new data comes in, we need to reiterate the model, right?

**[1:28:52]** Or we can go with periodic retraining also, right, to take care of any unseen drift. Okay, right. We may not be able to detect any drift in the data or feature labour relationship, but there could be environmental other factors would be there.

**[1:29:12]** Right, which need to be account for, so that right, if if the model is not performing well right, we may schedule the retraining maybe periodically after a week during the right.

**[1:29:31]** weekends maybe right and run those pipelines. This can be done. So these are certain tasks we should be performing while monitoring our model.

**[1:29:44]** monitoring our deployment.

**[1:29:49]** Alright, so...


#### Recap — ML basics & deployment  `[1:29:52]`

**[1:29:52]** I think we have seen certain basics related to what is machine learning, what is how we can deploy a model.

**[1:30:02]** Going ahead, what is ML Ops?

**[1:30:05]** how to operationalize a machine learning solution so we can monitor our deployment and what are the best practices. So Will, anything would you like to add before we proceed to the next part here?

**[1:30:26]** If that's all good.

**[1:30:39]** All right, so we'll now focus on how to use Azure Machine Learning, right? How we can use the creative workspace, use the workspace to create certain experiments and try to train a model, right? So let's look at certain.

**[1:30:59]** Ohh.

**[1:31:00]** features of the Azure Machine Learning workspace, right? So before we look at how to do model training, okay, let me take you to the Azure portal and show you how we can create a workspace. So I'll go to...

**[1:31:19]** Hotel.azure.com.

**[1:31:23]** Let me sign in with...

**[1:31:26]** Correct credentials here, and...

**[1:31:47]** All right, so we are at portal.azure.com, and here we have one of the service Azure Machine Learning, and if I click on this, we can go ahead and create a new workspace. So, when we create an Azure Machine Learning workspace.

**[1:32:05]** Right, when we see here.

**[1:32:08]** Right, we provide the workspace name here. Let's say something. So along with the workspace that getting created, other some additional resources are also getting created, like storage account.

**[1:32:23]** A keyword.

**[1:32:25]** an application inside a container registry. So these are additional resources getting created. So because we may want to store our data in a BLOB storage and then connect the BLOB and use this BLOB storage with the Azure Machine Learning workspace.

**[1:32:45]** Okay.

**[1:32:47]** Just to maintain data privacy, right, we need to keep the access to my storage account safe in a key vault. So this key vault.

**[1:32:58]** Can have connexion with can store storage account connection.

**[1:33:05]** The storage connexion string can be kept safe in a key vault. We make use of application insight for monitoring our application. We will be using the container registry because later on for deploying the model, we need to have an image created.


#### Container registry & images for deployment  `[1:33:26]`

**[1:33:26]** that gets stored in the Azure Container Registry and this image will be used by the container when we are deploying the model to an endpoint. So these are additional resources that gets created when we create a workspace. And I've already created a workspace.

**[1:33:47]** OK.

**[1:33:49]** So let me go to this. Okay, let me just go to the resource group.

**[1:33:57]** So this resource group has the workspace. So as we see, Azure Machine Learning workspace, along with other resources like storage account, key vault, application site, right? And if I go to my workspace here.

**[1:34:16]** In the workspace, we may find Studio. So Studio is like a UI, a user interface, where we can manage our workspace. We can see what all resources are connected to this workspace, what is the compute we are using, or we can

**[1:34:35]** Create a compute so that we can.

**[1:34:40]** Create a notebook, and maybe we can train a model. OK, so that's the studio available, which is ml.azure.com.

**[1:34:54]** And let me go to the studio.

**[1:35:07]** All right.

**[1:35:09]** So here we see in the studio, we can author or we can create a notebook.

**[1:35:16]** We can do other things like auto ML, the automated machine learning we can do.

**[1:35:22]** We'll talk about these features later on. What is a designer? So we can see, we can read a Jupyter notebook, we can write certain Python code, we can create scripts, the Py files we can create, and we can do a task maybe to train a model, etc.

**[1:35:43]** Then it has a, we have assets here where data is there, like, so we can create a data asset which can connect to.

**[1:35:56]** which can connect to, let's say, to a BLOB storage or like to any file location that we can provide. So if I click on data asset here.

**[1:36:09]** Create a data set. Let me give any name here and.

**[1:36:15]** If I go ahead with your file, so we can see, we can upload files locally from Azure Storage, we can establish a connection. So if I click on Azure Storage, we can see Azure Data Lake Storage.

**[1:36:36]** Can be connected to or Azure Blob Storage, Azure File Share, so these are.


#### Data assets  `[1:36:42]`

**[1:36:42]** The options available, and we can create a data asset which is pointing to data.

**[1:36:53]** at certain location, right? So we'll see more further data. There are data assets here. There are other assets here, right? So let's say, for example, we have deployed a model to an endpoint.

**[1:37:10]** Then endpoint would be appearing here. What all endpoints are created in this workspace? We can cheque what is a deployment at that endpoint, the deployment status we can see.

**[1:37:23]** We have environments available, so there are inbuilt environments are there, the curated environments, which we can use and maybe we want to execute a PI file.

**[1:37:38]** So using those environments, we can do that under compute. OK, maybe I can just go ahead and create a compute instance.

**[1:38:01]** So when we are creating a compute, it could be a CPU or GPU. These are the VMs available under my subscription and maybe I can just go with the cheap compute.

**[1:38:15]** Ohh, and we can go ahead and create this compute instance.

**[1:38:24]** All right, so I can do that. Maybe it's not required right now, so I'll just leave it.

**[1:38:32]** Okay, so these are some components available in the studio and we would be further exploring right in the labs as well.

**[1:38:45]** Alright, so that's the Azure Machine Learning workspace we have.

**[1:38:52]** Let me go ahead now.

**[1:38:56]** Let's talk about automated machine learning, how we can do automated machine learning in our workspace. Okay, then we'll go ahead and see how to optimise model training, further talk about model experimentation. We'll further then talk about RAI dashboard.

**[1:39:17]** what is a dashboard and right how we can create a dashboard in Azure Machine Learning workspace.

**[1:39:27]** So, let's continue. Let's talk about automated machine learning.

**[1:39:34]** So.

**[1:39:37]** Considering that we have the data available, so there is a CSV file, let's say available, and which contains certain health records of patients, and we want to build a predictive model predicting person is diabetic or not.

**[1:39:55]** Now, we have the data. Now, there are many algorithms available, many machine learning algorithms are available, so...

**[1:40:07]** Which one is good for my data? Okay, we are not very sure. We may go with trial and error approach, train multiple models individually, right?

**[1:40:20]** and train them, look at their performance, and then take a decision.

**[1:40:26]** Which model or which algorithm is best?

**[1:40:31]** Working on my data.

**[1:40:33]** So, instead of going with that approach, the manual approach of training multiple models, we may go with automated machine learning, where we simply provide a list of algorithms.

**[1:40:49]** We pass over data.


#### Automated ML (AutoML) — jobs & best model  `[1:40:52]`

**[1:40:52]** And we configure AutoML job where the job is configured and we would be able to train the models, the machine learning models.

**[1:41:09]** So we have, we are able to train.

**[1:41:13]** ML models here, and we would should we are able to retrieve a best model, right? So, which models are working best on my data? So, this can be done using automated ML, right? So, the feature is basically to...

**[1:41:31]** It facilitates us with training multiple models in parallel, right, and retrieving the best model as per our performance metric, because if we say we want to retrieve the best model, so best will have the criteria, right?

**[1:41:50]** on what criteria we are defining what's the best model. Maybe best model is the one having the highest accuracy.

**[1:41:58]** Or maybe the best one is the one.

**[1:42:02]** with, let's say, with a high AUC value.

**[1:42:07]** Right, etc. So, these are certain metrics, right? The performance metrics, which act as a criteria for selecting the best model. So, this is automated machine learning, and we'll see how to...

**[1:42:25]** How to configure an AutoML job, submit the job and see what is the outcome.

**[1:42:33]** Of the auto ML.

**[1:42:36]** Right, so here we see when we are going with building a machine learning model, right? These are certain workloads we have, classification, regression, etc.

**[1:42:49]** Right.

**[1:42:53]** Yeah, that's a nice question, I think. How do we determine which is right? How do we confirm which algorithm is more accurate, more useful for your model training? So that's what the auto ML does, right? It would be training.

**[1:43:12]** algorithms. So we simply provide a list of algorithm and these algorithms using the algorithms, the models we are able to train here and we need to provide the criteria, right, which defines which is the best model.

**[1:43:31]** Maybe like there is model 1 trained, model 2 trained here, model 3 we have trained. So model 1 may be having the.

**[1:43:42]** highest FL score, right? But our criteria, if it is that...

**[1:43:47]** if the accuracy is highest, accuracy is our criteria to selecting a best model and maybe M3 is the model which has the highest accuracy. So, this would be the best model for our data.

**[1:44:03]** Like that.

**[1:44:06]** Yeah, I hope the query is resolved here.

**[1:44:15]** So.

**[1:44:17]** We can go ahead and we would be logging those performance metrics, right? And I'll show in the lab as well, right? Yeah. Thank you.

**[1:44:29]** So where we would be training multiple models.

**[1:44:33]** And.

**[1:44:34]** We will see.

**[1:44:36]** The individual models, which is our best model. OK, what are the performance metrics of the best model, right? So, those are things we can explore in the in the work workspace.

**[1:44:50]** Great that. So we see.

**[1:44:53]** Using AutoML.

**[1:44:57]** We provide the performance matrix based on that matrix, we define the criteria of.

**[1:45:04]** A best model.

**[1:45:06]** We provide a list of algorithms.

**[1:45:11]** To select right list of algorithms for using those algorithms, we can train machine learning models. Auto ML also support featurization, right? So any data pre-processing, if you want to do auto ML can do that, right? So if you have a data available.

**[1:45:32]** Right, maybe the data requires some pre-processing. We can configure the AutoML so that it can do featurization, it can do data pre-processing. So, what all different modes are there? OK, so let me just...

**[1:45:49]** Take you to a link here.

**[1:46:02]** Oh, yeah.

**[1:46:29]** So over this page we can see what are the ways how we can do data featurization in AutoML.

**[1:46:38]** So, we note that.

**[1:46:41]** We can.

**[1:46:43]** We have three featurization mode, like featurization can be set to auto. So if it is set to auto, it means that let the AML decide if any data pre-processing is to be done. It will automatically decide which technique to use and.

**[1:47:02]** it will do the featurization. Okay, so for example, if let's say we have a data.

**[1:47:09]** maybe a CSV file. It may have some null values.

**[1:47:14]** some empty cells it may have, which need to be removed before we pass this data for model training. So if we set the featurization to be auto, it will look at that column, understand what is the data, what is the data distribution we have.

**[1:47:31]** Okay, and it will try to maybe remove the null values, remove all the rows with the null values. Maybe it will impute certain values, impute the average of that column in place of null value. It may approximate that. So we can set the featurization to auto.


#### AutoML — preprocessing & featurization  `[1:47:51]`

**[1:47:51]** Let the AML do data pre-processing if there is any requirement. Okay, if you don't want AutoML to do any kind of featurization, we can set featurization to be off. So if we set it to off, it means that...

**[1:48:08]** The data remains as it is, and it is passed to the algorithms for model training.

**[1:48:15]** If you set the feature to be off.

**[1:48:18]** We may even configure featurization, that is, we may specify that for the age group, if there are null values, those null values must be replaced with the median of that column.

**[1:48:34]** Okay, something. Maybe there's a gender column, right? And if there are null values, for example, then the null values should be replaced with the...

**[1:48:46]** With the mode value, the most occurring.

**[1:48:50]** most occurring gender category, maybe male or female in the data set. So whichever category is most frequently occurring, that would be replacing the null values. So we can specify what pre-processing technique to apply for which columns.

**[1:49:09]** So, that's that's how we can configure featurization.

**[1:49:13]** And further, if you can scroll down in the documentation link, we can see what all different features and steps are there. If there is a text in the data, we can use these techniques and convert the text into numeric form. These are scaling operations that we can do on a...

**[1:49:33]** on our data.

**[1:49:36]** Great, so these are supported techniques, OK?

**[1:49:40]** Then we have data guardrails also. So data guardrails, it's like it's a guardrail which look for any potential problem with our data quality. So as like we were discussing, if there's a class imbalance issue, 90, 10% is there, then auto ML.

**[1:50:00]** has a guardrail which can give an alert like so we under supported guardrails we can see that if let's say there there is class imbalance detection is there so it can raise a status and tell any issues with our data quality.

**[1:50:20]** So it will provide the status like passed, it means no data issues are there, right? Done means AML is able to detect an issue and it has fixed that issue also. Alerted when it found an issue.

**[1:50:40]** But the it is not is not able to fix it, so it simply gives an alert that there's a data quality issue.

**[1:50:49]** So there are different guardrails, data guardrails are there, including class imbalance detection, many further are there, right? And we can use guardrail to know the data quality.

**[1:51:06]** So that's the AutoML featurization.

**[1:51:23]** You may further explore the link.

**[1:51:27]** The.

**[1:51:29]** Going ahead then.

**[1:51:31]** Let me go back.

**[1:51:34]** Okay.

**[1:51:36]** So when we do auto ML, we when we want to create an auto ML job, we have an option to configure featurization. Algorithms we may select, we may select provide the criteria. Of criteria of a test model, right?

**[1:51:56]** that we can do.

**[1:51:58]** So before we look at the auto ML configuration, like how we can.

**[1:52:05]** Create an AutoML job.

**[1:52:10]** and how we can submit the job, how we can configure this job. Let's look at, let's have this quick knowledge cheque here.

**[1:52:20]** ABC. So just to have a bit of interaction, can you answer the first one and which is more appropriate option if you can write in the chat?

**[1:52:40]** Regression.

**[1:52:45]** So I see B or C?

**[1:52:50]** C being the more frequent option. So of course, it's the answer is C here because we want AI to predict whether the customer will churn or not. So the machine learning model has the prediction category that churn and not.

**[1:53:08]** Sure. So it's a classification problem machine learning model is trying to solve. So that's a classification task. That's very correct. See. And then we have ABC here. We see it's B.

**[1:53:29]** For 2.

**[1:53:33]** So we agree with B here, right? Computer vision. So we are working with images and it's looking for detecting abnormalities. So of course it's B. That's great. That's great to know.

**[1:53:49]** Thanks for providing the responses. So second, it's B. That's the correct answer.

**[1:53:57]** Thank you.

**[1:54:00]** Let's continue that. OK, so.


#### Configure an AutoML job with the SDK  `[1:54:04]`

**[1:54:04]** We started discussion about the AutoML, and we'll see how to configure the AutoML job, right? So, here we note.

**[1:54:17]** When we are, when we want to create or run an auto ML experiment, we need to have the data available.

**[1:54:25]** Okay, data is to be provided while configuring the AutoML experiment, so the data is loaded using data asset, so we need to create a data asset, and there are three types of data assets we can have in Azure Machine Learning.

**[1:54:44]** One is the ML table. So ML table, it's a data set which points to a regular data.

**[1:54:56]** Right.

**[1:54:57]** And...

**[1:54:59]** To create an ML table data set, we also need to provide a schema, how to read a tabular data, because the data could be a CSC file, it could be a TSC file, et cetera, right? So when we create a ML table, right, it points to a tabular data and...

**[1:55:18]** It is looking for a schema also which tells how to read the data. So if the data is a CSV in the schema, we define that the delimiter is comma and that's how you should be reading the data. So that's a ML table data set we can create.

**[1:55:37]** Data asset types are URI file.

**[1:55:43]** which points to any file, maybe in a BLOB storage or in a data lake, right? So URF file points to a file. Okay, it could be a PDF file. It need not to be a tabular data. It could be an image. It could be an audio file, for example.

**[1:56:01]** Then there is URI folder.

**[1:56:05]** which points to a folder and the folder will have multiple files in that folder. So these are the three type of data assets we have, ML table, URL file, and URL folder.

**[1:56:21]** Okay, so once we are able to create a data asset, right, we can make use of input. So we need to install a library with this Azure AIML using pip install.

**[1:56:39]** Azure AIML, right? This will install the Python SDK to use the AML resource, right? So this library has the packages so that we can.

**[1:56:59]** Let's say manage our Azure Machine Learning workspace. We can create a compute using this library. We can configure our compute, we can create a data set, right, etc. So here we are seeing we are using this.

**[1:57:17]** package importing input here and using input. We are able to.

**[1:57:25]** Use a data asset.

**[1:57:29]** The data set name is, that's the name of the data asset, right? It's an ML table data asset, and we are able to get the data into this variable.

**[1:57:43]** So we can create a data set, we can use an existing data asset and write using input and get the data loaded. So this is the input command to load a data.

**[1:58:00]** Using a data asset.

**[1:58:04]** So simply providing name of the data set and right, we are able to load the data. So that's the first step we need to do before we can configure auto ML job. We need to get the data available in our Jupyter Notebook.

**[1:58:19]** Then we can do featurization; we can configure featurization.

**[1:58:27]** So.

**[1:58:29]** These are some of the featurization techniques, right? We can do feature engineering, creating some new columns, remove certain high cardinality features in the data because they are not important for making a prediction. So we should be dropping some columns like ID columns, which are unique for every row. So we may have high cardinality features which we, which we.

**[1:58:52]** We may try to drop.

**[1:58:55]** If you have text in the data, we can use encoding techniques like one-hot encoding, bag of words.

**[1:59:03]** So, numerous techniques are supported in featurization. We may try providing a technique how to treat the null values, right? So, this all things can be configured. We may set featurization to auto, we can set featurization to off, or maybe we can...

**[1:59:22]** Configure the.

**[1:59:24]** featurization step. This can be done. Once this is done, we can explore what all algorithms are available. So around 30 to 35 algorithms are available for auto ML support, right? And maybe.

**[1:59:44]** for our requirement, we need to be restricting ourselves. Okay, maybe we don't want to train a certain algorithm. So for example, if let's say we are building a fraud detection system and we do not want auto ML to train a simple model like logistic regression.

**[2:00:04]** Okay, so we can put this model into restriction.

**[2:00:11]** while we configure auto ML jobs. So this model will not be getting trained. So it will look at all the models which are not restricted. It will randomly select among that list and pick up those algorithms, use it, and train those models.

**[2:00:30]** In parallel.

**[2:00:38]** Yeah, so...

**[2:00:40]** This can be done. Going further, we further define the primary metric. We set the limits to our experiment because AutoML could be a time-consuming job because let's say if we are training 5 models or

**[2:00:59]** It means that there are five trials we are doing. Each trial means one model training. Okay, so we may have 5 models to be trained that will be consuming the time and the resource. So to have a balance between the cost and the time.

**[2:01:19]** Great, we can set the limits that.

**[2:01:22]** For each time.

**[2:01:25]** for each model training, you should not be spending more than 20 minutes. So we can set the timeout limit for each model training for the whole experiment. Also, we can set the limits that maximum you can have.

**[2:01:41]** 60 minutes and the job should be completed, else the job would be terminated then. So we may set these limits while configuring the job. Further, we can configure featurization, et cetera, right? The training properties can be set.

**[2:02:01]** Once it is set, we can use AutoML.classification if you are doing a classification job.

**[2:02:09]** If you're doing the...

**[2:02:11]** Regression. So that's auto ML regression and we can configure the regression task. So currently auto ML supports classification, regression.

**[2:02:24]** and time series forecasting.

**[2:02:28]** So, for using Azure AML, we are importing AutoML. We are configuring this job, which compute to use to do the AutoML, the name of the experiment.

**[2:02:43]** This is the data.

**[2:02:47]** Here we need to provide target column that this is the target column in the data. So this is our column name.

**[2:02:58]** So because model to get trained, it should know what are the inputs, what is the target column. So it will train the model on this data. Primary metric we specify as accuracy.

**[2:03:14]** Further going ahead, we are providing cross validation 5 folds for evaluating the model, evaluating each trial. We may set explainability as true, which allows us to get the model explanation.

**[2:03:35]** So what is the model explanation? So maybe like model, let's say it is predicting person is diabetic. So on what grounds it says that person is diabetic, right? We should be able to, the model should be able to explain.

**[2:03:54]** explain that. Okay, if we set the explainability as true, it would be providing certain bar charts, right, that we will be looking when we talk about RAI dashboard.

**[2:04:07]** Okay, so it provides certain bar charts which tells that even if the model is predicting that person is diabetic, is it using the age as more important feature or is it using the, let's say, BMI value as important feature and making the prediction? So

**[2:04:26]** The model is explaining its decision why the person is diabetic, what features were important to predict the person is diabetic. Okay, so explainability is important because we cannot just have a black box AI which predicts the person is diabetic or not.

**[2:04:46]** The AI should be explaining why it is diabetic, or on what grounds it's predicting it's diabetic. This help us better interpret.

**[2:04:57]** Model output.

**[2:05:01]** We develop a better, we develop trust on the model, why it is doing so, and maybe if the model is wrong, we can debug that and...

**[2:05:13]** we can debug and see what all corrections has to be done so that model generates a correct outcome. So this can be done if we set the model explainability as true.

**[2:05:29]** Yeah.

**[2:05:31]** So, we can set the limits further, limits for each trial for the whole experiment. How many trials we want to have? Five trials means what? It would be training, it will be picking up five randomly algorithms, training the five models, and...

**[2:05:49]** Right, providing the five models, we may set early termination as true. This also we can set, so we can set early termination as true, because...


#### AutoML — cost, early stopping & child jobs  `[2:06:01]`

**[2:06:01]** The AutoML, it is expensive, right? Because we are training multiple models that may take some time. And early termination.

**[2:06:13]** Make sure that.

**[2:06:15]** If the model that we are training.

**[2:06:18]** If with training iterations, right, if it is not improving.

**[2:06:24]** It should stop training further.

**[2:06:27]** So, if the training, because we should not be unnecessarily doing a...

**[2:06:35]** iterating, right? We should not be iterating on if the model is not improving with iterations, right? So there's no point of having a very long model training going on without any improvements we see in model training. So we may set early termination.

**[2:06:54]** Set, we can set it as true. If you're setting as a true, then...

**[2:06:59]** The model.

**[2:07:01]** which is getting trained, right? If it is not improving, right, during the training process, we must stop training the model further and we can go ahead with the next model training.

**[2:07:12]** So we can set early termination, early we can terminate model training. This can be done just to have a balance between cost and rate.

**[2:07:27]** And the resources we are we are consuming, right?

**[2:07:31]** And once it's all done, once we are setting up the limits, configuring a classification or a regression job, defining the compute, the target columns, the primary metric, we can simply go ahead and create or update. So using this, we are.

**[2:07:50]** Simply submitting the job.

**[2:07:56]** So when we are submitting the job, the job returns a URL. It returns a URL where we can go to the URL and cheque the job status. Okay, how's the job? Is it in queue? Is the job running or is it in the finalising stage?

**[2:08:15]** etc. So even if the job has failed, we can cheque the reason why the job has failed, right? So those things can be examined by going to the URL.

**[2:08:27]** Okay.

**[2:08:29]** Where we can cheque the Auto ML job now.

**[2:08:34]** When we submit this job, right? Let's say we have set it to five trials, so each trial is 1 child job.

**[2:08:45]** Auto ML itself is a job. It's an Auto ML job we have. Within this job, we have many child jobs because training one model is 1 child job.

**[2:08:59]** Training the second model is another child job. Even if you're doing featurization, let's say we are normalising the data. That again is a step in AutoML, which is again another child job we have. So in the AutoML job, we can find many child jobs.

**[2:09:19]** pointing to a featurization step, pointing to an individual model getting trained, right? So that's the AutoML job we would be looking at in the AML.

**[2:09:38]** And here we see the output of auto ML. So we can see this is the job and we can see, we can go to the models tab and we can see five models are trained here. And their best model is the voting ensemble model because the primary metric was accuracy and.

**[2:10:00]** It has the highest accuracy. We can click on view explanation and see the model explanations. This can be done. We can go to data guardrails and see any potential issues with our data. We can go to child jobs and see all the child jobs of the auto ML job.

**[2:10:21]** Okay, go to overview to this to see the summary of the AutoML job. So this is something how we would be looking in the.

**[2:10:31]** Looking the job.

**[2:10:34]** the AutoML job, right, where we can explore the job and right.

**[2:10:40]** Ohh.

**[2:10:42]** See the output of the auto ML. So the outcome is voting and symbol is the best model.

**[2:10:48]** On our data.

**[2:10:50]** Great.

**[2:10:56]** And here we see that guardrails, as we discussed, right? It has the three states, pass, done, alerted, right? It can, it has supported data guardrails for different data quality checks, right?

**[2:11:17]** So, I can know, sorry.

**[2:11:24]** We can take this short knowledge cheque and then we'll take a short break going further than.

**[2:11:33]** We will explore how to do auto ML in machine learning. So I have that demonstration available and I'll show you the auto ML outcome. OK, after the break. So before we take a break, let's quickly have this knowledge check. Can we?

**[2:11:52]** It's ABC. What do you what you said for the first one?

**[2:12:10]** B.

**[2:12:13]** B OK.


#### Knowledge check  `[2:12:21]`

**[2:12:21]** Okay, thank you for the responses. So here it says we are using AutoML. We need to find the best model.

**[2:12:32]** With the best AUC weighted metric.

**[2:12:52]** Yeah, so B may not be an appropriate answer. It would be the C because it's a metric, right? It's a primary metric, which it's the criteria to define a best model.

**[2:13:07]** Right, so this is a primary metric. Maybe it's accuracy, it's AUC value right now, right? So it's the primary metric which decides which is the criteria, right, for selecting the best model. Target column name would be the...

**[2:13:26]** maybe diabetic, right, which help AutoML understand what is target, what is the input, and it will train the model. So to find the model with the best EUC weighted metric, it's the primary metric parameter.

**[2:13:45]** I hope that's correct.

**[2:13:49]** And second one.

**[2:14:06]** A, B, or C?

**[2:14:17]** It.

**[2:14:22]** So we agree to it. It's C because we don't want the data to be changed.

**[2:14:29]** Data should not be changed. We set the featurization to off.

**[2:14:35]** Yeah.

**[2:14:37]** That's correct.

**[2:14:41]** And thank you for the responses. It's really great to see. So we all agree with the option C. Great. That's nice.

**[2:14:55]** So we may take a short break here. Coming back then, we will...

**[2:15:04]** We'll go ahead and have a demonstration on AutoML.

**[2:15:09]** Yeah, I hope that's all good. Anything before we take a break?

**[2:15:16]** Uh, Kaushal, can you help me with the going on platform?


#### Break  `[2:15:20]`

**[2:15:20]** Yes, yeah, so let me just share the timer and guys, you may take a short break here for 15 minutes and let me take the issues related to the coinit portal, if yeah, please, yeah.

**[2:15:36]** Yeah, Rohit, please, if you can share your screen.

**[2:15:40]** Yeah, just let me, wait a minute.

**[2:16:11]** I don't see it's getting reflected here.

**[2:16:19]** Okay.

**[2:16:22]** Mm.

**[2:16:30]** Ohh.

**[2:16:35]** We have logged out and login. Did we try that?

**[2:16:39]** Yeah, I have tried it.

**[2:16:43]** Okay.

**[2:16:46]** Same problem for me, also.

**[2:16:53]** SH.

**[2:16:54]** Can you share that screenshot of that drop down? I'll just raise a ticket. Who else? Yeah, who else facing the same issue? If I know it's.

**[2:16:59]** Yeah, sure.

**[2:17:05]** Yeah, I'm also not able to see.

**[2:17:08]** Yeah.

**[2:17:09]** In the drop-down.

**[2:17:12]** So Lokesh, if you can provide me with your mail ID along with Harshit with your screenshot, please provide me the mail ID. I'll just raise a ticket for it.

**[2:17:23]** Please provide the mail ID in the chat. Yeah.

**[2:17:24]** Oh, sorry.

**[2:17:25]** Yeah.

**[2:17:28]** Pauroosh, I am also able to log in to both, as in the training key is training key and that vote input.

**[2:17:28]** Okay.

**[2:17:43]** Yeah.

**[2:17:45]** We are so you are also not able to see the course name, right?

**[2:17:45]** Okay.

**[2:17:49]** Kaur.

**[2:17:51]** I have shared the screenshot in the chat box.

**[2:17:51]** OK, please.

**[2:17:55]** That.

**[2:18:00]** I'm unable to log in to the key provider.

**[2:18:04]** Kaushal, it's your issue with the key, the key redemption or with the accessing the Queenic portal if I know that.

**[2:18:14]** What?

**[2:18:15]** Both, OK.

**[2:18:19]** S.

**[2:18:19]** Ohh yeah, hi Kaushal. Actually, the this training is not showing in my portal, like actually it was part of the other two trainings also, so the other two is showing this one is not showing.

**[2:18:22]** Jha.

**[2:18:34]** Please provide your mail ID in the chat. OK, yeah, yeah.

**[2:18:37]** Sure, sure.

**[2:18:42]** Thank you.

**[2:19:04]** Kaushal, if you're using a personal laptop or because I see that's a restriction from the KPMG, right, for key redemption.

**[2:19:06]** Yeah.

**[2:19:14]** I'm not using, I'm using, I'm logging through my work laptop.

**[2:19:14]** Dread.

**[2:19:22]** Yeah, please log in with a personal account, personal ID using Microsoft account. If you can share your screen, I can just look at that.

**[2:19:27]** Okay.

**[2:19:33]** Yeah, I am logging it through this KPMG account, so I need to use my personal ID.

**[2:19:39]** Correct. So you need not to select Intra ID, select Microsoft account, use your personal ID and login.

**[2:19:48]** This should work.

**[2:19:48]** Yeah, I'll just try it. I'll try it.

**[2:19:51]** Yeah.

**[2:20:43]** So I got the screenshot and collected all your mail IDs and let me just cheque with the team, right?

**[2:20:59]** And I would be able to resolve the query maybe by tomorrow's session. OK.

**[2:21:10]** Balram, if you can share your screen, is just we need to click on that course name and the drop-down appears.

**[2:21:19]** Actually, I did log in through my personal laptop in the 20 portal. So, and I'm attending this session with my official KPMs laptop.

**[2:21:25]** Okay.

**[2:21:31]** I cannot share the screen.

**[2:21:35]** Alright, so can you see the screenshot? It's just we need to click on that course name, your training topic, and all the course.

**[2:21:46]** you are enrolled with Koinic that will appear. So that's the dropdown we are referring to.

**[2:21:58]** You need to select your this class, this course, AI 300 and great. You should be able to find that course in the My Coinic portal. If not, just provide your mail ID in the chat.

**[2:22:11]** I will look into the issue, yeah.

**[2:22:12]** Um...

**[2:22:14]** Yep, I think I need to provide the mail ID on it because I'm not able to see the dropout.

**[2:22:21]** OK, OK, so that's the first course you have enrolled at Michael, if I know.

**[2:22:28]** No, I had also enrolled for AI 103 and it is reflecting in my profile.

**[2:22:36]** So that course is reflecting, but this course is not reflecting, right?

**[2:22:39]** Right, yep, yep.

**[2:22:41]** OK, may I know if you have marked your attendance?

**[2:22:44]** Yes, I did market with my phone.

**[2:22:51]** By using that scanner to work with.

**[2:22:57]** Okay, just to checking that.

**[2:23:03]** Checking your attendance.

**[2:23:04]** Yeah, I think it is a problem with attendance only because in AI 103 also we faced the same.

**[2:23:13]** Yeah, your attendance is not bad. If you can just mark your attendance again. I can't see your attendance here.

**[2:23:20]** Sure, just a second.

**[2:23:29]** Kaushal as well, I can't see your attendance. You need to mark your attendance so that you can see the course in the MyConic portal. So those who are not able to see the course in MyConic portal, your attendance is not yet marked. You need to mark it here.

**[2:23:45]** I have.

**[2:23:46]** I have done it two times and it has been submitted.

**[2:23:51]** Yeah, Kaushal, same from my side.

**[2:23:51]** Yeah.

**[2:23:53]** If same for my set, too.

**[2:23:57]** But if I just show you...

**[2:23:58]** Yeah, saying I also submitted attendance twice.

**[2:24:02]** If I just show you my screen, right? I have only these participants mark the tenants. I don't, I see Harshit here. Kaushal, your name is not here, right?

**[2:24:17]** Yeah, I think there will be some problem with attendance marking.

**[2:24:22]** Can you please cheque it again? I had we submitted it.

**[2:24:22]** Correct.

**[2:24:25]** How should I not wise, but mine is not reflecting. I'm not Harshil Gupta. Mine is Harshil Guru.

**[2:24:37]** Yes.

**[2:24:39]** Could you please refresh it? I had submitted it again.

**[2:24:47]** It may take a bit of time, maybe, but reflecting, it's...

**[2:24:55]** I think what maybe you can do is you can mark our attendance from your end to web click. That's what our previous trainer did. So it is not reflecting from.

**[2:25:05]** Okay.

**[2:25:06]** I cannot mark it. I cannot mark the first attendance that has to be done from your end only. I can mark the rest of the attendance if once it is marked the first if it is marked.

**[2:25:06]** I think from that.

**[2:25:14]** Ohh, OK.

**[2:25:18]** I mean.

**[2:25:21]** Yeah.

**[2:25:24]** Is the QR code working? I mean, we can see that attendance link and we can mark attendance rate.

**[2:25:31]** If I know that.

**[2:25:33]** If we are totally able to submit the attendance, we are getting the window also, like thank you and all submitting for your letter has been saved successfully, like that it is still.

**[2:25:37]** Yeah.

**[2:25:46]** Okay.

**[2:25:46]** Can you let me know now it is visible to you or not, because I have again submitted it?

**[2:25:56]** Maybe I'll just log out and refresh this page and okay, I'll just do that. Just give me a minute. Okay.

**[2:26:05]** If...

**[2:26:26]** It is not reflecting.

**[2:26:30]** Ohh, got you.

**[2:26:31]** Kaushal, is my attendance reflecting Satyam Raj?

**[2:26:38]** No.

**[2:26:39]** So, that's the reason why the course is not coming in the micro unique portal, because the attendance is the first attendance is not marked. That's the reason.

**[2:26:49]** Okay, and uh...

**[2:26:51]** Maybe if you can just give me, I have collected your mail IDs, right? Those who are facing attendance issue or logging or not able to find the course, right? Let me raise a ticket for this. Okay.

**[2:27:11]** But I hope we have redeemed the training key. Am I correct?

**[2:27:17]** Yes.

**[2:27:18]** Yes.

**[2:27:19]** Yeah, okay.

**[2:27:19]** Yes, yes.

**[2:27:21]** All good done. No worries.

**[2:27:25]** No worries, so make sure you have you are providing your e-mail ID in the in the chat. OK, and I'll raise I'll raise a ticket that attendance is not able to mark. OK.

**[2:27:43]** That should resolve the issue. Once attendance is marked, you would be able to find the course in the MyCoinique portal.

**[2:27:52]** Great, I'll get back to you on the attendance again.

**[2:27:58]** Sure, sure, question.

**[2:28:01]** Yeah.

**[2:28:06]** Training key.

**[2:28:35]** Sound.

**[2:28:44]** Kaushal, if you can just type or just simply copy paste the training key.

**[2:28:49]** Yeah, I have done it. So now I am able to go through this interactive labs.

**[2:28:55]** Okay, that's great. So we are able to redeem the key. Yeah, that's good.

**[2:28:59]** Open.

**[2:29:00]** We'll update you recording utterance later, OK? Yeah, OK.

**[2:29:03]** Thank you so much.

**[2:29:05]** Great. Let me go back then. OK.

**[2:29:12]** Flip.

**[2:29:21]** Okay, I see you guys after the break. Okay, then.

**[2:29:28]** Joshi.

**[2:42:23]** Welcome back, so everyone.

**[2:42:37]** Yeah.

**[2:42:39]** Chris.

**[2:42:46]** Great, great. Yeah, thank you for the reactions.

**[2:42:54]** So let me share my screen. OK.

**[2:43:43]** So those facing issues with the attendance, please, I'll update you. Okay, I have raised a ticket for this attendance issue. Okay.


### Lab — Find the Best Classification Model with Azure ML  `[2:43:58]`


#### Resume after break  `[2:43:58]`

**[2:43:58]** Alright, so let's get going.

**[2:44:05]** So, we have seen how we can use AutoML, right? We can configure an AutoML job, submit the job, and we can cheque the AutoML job outcomes as well. So, this is a part of our first lab.

**[2:44:23]** So, if I...

**[2:44:26]** If I go to the first lab here, which is find the best classification model with Azure Machine Learning. OK.

**[2:44:37]** That's our lab one.

**[2:44:40]** And let me quickly demonstrate this and we will move to the next topic.

**[2:44:47]** OK, so.

**[2:44:49]** Ohh, we'll see the last N.R. if we can find and we can perform the labs, else we'll be performing the labs tomorrow, OK?

**[2:45:03]** Because it's a very short duration course and we have so many labs to be completed, right? Let me provide the demonstration and then with what time remains, we will be going and performing the labs. Is that okay?

**[2:45:25]** Yeah, if I get your opinion on this.

**[2:45:32]** All right, great. Thank you. Okay.

**[2:45:40]** So...

**[2:45:42]** That's our first lab, and...

**[2:45:45]** Even know, let me.

**[2:45:51]** You can even access this lab or on a GitHub link. So let me share this GitHub link in the chat.

**[2:46:06]** And if you go to the GitHub link.

**[2:46:12]** You will find the instructions to complete this slag.

**[2:46:18]** Okay, so need not to worry about this GitHub link because when you perform the lab, you will launch a virtual machine. There you will find the instructions to perform the lab as well. But these instructions are available from Microsoft Learning at the GitHub repository as well, so which we can see.

**[2:46:41]** And here at this link, if we go to docs here, all the lab instructions are provided here. Okay, so going to docs, here is our first lab, the lab number one.


#### Lab walkthrough — AutoML job  `[2:46:57]`

**[2:46:57]** Find the best classification model with Azure Machine Learning. So I have gone through this instructions and even implemented it in the Azure. So let me take you.

**[2:47:13]** To the Azure portal, so here we are at the Azure portal.

**[2:47:19]** We can see a V.

**[2:47:23]** We have created the workspace. We are in the studio right now. And if we go to the notebook section.

**[2:47:34]** In experiments, in experimentation folder, there are few Jupiter notebooks available, so which here we can find classification with auto ML.

**[2:47:48]** OK, so.

**[2:47:51]** how to use automated machine learning to build multiple classification models and we can retrieve the best model.

**[2:48:00]** Okay, so these cells I have already executed and so first we need to install Azure AIML. We make sure it is installed. Then we go ahead, connect this notebook to the workspace so that we can write the code and consume the resources of.

**[2:48:20]** this workspace, right? So we connect this notebook to the workspace by passing the credentials and getting a client handle here. So using client handle, we can...

**[2:48:33]** Connect to the workspace resources like data asset and we can submit an auto e-mail job. So going further.

**[2:48:43]** Here we see we are getting the data asset that we have already created, diabetes training version one. And if I show you in the other tab, we can go to the assets under data.

**[2:49:01]** We can see diabetes training, that's a data asset is created. It is a ML table type. And if you go to the data asset, let's look at the data on which we are training models. So once we are at the data asset, we can scroll down.

**[2:49:22]** We can go to Data Store Browse, and we can go to the storage location where the file it's pointing to is available, so we can see diabetes or CSV, and it comes with a ML table schema, so if you click on the schema.

**[2:49:39]** It's a config file which tells how to read the CSV. So it uses a comma as a delimiter. And here is the data available.

**[2:49:50]** So this is the input data where we have these features, patient ID, number of pregnancies, plasma glucose, for example, BMI, and we have the target column available.

**[2:50:08]** OK. So going back then going to the notebook.

**[2:50:15]** So, once we are able to fetch the file using this input class, and going further using auto mail dot classification, we are able to create a classification job, updating the limits to that job, so we are...

**[2:50:33]** Maximum trials are five.

**[2:50:36]** We set the training so we are restricting or blocking logistic regression model here. Going further, we are submitting the classification job. The job when we submit, it returns a URL and we can click on this link. OK, we can cheque the auto ML job.

**[2:50:58]** This job has already completed for me and we can cheque the guardrails here.

**[2:51:07]** So it says status passed for the supported data cardrails. Then under models and the child jobs, we can see voting and symbol model has, is the best model.

**[2:51:24]** It has the accuracy, highest accuracy of 0.953 here. And there are, so we are able to train 5 models here. And maybe in fact click on this model. So we are looking at a.

**[2:51:40]** a child job within the auto ML job. So if I click on this.

**[2:51:46]** So, that's a voting ensemble.

**[2:51:54]** We can see all the metrics of this model, AUC score, accuracy value, and precision recall, FL score, etc.

**[2:52:04]** Fate.

**[2:52:06]** This you can see we can even go to the job section here and look at the AutoML job. This can be done. So if I go to jobs.

**[2:52:15]** This is the auto ML job experiment because that's what we provided here when we

**[2:52:24]** So here the experiment name is AutoML class dev, right? So.

**[2:52:30]** That's the experiment, and if we go to the experiment, we can see there are many child jobs within this job. So, if we can click on this arrow, these are the multiple child jobs available, and we have this best.

**[2:52:47]** The best joke.

**[2:52:49]** The best child job.

**[2:52:51]** And if you click on this, that will take us to the child job of voting ensemble only. So we can click on the model. We can see we get the model summary. That's the algorithm used and we get the IS accuracy.

**[2:53:07]** So this is like an expected output when we complete the auto ML lab here.

**[2:53:16]** OK, so let me go back. OK, because here we may note that.

**[2:53:24]** This is the lab instruction. We go ahead and...

**[2:53:30]** Complete the first part where...

**[2:53:33]** We have executed this notebook.

**[2:53:38]** Ten.

**[2:53:40]** We will further explore what is this ML Flow library. OK, how ML Flow help us tracking the model training. OK, so let's go to this topic. OK, anything before we go ahead? Would you like to add?

**[2:54:06]** All right.

**[2:54:10]** So let's go ahead. So we'll discuss further. OK, we'll talk about the ML Flow library and how it helps us tracking the model training. OK, so ML Flow is an open source library, right, where it has one of the component which is.

**[2:54:29]** the ML flow tracking, which allow us to log everything about the model that we are training. So because when we are training a model, let's say we are training a logistic regression model, this model.

**[2:54:45]** When we are training, this model has parameters.

**[2:54:50]** Okay, so what parameters this model may have so we can even cheque the

**[2:54:57]** logistic regression, scikit-learn documentation link, logistic regression.

**[2:55:07]** So, Scikit-learn is the open source, very popular library for building our own machine learning models, and we are at Scikit-learn and we are looking at logistic regression, so...


#### Train & deploy a model to an endpoint  `[2:55:22]`

**[2:55:22]** So this model, that's the logistic regression model and it will use the data and we would be able to train a logistic regression model. What we can note here is that these are the parameters.

**[2:55:37]** Of the model, so parameters are nothing but like these are the model parameters. OK, and by changing these values, our model performance may change. OK, so if let's say if the C value is 1, OK, so what's the C value?

**[2:55:57]** You can further look at different parameters and we see C's inverse of regular share strength. OK, so the more value we keep, there is a stronger regularisation and model may not overfit. OK, so if the model is overfitting, we may keep C's has a higher value and...

**[2:56:17]** we can train the model. So you can see maximum iterations are 100 by default. If we if I want to train for a longer period of longer time, right, we may set the maximum iterations to 1000 and the model will be trained for these many iterations.

**[2:56:36]** So these are the parameters, these are the default values of these parameters and we can change this parameter values also. And if we change the value, let's say C is 1, maybe the accuracy of the model is 80%. If I make it 0.01, the accuracy may be changed. Okay, so.

**[2:56:55]** these parameters has an effect on model performance. Okay, so when we, so let me share this link.

**[2:57:07]** Yes.

**[2:57:18]** So when we are training a model, right, the model training, we find the model will have, it's getting trained with certain parameters.

**[2:57:31]** which we may want to log because I want to log what is the value of C for which I am training the model. I want to log this. Then we can log model performance in terms of the performance metrics here. So maybe we are evaluating the model in terms of

**[2:57:51]** accuracy and effort score. So this also I would like to log. Further, if let's say I have a plan to deploy this model, I need to register it first. I need to save this model. ML Flow help us getting a model folder, okay, which is a very important folder which we need it later on.

**[2:58:14]** to deploy the model to an endpoint. So we want to log this model folder also. So if we log this, this folder will be containing some files like picker file it will have. So it's a binary form of our model that we have trained. So that's a picker file.

**[2:58:34]** that we need to log. Later, we need to use it for deployment purpose. Other files are also there, ML model file, metadata information, right, of our model training, right, that need to be logged. So it all comes under the model folder. So we need to log these.

**[2:58:55]** Ohh.

**[2:58:57]** These parameters, metrics, artifacts, maybe like we have image, we are creating a precision recall curve or maybe AUC curve, right?

**[2:59:13]** we are generating and we want to log this image also. So the image will be logged as an artifact. So ML Flow help us managing our whole machine learning experiment, logging the details so that maybe like we have trained model one, trained model 2.

**[2:59:32]** log their details and later I want to compare these two jobs. So, so model one, they have the accuracy of this and precision of this and model 2 have some other accuracy precision. So, two runs can be compared easily if you are able to log these details, right?

**[2:59:51]** We can filter.

**[2:59:55]** different jobs, right? Maybe I want to get only those jobs, right, where I'm training a random forest classifier. So I can, out of all the data, right, all the logs, I can apply some philtres and get only some relevant logs only.

**[3:00:15]** some relevant runs only, right? This can be done. So this is all managed using the ML flow.

**[3:00:22]** Right, so we'll explore how to use ML Flow.

**[3:00:27]** right, in our notebook and how we can log these parameters, metrics, artifacts, so that later it can be used for deployment purpose. So to use ML Flow in Azure Machine Learning, we need to install ML Flow, install Azure ML ML Flow.

**[3:00:47]** Great, so these are the package to be installed.

**[3:00:51]** Once installed, then we can configure the ML Flow UI. So ML Flow, once installed, right, when it is used in the code with model training, right, we need to 1st set the tracking URI. So it's the URI or it's a location where.

**[3:01:12]** we can launch the ML Flow UI, the user interface, where we can look at that interface, see what all runs that we have, we are able to log using ML Flow, what are the parameters of that run.

**[3:01:28]** What are the metrics, artifacts, right?

**[3:01:32]** So all of that can be seen in that UI. So the UI will be.


#### MLflow tracking  `[3:01:40]`

**[3:01:40]** will be launched using the ML flow tracking URI. So we can set that and then we can further go ahead and use the ML flow for tracking our model training. So the steps are, first we need to create an experiment. Okay, we train the model.

**[3:01:59]** So we need to import ML flow, right, and use ML flow while training the model. And we can review experiment runs, right, compare different runs, etc. and see which is our best run. We can retrieve that best run.

**[3:02:19]** and use it later on maybe for deployment. Okay, so to use ML Flow, we need to have, we have two methods of tracking any experiment. One is auto log method, where ML Flow will do the logging automatically. So it will be.

**[3:02:39]** Doing auto login.

**[3:02:43]** So when it does the auto logging, any metrics like once we are doing the auto logging, the default logs for parameters metrics will get automatically logged. So there would be, let's say we are training the logistic regression model.

**[3:03:04]** with ML flow in auto lock. So when we are using ML flow in auto lock, we would be able to get the default.

**[3:03:17]** parameters. So there would be default parameters which will be logged. Default metrics, so around 8 to 10 metrics are there that we would be able to log. We would be also able to log model folder containing information about the model training.

**[3:03:37]** So, so when, like, simply if you want to use the ML flow, this is the simplest way.

**[3:03:46]** to use ML flow using the auto log. Just one line of the code in our script and we are able to use ML flow and do all the auto logging. If you want to do custom logging because maybe have something very specific I want to log.

**[3:04:04]** I don't want to log all the metrics or the parameters. I can.

**[3:04:09]** Go ahead with the custom logging also using ML flow.log, right? So we'll see what are the ways how we can do the logging, do the custom logging.

**[3:04:24]** Select.

**[3:04:25]** So first going ahead, we need to create an ML flow experiment. So using set experiment, we are able to create an experiment.

**[3:04:37]** The name of the experiment is this. So any run will come within this experiment so that we can compare different runs within that experiment also. So using set experiments, we are able to create an ML flow experiment. And here we note if you're using ML flow in auto log.

**[3:04:58]** Simply import ML flow, one line of code, and ML flow will do the auto logging for what models we are trading here. So this can be done. That's a simple auto log. We can do custom logging using log parameter.

**[3:05:15]** Log metric, log artifact.

**[3:05:19]** Here we note.

**[3:05:22]** If you want to log a parameter, we use log underscore param and what we want to log, it comes as a key value pair. So maybe like log param, then I want to log, let's say, parameter estimator.

**[3:05:40]** Okay.

**[3:05:42]** And I provide the name of the estimator that is the random forest.

**[3:05:48]** something, okay, which I want to log. So it's all text, it will be coming as a key value pair. Okay, so I'm able to log this parameter. We can log metric also, right? Any custom, maybe I want to log only the accuracy. I can do that. I can log an artifact.

**[3:06:08]** So anything which is not parameter or metric, which it will be logged as an artifact. So maybe a text file that we are logging, we are writing a text file, we need to log it as an artifact. Any image we are creating that will be logged as an artifact. Maybe we want to save the image as a pickle file format.

**[3:06:29]** That would be again an artefact we are logging. So that's how we can write a custom code.

**[3:06:39]** and do the custom logging.

**[3:06:43]** So we'll cheque in the labs also, like how to use ML flow. And here is how the output of ML flow looks like. So when we are using ML flow, maybe we are logging a metric. So we can cheque the metrics tab and we can see we are able to log accuracy and EUC value.

**[3:07:03]** So here we are logging only two metrics.

**[3:07:08]** So it indicates that this is a custom logging we have done, because had it been an auto log, we would have logged 8 to 10 metrics like precision, recall, F1 score, etc. Those all getting logged. We can cheque the images tab.

**[3:07:27]** and see what we have logged. So we are able to log ROC curve the image. If it was the auto logging, by default it would be logging 3 images.

**[3:07:38]** One is the confusion matrix, then precision recall curve, and AUC, the ROC curve. Those 3 images are generated by default.

**[3:07:50]** So...

**[3:07:52]** The use of ML flow is to like do the model training logging. OK, once we get the logs, we can even use ML flow to search runs in our experiment.

**[3:08:07]** What export is the experiment name? We have that experiment ID. By passing the experiment ID, we can search for all the runs within that experiment. We can even apply a filter. We can write a query that if the runs...

**[3:08:23]** has an accuracy of more than, let's say, 0.8, then only it will come in the search results. So we can write a query, apply some philtres on our runs, and we can get certain philtre runs, and we can examine those runs. This can be done. So.

**[3:08:43]** For all of this, we can use ML Flow and helping us with the model, tracking the model training.

**[3:08:52]** Eight.

**[3:08:54]** So let me go to a notebook, right, and show you the ML flow, okay? How that, how logging is done and what is the expected output of using ML flow.

**[3:09:07]** Let me then go to the portal.

**[3:09:12]** And here we have another luck, which is...

**[3:09:18]** Track model training with ML Flow.


#### Notebook — connect to workspace & predict  `[3:09:28]`

**[3:09:28]** All right, so here we first make sure Azure AIML is installed, connecting this notebook to the workspace that we do. Okay, going further, we are making sure ML flow is installed. Then we get the data. So it's a simple experiment that we are doing.

**[3:09:49]** Great.

**[3:09:51]** We are reading the data, okay, splitting the data into X&Y, right? Then splitting the data into 70-30 ratio further, 70% for training, 30% for testing the model.

**[3:10:06]** Then here we are importing ML flow, creating the experiment name, which is diabetes 4. That's the experiment name we have set. Going further, we start a new run and it's an auto log and we are training a logistic regression model. So using fit method.

**[3:10:28]** We are training the model, so we have the data available, the training data set, we are passing it to train method, the fit method, and we are training a logistic regression with the C value of point C value of 10, right? And it's an auto log ML flow we are using.

**[3:10:48]** And if you cheque the job here, so if I...

**[3:10:52]** Go to the jobs.

**[3:10:55]** Let me search for...

**[3:10:58]** ML flu experiment diabetes 4.

**[3:11:02]** This would be the...

**[3:11:06]** this run, the last run, and this is an auto log job, right, where we have used ML flow in auto log and we can note that we are able to log.

**[3:11:18]** All the tags, the parameters of our model training, all the metrics getting logged here, so we can cheque in the metrics tab also.

**[3:11:30]** Images, it's able to log 3 images.

**[3:11:34]** RUC curve, confusion matrix, species and recall curve.

**[3:11:38]** Then important here is output plus logs here where we can see we are able to log a model folder. So when we are using ML flow in auto log, we are able to get this model folder created and.

**[3:11:54]** We can see here we are able to get the binary image of our trained model. We also get requirement or text file, right? So these are those dependencies, right? The packages that to be installed so that we can load.

**[3:12:15]** Saved.

**[3:12:16]** train model that is a pickle file. We can load the pickle file.

**[3:12:22]** use the picker file for the model to make the predictions. So these are the libraries required. So maybe we can install this in our compute on which, right, we want to run our endpoint. So.

**[3:12:41]** So these are the requirements that is to be satisfied.

**[3:12:45]** We can also find a ML model file here, which contains the metadata information of our model training. So if you click on this.

**[3:12:58]** Here we note.

**[3:13:01]** the flavours of our model training. So here we are using scikit-learn to train our model.

**[3:13:11]** Okay.

**[3:13:12]** It's a pickle model that is generated using the Cloud Pickle library. OK, we can see there is a run ID. So run ID is the unique ID of this run. Specifying this run ID, we can point to the pickle file and we can later further use it for deploying the model.

**[3:13:33]** Like that. So that's the ML model file generator.

**[3:13:38]** It also generates YAML files, certain configuration files, which we can add with.

**[3:13:46]** inbuilt environment and we can create our own image. This image is then hosted on the cloud for the deployment purpose. So to create our own image, right, we can use this YAML file, create our own environment image and...

**[3:14:05]** so that this image can load this pickle file and we can make predictions using this model. So this, that's a very important folder, getting logged using ML flow.

**[3:14:21]** So this is how we can cheque the results in auto log here. And maybe we can go further in this notebook where we are.

**[3:14:31]** disabling auto log and now we will do the custom logging. So here is an example where we are training a model and we are doing custom logging where we are logging 1 parameter and one metric.

**[3:14:47]** accuracy and the regulation rate we are logging. So if I go back to the jobs here, we go to this job.

**[3:14:59]** And we can see we are able to log only one parameter and one metric. So this is a custom logging.

**[3:15:08]** We did not log any image, so we don't find any images in this image tab.

**[3:15:14]** Also, we did not log the model folder as an artifact. We did not log that, so no model folder is available.

**[3:15:24]** We can do custom logging and log the model folder also using log underscore artefact and we can log the model folder. This also can be done.

**[3:15:35]** Right. Further in this notebook, we are trying with a different to...

**[3:15:45]** Here, we are trying with another run and training a logistic regression model, again doing the custom logging, then.

**[3:15:54]** This time we are training another model, decision tree classifier, logging these two parameters. Going ahead, we are logging these two, one parameter, one metric. We are also saving the figure here. So the figure we are saving will be appearing in the current directory.

**[3:16:17]** So this lab simply focuses on how to use ML flow in auto log and custom logging, and how we can track the model training. So with this, we complete the lab one.

**[3:16:33]** Great.

**[3:16:36]** Anything would you like to add here so far?

**[3:16:47]** If that's all good.

**[3:16:59]** So maybe we have some time here.

**[3:17:07]** Right, we may launch the lab.

**[3:17:10]** And we may try completing our first lab, lab one.

**[3:17:17]** So this will allow us to understand, right, how we can go to this learn on demand platform, launch a VM, use the credentials provided in this VM. So if I click on launch here.

**[3:17:40]** So a VM will start.

**[3:17:44]** And the VM has a tab, resources tab, where we can go to this tab and we can find the credentials that we can use to log into Azure. And we can create AML workspace.

**[3:18:00]** By following the instructions, right?

**[3:18:04]** And we can complete this lab.

**[3:18:14]** Yeah, can we perform this lab? We have some time and I think we should be able to complete this lab within 40 minutes. Yeah, so.

**[3:18:32]** This can be done. What do you say?

**[3:18:37]** Shall we perform love one?

**[3:18:40]** Since there are no challenges with redeeming the training key and right, we can perform this lab.

**[3:19:18]** So this is how the VM, once we launch the lab, looks like. And here we have the resources stack.

**[3:19:27]** Right, we can see the we can see the credentials to log into the Azure portal.

**[3:19:34]** We also have the VM username and the password, and maybe I'll just log in to this VM.

**[3:19:46]** Right.

**[3:19:48]** Coming back to the instruction tab, so we can go to next and we can follow the instructions and we can do auto ML.

**[3:20:00]** And we can also have another within the same lab here. We will be exploring ML flow.

**[3:20:12]** for auto login, custom login, that we can do.

**[3:20:24]** Any challenge with the lab?

**[3:20:28]** Right, we can we can go ahead and perform the lab.

**[3:20:32]** Let me know.

**[3:20:40]** I can come to your lab, so...

**[3:20:44]** Take control of a lab also if any issues are there, right? This can be done.

**[3:20:51]** So please go ahead and let's perform our first lap.

**[3:20:56]** Okay, later on, we may not be able to get time to perform all the labs during the training. Okay, this may happen because it's a very short duration training. Try performing the labs and any challenges you face.

**[3:21:16]** may face. Okay, we can discuss it during the training.

**[3:21:21]** Yeah.

**[3:23:56]** Yeah.

**[3:24:47]** Participants, those participants who cannot access my Quinnic portal and cannot find the course in my Quinnic portal, please drop your mail ID in the chat. Those have already provided the mail ID, it's good.

**[3:25:06]** Those who have not provided the mail IDs, please share it in the chat so that I can include it in the ticket.

**[3:27:02]** Adspense those who can't see the course AI 300 in my coin portal.

**[3:27:10]** Please provide your mail ID in the chat if not provided.

**[3:27:19]** Okay.

**[3:43:01]** Ohh.

**[3:43:03]** Guys, those who are facing the attendance issues, if if you can just try now, maybe someone, if you can just try marking attendance.

**[3:50:24]** I hope the attendance issue is resolved.

**[3:50:31]** Yeah, anyone facing the issue?

**[3:50:36]** Let me know.

**[3:50:46]** Yesh.

**[3:53:02]** Is any challenge with the with the lab?

**[3:53:06]** With the credentials provided the lab execution, if I know.

**[3:53:13]** It's all going good.


#### Q&A / lab troubleshooting  `[3:53:16]`

**[3:53:16]** Yeah, just one question in lab one instruction 5 says in the compute instance tab, click select the terminal, but I don't see any terminal option there. I only see Jupiter lab or Jupiter something.

**[3:53:33]** Yeah, just next to Jupiter Lab, there is 3 dots out there. Just click on that, that will take you to the terminal.

**[3:53:49]** Let me, let me come. Did you get it?

**[3:53:49]** Let me see.

**[3:53:54]** Yeah, I got it now.

**[3:53:55]** Okay.

**[3:57:48]** Guys, I hope the attendance link it's working fine and those who are facing the issues with the attendance, marking the attendance, you can log into my query portal.

**[3:58:04]** It is resolved. You should be able to see the course in your MyQE portal. If anyone still cannot see, just let me know now.

---

## Day 2 Part 1 - Tue 2 Jun 2026 - Day 1 session close


- **Date:** Filed under Tuesday, 2 June 2026 (night batch, 21:30–01:30 IST)
- **Trainer:** Pauroosh Kaushal (Microsoft Certified Trainer), Koenig Solutions
- **Recording:** `…20260601_213008-Meeting Recording 1.mp4` (Part 1 of 2 listed under Tue 2 Jun, SharePoint Stream)
- **Length:** ~3:50  ·  **Captions:** 20



### Session close & Day 2 preview  `[1:05]`

**[1:05]** Anyone else facing issues with the attendance? Let me know in the chat.

**[1:12]** Okay.

**[1:15]** We should be able to find the course in my query portal. Today's recording will be available from tomorrow onwards, right? And you can cheque the recording link as well in the portal.

**[1:32]** So I hope no challenge so far, right?

**[1:47]** So tomorrow we'll go ahead, right?

**[1:52]** optimised model training that we'll do in Azure Machine Learning. We'll further go ahead and see how to integrate GitHub, GitHub actions to our AML and build a CICD pipeline. So this we can do.

**[2:13]** Okay, we will be deploying the model, right? So that would be the agenda for tomorrow's training, right? I hope it was informative.

**[2:25]** Yeah.

**[2:30]** Oh, Satyam, still not visible. I can see your attendance is marked and...

**[2:46]** Right.

**[2:47]** It is smart, you may try logging out and log in and you should be able to see the course.

**[2:59]** I hope you can see my screen and the attendance is marked. Yeah.

**[3:09]** Okay, okay, so sorry. I was reading the wrong message. My bad, Sanjay. Yeah. Oh, okay.

**[3:17]** So guys, thank you for joining and anything before we wrap up this today's session.

**[3:31]** All good.

**[3:33]** Okay, I see you guys then tomorrow, same time, and have a good day ahead.

**[3:40]** Yeah.

**[3:42]** Yep, thanks for attending the session and I'll see you tomorrow.

**[3:47]** Thank you.

**[3:50]** Great. Thank you.

---

## Day 2 Part 2 - Tue 2 Jun 2026 - Training, Tuning, Pipelines, CI-CD


- **Date:** Tuesday, 2 June 2026 (21:30–01:30 IST)
- **Trainer:** Pauroosh Kaushal (Microsoft Certified Trainer), Koenig Solutions
- **Recording:** `…20260602_213016-Meeting Recording.mp4` (Part 2 of 2 listed under Tue 2 Jun) — the full Day 2 session
- **Length:** ~3:59:55  ·  **Captions:** 992




### Recap & Module 1 (continued) — Training, Tuning & Pipelines  `[0:00]`


#### Session start & recap  `[0:00]`

**[0:11]** I hope you're doing well, and yeah, hi, Bera, if I'm correct here, please.

**[0:21]** Okay.

**[0:23]** Pete.

**[0:26]** Okay, that's great. Yeah, thank you for her response. Yeah, so guys, I just wanted to say we may spend just two more minutes, let all the participants join.

**[0:40]** With the session.

**[0:43]** And let me share the attendance link in the chat while the participants are joining.

**[0:53]** Yes.

**[1:19]** Oh, very good morning to all the participants.

**[1:23]** Let's wait for a minute. Let all the participants join. While the participants are joining, kindly mark your attendance. The attendance link is shared in the chat.

**[2:11]** Thank you.

**[3:11]** All right.

**[3:16]** So I hope there is no challenge marking the attendance, right? We are able to mark today's attendance.

**[3:30]** Great.

**[3:35]** OK. Thank you.

**[3:39]** Okay.

**[3:48]** So let's get going. Let's get started with the session. Let me share my screen.

**[3:58]** OK.

**[4:06]** Today's.

**[4:08]** Of.

**[4:12]** This one is marked for me.

**[4:19]** OK, sure.

**[5:28]** All right, so you may, sorry, you may track your attendance by logging to my query portal, right? For the queries regarding the attendance, so please find the QR code in the chat and you may mark the attendance. The link is the same if you have.

**[5:48]** Like if I have access to the previous day code, QR code, you can use that. The link, the attendance link remains the same.

**[5:57]** Ohh.

**[5:59]** Okay, so...

**[6:01]** Yeah.

**[6:04]** Let's get going.

**[6:08]** And.

**[6:15]** All right.

**[6:18]** I hope no challenge with marking attendance.

**[6:22]** Yeah.

**[6:27]** All right.

**[6:30]** Let's get started then. Okay. So let me share my screen.

**[6:38]** Any queries with the utterance link you may write in the post, you may post it in the chat and I'll be addressing the queries, no worries. Okay, so.

**[6:50]** Please find the QR code, the attendance link in the chat. You may mark your attendance. Further, you can track your attendance by going to mycoinning.com portal and you can track your attendance. You can go ahead and explore the coinning portal where...

**[7:09]** You can find the recording link for yesterday's session as well.

**[7:14]** OK, alright, so...

**[7:19]** Let's get going then. Let me share my screen.

**[7:37]** Alright, just give me a minute.

**[7:41]** Okay.

**[7:44]** Vatan.

**[7:55]** Alright, so let's review yesterday's session.

**[8:01]** So, in yesterday's session, we are able to...

**[8:07]** understand what is machine learning, right? What is a machine learning workflow, right? How we can build an AI development life cycle. We have seen the life cycle. Further going ahead, we explored the Azure Machine Learning workspace.

**[8:26]** where we have seen we can make use of auto ML so that we can train multiple models and retrieve the best model which is the best fit for our data. So we are able to submit the auto ML job, completed the job as well.

**[8:46]** Right. I hope with yesterday's lab there was no challenge so far, right? And we are able to perform the lab.

**[8:56]** Okay, then we went ahead, discussed the ML Flow library. We have seen the two logging ways, how we can log a machine learning experiment using ML Flow. We have the auto log and we can do custom logging as well.

**[9:16]** And we can track our model training.

**[9:21]** Right, so we can not only just do the logging, we can compare the logs, and we can identify which runs are giving the best performance, etc.

**[9:34]** So we can do custom logging as well as auto logging and we are able to complete this exercise.

**[9:42]** King.

**[9:44]** So today's agenda would be further going ahead, how we can optimise model training. We will talk about this. We'll go ahead and talk about hyperparameter twinning. So that's another important stage for optimising model training. Then.

**[10:06]** We'll look at how we can.


#### Register a model  `[10:09]`

**[10:09]** register a model or like we can further go ahead and see how we can register a model because that's a necessary step before we go for model deployment.

**[10:22]** Then we will talk about MLOps. We will see the integration of GitHub with Azure Machine Learning so that we can build certain automated CI/CD pipelines can be built. Okay, and finally we'll go ahead and deploy a model.

**[10:42]** Using Azure Machine Learning Service, so these are certain topics we'll be discussing today.

**[10:48]** Great.

**[10:50]** So anything would you like to add before we get going?

**[10:57]** If any challenge, yeah.

**[10:58]** Just one thing. Like, I'm not sure if it is already covered or will it gonna cover. The feature selection part, like sometime we have the file data and the data sets and some fields are not even required for this machine learning model, right?

**[11:11]** Mm.

**[11:18]** So how we do that feature selection or will it already gonna provide will they whoever have the data set they will gonna provide the details that which are.

**[11:30]** Ohh, like there is an output column right, which which is dependent in which which columns input fields.

**[11:35]** Just.

**[11:40]** Oh, yeah, so...

**[11:46]** Yeah, thank you for this question. Let me share my screen. Regarding the feature selection, right? So there are techniques like wherein we can identify which features are more important than the other, right? This...

**[12:05]** This is an essential part of a machine learning workflow, right? The techniques used are like recursive.

**[12:17]** Recursive feature elimination technique.

**[12:23]** Okay, we can use some techniques like PCA, principal component analysis. We can make use of, if we are specific to certain algorithms, there are techniques like P-value, we have, those can be used for doing the feature selection.

**[12:42]** So this is currently not the scope of this training. Okay. It's a part of the machine learning development, right? But as said, we don't have the topics related to it or the labs related to feature selection. Maybe I'll provide you certain documentation link in the chat.

**[13:01]** Okay, which is related to how to use scikit-learn library, what technique to use to do feature selection.

**[13:12]** Yeah, that that I'll shortly share it, maybe during the during the break, I will share the these links related to feature selection.

**[13:24]** Yeah, sure. Yeah, thank you.

**[13:24]** I hope that's okay, great.

**[13:28]** And.

**[13:35]** All right, so, so, so far we are using, yeah, yeah, so far we are creating a notebook that we have done in the previous session, and we are able to submit an auto ML job and we are able to train certain models and.

**[13:55]** It did do the best model right now, further going ahead, how we can optimise model training. Okay, so we should be working at at code level, how we can optimise ML workflow right further.

**[14:15]** How we can better prepare?

**[14:18]** a script, okay, so that it's production ready and later on the script can be used for deployment. So what are the best practices? Okay, what we should be going from the ideation phase, okay, through the experimentation. So when we are doing the experimentation.

**[14:38]** with different machine learning models. And during that period, right, we are working with the Jupyter notebooks because maybe we want to inspect certain variables during machine learning training. We may write some unnecessary code.

**[14:58]** Like some checkpoints, we may provide certain print statements we may provide to better do the experimentation and exploring the data as well as algorithms, right? But as the as we are more confident as the machine learning work.

**[15:17]** pipeline, it's more matured, right? We are sure that which algorithm to use for my data, right? Or what data pre-processing steps need to be performed to clean the data and which may give better results. So

**[15:36]** From the notebook, we should be going ahead to creating a script, so we convert.

**[15:47]** We convert the IPYNB file to a script file, the PI file. And when we do this conversion, we should make sure that we are removing non-essential codes, the checkpoints, or certain print statements, right, which are not necessary.

**[16:06]** which were used previously for debugging the code or looking at the intermediate outputs, etc. So we may go ahead and remove those code. We can further go when we are creating the PI file, we should be making sure that we refactor the code into functions.

**[16:26]** We have multiple functions in our PI file. Maybe there is a function, one for cleaning the data, one of the step of pre-processing, another function to drain the model, another to evaluate the model. So this makes the code more readable and...

**[16:45]** It's easy to debug the code as well.

**[16:48]** Finally, when we are creating this PI file, right, we should we are when we are testing the PI file in the terminal, right?

**[16:59]** Right, this should be done, and when we are testing file files, right, we should be using certain libraries, like our past library. OK, so our past library, we'll just see that, so even when we are testing the...

**[17:17]** our PI file. Maybe we want the test, we want the PI file to be tested on some new data and we may provide that new data in the terminal itself. So use those certain libraries like arg pass library, providing, helping us with providing arguments in the terminal.

**[17:37]** And so that we need not to go back to the PI file, right? Edit the PI file and then execute the PI file. So certain parameters, model parameters, if we have certain new data, those can be passed directly from the terminal rather than editing.


#### Run a script as a command job  `[17:56]`

**[17:56]** The PI file, so this can be included, right, so that we can better prepare a script, okay, which is more useful for later for model deployment.

**[18:11]** Here we see.

**[18:13]** Earlier, we have seen the AutoML job, right, where we are training multiple models. Now, we have another type of job in Azure Machine Learning, which is command job. Command job is the job where we are executing a single...

**[18:33]** Firefight.

**[18:35]** So when the requirement is to execute a single PI file, okay, it is executed as a command job. Okay, so we need to 1st configure this job and pass the PI file, right, to the command job and we submit the command job.

**[18:55]** Just like with AutoML job, right? We get the URL also where we can track the job status and...

**[19:05]** We can look at the output of executing the BI file. So that's the command job. To configure a command job, right? We use the Azure AIML library like we have used before for importing auto ML class and.

**[19:25]** Okay, so we use the Python, we use this Azure Machine Learning SDK.

**[19:32]** And we get the command.

**[19:36]** Class where we provide the code, like the location where file exists, right? We specify the environment. Azure Machine Learning comes with certain curated or inbuilt environments, right? So.

**[19:55]** inbuilt environments are available, right, that we may use. Even we have a flexibility to create our own environment, maybe by...

**[20:06]** passing a YAML file, a configuration file containing the packages with a base environment, and we can create our own custom environment also. So we need to provide the PI file, right, the environment information, the command line, like which file to be executed with those what parameters.

**[20:28]** Okay, so the compute that would be running that job, right? So once we are able to configure the command job, we simply go ahead and submit the job and we are able to execute the PI file. Okay, so maybe the PI file is.

**[20:45]** Uh, training a model or doing some data pre-processing, etcetera, right?

**[20:52]** So, that's the command job, and...

**[20:57]** Further.

**[20:59]** As we are discussing when we are creating a script, right?

**[21:06]** We can make use of our pass library, where when we are testing the PI file in the terminal, Python train.py, we may pass the parameters like training data, and maybe we have the new data, so instead of editing the PI file, maybe we can.

**[21:25]** Simply provide the information in the terminal. This data would be used for training the model. Or maybe we have a model parameter like regulation rate when we are training a logistic regression model. So maybe I want to try calculating the performance at a different regulation rate.

**[21:45]** So, instead of editing that PI file and executing it, I can simply pass a parameter here with different values, and we can cheque the model performance, right? So, these are certain ways how we can improve the code quality, right?

**[22:05]** Including our past library, creating a PI file, right, and then submitting the PI file as a command job. So let me take you to this exercise here, right, where we will be.

**[22:23]** Let me go to the...

**[22:27]** Foundry here.

**[22:29]** Okay, just give me a minute.

**[22:35]** So where we will be exploring how we can optimise model training, how we can submit a command job. So I have the workspace already created. Let me go to the

**[22:52]** Studio here.

**[22:56]** Right.

**[23:00]** All right, let me just...

**[23:31]** Alright, so over here.

**[23:42]** Let's see how we can run a script as a commercial.

**[23:46]** Okay, so we have a training script available. So if I go back, we have a PI file available in the source folder. Let's look at this PI file. We have train model parameter shot 5.

**[24:03]** OK, where we are using ML Flow or pass library, right? And...

**[24:10]** We have the code written into functions here, right? So there is one function to read the data, another function to, let's say, split the data, another to train the model, we are evaluating the model. We are custom logging using ML flow.

**[24:30]** Right, so that's the code we have.

**[24:34]** Alright, so we also note that this code contains you, it has that arg pass library as well, so if I go back.

**[24:44]** We may note that.

**[24:47]** Where we are using our pass library, we are defining A parser, adding the two arguments. So one is an optional argument, the revolution rate, but it is mandatory to pass the training data when we are running this PI file, right? So.

**[25:07]** If we don't pass regulation date, it defaults to.01 and it's mandatory to pass the training data. So when we provide this information, right, when we are running the script in the terminal.

**[25:22]** Right, that data would be used.

**[25:26]** We are getting a data frame using get data function here where we are reading the data, right? So it's using Pandas library to read the data into a data frame and then further analysis is done.

**[25:41]** Right, so that's the PI file we have, making use of ML Flow, our past library, and we would be executing this PI file as a command job. So, to do that, we need to 1st configure a command job now.

**[25:57]** These cells are already executed and we have this notebook which we are connecting to the workspace. Now we are initialising the command job. So where we are using Azure AI ML, okay, importing the command. So the code lies in the source folder.

**[26:19]** The command is Python train model parameters.py and we are passing the parameters here, right?

**[26:29]** Training data. OK, if we may further go ahead and if we want to explore, we can provide the regulation rate value, maybe 10. OK, some OK, this we can try and see what is the response of the model. So, the default regulation rate value is 0.01.

**[26:48]** Maybe you can explore what is the model performance when the regulation rate is 100. So it would be very different.

**[26:57]** So here we provide the command line. The input is the training data, which is...

**[27:05]** pointed by a data asset, a URI folder, right, pointing to this folder diabetes data. We further specify the curated environment here, which is the Azure ML.

**[27:20]** So it's an Azure ML environment, an inbuilt environment. We can cheque this environment available in the Microsoft artefact registry also. We can go to the site and see all the inbuilt environments provided by the Microsoft.

**[27:39]** So here we are specifying this environment, helping us running a PI file which contains scikit-learn package, providing compute information, the experiment name here, and we are simply going ahead and submitting the command job.

**[27:58]** So, when this is executed right, we get a URL here, and if I click on this, this job is already completed, and we note that we are able to train a model with the metrics logged as.

**[28:18]** accuracy and EUC value because we have logged only two metrics.

**[28:24]** With the custom login.

**[28:29]** Alright, then one image is logged and there is no model folder because we did not log the model folder.

**[28:39]** Okay.

**[28:41]** Right, so...

**[28:44]** So that's how we can create a PI file, right? And we can execute the PI file by submitting a command job.

**[28:53]** Right, so we can do auto linking also with ML flow, just making a change in the PI file instead of custom logging, we can do the auto logging and we can submit the job as well. This can be done.

**[29:09]** So that's how we can execute a PI file and we can train a model.

**[29:16]** Using Jupyter Notebook and in the workspace.

**[29:22]** Let's go ahead then and think before we go ahead.

**[29:34]** Okay, so if it's all good, let me...

**[29:40]** Further go, so this is the second lab, right? A short lab.

**[29:46]** which we have seen. Now we will, okay, okay, so let's take this knowledge check, okay, before we move to the next topic.

**[29:56]** So.

**[30:00]** You can provide your response in the chat.

**[30:09]** Answer to the first one.

**[30:29]** Okay, so when you first say it's C, definitely it's the correct answer is C here. It's not A or B. The reason because...

**[30:44]** We want to track model performance. Performance is the metric and we want to log the RMSE, root mean square error. So it is one of the metric.

**[30:56]** So to log a metric, we use log underscore metric.

**[31:02]** That's the correct answer.

**[31:06]** Let's have the second one.

**[31:39]** So if you're enabling auto logging, where we can find the model folder, because model folder is a folder which contains all the model assets. Is it not? In a model folder, we get the picker file, the requirement text file, we may get.

**[31:58]** then other files like YAML files, ML model files, the metadata file. So all those files are saved in the model folder. So where do we find the model folder? It is under output in the log section.

**[32:19]** Yeah.

**[32:24]** So, in the first lab, when we did the auto logging right, we can go to the tab output and the logs, and we should be able to find a model folder where we have logged all the model assets.

**[32:41]** Like pickle file.

**[32:46]** So if that's all good.

**[32:53]** Let's let me go back then.

**[32:56]** All right, so we have seen when we did the AutoML, maybe like using AutoML, we are able to see that the best model is the, let's say, is the logistics regression, which is the best fit, right, working well with our data.

**[33:16]** No.

**[33:18]** We can further optimise this model, right? Because maybe like if we have logistic regression with parameter, let's say the value of C, right? And maybe with the value of C, value C value as one, maybe the performance of the model is so.

**[33:37]** 80. OK, then with a different value of C, which is a hyper parameter value, right? Maybe like the C values 5, the model accuracy may be improved, OK? Or with a different value of C, maybe the performance would be different.

**[33:57]** Okay, so...


#### Hyperparameter tuning — sweep jobs  `[33:59]`

**[33:59]** It's not simply enough that we do AutoML and we are able to retrieve the best model. This model needs to be further optimised using hyperparameter tuning so that we are able to find the optimal hyperparameters with at that optimal hyperparameter.

**[34:19]** The model is performing at the maximum, so that's what is hyperparameter training, training a hyperparameter so that we are able to train our best model.

**[34:34]** OK, so the difference between halfway parameter training and auto ML is that in auto ML we have different algorithms that we want to try different algorithms and we are retrieving the best algorithm.

**[34:53]** But in case of hyper-penumbral tuning, we need to have our base base algorithm available; the base model should be there, so...

**[35:03]** There has to be a base model like, let's say, logistic regression. It could be the best model we have retrieved after doing the auto image. So maybe we have the logistic regression, which is our base model. Now, this model may have many hyper parameters.

**[35:23]** So, what hyper parameters are? These are the parameters. By changing those parameters, it directly affects the model performance, like...

**[35:34]** I could see a fun school.

**[35:37]** Like that, so in case of logistic regression, the more common hyperparameter values are strength of regression rate, which is the value of C, and the solver that we use to train our logistic regression model. If the base model is different.

**[35:58]** Maybe like if you're working with, let's say, random forest.

**[36:04]** random forest model, then the hyper parameters would be depth, number of the depth of the tree, number of trees in our random forest, etc. So the idea is we may have, depending on the model, depending on the base model,

**[36:25]** We may have a different hyper parameters, and with those hyper parameters I would want to know which is the best hyper parameter value, so that my model is outperforming. OK, it's giving it the maximum performance. Here is an example.

**[36:44]** where we are passing a list of C values.

**[36:50]** which could be 0.01, 0.1, 1 here. So for different value of C, the model performance would be different. So which is the best C value? Okay, either we go manually train multiple models or we may go with doing hyper parameter.

**[37:10]** tuning in Azure Machine Learning. So when we do hyperparameter tuning, we create another type of a job which is called as a sweep job.

**[37:22]** Okay, where we are passing a search space.

**[37:29]** where so that's the space which we want to explore and find the best value of C so that the model is giving the highest performance. So here we have provided 3 values. For each of the value, the model would be trained. So for three,

**[37:49]** C-values, we are able to train three models.

**[37:54]** Okay, and to identify which is the best model, again, we need to provide the criteria. So what is the criteria of best model? Either accuracy is the criteria or F1 score or precision or recall. So what is that criteria? We need to define that criteria based on the criteria.

**[38:13]** The best model would be retrieved.

**[38:18]** So, here we see with C value of 0.1, the model is doing well here, and this is the best model we get.

**[38:27]** So this is hyperparameter tuning, right? So that we are obtaining our best model, right, which can be further used for building, for registering the model and later deploying the model. So how to do hyperparameter tuning in?

**[38:47]** Azure, in Azure Machine Learning.

**[38:52]** As we discussed, we need to 1st have a base model available, because once we have that base model, we can configure a sweep job. So if it is a logistic regression, the search space would be different. If it is a random forest, it's a decision classifier, it would be having another search space.

**[39:13]** Right, so we have, we need to have a base model available. To get the base model, we need to 1st create a training script. So we need to create a PI file.

**[39:26]** Right, which where we are training a model?

**[39:31]** Right, and we submit, we execute this PI file as a command job.

**[39:37]** Now, on top of this common job, because we need that base model, that information is provided in this job.

**[39:45]** So, on top of that job, we are configuring the sweep job. So, if you are training logistic regression model, we get that base model. Now, we will configure the sweep job, where we will do hyperparameter twinning.

**[40:03]** Now, if let's say we are doing half a parameter tweeting with C value as let's say 0.1, 1 and 10. So we are training 3 models.

**[40:17]** So in a sweep job, there are many child jobs equivalent to the number of trials that we have. So if we have three trials here, we will get three child jobs in our sweep job. And

**[40:34]** The sweep job would be telling us which is the best model and we can retrieve the run ID or the job output of this best model and then we can further go ahead and register our model.

**[40:53]** Right.

**[40:55]** So, let's see further how we can configure a suit job.

**[41:00]** So once we have the base job or the command job available, on top of it we are building a sweep job.

**[41:11]** Now, in sweep job, we need to pass hyperparameter values, so that we define by defining a search space. So, how we define a search space by using a method called as a choice, and within the choice.

**[41:29]** We provide the list of values for which a list of hyper parameter values for which we want to train multiple models and retrieve the best model. Now, when we define the search space, it's important that we define the discrete hyper parameters.

**[41:49]** not the continuous hyper parameters. Discrete means that the hyper parameters have the discrete values, okay, not a continuous value. It will have certain intervals so that we can approximate what would be the value of C.

**[42:08]** Okay.

**[42:09]** for which the model is performing well. So maybe, right, we can have with a multiple of 10 and we can provide a list of search space rather than providing continuous hyperparameters where C can take the value like 0.1.

**[42:30]** 0.11, then 0.12 example. So if we have a lot many hyper parameters, values here, we end up with training a lot, a large number of models getting trained and which could be very expensive.

**[42:48]** Right, so we should be defining the discrete hyperparameters, right?

**[42:56]** Right, and then...

**[42:58]** Going further, we can configure the sweep job.

**[43:03]** OK, so the first step in conferring screw job is defining the search space using choice method.

**[43:12]** OK, in Azure AIML.

**[43:15]** Then we further define the sampling technique. OK, that because sometimes what happens if we have many hyper parameters, let's say we have the C value, which is let's say 444 values are there.

**[43:36]** Okay, and then we have solver. We have used solver also as a...

**[43:43]** Another hyper parameter, so two, three options, maybe if you have, maybe we provide three options here, right? So one could be linear, lib linear is there, lib linear. Then we have some Newtonian method.

**[44:03]** Further, so these are some popular solvers are available, so if we have...

**[44:09]** many hyper parameters with large possible values. So if we see here, even we have 4 here and three values in the solver. If we try all the possible combinations, we need to train.

**[44:23]** Isko side me Rabari.

**[44:25]** Twelve models.

**[44:31]** Right. So we would be training 12 models. And if, let's say we are building a random forest classifier, we may have four to five hyper parameters and we may end up with large combinations, right? And ending up with training large number of models.

**[44:52]** So this becomes expensive, right? So we may not try every possible combination. If we try every possible combination from our hyperparameter search space, this is called as a grid sampling. But if the combinations are too many, what we can do is we can go with random sampling.

**[45:13]** where we can simply provide that in five trials.

**[45:21]** Okay, so from the given combinations, it will be picking up the few ones, the five combinations randomly and training those five models. Okay, so which is a trade-off between the cost and the quality of hyperparameter tuning that we are doing.

**[45:40]** But we may, we cannot try large combinations, right, as it becomes too expensive, so we may go with random sampling.

**[45:51]** The random sampling, if we try right, we can make this results reproducible by adding a seed. OK, that is, if let's say we are doing random sampling and in my first run, in my first...

**[46:10]** run first C job that we have. I got the highest, the best model with the accuracy of let's say 90%. There it has tried a combination where C value is 10 and solver is lib linear.

**[46:29]** Okay, let's see. But next time if I do the run, okay, there is no guarantee that the same combination will be same random combinations would be picked up, right? And this makes our results getting not reproducible because it's a random sampling.

**[46:49]** In my next run, some other combination could be picked up, right? So, how we can make sure that the random sampling that we are doing is reproducible?

**[47:00]** This is done by adding a seed. OK, so for example, if we add a seed of value 42, OK, it has a fixed random pattern. OK, it will, whenever we may go ahead and execute a run, it will always pick up the same random combinations.

**[47:21]** As long as the seed value remains the same, if seed value is different, maybe in zero forty-two we may have 10 right, then it will have another fixed random pattern, so whenever I make a new run.

**[47:37]** Okay, every time I will get the same combination picked up and the results are also reproducible. So when we are doing random sampling, we always add a seed so that the results are reproducible.

**[47:54]** That's another technique, how we can configure sampling if we have a large number of combinations, right? Then another sampling is Bayesian sampling. OK, works on the Bayes theorem, wherein it's more intelligent.

**[48:12]** Way of doing the sampling where.

**[48:17]** The new combinations are picked up depending on the previous results. So for example, if let's say with C value, if we are increasing, that is leading to an increase in the model performance. Then the next value would be picked up.

**[48:36]** Would be again with the same trend with increasing the same value. OK, so.

**[48:42]** The Bayesian sampling allows us to converge right to a more optimal combination, rather than doing the random sampling, so...


#### Sampling & early-termination policies  `[48:54]`

**[48:54]** If you want to do intelligent sampling, we may go with Bayesian. Or generally with large combination, random sampling is preferred. That's a simple sampling technique. If you have less number of possible combinations, we may go with grid sampling and try all the combinations and train all the models.

**[49:16]** This can be done, so...

**[49:19]** That's how we can configure the sampling method now.

**[49:25]** We can further see how we can add early termination to our sweep job.

**[49:33]** Because when we are submitting a sweep job, we are training multiple models, right? And...

**[49:41]** It's better that we implement early termination policy when we are doing a seed job. Even if you remember, even when we did the auto ML.

**[49:53]** We enabled the early termination.

**[49:56]** The reason, because...

**[50:00]** When we have large models to be trained, we should be optimising our model training so that we are not wasting our resources. So in early termination, what we do is that when we are...

**[50:15]** Running a trial when we are training a model.

**[50:19]** So...

**[50:22]** So for example, if you are training a logistic regression model, by default, it has the iterations. The number of iterations for which the model would be trained is 100. The maximum iterations that it can have is 100. So this is the default.

**[50:42]** Parameter in in our model.

**[50:47]** Now, let's say, so one iteration means all the data is passed to that model. Model has learned that data. And then in the second iteration, we again pass the data to the model. Model try learning the pattern again, right? So.

**[51:06]** So, with iterations, the model training improves. So, for example, we have training from 1 to 100.

**[51:14]** And for every iteration, we are looking at the loss of our model or maybe the accuracy of the model. And we can see how my model is performing as the iterations are increasing.

**[51:29]** So with increase in iteration, the model is getting exposed again and again to the data and it's a learning that data. So in the first iteration, right, the loss could be higher. Loss or the error of my model. It would be high.

**[51:49]** But, as the iterations increase, OK, ideally the loss function should decrease.

**[51:58]** Like that.

**[52:01]** All right, so, but sometimes what happens is that after certain iterations, the model performance do not improve. OK, it may become it may become going up and down, giving a noisy pattern, or may even it can diverge. It may become unstable also, so this may also happen.

**[52:23]** So, with increasing the iteration, the loss function further increases. So, the idea of early termination is that when we are training a model.

**[52:38]** Right, we should stop training.

**[52:42]** then the model is not improving further. So stop or doing the early termination. Terminate the training if the model is not improving. So maybe like in this case, around at...

**[52:57]** Four or at the 5th iteration, we should be stopped training the model.

**[53:03]** Because after that, the model is not improving.

**[53:08]** Okay, so this will avoid wasting our resources, the time we are spending to further train the model, right? So that would be avoided. Okay, we save on our compute and instead of training this model, we can go ahead with training the next model.

**[53:26]** So that's early termination.

**[53:31]** Right, so terminating the training process, right? If the training is not helpful, that's early termination, and if you want to implement early termination in a sweep job.

**[53:41]** Anywhere.

**[53:46]** We need to implement an early termination policy.

**[53:53]** So...

**[53:54]** Or what's in the policy? OK, let's explore what all options are there, how we can set early termination policy. So there are...

**[54:06]** Who?

**[54:08]** parameters that we want to play with, right, to define a policy here. First is the delay evaluation. That is.

**[54:19]** It's the minimum iterations a trial has to go before we can implement early termination. Maybe if we can set it at 10. So it will go through 10 iterations at least, right, before early termination kicks in, right?

**[54:39]** So that's the delay evaluation. Then we specify evaluation interval, that is the step after which we should be evaluating the model performance. Okay, so maybe if we keep it as two, right? So since we are starting the early termination at...

**[54:57]** Tent, so...

**[55:01]** Azure Machine Learning will be, or this policy would be looking at the performance at iteration of 10, then it will look at iteration of 12, then at 14, etc. So it will see 10 and 12. Is the model performance improving or not? If it is improving.

**[55:21]** Go ahead with further model training.

**[55:25]** So it goes with the steps of two. That's the evaluation interval. So we need to 1st define when we need to start implementing this policy and at what iteration the policy has to be evaluated.

**[55:44]** And if let's say we are evaluating at 10, at 12, how we can make a decision that is it improving or not? Right. There are certain policies available. One is the bandit policy. Then we have median stopping, truncation selection policy. So these are the commonly used

**[56:05]** policies when we set the early termination.

**[56:11]** So, what these policies are? Let's look at that.

**[56:17]** Here we have the bandit policy.

**[56:20]** So bandit policy where we continue with our trial, right? We are logging the performance of the model, right? And we define a margin. Right now here we see the margin of 20%.

**[56:38]** Okay, that is so bandit policy says that we should be stop a trial. We should stop training a model if the performance is below a specific margin. So if it is falling below a specific margin, stop training the model, else continue with the model training. So here we see.

**[56:57]** For example, right now we have delay evaluation of five. So at least five iterations will continue. And here we see with five iterations, we are, our model performance is improving. Right now we see it's 90%, which is the best trial, which is the best performance so far.

**[57:19]** The slack amount is 20%, it means that 70% would be the threshold. And at 6th, we are checking whether its performance is improving or not. So it is below the...

**[57:35]** the best performance, but it is not falling below the margin, right? So we can continue with our model training.

**[57:45]** But if...

**[57:47]** The performance falls below the margin, margin of 20% here, that is 70. If the performance falls below that, we should stop training the model.

**[58:01]** So that's the bandit policy.

**[58:05]** Then other policies, median stopping.

**[58:11]** Vatan.

**[58:13]** We take the median of all the previous trials, we have that median or the middle, the median value. If the trial value...

**[58:24]** trial performance is above the median, we continue with the model training. If it falls below that median, we stop training the model further. So this is more flexible where it gives us opportunity to continue with the training even if.

**[58:42]** there is a small drop in the performance, right? So this is more robust as well, right? Since it's using the median to take a decision. Okay, that's the median stopping policy. We have truncation selection policy. This is more iterative in nature.

**[59:02]** Where?

**[59:04]** From the previous trials, right?

**[59:07]** we will be dropping the lowest performing, let's say, 20% of the trials.

**[59:14]** So, like, we have...

**[59:17]** One, two, three, 4, 4 trials we have. Maybe we drop 20% of four. So maybe we are dropping the lowest trials. Maybe we are dropping this trial. Okay. So as long as the current trial is not.

**[59:37]** Among the lowest performing percentage of the trials, we continue with the model training.

**[59:44]** And if we see over here, the current trial is one of the lowest performing 20, it's coming under one of the lowest performing 20% of the trial. So if it is, then we can further do not train the model. We stop model training and...

**[1:00:04]** We can move to the next model training.

**[1:00:08]** So these are certain policies, right, that we may use so that the experiment is not expensive and we are able to train multiple models with different hyperparameter values and we should be able to identify which is the...

**[1:00:28]** Best hyperparameter.

**[1:00:31]** For my algorithm.

**[1:00:34]** and for which the algorithm is doing its best. And we can then pick that model, right? And we can further go ahead and register the model.

**[1:00:47]** This can be done.

**[1:00:51]** So, that's...

**[1:00:53]** This truncation selection policy, right, and the early termination policies that we have seen, so...

**[1:01:02]** So far, right, we have gone through these concepts related to the hyperparameter tuning. And let's see how we can implement hyperparameter tuning in Azure Machine Learning.

**[1:01:18]** Before I show you the demonstrations, anything would you like to add here?

**[1:01:34]** All right.

**[1:01:42]** So if that's all good, maybe I'll go to the Azure portal here and we have another notebook where we are.

**[1:01:55]** Implementing hyperparameter 20.

**[1:02:02]** So first, to do hyperparameter training, we need to 1st have a training script. We need to submit a command job. And then on top of it, we will build a C job.

**[1:02:17]** So over here, we make sure Azure AML is installed. Connecting the notebook to the workspace, all good. Here we are creating a training script, a PI file we want to create. So we create a source folder. We create a PI file.

**[1:02:36]** Train.pi.

**[1:02:40]** Right, which uses ML Flow Arc past library, and we are training a model.

**[1:02:46]** So, which model we are training a linear logistic regression model that we are training?

**[1:02:55]** So that's a PI file and we are creating this PI file. Now to execute the PI file, we need to submit a command job. So we configure the command job here.

**[1:03:06]** Python train.py, passing the input, etc. and submitting the job. And we can see that the job has completed. It is completed.

**[1:03:22]** And here we see it's completed and we can cheque the metrics.

**[1:03:27]** Of model training.

**[1:03:31]** The regulation rate value is 0.01, that's the default regulation rate value.

**[1:03:39]** Further going ahead in the notebook.

**[1:03:44]** Here we are defining a source space now. So here we note that.

**[1:03:50]** We have the job which is submitted and completed. And using that same job, we are using the choice method here. And we are passing the list of the search space for the value of C for the regulation rate value.

**[1:04:10]** Right.

**[1:04:12]** Then we use C and configure a C job. Here we are using grid sampling. So we note that there are three values. So it would be training 3 models. We should be able to get the best C value for my model.

**[1:04:33]** Okay, which is the best one? Okay, so we should be able to identify as an outcome of a sweep job.

**[1:04:44]** Going further.

**[1:04:46]** We define the sweep job here. We are doing grid sampling, training all the models.

**[1:04:52]** We specify the primary metric, which is the accuracy, right? Because we need to define what is the metric, what is the criteria for the best model. So it's the accuracy selected. Goal is to maximise the accuracy.

**[1:05:09]** Going further, we can set the limits that we it can maximum train 4 models.

**[1:05:17]** This condition is redundant because...

**[1:05:22]** We have 3 total combinations and maximum it can train is 4. So maximum it can train only three models. Parallelly, we can train 2 models. We specify the timeout for our experiment. And we are submitting a sweet job. And if you look at the output of the sweet job,

**[1:05:45]** This view job is completed, and...

**[1:05:49]** We note that we can go to the trials, or maybe...

**[1:05:55]** Here we may see that. We can also see the best trial here.

**[1:06:01]** So we are able to get the child job here of my best ride.

**[1:06:08]** So if I click on this...

**[1:06:16]** We see that the regulation rate of 0.01, this is the best C value.

**[1:06:25]** Okay, so the parameter is 0.01.

**[1:06:30]** and we are getting the accuracy of 774.


#### Compare trials & pick the best model  `[1:06:35]`

**[1:06:35]** Maybe I'll go back to our main sweep job here, where we can compare all the models that are trained. So under the trials, we can scroll down and we can see.

**[1:06:51]** We have, we are.

**[1:06:54]** able to train 3 models here.

**[1:06:57]** with a different regulation rate value.

**[1:07:02]** regular rate of 0.01, 0.1 and 1.

**[1:07:08]** And it's very clear that regulation rate of 1 has the lowest accuracy.

**[1:07:15]** It is the lowest. So this cannot be a best drive. So it could be either 0.01 or 0.1 because it's a tie here. We are able to get the same performance, same accuracy.

**[1:07:32]** Right, so...

**[1:07:34]** It picks up any one of it randomly because the criteria is the training accuracy and we have a tie here. It could be either of the...

**[1:07:45]** regulation rate value and it has picked up 0.01 as the best drive.

**[1:07:55]** So this is our best try. So ML flow 0. OK. That's the display name.

**[1:08:07]** Even we can, uh, let me go back to the experiment.

**[1:08:11]** So, in the experiment, where we can see all the three.

**[1:08:18]** child jobs here. We can see ML flow 0 is the best one. So we can confirm it over here also.

**[1:08:28]** Right.

**[1:08:31]** So, maybe if I, if we again go back to the main sweep job here, go to the trials, and here we can see we are able to get a plot between accuracy and the...

**[1:08:44]** The the trial name here, so...

**[1:08:48]** The ML Flow 2 has the lowest accuracy.

**[1:08:53]** We have a tie here between ML Flow Zero and ML Flow One.

**[1:08:59]** These 2 trials.

**[1:09:01]** We may cheque the other metrics also how other metrics are we can go to AUC.

**[1:09:09]** And we can see ML Flow One has the higher AOC value; it has the highest AOC as compared to ML Flow Zero and ML Flow Two.

**[1:09:20]** Right, so ML Flow One has.

**[1:09:25]** Highest.

**[1:09:28]** Accuracy, which is which is a trial with another trial. OK, it also has the highest EOC value. OK, but since the criteria is the accuracy only, OK, it it has picked up ML Flow Zero as the best trial.

**[1:09:47]** So this is our best trial. So the most optimum value is C value equals 0.01. And we can go to the best trial also, right? And we can register that trial. OK, this we can do model registration.

**[1:10:07]** this can be done. So what's model registration? We'll see that in the coming slides. Okay. It's simply we are logging the model folder.

**[1:10:20]** That's registering a model.

**[1:10:27]** All right.

**[1:10:28]** We can see other charts also like parallel coordinates chart where we can visualise the line between the regression rate and what is the accuracy of the model or the AUC value. We can cheque the scatter plot of what experiments we have done.

**[1:10:46]** OK, we can look at that scatter plot as well. So, this is the outcome of the hyperparameter tuning. We can cheque the trial, OK, see which is the best trial. So, if we go back, maybe we can note that.

**[1:11:04]** ML Flow Zero.

**[1:11:06]** Is the best trial? We can go to this child job.

**[1:11:10]** Okay, if you want to register, we can register the model here. Okay, this can be done. However, right now it's not possible. The reason because we have used the ML flow to do the tracking, but...

**[1:11:25]** Oh.

**[1:11:26]** We are not logging.

**[1:11:29]** the model folder. That's the reason. Because when we are registering a model, we are basically saving that model folder. So since we are not logging that folder, even specifying the job output, we will not be able to log or register this model.

**[1:11:47]** Okay, we'll see how we can register a model. Okay, incoming labs, we will be looking at that.

**[1:11:58]** So, that's done, right?

**[1:12:03]** OK, so this is a hyper parameter 20.

**[1:12:08]** Yeah.

**[1:12:12]** If that's all good.

**[1:12:20]** Any queries regarding this? Take note.

**[1:12:30]** Yep, Pauroosh, I have a query. Why we executed the command job first, and then we went to sweep job.

**[1:12:33]** Yeah.

**[1:12:39]** Correct, yeah, that's a great question. So we need to we need to 1st have the base model because the sweep job would be would be doing hyperparameter training, right? If it knows that, which is the base model.

**[1:12:57]** Right, it need to have that algorithm available.

**[1:13:02]** Right, and how do we provide that algorithm information?

**[1:13:07]** By providing that information from the command job, so in command job, we are training the model, we are training logistic regression model on top of the command job, we are building a sweep job, where the sweep job has the job, the command job information that.

**[1:13:25]** logistic regression is the model. And then in Sweep job, we are adding choice method, we configure it, and then we submit it. Nowhere in the Sweep job we mention that it's a logistic regression for which we want to do hyperparameter training. That information it extracts from the command job.

**[1:13:45]** So, save job is built on top of a command job.

**[1:13:50]** Okay, got it.

**[1:13:52]** Great, great. That's nice.

**[1:14:05]** So, let's continue further, OK?

**[1:14:11]** Yes.

**[1:14:14]** So, so far, we have, we are able to, let's say, do auto ML. We are able to get the best algorithm out of many algorithms. Then with that best algorithm, we can do hyperparameter tweeting, and we are able to get the best model.

**[1:14:33]** Which, which is?

**[1:14:36]** Giving highest performance format data for the given hyper parameters. Right now, we have a bit more matured machine learning that we know what model to use. We also know that...

**[1:14:53]** how we should be cleaning the data, right? What is the data pre-processing that we are doing, right? So from the early initial experimentation, right, we know, let's say we are using some technique for maybe like...

**[1:15:13]** If our data has a null value, we are imputing those null values with the mean value. Okay, this is the cleaning technique we have finalized, right? Then model selection we have done, which algorithm is good for my data. Okay, and we are able to train our best model.


#### Pipelines & components  `[1:15:32]`

**[1:15:32]** Okay, so we know the steps, right, to train our model.

**[1:15:40]** OK, now we may want to make this automated.

**[1:15:46]** the development, we want to make it automated. The reason because, let's say, a new data comes in and we want to do retraining, we want to retrain the model. So we know these steps, right? What steps, what development steps we need to go through and we should be able to get the best model.

**[1:16:08]** trained. So every time if we get a new model we need not to be

**[1:16:14]** Exploring the.

**[1:16:16]** techniques, model selection, auto ML need not to be done again and again, right? Hyperparameter tuning need not to be done again, right? Once we know what is the nature of the data and right, if some new data comes in, we simply want to automate this process and...

**[1:16:36]** We can bring automation and building a machine learning workflow is by building a pipeline. So pipeline allow us to automate the...

**[1:16:48]** the machine learning workflow. Okay, so that's the reason why we build pipelines and let's see how we can build a pipeline in Azure Machine Learning workspace.

**[1:17:01]** So pipeline, it's basically sequential steps we want to perform in an automated way.

**[1:17:11]** Right, so maybe like we want to train a model periodically after every week. Okay, so since we know the steps, the steps can be put all together.

**[1:17:23]** Right, and we can build the pipeline.

**[1:17:27]** So when we are building the pipeline, the pipeline building block is a component. So component is 1 task of our pipeline.

**[1:17:38]** For example, we have component one, which is treating the null values.

**[1:17:46]** There is second component, which is normalising the data using, let's say, min-max scalar. We have component 3, which is training the model. Fourth component is evaluating the model. Okay, so these components would be put in a sequence, right?

**[1:18:04]** and we can build a pipeline and then we can trigger a pipeline. We can even schedule.

**[1:18:11]** a pipeline. When should that pipeline be automatically running? OK, this can be done. So first, let's talk about a component, how we can create a component and then using the component, how we can build a pipeline.

**[1:18:30]** So...

**[1:18:31]** Components are like, it's a individual unit, right, which has a specific task which it can do. And most important is these components are shareable.

**[1:18:51]** Okay, that is, for example, if we have a component that we have created, which is treating null values, removing the null values with the mean of that column. So that's a component that we have created. This component is shareable, shareable across different machine learning projects.

**[1:19:10]** So we need not to write a logic again if the task is to be done, the same task is to be done in a different project. So the components are shareable across the workspace, right? And we can reuse it, right?

**[1:19:29]** for many projects that can be done. So that's a component. So let's see how we can create a component. OK.

**[1:19:40]** To create a component.

**[1:19:44]** We need these two files and using these two files we can.

**[1:19:50]** get the three parts of the component. Like the first part of the component is the metadata information where a component has its name, it has its version, it has its description, for example.

**[1:20:04]** every component has an interface. So maybe like this is a component treating null values with the mean value. All right, and this component has an input. It also has an output. So input would be a CSV file.

**[1:20:25]** So it will not be the input as a CSC, but CSC pointed by a data asset.

**[1:20:31]** It could be a URI file, URI folder, or it could be a mail table which is pointing to a data. So input would be a data asset. Output would also be a data asset which contains the processed file.

**[1:20:52]** Right, so if you are treating the null values, input is a raw file and the output is a processed file. So every component has an input and the output. It could be like input is a data asset, okay, where we pass the clean data.

**[1:21:12]** To the component, the component is training the model.

**[1:21:17]** And the output is a model folder.

**[1:21:21]** which is again pointed by a data asset.

**[1:21:25]** So input could be the data, output would be a model folder which contains all the data assets, the machine learning asset like pickle file, requirement text file, etc. So that's the interface.

**[1:21:43]** Every component has its functionality. So if it is like training the model, it is linked with a PI file, right, which is actually training the model. Okay, so it will be having code, the environment to run that code, the command line.

**[1:22:02]** Right, so these define the functionality of the component.

**[1:22:07]** Great, so these are the three parts of a component and these are defined in these two files. The first file is our script, the PI file, which define the functionality. We have that PI file.

**[1:22:24]** Then we have a configuration file, the YAML file, where we have the metadata information of our component, its interface information, what is the input data set, what is the output data set, other things. And using this YAML, we can create a component.

**[1:22:49]** So once we are able to create a component, we can easily go ahead and build a pipeline. So right now we see there are two components here. Component one, which is preparing the data. Input is our data asset. It has certain logic, right, where it is doing the data cleaning.

**[1:23:09]** Preparing the data, the output of component one is the input of component 2.

**[1:23:16]** In component 2, we are training the model, and the output of component 2 is...

**[1:23:24]** the model folder which is pointed by a data asset.

**[1:23:33]** All right, so so it's simply we can connect these components using a pipeline function.

**[1:23:41]** Right, so we can configure a pipeline job using pipeline function. We can then submit a pipeline job. So this is another type of a job in Azure Machine Learning. We have command job, sweep job, and we have a pipeline job here.

**[1:23:57]** We can even schedule a pipeline job when we can trigger this pipeline, on what days, at what time we should be triggering this pipeline. This all can be managed right using job schedule class, and we can schedule.

**[1:24:17]** Pipeline job.

**[1:24:23]** So with this information, we can go ahead with our next lab where we'll see how to build a pipeline and we will observe how we can cheque the results of the pipeline job. Let's look at that.

**[1:24:43]** If no questions, and we can proceed then.

**[1:24:54]** All right, so here.

**[1:24:57]** Let me go to Azure Portal.


#### Run a pipeline job  `[1:25:03]`

**[1:25:03]** I can go to a notebook here where run a pipeline job. So there is a notebook available and we'll execute this.

**[1:25:18]** So here we will first create 2 components.

**[1:25:25]** So to create the components, first we need to create a pipe file and YAML file of each of the component. Then we will use pipeline function, build a pipeline, and then submit a pipeline job. So let's go ahead.

**[1:25:40]** So here we are first making sure Azure AML is installed, going further, connecting this notebook to the workspace.

**[1:25:52]** We get the client handle here, then we are preparing the data, so we create a source folder, create the spy file, wrapdata.py, where we are using two functions, clean data and normalised data. So, in clean data, we are using drop method.

**[1:26:11]** And we are creating the null values, so remove the row if the row contains the missing value, right? So, that's the drop any method using min-max scalar, we are doing data normalisation for these columns.

**[1:26:32]** We may note that.

**[1:26:34]** Patient ID is one of the columns, and it is not included for doing normalization.

**[1:26:42]** So now in min max scale, if let's say we have this column pregnancies, it has it in the data, it may have the range between 0 to 14. When we do normalization, the column values are converted into zero to 1. So basically we are scaling the data right.

**[1:27:02]** using a min-max scaler.

**[1:27:05]** That's what how we are doing normalisation and we are creating this spy file.

**[1:27:11]** Another PI file is created where we are training a model. So we are training a...

**[1:27:18]** logistic regression model here.

**[1:27:22]** And here we can see.

**[1:27:25]** VR.

**[1:27:27]** Saving the model folder using save model.

**[1:27:33]** And then evaluating the train model as well that we are doing. So that's a that's a PI file where we are training the model, logging the model folder.

**[1:27:46]** Right, because later on we want to save it, which is pointing, which is pointed by a data asset.

**[1:27:55]** All right.

**[1:27:57]** So going further, so we have two PI files available. Now we will create the YAML file. So prep data.yaml, which contains the metadata information of the component name, display name, the version of it. Then here we note inputs.

**[1:28:17]** Input is a URI file, output is a URI folder.

**[1:28:24]** And it is executing the spy file.

**[1:28:28]** Webdata.y.

**[1:28:31]** We go ahead and create another YAML file for our second component.

**[1:28:36]** Input is a URI folder, so it's nothing but the output of the first component is the input of our second component.

**[1:28:45]** Output of this component is ML flow model.

**[1:28:50]** and we are executing this file file.

**[1:28:54]** So we have BI files available. We have the YAML file. We can use the YAML file and we can create a component. So this is component one created, component 2 created.

**[1:29:09]** Now we need to simply connect them in a sequence.

**[1:29:13]** Using the pipeline function here.

**[1:29:17]** Where?

**[1:29:18]** We are providing a URL file, which is our data. We are calling this function, so that's the input to this function, which is diabetes.csv file, which is nothing but the input data of our component one.

**[1:29:36]** So, component one has an input, which is a URI file pointing to diabetes.csv, and we get the output clean data. The output of first component is an input to the second component, so the second component.

**[1:29:56]** Input is training data and the output of the first component is the input to the 2nd component. And we get the output of the 2nd component. And what this function is returning, it's returning output of first component and output of the 2nd component.

**[1:30:14]** So that these are the two objects it is returning.

**[1:30:23]** Then further, before we submit the pipeline job, we can simply print it.

**[1:30:31]** So that we can see everything is in order, right? Then we can further update the pipeline job, like specifying the compute output of.

**[1:30:44]** The pipeline would be stored in a BLOB storage, right? And we can go ahead and submit the pipeline job. Once you submit the pipeline job, we get a URL to track the job, and...

**[1:31:06]** Here is the pipeline job completed.

**[1:31:12]** where we have component one and then component 2.

**[1:31:16]** We may cheque the output of each of the components; this can be done, and let me go to...

**[1:31:25]** First component here, if I expand it.

**[1:31:30]** So first component does the data cleaning. So we can note the output is pointed by our data asset. And if we come to this data set, we can cheque the output data.

**[1:31:43]** So here we can go to browse and we can look at the output data.

**[1:31:50]** Which is this is the output diabetes dot CSV. And if we look here, we are able to normalise the data.

**[1:32:00]** So, all the values are in the range between zero to one.

**[1:32:07]** So, we are able to do normalization.

**[1:32:10]** We also note that patient ID column is not normalised because this column is not included in the.

**[1:32:19]** when we applied min-max scalar.

**[1:32:27]** Right. So this is the output of component one. We are able to verify it. Let me go back.

**[1:32:46]** Let me go back to the pipeline job. Okay.

**[1:32:58]** I let me just go from here also, OK?

**[1:33:04]** Okay, yeah, over here.

**[1:33:07]** So let's look at the output of second component. So if we double click on it and we can go to.

**[1:33:15]** The output.

**[1:33:17]** model output here and...

**[1:33:23]** We can go to the artefacts and see we are able to log model output here.

**[1:33:31]** Which is nothing but the model folder that we are, we are able to log containing the pickle files, other files, right?

**[1:33:41]** So, so since now we have this model folder available, we can use it and we can register a model. This can be done. OK, so if I go to the job section here.

**[1:33:57]** Let me go to the pipeline job here.

**[1:34:02]** That's the one pipeline diabetes. It has two child jobs because each component is 1 child job. Okay, so we have...

**[1:34:16]** Maybe I'll go ahead. OK, sorry, this one is failed. OK, so I'll go with this pipeline job and we have train model. That's the component, and if I click on this.

**[1:34:34]** So this is a job which has an output model folder. I can go and click on register model.

**[1:34:42]** Right, it's able to detect that it's a ML flow model that is logged. It has the job output here and we can go to next. Maybe I can just provide a name of the registered model. Let me just say here.

**[1:35:04]** Registered model.

**[1:35:07]** OK.

**[1:35:08]** We may provide version number, etc. and just going next and we can register.

**[1:35:16]** So once we are registering the model, because that's the step, once we have the best model available, right, we before we deploy, we need to 1st register this model. OK, what we are doing in registration in model registering, basically we are able to save that model folder. So if I go to model section here.

**[1:35:42]** So if you go to models, we can see the list of models that we have registered. Right now, this is the model that we have registered. And if we click on this, we can go to artefacts and we see it simply we are logging this model folder. That's the model registration we are doing.

**[1:36:02]** It will have a version, et cetera, right?

**[1:36:07]** And maybe I can just select my registered model and then I can go ahead and deploy it also as a real-time endpoint or the batch endpoint. Okay, that I can do.

**[1:36:22]** So we'll look at the deployment part later on. We have seen what is register a model.

**[1:36:34]** Alright, so with this, we are able to.

**[1:36:39]** Build A pipeline, execute the pipeline. We have seen the output, how we how we observe the output of a pipeline, right?

**[1:36:59]** All right.

**[1:37:03]** If that's all good.

**[1:37:07]** Let me go ahead.


### Module 2 — ML Ops: CI/CD with GitHub Actions  `[1:37:11]`


#### Why integrate GitHub with Azure ML  `[1:37:11]`

**[1:37:11]** So, we are able to run a pipeline Azure Machine Learning right, and now we'll discuss about the ML Ops, how we can operationalize a machine learning solution, planning and preparing for.

**[1:37:31]** an MLOps solution. Further going ahead, we will talk about the machine learning deployment.

**[1:37:40]** Okay, how we can deploy models? So we have two options, either online endpoint and the batch endpoints. So we'll see how we can use Azure AIML, the classes available to do model deployment. Okay, that will be.

**[1:37:59]** Going ahead and seeing that.

**[1:38:04]** All right.

**[1:38:11]** Let's continue, so...

**[1:38:15]** To plan an MLOps solution, right, operationalizing the machine learning solution, here is the MLOps architecture where...

**[1:38:26]** We can build end-to-end machine learning solution, deploying the model, and then monitoring the deployment also, so...

**[1:38:35]** The first step is doing the setup, right?

**[1:38:40]** provisioning the Azure resources, creating Azure machine learning resource, creating other resources, data assets, etc. Right? That's the first step, right? So first we will go ahead with the experimentation phase where in the first step we are doing setup.

**[1:39:02]** Then we are.

**[1:39:04]** Experimenting right and training multiple models, retrieving the best model, doing hyperparameter training, etc., and the output is the best model. Now, the best model that we have need to be packaged, so this...

**[1:39:23]** Third step is packaging and registering the model where we are.

**[1:39:28]** Able to log the model folder, OK, using ML Flow, so that packaging we are able to do, and later on, if let's say we need to retrain the model or if some new data comes in or if there is a drift in the data, so...

**[1:39:47]** It could be a different condition, and we may want to go back right and again train the model and then package the model right. This can be done right by automating using pipeline job, or if let's say we are working.

**[1:40:06]** on a project, right? Multiple members are working on a project. We may have integration with GitHub as well, GitHub actions, so that we can trigger an action and the pipeline can be triggered, okay?

**[1:40:26]** So we'll see the integration of GitHub with Azure Machine Learning in coming slides. So this will incorporate continuous integration that.

**[1:40:39]** Continuously, we can.

**[1:40:42]** We can.

**[1:40:44]** or train a model, right? We can get the data, do the model training, package the model. So that is our continuous integration, right? This can be done. Okay. Then once we are able to package the model, right, we go ahead with the model deployment where we are deploying the model.

**[1:41:05]** to an endpoint.

**[1:41:07]** So the model is deployed to a URL, right? And once the model is deployed, it would be consumed via the client application. So the client application submits the STPD request to the endpoint. The model makes a prediction, it provides the response back to the.

**[1:41:28]** Client application, right?

**[1:41:31]** No.

**[1:41:33]** So this is basically integrating the model.

**[1:41:37]** Into the application, and we also need to do monitoring, monitor our deployment, that is looking for the production data, what model is getting a request, how it is generating a response, what are the performance metrics of the deployed model.

**[1:41:58]** Do we need to retrain the model, right? So let's say we want to schedule the retraining so we can go from six to one, right?

**[1:42:09]** Like, where we identified a drift, or maybe it's a periodic automation that we want to do, wherein we want to train the model, package the model, maybe on a new data, or with a better performance, right? And then doing the CI part.

**[1:42:29]** continuous integration and continuous deployment.

**[1:42:35]** OK.

**[1:42:37]** Right. This this we may want to do.

**[1:42:42]** So, that's an overall MLOps architecture.

**[1:42:48]** Right.

**[1:42:51]** Going ahead, then.

**[1:42:54]** So we'll see how to do CI/CD using GitHub actions that also we will see, right? For example, let's say we are able to package the model here. And as we are building or making some improvements in the model, maybe we are changing the value of C from one to.

**[1:43:15]** say 5, maybe this is resulting in a better performance of the model. So we can make a change, right? And this would be triggering A workflow and we can rebuild our model, right? So that's a CI can be done. Further, we can extend it to CD.

**[1:43:35]** Right, once we are able to package it, we can do the redeployment. OK, this can be done, so we'll see how to use GitHub for, yeah, how to automate the model training, how to do CI part, the continuous integration.

**[1:43:55]** Using GitHub Actions.

**[1:43:59]** Let's explore this.

**[1:44:02]** So, over here.

**[1:44:05]** No.

**[1:44:07]** Integration with GitHub is important, or integrating Git with our code files, right? Adding with the Git is important for version control or for the source control, because we may want to update the code and keep track of our code files.

**[1:44:27]** The prompts also, if you're working on a generative AI model, the configuration files like YAML files, etc., right? Maybe we are making certain changes. We need to track the changes. So Git allows us to do the version control. So for example, if we have a file, rain.py.

**[1:44:48]** where we are training the model. We may have a version one. And then, so that's the code file we have. Later on, we make some edits that would be the version two. Another edits, we may have the third version. Later on, if we want to go back to a more stable version, maybe.

**[1:45:06]** To the version three, we can do rollback. OK, so the rollback strategy should should be available so that we can do the time travel and we can go back to the previous version and.

**[1:45:21]** Use this version for deployment. Okay, this we should be able to do using Git packing right now. Git is not sufficient. We may also need to go to GitHub because there would be people collaborating on a project.

**[1:45:41]** Right, so the files would be shared over a GitHub repository, and different teams can work on a project with a different branch, and later on we can merge the branches also. So, for example, let's say we have a code file.

**[1:46:00]** Right, in our main branch, right, which is...

**[1:46:06]** our production branch which carries the production code. This can be used by a new branch with a team member. Maybe we are editing a PI file.

**[1:46:20]** Right and right, so.

**[1:46:25]** We are trying to do some improvements in a new branch here. It could be a feature branch where we are trying to improve some features and trying to optimise the model training. OK, now.

**[1:46:42]** If you are making certain edits, right, and later on we want to merge it to the main branch, right? This can be done, right, by creating a PR, the pull request.

**[1:46:57]** OK, now.

**[1:46:59]** If the, if let's say the admin or the lead scientist, maybe like if they approve the pull request, then only the edited PI files would be merged with the main branch. Also, we can create certain jobs, okay?


#### GitHub Actions & pull requests  `[1:47:18]`

**[1:47:18]** Like when we are creating a new pull request, we can make use of GitHub actions.

**[1:47:27]** GitHub Actions.

**[1:47:31]** to automate certain workflow, to trigger a workflow.

**[1:47:35]** So for example, if you are making some edits in a PI file, right, and creating a PR, then when we are creating a PR, okay, what edits we have done, maybe it will be using this PI file and it is testing the code, right?

**[1:47:54]** Oral.

**[1:47:56]** Right, it's working on the code logging, let's say the performance metrics, evaluating the train model, those.

**[1:48:06]** Those workflow can be triggered using GitHub Action, right? So GitHub Action is simply it provides us with a YAML file, a configuration file with a certain logic, certain automated pipeline that can be triggered using GitHub Action.

**[1:48:25]** So the workflow can be triggered if we are creating, let's say, a pull request. So when we create a pull request, a workflow is triggered and maybe some other files would be running, evaluating our PI file, maybe linting the script or doing testing on this PI file.

**[1:48:45]** is done. If it's done correctly, the approval team looks at the output of this evaluation profile. If it finds everything's okay, then...

**[1:48:59]** We can merge the feature branch to the main branch and we can update the code of the main branch.

**[1:49:05]** Right, this can be done. So we can bring automation, right? If we are making some changes, right? Those changes would be triggering certain workflows and...

**[1:49:17]** If so, we can automate certain tasks that if we are creating a pull request, it will be executing certain task, right? And then if things are okay, we can merge it to the main branch. So using GitHub actions, we are.

**[1:49:34]** Getting automation. OK, some part of right of.

**[1:49:40]** This collaboration, right? We can we can automate so that things are streamlined and we can update the main branch with the correct code, right?

**[1:49:52]** This can be done. OK, so, so that's how we can integrate GitHub with Azure Machine Learning, and we'll see as well how we can integrate GitHub.

**[1:50:07]** With Azure Machine Learning, right, that we would be doing.

**[1:50:12]** But I hope we got the concept like why we should be integrating GitHub with machine learning. Maybe for tracking the version control, right? Any edits we are doing then before we merge to the main branch, maybe we can bring some certain automation, do an automated task and...

**[1:50:32]** Then we can merge a feature branch to the main branch. This can be done.

**[1:50:42]** So that that's a task we would be doing in our 4th lab. OK, and here we note.

**[1:50:49]** So when we are building, when we are developing a machine learning workflow, it should be a run based like because we should not be touching the main branch. Anything that we want to explore would be done in a different branch, in a feature branch.

**[1:51:08]** So, the main branch.

**[1:51:11]** Contains the production code, right?

**[1:51:16]** Any changes we want to do, it will be done in the feature branch. We are making some edits.

**[1:51:24]** Right, and to merge it with the main branch, right, we create a PR.

**[1:51:31]** Right, when we create a PR, it would automate.

**[1:51:37]** Certain tasks that is the edits that we have done. We may want to validate those edits, right? So that can be automated by using the GitHub action and it will trigger a validation workflow.

**[1:51:54]** This validation workflow will provide us with a result.

**[1:51:58]** OK, the approval team will observe the result and it takes a decision whether to merge with the main branch or not. And if it is merged, then we are updating the main branch with a better code, right? This can be done. OK.

**[1:52:15]** So we may have for different variants. Let's say there is one branch working on the feature. There could be another branch, right, working on a different algorithm. Maybe instead of logistic regression, we have a random forest classifier, right? So that would be the other branch.

**[1:52:35]** the other team working on that branch and it may be merged with the main branch, right? This can be done. So these are certain ways how we can optimise working with a machine learning project, collaborating with teams, right? That can be done.

**[1:52:56]** Here is one simple example where we are doing continuous integration. And it's done with a manual trigger.


#### Define a workflow (YAML) & trigger a job  `[1:53:09]`

**[1:53:09]** That is, here we are defining a YAML file, so the GitHub actions allow us to do to bring certain automation, right? So we can create a YAML file, right?

**[1:53:26]** And this YAML file will be triggered on certain condition. Right now we see this is a YAML file which gets triggered on workflow dispatch. That is for a manual trigger.

**[1:53:43]** Okay, so when the user manually triggered this workflow, right, this YAML file will be triggered. It will have the jobs.

**[1:53:51]** The job will have the steps, it will be executing these steps in a sequence, and it would be completing a task. So, for example, let's say we are we have made, let's say, a change in our in our PI file, right?

**[1:54:10]** And we want to do model retraining. OK, so to do retraining we can go to GitHub actions. We can trigger this workflow, right? So right now it is a manual trigger.

**[1:54:28]** We can add some other trigger that if we are making a pull request, if it is a pull request, then this workflow would be triggered. There's a pull request to the main branch, execute this workflow. If you are making a push request, right, to this GitHub repo.

**[1:54:47]** Then again, this YAML file would be triggered, right? So those are.

**[1:54:53]** Different ways how we can.

**[1:54:57]** We can automate this trigger, right? So right now it's a manual trigger. So we have, let's say, made edits in our PI file.

**[1:55:06]** We manually trigger this workflow.

**[1:55:09]** and it has a job where we are training a model.

**[1:55:14]** It uses a runner, the Ubuntu latest, so it uses the GitHub.

**[1:55:22]** hosted runner, GitHub hosted machine, which is 1-2 machine, and these are the steps it would be performing. So the first step would be logging to the Azure using the Azure credentials. These are saved in the Azure, in the GitHub secrets.

**[1:55:42]** And we can.

**[1:55:45]** access those secrets and we are able to log into Azure. So that's the first step done. Once this step is completed, then we are running this job.

**[1:55:57]** So, we are creating a job, and in this job we are executing the PI file, and we are training the model.

**[1:56:06]** OK, so right now this job is created using the YAML file which contains the command line to.

**[1:56:15]** Execute the Wi-Fi.

**[1:56:20]** Right, so simply giving, simply triggering this workflow, we are able to submit a job and we are able to train a model.

**[1:56:31]** Right.

**[1:56:34]** This we can do. Okay, so we'll see the exercise wherein we would be able to manually trigger the workflow. We'll go ahead and add, let's say, pull request. And if there is a new branch, we want to merge it to the main branch.

**[1:56:54]** Right, we create a PR and that will trigger a workflow, and then...

**[1:57:01]** Then we can merge it to the main branch.

**[1:57:05]** This can be done. OK, so we will talk about this, right?

**[1:57:13]** after a short break. And then we'll move to the next agenda, which is deployment of a model to a batch and the online endpoint.

**[1:57:26]** Any queries before we take a break?

**[1:57:29]** Anything would you like to add here?

**[1:57:56]** Alright, so if it's all good, let's take a short break here and...

**[1:58:10]** Alright, have a nice break. I see you then.

**[1:58:14]** Yeah.

**[2:13:47]** Oh.

**[2:13:48]** Welcome back, everyone.

**[2:13:54]** Yeah.

**[2:13:56]** I hope you can hear me, and yeah.

**[2:14:02]** Mm.

**[2:14:06]** Great.

**[2:14:08]** Great, thank you.

**[2:14:12]** Thank you for your reactions.

**[2:14:16]** So, let's get going. OK, let me share my screen.

**[2:14:32]** So.


#### GitHub Actions — repo setup & workflow (after break)  `[2:14:36]`

**[2:14:36]** We were discussing how we can integrate, we can do GitHub integration with Azure Machine Learning workspace.

**[2:14:47]** So let's see the lab 4, right? If I go back here.

**[2:15:04]** Let me go ahead and log in.

**[2:15:48]** All right.

**[2:15:53]** So now we are looking at true.

**[2:15:58]** The next lab, which is lab number 5, where we can automate model training with GitHub actions. Okay, so let me take you to the lab instructions.

**[2:16:28]** Just give me a minute.

**[2:16:31]** Gurpreet.

**[2:16:33]** Okay.

**[2:16:43]** So we'll understand how we can use GitHub actions for automated model training. We can do CI and later on this concept can be extended to do continuous deployment also. So

**[2:16:58]** We need to log into GitHub for that. Let me go to GitHub. I'm able to log in and I'm able to clone this Git repository, right, which we have seen before, right?

**[2:17:18]** The.

**[2:17:20]** Which contains all the instructions of the ML Ops right, so we can go to the docs here, we can see all the lab instructions available right, and right now.

**[2:17:36]** We see we are in the main branch, right? We have all the codes available in this repository. If I go to the source folder, there we have a job.yaml. Okay, now even before we look at...

**[2:17:54]** This YAML file, what it contains, etc. Right? Let me first tell you how we can use Azure, the Azure Machine Learning, how it is integrated with GitHub, how the GitHub can use the credentials of.

**[2:18:14]** Azure Machine Learning workspace and then it can do a task. So let's say we have a data asset in Azure Machine Learning. How the GitHub can connect to the data asset. So basically we want to connect the Azure Machine Learning workspace to GitHub. To do that we need to.

**[2:18:34]** Go to the settings here. We need to 1st create a service principle.

**[2:18:43]** An Azure service principle with the access with the contributor access.

**[2:18:53]** To our machine learning workspace, so we can do that if I, if we go to the instruction here.

**[2:19:03]** Home.

**[2:19:06]** So let me go back.

**[2:19:24]** These are the lab instructions. So first, the step is we need to log into GitHub, load the GitHub repository, etc. We go to the cloud shell and we create a service principle here, right, which with a contributor access.

**[2:19:43]** To the resource group name, so this principle.

**[2:19:47]** Then, programmatically, we can use the service principle to access the resources which are present in this resource group, so we have.

**[2:19:59]** If I, if I go back here, let me go to the Azure portal.

**[2:20:12]** The workspace is available in a resource group, and for that resource group, so that's the resource group we have, and we are able to create a service principle. OK.

**[2:20:26]** In the instructions, OK, once we are able to create a service principle, right?

**[2:20:34]** It will generate certain credentials like the subscription ID and other credentials it would be generated that we need to update in the GitHub with Azure credentials. So we may go back to the.

**[2:20:55]** GitHub repo here, go to the settings.

**[2:20:59]** The service principal credentials are stored in secrets and variables section.

**[2:21:05]** And over here, we can see we have the repository secret, which is the Azure credentials, and it is updated with the service principal credentials which are generated when we create the service principal, right? Along with that, we are...

**[2:21:25]** also creating certain variables that we will use in our GitHub repo.

**[2:21:33]** The Azure Resource Group and the workspace name, and it's all edited. OK, so these are the values it has currently. That's very correct. OK, and once it is all done, we can go back to the code and now we want to automate.

**[2:21:52]** model training using GitHub action. So we can go to the source folder. There is a job.yaml file. There is a train model parameters.py file is available. So what this py file is, it's training a model.

**[2:22:08]** It's using M.L. Flu, our cost library, and we are training a model, a regression model here.

**[2:22:12]** Thank you.

**[2:22:18]** Yeah.

**[2:22:20]** So, if all good.

**[2:22:23]** Now we can see job.yaml here. So this is a configuration file where we are writing this command line, the Python file name here, and we are executing this Py file. To execute the Py file, data is available in a URF file, which is available in the Azure.

**[2:22:42]** Machine learning workspace. It's the name of the data set is diabetes data. We are using regulation rate of 0.9 and we are training the model.

**[2:22:55]** Okay, now to train the model, the PI file, right, it's using...

**[2:23:02]** The compute.

**[2:23:05]** Right, so when we are submitting this job, OK, let me go back to YAML. When we are submitting the job, we can see the compute is the AML cluster. This should be available in the in my.

**[2:23:22]** in my workspace so that it can use this compute. So let me create this compute cluster.

**[2:23:47]** All right, so while this is creating, let's go back to the repository. So we have job.yaml, which would be executing this PI file, and we are able to create a job, okay, and we are able to train this model, right, the logistic regression model from this PI file.

**[2:24:07]** So this is a job.yaml and it should be.

**[2:24:13]** This job should get triggered using a manual GitHub actions workflow.

**[2:24:20]** Okay, so we can go back here.

**[2:24:23]** and go to the GitHub workflow and there is a workflow available which is manual trigger job.yaml.

**[2:24:35]** Okay, now this workflow gets triggered on workflow dispatch on a manual trigger, right? This workflow can also be triggered if we are making a pull request on the main branch. Okay, so under these conditions, this workflow will be triggered.

**[2:24:54]** And what this workflow is doing, it is first checking out to the main branch. We are then installing Azure extension, logging to Azure. Then we are able to log into Azure using the Azure credentials.

**[2:25:13]** This is the service principal credentials that we have. Using the service principal credentials, we are able to log into Azure and we can explore the resources or use the resources of.

**[2:25:26]** which are deployed. And then finally we are creating a job using this job.yaml. We are executing the PI file and we are training the model.

**[2:25:40]** Right, so.

**[2:25:44]** Right, so the model gets trained with a regulation rate of 0.9 and we should be able to train a model. Okay, if we are able to manually trigger this workflow. So to do this, maybe I'll go back here.

**[2:26:04]** OK, we can go to GitHub actions.

**[2:26:08]** And.

**[2:26:12]** We can see there is a manual trigger of workflows available. So if I click on this, it says here this workflow has a workflow dispatch event trigger and I can manually run the workflow.

**[2:26:28]** Okay, this I can do. Now before I go and trigger this workflow, let me go back here and see the cluster is available. It has succeeded. Now let me go back, run the workflow on the main branch.

**[2:26:48]** Current workflow.

**[2:26:52]** So manually we are triggering this workflow and we are training the model.

**[2:26:59]** And when we...

**[2:27:02]** Check.

**[2:27:04]** This workflow here, that's the name of the workflow train, and right now.

**[2:27:10]** It's installing Azure Machine Learning Extension, then it will log into Azure and it will create a job.

**[2:27:19]** Right. So while this is running, I can duplicate this tab.

**[2:27:33]** Let me show you my previous run, previous workflow here. If I go back to the action.

**[2:27:42]** We can see manually triggering an Azure Machine Learning job. So if I click on this, earlier this job ran successfully.

**[2:27:52]** Where we are able to log into Azure, then no.

**[2:27:56]** We are able to create a job to execute the PI file and we can see the job URL also. So if I click on this URL.

**[2:28:09]** Ohh.

**[2:28:10]** This will take us to the job.

**[2:28:18]** And this job has completed, where we can see the regulation rate was 0.9 and we are able to train a model with the accuracy of 773.

**[2:28:32]** So when the reg rate is 0.9, the accuracy is 0.773, right? We are able to manually trigger this workflow, create a job, complete the job, and we are able to train the model.

**[2:28:47]** Great.

**[2:28:49]** So, if I go back...

**[2:28:51]** Right now we see Azure login has completed and right now we are at this job and we can look at this job.

**[2:28:58]** Hmm.

**[2:29:01]** the current job here.

**[2:29:13]** Right now it is in cube.

**[2:29:18]** We'll wait for this to be completed.

**[2:29:23]** Okay.

**[2:29:54]** Okay, so this job is running now.

**[2:29:59]** It will take two or three minutes and it would be completed.

**[2:32:19]** Yeah.

**[2:32:22]** This is 1 is the older one. Okay. Yeah, it is still running and I think it's we are able to complete this. We can see the results here.

**[2:32:38]** Yeah, so this job is completed.


#### Trigger workflows in GitHub Actions  `[2:32:42]`

**[2:32:42]** So we are able to go to GitHub actions, right, trigger a workflow.

**[2:32:51]** manually we are triggering this workflow and the workflow allows us to execute a PI file where we are training a model.

**[2:33:04]** Right, we can also further do automated triggers. For example, if let's say we are making a PR, when we are creating a PR, we want to execute this PI file. OK.

**[2:33:20]** Right, this can be done. So for example, we have this PI file available in the main branch, right? And we create a feature branch where we are editing this PI file.

**[2:33:34]** Let's say we edit the PI file. Maybe we are changing the regulation rate.

**[2:33:41]** to let's say 100. OK, then.

**[2:33:47]** Once this edit is done, we make a commit and we update this branch. After that, then we want to, let's say, merge it to the main, right? We need to create a PR, the pull request. So when we create a PR, the workflow will be triggered.

**[2:33:55]** I think so.

**[2:34:00]** Yes.

**[2:34:06]** Right, it would be executing this PI file with a regulation rate of 100. We are able to cheque the metrics, like accuracy, etc. And before we merge it to the main branch, okay, we can observe the output. We can take a decision whether to apply.

**[2:34:08]** That's really mean.

**[2:34:15]** Thank you.

**[2:34:19]** It.

**[2:34:25]** The.

**[2:34:27]** Approve this PR or to close the PR. If we approve PR, we approve PR maybe when the performance is improving, but if the performance is not improving, we may simply close the PR. OK, and the main branch remains untouched if that improves the code.

**[2:34:29]** She.

**[2:34:36]** See.

**[2:34:38]** Next.

**[2:34:43]** Yeah.

**[2:34:46]** We can improve the model performance. We may merge, we can merge with the main branch, right? And we can update the code of the main.

**[2:34:52]** So.

**[2:34:56]** Sit.

**[2:34:57]** This we can try to do. Okay, so right now it's a simple manual trigger we have done and we get the accuracy of 774 with a revolution rate of 0.9.

**[2:35:05]** Thank you.

**[2:35:08]** Sim.

**[2:35:11]** Okay, let's try doing it with a new branch. Okay, so if I go ahead, let me...

**[2:35:13]** Yes.

**[2:35:14]** So.

**[2:35:22]** Go to the other branch, so if I maybe we may create a new branch, OK, or right now I'm taking this feature branch here.

**[2:35:22]** St.

**[2:35:25]** Things.

**[2:35:30]** Just.

**[2:35:31]** Just.

**[2:35:36]** Let me.

**[2:35:37]** See.

**[2:35:38]** Go to the source file.

**[2:35:41]** Update this job.yaml.

**[2:35:42]** People.

**[2:35:44]** Okay.

**[2:35:45]** Still.

**[2:35:46]** But.

**[2:35:49]** Six.

**[2:35:49]** Yes.

**[2:35:57]** Over here, right now we see in the feature branch here, we have the regulation rate of 90. Maybe I'll just edit this file. Let me make it 100.

**[2:36:13]** Okay, commit changes. So we have the main branch and we get the feature branch and we are committing to the feature branch here.

**[2:36:26]** So what we have done?

**[2:36:30]** We cheque out from the main branch.

**[2:38:17]** Hello, can you hear me? I think I got lost.

**[2:38:43]** Can you hear me?

**[2:38:46]** K.

**[2:38:52]** Yes, but.

**[2:38:54]** Okay, okay. Thank you. Thank you, Raghu. Thank you. Okay, I think I got lost for a minute. Yeah.

**[2:39:03]** Yeah, let me go back. OK, just change my network.

**[2:39:10]** I think just change it to the stable network. OK, I think it's all good, so no.

**[2:39:17]** So let me share my screen, OK?

**[2:39:28]** So.

**[2:39:30]** What we have done so far is we can manually trigger the workflow and we are able to submit a job and we are able to train a model.

**[2:39:42]** Great.

**[2:39:45]** This we have done. Now we are coming to the feature branch. Okay, so we have main branch.

**[2:39:54]** Okay, we create a new branch, that's the feature branch, and we are editing this job.yaml.

**[2:40:07]** Right, updating the regulation rate value to 100.

**[2:40:12]** And.

**[2:40:15]** So once it is updated, we have made commits also and

**[2:40:21]** Yeah, I think we have made the commit as well, right? It's 400 now. Now we have the feature branch, right? The main branch, maybe with revolution rate of 100, we want to merge it to the main. So before we can merge it to the main, we...

**[2:40:40]** may want to do a task, an automated task that...

**[2:40:46]** That, if let's say the version is 100, OK, how is my training performance? What is the model accuracy? So, I want to execute the PI file, so when we are reading a PR right, then...

**[2:41:02]** This workflow should get triggered. So let me go ahead and go to pull request.

**[2:41:10]** and create a new pull request.

**[2:41:18]** From the feature branch to the main branch.

**[2:41:23]** Right, let me create a PR.

**[2:41:28]** So when we create a PR.

**[2:41:35]** The workflow gets triggered so we can in the other tab let me okay.

**[2:41:42]** Let me go to GitHub Actions.

**[2:41:45]** A workflow should get triggered because the trigger is on for pull request and we may ignore this pull this trigger because that's from another task and here we see we are able to.

**[2:42:04]** trigger this workflow where we are training the model. And this time we are training the model with a regulation rate value of 100.

**[2:42:15]** So right now we are logged into Azure. Once done, we will go ahead and create a job here.

**[2:42:24]** Let's look at the job output. Is it improving the model performance or not?

**[2:42:45]** So it would provide a URL. Go ahead and...

**[2:42:51]** Access the job URL.

**[2:43:01]** Alright, so right now this job is in queue. It is submitted to the compute.

**[2:43:43]** Let it complete.

**[2:43:47]** If...

**[2:43:49]** Alright, so while it is going on, maybe I can show you the previous result, and if I...

**[2:44:02]** Okay, this one is running.

**[2:44:14]** So, if I go back to the actions.

**[2:44:20]** The feature update parameter, I have executed it before also and if you go to this job, okay, where we are able to train a model with a regulation rate of 90 because earlier it was 90. Now we have changed it to 100.

**[2:44:39]** We can go to this run.

**[2:44:50]** And here we may find that with a regulation rate of 90, the model accuracy is 0.73. So earlier when the regulation rate was 0.9, the accuracy of 0.774. Now we have

**[2:45:09]** Increase it, right? It's too much regulation we are doing that has led to a decrease in model performance, and we have 0.73 accuracy, right? So, so this is the this edit we have done, we have triggered the workflow in the feature branch.

**[2:45:30]** And if you want, we may merge it to the main branch that we can do, okay? Or since the performance is degrading, we may simply close the PR, okay? We may not merge with the main branch. Okay, this we can do, right? So thereby we have seen.

**[2:45:49]** How we can edit, we can create a new branch, do some experimentation without touching the main branch. OK, and then we go ahead and create a PR, then...

**[2:46:05]** It's up to us, right? The approval team, right? Whether to approve and edit or touch the BM branch or not. OK, so this can be done. So this brings like, like depending on what triggers we have run, what automation.

**[2:46:24]** we have done, what tasks we have done when the PR is created, observing the output, we take a decision whether to merge it or not, right? So we can do such task, right, with, right, we can do automation.

**[2:46:42]** Right.

**[2:46:44]** In our main branch and the other branch, OK, so...

**[2:46:58]** Let's look at the job again, OK?

**[2:47:02]** This job is currently running.

**[2:48:47]** Alright, so the job is completed now.

**[2:48:51]** And we can see with the regulation rate of 100, okay, the accuracy is...

**[2:48:58]** The accuracy is 0.773. OK, yeah, that's the value we get, so we may go back to our PR, right?

**[2:49:20]** Right, and this job is just about to get completed.

**[2:49:25]** Right, we may.

**[2:49:27]** want to merge the pull request. If you want, we can do that. Or we may simply close the pull request. OK, so if you merge, that would be updating the main branch, right? Else we will simply go ahead and close pull request.

**[2:49:45]** Right, so this is closed now.


#### Recap — collaboration with GitHub  `[2:49:49]`

**[2:49:49]** So we have seen how we can collaborate, like using GitHub, right? Trigger certain workflows, trigger automated workflows, right? Using GitHub actions, do a certain task based on it. We may update the main branch.

**[2:50:08]** Like, this can be done, OK?

**[2:50:13]** Any any query we have here? It's all good.

**[2:50:19]** Yeah.

**[2:50:25]** All right.

**[2:50:27]** So, let's go ahead then, OK.

**[2:50:34]** And we'll talk about deployment.

**[2:50:38]** Right, how we can deploy a model using Azure Machine Learning Workspace. So that would be the lab number six, and once I complete the conceptual slides, we can go ahead and we can perform the lab also. So, so far we have completed all the labs from one.

**[2:50:57]** Two 6 right, and we may try performing these labs. OK, so let's go ahead talk about model deployment using Azure Machine Learning. So let's go ahead.

**[2:51:14]** So when we deploy a model, right, so we need to 1st register the model.

**[2:51:22]** Where we are able to save the model folder.

**[2:51:26]** And this model folder would be.

**[2:51:30]** then put to an endpoint, right? Maybe the endpoint is a batch endpoint, or it could be an online endpoint. And we can consume the model from the endpoint. So let's try.

**[2:51:44]** So, here.

**[2:51:46]** The.

**[2:51:49]** The batch endpoints are the endpoints where we pass a batch of inputs.

**[2:51:57]** Okay.

**[2:51:59]** submit the batch of inputs to the endpoint, and the model is deployed to the endpoint. The model will receive the batch inputs, and it will generate the responses for every observation. Maybe the total batch size is, let's say, 1,000 records we have.

**[2:52:19]** And we may want to, we convert the batch into mini batch size of, let's say, 100 inputs per batch. So we have 10 batches and that's how we submit a request to the model, right? We provide the batch input and which get further split into mini batches.

**[2:52:41]** and then submit it to the model for predictions. The model generates a response and since we are passing 100 inputs, it would be providing 100 or 1000 here, 1000 inputs and for 1000 inputs we have 1000 predictions.

**[2:52:59]** right, are generated. But since the inputs are put into mini batches, each batch of size 100, so model would be predicting, providing the responses for all the mini batches.

**[2:53:18]** Okay, and we configure the back job that how to handle all the responses of mini batches, whether to append or how we want to write.


### Module 2 (continued) — Model Deployment & Endpoints  `[2:53:35]`


#### Online endpoints — request/response  `[2:53:35]`

**[2:53:35]** add the output of or add the model predictions so that it can be sent back to the client application. So we'll see how we can configure a batch endpoint. So first we'll talk about what how we can create a batch endpoint.

**[2:53:54]** To create a batch endpoint, we need to trigger a batch scoring job. OK, this job has to be triggered, right? And...

**[2:54:06]** and then submit it so that...

**[2:54:10]** The inputs are passed to the send the request to the model and model generates a response. So first how we can create.

**[2:54:21]** A batch and what?

**[2:54:24]** To create a batch endpoint, we use Azure AIML SDK, right? Use the batch endpoint class, and we are able to create a batch endpoint. We simply provide the name of the endpoint, endpoint description, use the method begin create or update.

**[2:54:43]** This will we are submitting.

**[2:54:46]** A job which will be allowing us to create a batch endpoint.

**[2:54:54]** Okay, so once the endpoint is created to the endpoint, we want to deploy the model. Okay, the model has to be a registered model first. Okay, it so we may use a ML flow and log the model folder, and then we can register the model once the model is registered.

**[2:55:15]** we can go ahead and deploy the model to an endpoint using the classes of the Azure AI ML. So if we go to the studio, go to the endpoint section here, and we can note that the deployment status of the batch endpoint, we can simply go ahead and add the deployment.

**[2:55:36]** We can do, and right go ahead and deploy a model, OK, to that endpoint.

**[2:55:44]** So...

**[2:55:46]** this we can do. So the deployment we make would be a default deployment and then once we are able to deploy.

**[2:55:57]** Model to the batch endpoint, right? We need to configure the batch scoring job, right, so that the compute...

**[2:56:09]** So that right, so once we are able to deploy the model to the batch endpoint.

**[2:56:17]** We would want to invoke the endpoint with the inputs. So the model is deployed to the endpoint from the client application or maybe we can test the endpoint, the batch endpoint can be tested in the Azure Machine Learning workspace in the studio itself.

**[2:56:36]** We may submit the request and get the response from the endpoint, so the endpoint is running on a compute, and since it's a batch endpoint, right, it's not a real-time endpoint, so we don't need a dedicated compute.

**[2:56:56]** to work 24 by 7 with low latency to provide the real-time responses. Since it's a batch endpoint, right, we pass the batch of input and let the compute make the predictions. So in this scenario, the compute we can use.

**[2:57:16]** can be an inexpensive compute, right, which could be a simple cluster compute that we have created with nodes ranging between zero to four. So we have seen, we see that the VM we are using, right, for invoking the batch endpoint.

**[2:57:36]** right? It could be DS11V2. So it's simple, a two-core compute we may use, right? And that can do the batch scoring. Okay, that can generate the predictions from the batch of input. So here is the code.

**[2:57:56]** Where we can create a compute.

**[2:58:00]** Using the Azure AI ML.

**[2:58:05]** SDK.

**[2:58:07]** So once we are able to get the compute created, okay, we go ahead and deploy our model to the batch endpoint. So when we deploy our ML flow model, right, we can configure this deployment that what is the instance count that would be running the.

**[2:58:29]** The endpoint, OK? How many VMs we make the instance required, OK?

**[2:58:36]** to invoke the endpoint, then what is the concurrency per instance? So maybe like if you have 1000 rows, it can process, let's say 20 requests, right, 20 inputs can be badly processed.

**[2:58:56]** We can define mini batch size, let's say the size of 100, so we can get the 110 batches. And for every batch, the model is making the predictions, right? So let's say 100 predictions for batch one, then 100 predictions for batch 2.

**[2:59:17]** Then, how to handle this output, these predictions, so maybe we can provide the output action that these are appended. We may want to append the responses generated by the model, so we may append and we can get the...

**[2:59:36]** responses for 1000 observations. And we can save it in a file. It could be a CSV file we may specify and we can save the results, the predictions generated in a CSV file. So this can be done.


#### Batch endpoints  `[2:59:56]`

**[2:59:56]** So, this, that's how we can configure the model deployment right to the batch endpoint.

**[3:00:04]** Then.

**[3:00:06]** If it is a custom model deployment, because earlier we are looking at the ML flow model, right? And we are...

**[3:00:17]** The endpoint that we are creating is a managed endpoint. Managed endpoint means that the endpoint that is created, right, the deployment.

**[3:00:32]** available at that endpoint, right?

**[3:00:35]** The running of the pickle file, loading that pickle file, using that pickle file to make the predictions right, it is all managed by Azure.

**[3:00:46]** Okay, so any endpoint, whether it's a batch endpoint or online endpoint, these endpoints are, could be managed endpoint.

**[3:00:58]** Or it could be a custom.

**[3:01:01]** Endpoint.

**[3:01:06]** OK, custom endpoint means that.

**[3:01:10]** that it's not managed by the Azure. So what do you mean by managed? Managed by the Azure means that if the endpoint is managed by the Azure, it means that loading the picker file, okay, then making inferences or predictions, right?

**[3:01:30]** Will be taken care by the Azure. OK, further the environment required right to run the pickle file right, the image, etcetera, right, which would be hosted to that endpoint. It's all managed by the Azure if it is a custom.

**[3:01:50]** deployment that we are doing, user needs to, the developer needs to provide the scoring script, the environment is to be created, right?

**[3:02:01]** Which will be running the scoring script, right? So this has to be done by the...

**[3:02:10]** By the team, OK, if it is not managed by the Azure, so.

**[3:02:16]** So what is the scoring script? So it's like a helper script that we want to.

**[3:02:23]** we need to create so that we can load picker file and use that picker file to make the predictions. So let me show you the sample scoring script. Okay, so that will give us an idea, give us an understanding, right?

**[3:02:40]** It.

**[3:02:42]** What's the structure of a scoring script? So this is a scoring script where it's using certain libraries like job lib, numpy, etc. Right? It has two functions. One is init function where we are loading the picker file.

**[3:03:03]** So there's a pickle file available and we are loading that. Okay, so initializing, that's an in function we have. Then we have run function where the model that is loaded, right, we are using that model to make the predictions.


#### Scoring script & MLflow model deployment  `[3:03:21]`

**[3:03:21]** So, this coding script basically can load pickle file, use that pickle file to make the predictions, and it returns the result.

**[3:03:31]** The result of the prediction result, so...

**[3:03:36]** If it is a managed online endpoint, or say managed batch endpoint, we need not to worry about scoring script. The environment required to run that scoring script, right? It is all taken care by the Azure. OK, if it is a custom, like where we want a...

**[3:03:56]** a better control over the deployment. We need to create a scoring script environment and we can

**[3:04:08]** We can then use the endpoint, right, to make the predictions.

**[3:04:13]** So here we see once we are able to deploy.

**[3:04:18]** Model to the endpoint, we can.

**[3:04:23]** Consume that model.

**[3:04:27]** by passing the batch of input. So since we have a file where we would have batch of inputs, maybe it's a CSV file, it would be pointed by a data asset. So we need to create a data asset pointing to the batch input. We use the input method.

**[3:04:47]** It is referencing the.

**[3:04:50]** The input file, right, pointed by the data asset.

**[3:04:56]** And we pass it to the invoke method, and...

**[3:05:03]** We can invoke the the batch endpoint with the inputs, and we get the job, and then we can submit the job as a batch scoring job.

**[3:05:20]** So.

**[3:05:22]** With this, we are able to consume the model deployed to a batch endpoint.

**[3:05:29]** Then we have online endpoint where we have a dedicated compute which would provide real-time predictions. So the input would be a single example or a single input that we pass it to the endpoint.

**[3:05:47]** where at the endpoint we have the model deployed and it would provide the response back to our application.

**[3:05:56]** So right now it's a managed online endpoint, so we need not to worry about scoring script. The environment to run that scoring script, it's taken care by Azure. So here we note that in a managed online endpoint, the user provides a request. The request has to be in a...

**[3:06:18]** JSON file format. The request is submitted and model makes a prediction. The prediction again is in a JSON format and we can look at the output also. Okay, so we can test our online deployment as well.

**[3:06:37]** So, here we note there are two ways, like one is a managed way.

**[3:06:45]** where we have the ML flow model available. We have registered the ML flow model. Simply deploy the model to that endpoint. So we need to create the endpoint, just like we have created the endpoint using the batch endpoint class. We have a...

**[3:07:05]** We have online.

**[3:07:07]** Endpoint class, which allow us to create an online endpoint. So, once endpoint is created, we register the model. OK, the registered model is then deployed to the endpoint, right? And we can then simply go ahead and consume.

**[3:07:25]** The model.

**[3:07:27]** But if it is not a managed online endpoint, if it is a custom model, so we need to 1st register it. So the registering model has to be done. Only thing is we need to take care of scoring script, execution environment to execute the scoring script.

**[3:07:48]** So this has to be taken care and.

**[3:07:53]** deploy the model to the endpoint and then consume the model. So these are the two options we have, right? Whether it's a managed online endpoint or it's a batch endpoint, right?

**[3:08:07]** OK, the process is quite similar. We make use of Azure AML classes to create the endpoint, do the deployment, and consume the deployment.

**[3:08:20]** So once we have the online endpoint created.

**[3:08:25]** We can test the endpoint by passing a JSON input. So we know that here is the input, a single example where we have the feature names here, the feature name and their values. So these are the values and

**[3:08:49]** We submit this request to the endpoint. The model makes a prediction. The output is in a JSON format. Right now, it outputs one. It indicates that person is diabetic.

**[3:09:04]** K.

**[3:09:06]** So that's how we can test the endpoint before we can integrate with any client application. So we can go to the Consume tab.

**[3:09:16]** Right, where we can see the Python code, how we can write a client application which can submit a request to the model, deployed to the endpoint, and provide the response back.

**[3:09:32]** So, we can test our online endpoint in the studio itself, right? This can be done.

**[3:09:40]** We can go to consume tab and see how it can be consumed via a client application using C or maybe using Python code. So supported languages are available that we can test.

**[3:10:01]** So with this, we complete all the concepts related to.

**[3:10:10]** Machine learning, the machine learning operations, right?

**[3:10:16]** And we are all set to complete the labs from 1 to 6.

**[3:10:24]** Right, that that we can do.

**[3:10:28]** So if I go back here...

**[3:10:34]** Right, so we have 6 labs related to Azure Machine Learning.


#### Tomorrow's agenda & lab time  `[3:10:39]`

**[3:10:39]** And tomorrow's agenda would be...

**[3:10:43]** Talking about generative AI.

**[3:10:47]** The AI applications that we can build, we can build using the Foundry portal.

**[3:10:55]** Okay.

**[3:10:57]** Okay, so we have labs from 7 to 11.

**[3:11:02]** On Gen Air Ops.

**[3:11:07]** So that would be the agenda for next two days, tomorrow and day after tomorrow.

**[3:11:19]** So if no questions, we can go ahead and perform the labs. We have.

**[3:11:26]** So, time available, right?

**[3:11:31]** So.

**[3:11:34]** Is it okay if we can go ahead and perform lab here?

**[3:11:38]** We may choose any lab, right? Yeah, great, great. Thank you. From 1 to 6, if you have already completed first lab yesterday, right, we can proceed with second lab.

**[3:11:53]** This can be done.

**[3:11:57]** So any lab can be performed without the sequence because all the labs are independent.

**[3:12:04]** Right.

**[3:12:21]** I can come to your lab.

**[3:12:24]** Right, for if we have any challenges, right, that we can see.

**[3:13:16]** Any quiz regarding the attendance link, if I know?

**[3:13:26]** I hope we are able to mark attendance. We can track the attendance by going to my quenic portal, right?

**[3:15:16]** Guys, please go ahead. We may launch the labs. Yeah.

**[3:15:21]** From one to six, this we can do.

**[3:15:31]** Yeah.

**[3:37:43]** Yeah.

**[3:39:52]** I hope no challenges with the lab execution so far.

**[3:39:59]** If that's all good.

**[3:59:40]** So, I see guys, we are able to perform the lap, but no as a challenge.

**[3:59:50]** Pete.

**[3:59:55]** So please continue with the labs, right? And please perform till 6th lab. We may discuss any challenges if you are facing in any of the labs.

---

## Day 3 Part 1 - Wed 3 Jun 2026 - Day 2 session close


- **Date:** Filed under Wednesday, 3 June 2026 (night batch, 21:30–01:30 IST)
- **Trainer:** Pauroosh Kaushal (Microsoft Certified Trainer), Koenig Solutions
- **Recording:** `…20260602_213016-Meeting Recording 1.mp4` (Part 1 of 2 listed under Wed 3 Jun, SharePoint Stream)
- **Length:** ~1:30  ·  **Captions:** 10



### Session close & Day 3 preview (GenAI Ops)  `[0:17]`

**[0:17]** So...

**[0:19]** Tomorrow we'll get started with the generative AI ops, the operationalizing generative AI solution. So we will be exploring Foundry portal on, we'll be exploring Microsoft Foundry and building generative AI solution.

**[0:38]** So, that would be the agenda for tomorrow.

**[0:42]** And thank you everyone for joining.

**[0:47]** Anything before we wrap up this session? Anything would you like to add here?

**[0:59]** All good. So thanks for joining today and I see you guys tomorrow. Have a nice day ahead. Yeah.

**[1:11]** Yep, yep.

**[1:13]** Thank you, Raghav. Yeah, I see no challenge, right? The labs are going well.

**[1:23]** A good.

**[1:27]** Okay, that's great to hear. Yeah, thank you so much. So thank you guys. See you tomorrow. Good day. Yeah.

---

## Day 3 Part 2 - Wed 3 Jun 2026 - Module 3 GenAI Ops


- **Date:** Wednesday, 3 June 2026 (21:30–01:30 IST)
- **Trainer:** Pauroosh Kaushal (Microsoft Certified Trainer), Koenig Solutions
- **Recording:** `…20260603_213018-Meeting Recording.mp4` (Part 2 of 2 listed under Wed 3 Jun) — the full Day 3 session
- **Length:** ~3:59:57  ·  **Captions:** 897




### Module 3 — GenAI Ops: Operationalize Generative AI Solutions  `[0:00]`


#### Session start & agenda  `[0:00]`

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


#### Generative AI models & agents  `[11:28]`

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


#### LLMs with tools — agent examples  `[21:07]`

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


#### Evaluating GenAI before production  `[36:20]`

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


#### Token-based cost  `[52:15]`

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


#### Foundry portal — model catalog & deployment  `[55:13]`

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


#### RAG app & endpoints  `[1:06:42]`

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


#### Create an agent & evaluators  `[1:14:04]`

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


#### Foundry project — experiment to production  `[1:30:54]`

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


#### Build an agent (weather agent) & prompt versions  `[1:37:38]`

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


#### Managing prompts  `[1:51:07]`

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


### Module 3 (continued) — Prompt Management & Evaluation  `[2:08:16]`


#### Recap & tracking prompts in files (after break)  `[2:08:16]`

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


#### Prompt evaluation — accuracy & relevance  `[2:18:18]`

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


#### Batch testing & prompt templates  `[2:24:16]`

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


#### Branching & comparing prompts  `[2:30:28]`

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


#### Lab — manual evaluation & prompt optimization  `[2:37:29]`

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


#### Baseline experiment & new agent versions  `[2:44:55]`

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


#### Knowledge check & extended lab time  `[2:53:52]`

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


#### Lab — quota limit troubleshooting  `[3:58:49]`

**[3:58:49]** OK, now it throws the quota limitation error, right?

**[3:58:57]** Insufficient quota.

**[3:58:59]** Gurpreet.

**[3:59:06]** Okay, let's try East US 2 because it's a training key temporarily. Sometimes the resources are not available in a particular region. So either we try West US, East US 2 or Sweden Central, right? We should be able to provision the resource here.

**[3:59:23]** Okay.

**[3:59:57]** Not sure where it is east.

---

## Day 4 - Thu 4 Jun 2026 - Day 3 close - Day 4 lecture pending


- **Date:** Filed under Thursday, 4 June 2026 (night batch, 21:30–01:30 IST)
- **Trainer:** Pauroosh Kaushal (Microsoft Certified Trainer), Koenig Solutions
- **Recording:** `…20260603_213018-Meeting Recording 1.mp4` (the only item listed under Thu 4 Jun, SharePoint Stream)
- **Length:** ~5:56  ·  **Captions:** 34



### Day 3 close — lab quota troubleshooting & sign-off  `[0:06]`

**[0:06]** Yeah.

**[0:18]** If this also fails, we may need to restart the lab because it's a temporary issue. Maybe we wait for five, 10 minutes and then we again try. Yeah.

**[0:29]** Okay.

**[0:33]** Correct.

**[0:40]** Quicker than the current available, current capacity is 0.

**[1:15]** Let me try this time, else.

**[1:19]** We need to relaunch the lab then, yeah.

**[1:25]** So...

**[1:28]** Maybe I can take...

**[2:41]** Doesn't have access to OK.

**[3:03]** Okay.

**[3:04]** Yeah.

**[3:07]** Sometimes it becomes a temporary issue. Yeah, since it's a training key, it's taking West US2.

**[4:15]** All right.

**[4:17]** So.

**[4:20]** That one.

**[4:22]** Let me take this screenshot.

**[5:00]** Alright, so we will try this lab later.

**[5:05]** Because.

**[5:08]** Temporary, it's not provisioning the resources in Sweden Central. Okay, that's the issue we have.

**[5:19]** No worries, Pauroosh, we can try a little.

**[5:20]** Yeah.

**[5:22]** Yes, meanwhile, I'll just raise a ticket to scalable also, yeah, okay.

**[5:31]** Okay.

**[5:34]** All right.

**[5:36]** Hmm.

**[5:37]** So, okay, so thank you. Thanks. I will wrap up the session then.

**[5:44]** Sure.

**[5:45]** Yeah.

**[5:46]** Thank you so much.

**[5:47]** Yeah, I see you then tomorrow. Yeah, bye-bye.

**[5:51]** Good.

**[5:51]** Good.

**[5:56]** Bye, everyone. See you tomorrow. Thanks for joining.