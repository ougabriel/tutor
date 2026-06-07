# AI-300T00: Operationalize Machine Learning and Generative AI Solutions — Day 2 (Part 2)

- **Date:** Tuesday, 2 June 2026 (21:30–01:30 IST)
- **Trainer:** Pauroosh Kaushal (Microsoft Certified Trainer), Koenig Solutions
- **Recording:** `…20260602_213016-Meeting Recording.mp4` (Part 2 of 2 listed under Tue 2 Jun) — the full Day 2 session
- **Length:** ~3:59:55  ·  **Captions:** 992

> Transcript captured from the on-screen auto-generated captions for personal study. Captions are machine-generated (Microsoft Stream) and may contain errors. Section headings were added at the points where the trainer moves to a new topic; the caption text itself is verbatim.

## Contents

- `[0:00]` Recap & Module 1 (continued) — Training, Tuning & Pipelines
  - `[0:00]` Session start & recap
  - `[10:09]` Register a model
  - `[17:56]` Run a script as a command job
  - `[33:59]` Hyperparameter tuning — sweep jobs
  - `[48:54]` Sampling & early-termination policies
  - `[1:06:35]` Compare trials & pick the best model
  - `[1:15:32]` Pipelines & components
  - `[1:25:03]` Run a pipeline job
- `[1:37:11]` Module 2 — ML Ops: CI/CD with GitHub Actions
  - `[1:37:11]` Why integrate GitHub with Azure ML
  - `[1:47:18]` GitHub Actions & pull requests
  - `[1:53:09]` Define a workflow (YAML) & trigger a job
  - `[2:14:36]` GitHub Actions — repo setup & workflow (after break)
  - `[2:32:42]` Trigger workflows in GitHub Actions
  - `[2:49:49]` Recap — collaboration with GitHub
- `[2:53:35]` Module 2 (continued) — Model Deployment & Endpoints
  - `[2:53:35]` Online endpoints — request/response
  - `[2:59:56]` Batch endpoints
  - `[3:03:21]` Scoring script & MLflow model deployment
  - `[3:10:39]` Tomorrow's agenda & lab time

---


## Recap & Module 1 (continued) — Training, Tuning & Pipelines  `[0:00]`


### Session start & recap  `[0:00]`

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


### Register a model  `[10:09]`

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


### Run a script as a command job  `[17:56]`

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


### Hyperparameter tuning — sweep jobs  `[33:59]`

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


### Sampling & early-termination policies  `[48:54]`

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


### Compare trials & pick the best model  `[1:06:35]`

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


### Pipelines & components  `[1:15:32]`

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


### Run a pipeline job  `[1:25:03]`

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


## Module 2 — ML Ops: CI/CD with GitHub Actions  `[1:37:11]`


### Why integrate GitHub with Azure ML  `[1:37:11]`

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


### GitHub Actions & pull requests  `[1:47:18]`

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


### Define a workflow (YAML) & trigger a job  `[1:53:09]`

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


### GitHub Actions — repo setup & workflow (after break)  `[2:14:36]`

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


### Trigger workflows in GitHub Actions  `[2:32:42]`

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


### Recap — collaboration with GitHub  `[2:49:49]`

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


## Module 2 (continued) — Model Deployment & Endpoints  `[2:53:35]`


### Online endpoints — request/response  `[2:53:35]`

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


### Batch endpoints  `[2:59:56]`

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


### Scoring script & MLflow model deployment  `[3:03:21]`

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


### Tomorrow's agenda & lab time  `[3:10:39]`

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
