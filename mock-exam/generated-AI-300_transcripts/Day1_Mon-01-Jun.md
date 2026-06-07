# AI-300T00: Operationalize Machine Learning and Generative AI Solutions — Day 1

- **Date:** Monday, 1 June 2026 (21:30–01:30 IST)
- **Trainer:** Pauroosh Kaushal (Microsoft Certified Trainer), Koenig Solutions
- **Recording:** Day 1 — Meeting Recording (SharePoint Stream)
- **Length:** ~3:58:04  ·  **Captions:** 1073

> Transcript captured from the on-screen auto-generated captions for personal study. Captions are machine-generated (Microsoft Stream) and may contain errors. Section headings were added at the points where the trainer moves to a new topic; the caption text itself is verbatim.

## Contents

- `[0:00]` Introduction & Course Overview
  - `[0:00]` Session start & housekeeping
  - `[13:14]` Audience check — Azure ML experience
  - `[16:42]` About AI-300 — ML Ops & GenAI Ops
- `[35:08]` Module 1 — ML Ops: Build & Train ML Models on Azure
  - `[35:08]` The machine learning process
  - `[51:04]` Connecting & splitting data
  - `[57:45]` Evaluate & deploy the model
  - `[1:00:37]` Azure data & AI services overview
  - `[1:09:35]` Use cases & the AI development lifecycle
  - `[1:19:11]` Batch scenarios & model monitoring (drift)
  - `[1:29:52]` Recap — ML basics & deployment
  - `[1:33:26]` Container registry & images for deployment
  - `[1:36:42]` Data assets
  - `[1:40:52]` Automated ML (AutoML) — jobs & best model
  - `[1:47:51]` AutoML — preprocessing & featurization
  - `[1:54:04]` Configure an AutoML job with the SDK
  - `[2:06:01]` AutoML — cost, early stopping & child jobs
  - `[2:12:21]` Knowledge check
  - `[2:15:20]` Break
- `[2:43:58]` Lab — Find the Best Classification Model with Azure ML
  - `[2:43:58]` Resume after break
  - `[2:46:57]` Lab walkthrough — AutoML job
  - `[2:55:22]` Train & deploy a model to an endpoint
  - `[3:01:40]` MLflow tracking
  - `[3:09:28]` Notebook — connect to workspace & predict
  - `[3:53:16]` Q&A / lab troubleshooting

---


## Introduction & Course Overview  `[0:00]`


### Session start & housekeeping  `[0:00]`

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


### Audience check — Azure ML experience  `[13:14]`

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


### About AI-300 — ML Ops & GenAI Ops  `[16:42]`

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


## Module 1 — ML Ops: Build & Train ML Models on Azure  `[35:08]`


### The machine learning process  `[35:08]`

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


### Connecting & splitting data  `[51:04]`

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


### Evaluate & deploy the model  `[57:45]`

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


### Azure data & AI services overview  `[1:00:37]`

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


### Use cases & the AI development lifecycle  `[1:09:35]`

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


### Batch scenarios & model monitoring (drift)  `[1:19:11]`

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


### Recap — ML basics & deployment  `[1:29:52]`

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


### Container registry & images for deployment  `[1:33:26]`

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


### Data assets  `[1:36:42]`

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


### Automated ML (AutoML) — jobs & best model  `[1:40:52]`

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


### AutoML — preprocessing & featurization  `[1:47:51]`

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


### Configure an AutoML job with the SDK  `[1:54:04]`

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


### AutoML — cost, early stopping & child jobs  `[2:06:01]`

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


### Knowledge check  `[2:12:21]`

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


### Break  `[2:15:20]`

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


## Lab — Find the Best Classification Model with Azure ML  `[2:43:58]`


### Resume after break  `[2:43:58]`

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


### Lab walkthrough — AutoML job  `[2:46:57]`

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


### Train & deploy a model to an endpoint  `[2:55:22]`

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


### MLflow tracking  `[3:01:40]`

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


### Notebook — connect to workspace & predict  `[3:09:28]`

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


### Q&A / lab troubleshooting  `[3:53:16]`

**[3:53:16]** Yeah, just one question in lab one instruction 5 says in the compute instance tab, click select the terminal, but I don't see any terminal option there. I only see Jupiter lab or Jupiter something.

**[3:53:33]** Yeah, just next to Jupiter Lab, there is 3 dots out there. Just click on that, that will take you to the terminal.

**[3:53:49]** Let me, let me come. Did you get it?

**[3:53:49]** Let me see.

**[3:53:54]** Yeah, I got it now.

**[3:53:55]** Okay.

**[3:57:48]** Guys, I hope the attendance link it's working fine and those who are facing the issues with the attendance, marking the attendance, you can log into my query portal.

**[3:58:04]** It is resolved. You should be able to see the course in your MyQE portal. If anyone still cannot see, just let me know now.
