# AI-300 Mock Exam (Combined) — Operationalize Machine Learning and Generative AI Solutions

> **Full-length combined practice exam** modeled on the official Microsoft *Exam AI-300* skills-measured blueprint (study guide last updated 05 Mar 2026), cross-checked against the AI-300T00 course transcripts (Days 1–4) and Microsoft Learn module content. Questions are original and written in the Microsoft practice-assessment style. They are **not** copied from live exam content or brain dumps (those violate Microsoft's NDA and are usually inaccurate). Use this to gauge readiness and find weak spots.

## What's in this combined exam

This single file now contains **two full question sets plus three case studies** — roughly **175 items** in total:

- **Set A** — Q1–Q80 (Sections 1–5) + Case Study 1 & 2. Answer key in Section 8.
- **Set B** — Q81–Q164 (Sections 10–14) + Case Study 3. Fresh questions, no answer overlap with Set A, with extra depth on topics the trainer emphasized (AutoML/MLflow internals, command jobs, sweep policies, pipelines/components, GitHub Actions YAML, scoring scripts, Foundry agents/tools, tracing, prompt variants/branching, automated evaluators, quotas). Answer key in Section 15.
- **Revision checklist** in Section 9; **glossary/quick-reference** in Section 16.

## How to use this exam

- **Pass mark:** Microsoft uses a scaled score; **700/1000** is a pass. As a study target, aim for **~80% correct** here to be comfortable.
- **Length:** ~164 questions + 3 case studies. The real exam is typically 40–60 questions with 1–2 case studies. This is an over-sized practice bank by design — do Set A as one timed run and Set B as another.
- **Timing:** Give yourself ~110 minutes per set for a realistic run, then mark and review.
- **Format:** Single-best-answer unless the stem says "select all that apply" / "each correct answer presents part of the solution." Some items are *yes/no design-decision* style, mirroring the real exam.
- **Answers + explanations:** Set A in Section 8, Set B in Section 15. No peeking until you've finished a domain.

## Exam blueprint (official weightings)

| # | Skill area | Weight | Questions here |
|---|------------|--------|----------------|
| 1 | Design and implement an MLOps infrastructure | 15–20% | Q1–Q14 |
| 2 | Implement machine learning model lifecycle and operations | 25–30% | Q15–Q36 |
| 3 | Design and implement a GenAIOps infrastructure | 20–25% | Q37–Q54 |
| 4 | Implement generative AI quality assurance and observability | 10–15% | Q55–Q66 |
| 5 | Optimize generative AI systems and model performance | 10–15% | Q67–Q80 |
| — | Case studies (mixed domains) | — | CS1, CS2 |

---

# Section 1 — Design and implement an MLOps infrastructure (15–20%)

**Q1.** You are creating an Azure Machine Learning workspace with Bicep. The data science team needs the workspace to store secrets, model artifacts, and metrics securely. Which three Azure resources are **automatically provisioned as dependent resources** when you create a workspace? Each correct answer presents part of the solution.

- A. Azure Key Vault
- B. Azure Storage account
- C. Azure Application Insights
- D. Azure SQL Database
- E. Azure Cosmos DB

**Q2.** Your team wants to connect an existing Azure Data Lake Storage Gen2 account to the Machine Learning workspace so data scientists can reference data without embedding credentials in code. What should you create?

- A. A compute instance
- B. A datastore
- C. A data asset of type `uri_file`
- D. An environment

**Q3.** You must give a group of data scientists permission to create and run jobs and register models in a Machine Learning workspace, but they must **not** be able to create or delete the workspace or manage role assignments. Which built-in RBAC role should you assign?

- A. Owner
- B. Contributor
- C. AzureML Data Scientist
- D. Reader

**Q4.** You want compute that automatically scales to zero nodes when idle and scales out for training jobs submitted via the SDK. Which compute target should you create?

- A. Compute instance
- B. Compute cluster (AmlCompute)
- C. Attached Azure Kubernetes Service cluster
- D. Serverless Spark compute

**Q5.** You are authoring a Bicep template to deploy a Machine Learning workspace into a customer's subscription as part of a GitHub Actions workflow. Which two statements about using Bicep for this scenario are true? Each correct answer presents a complete solution.

- A. Bicep is a declarative IaC language that compiles to ARM JSON.
- B. Bicep deployments are imperative and run top-to-bottom like a shell script.
- C. Bicep supports idempotent deployments, so re-running the template converges to the declared state.
- D. Bicep can only be deployed from the Azure portal, not from a CI/CD pipeline.

**Q6.** In a GitHub Actions workflow that deploys Azure resources, you want to authenticate to Azure **without storing a long-lived service principal secret** in GitHub. Which approach should you use?

- A. Store the service principal client secret in a GitHub repository variable
- B. Use OpenID Connect (OIDC) workload identity federation with a federated credential
- C. Hard-code a SAS token in the workflow YAML
- D. Use the workspace primary key as a GitHub secret

**Q7.** You need to restrict inbound network access to a Machine Learning workspace so it is reachable only from within a virtual network. Which feature should you configure?

- A. A managed online endpoint with key auth
- B. A managed virtual network / private endpoint for the workspace
- C. A data drift monitor
- D. A compute instance schedule

**Q8.** A reusable training step (data prep) must be shared and versioned so multiple pipelines across the team can consume it. Which Machine Learning asset should you create?

- A. A component
- B. A datastore
- C. A compute cluster
- D. An endpoint

**Q9.** You want to share a registered model and environment from a central team to multiple project workspaces in different resource groups. What should you use?

- A. A workspace datastore
- B. A Machine Learning registry
- C. A compute instance image
- D. A managed identity

**Q10.** You are configuring a managed identity for a Machine Learning compute cluster so training jobs can read from an Azure Storage account without keys. Which identity type lets you assign the **same** identity to multiple resources and manage its lifecycle independently?

- A. System-assigned managed identity
- B. User-assigned managed identity
- C. Service principal with client secret
- D. Shared access signature

**Q11.** Which file format/specification defines the Python packages, conda dependencies, and base Docker image used to execute a training job in Machine Learning?

- A. A data asset
- B. An environment
- C. A compute target
- D. A datastore

**Q12.** Your CI pipeline needs to create or update a Machine Learning workspace's resources using the command line within a GitHub Actions runner. Which tool combination is most appropriate?

- A. `az ml` CLI (v2) extension plus Azure CLI authentication
- B. The Machine Learning designer drag-and-drop UI
- C. The Azure portal Cloud Shell only
- D. `kubectl` against the workspace

**Q13.** You want changes to training code in a Git repository to automatically trigger provisioning and a training run. Which GitHub Actions concept defines when a workflow runs?

- A. A `job`
- B. A `runner`
- C. A trigger / `on:` event (such as `push` or `pull_request`)
- D. A secret

**Q14.** For source control of a machine learning project, which practice best supports collaboration and traceable change history?

- A. Store notebooks and scripts only on each data scientist's compute instance
- B. Use a Git repository with branches and pull requests, integrated with the workspace
- C. Email zipped notebooks between team members
- D. Keep a single shared notebook edited live by everyone

---

# Section 2 — Implement ML model lifecycle and operations (25–30%)

**Q15.** You want to log parameters, metrics, and model artifacts during training so runs can be compared in the Machine Learning studio. Which framework is natively integrated for experiment tracking?

- A. TensorBoard only
- B. MLflow
- C. Azure Monitor Logs
- D. Application Insights

**Q16.** You start an automated machine learning (AutoML) job for a binary classification problem and want it to stop spending compute once the metric stops improving. Which setting should you enable?

- A. Featurization
- B. Early termination / early stopping
- C. Cross-validation folds = 1
- D. Forecasting horizon

**Q17.** In AutoML, you set the **primary metric** to `accuracy` for an imbalanced fraud dataset where positives are rare. Which statement is the best critique of this choice?

- A. Accuracy is ideal because it always reflects minority-class performance.
- B. Accuracy can be misleading on imbalanced data; AUC-weighted or a precision/recall-based metric is usually better.
- C. AutoML does not support classification metrics.
- D. Accuracy and AUC are mathematically identical.

**Q18.** You need to automate hyperparameter tuning across a defined search space, sampling learning rate and batch size, and want to terminate poorly performing runs early. Which Machine Learning capability should you use?

- A. A sweep job
- B. A batch endpoint
- C. A data asset
- D. A model registry

**Q19.** In a sweep job, you want the search to focus more attempts in promising regions of the search space based on prior results rather than testing fixed combinations. Which sampling method should you choose?

- A. Grid sampling
- B. Random sampling
- C. Bayesian sampling
- D. No sampling

**Q20.** You are training a large deep learning model that does not fit on a single GPU and want to split work across multiple GPUs/nodes. Which approach does Machine Learning support for this?

- A. Distributed training (e.g., PyTorch DDP / `distribution` config with `process_count_per_instance`)
- B. A compute instance with one CPU core
- C. A batch endpoint
- D. AutoML featurization

**Q21.** You want to build a repeatable, multi-step training workflow (data prep → train → evaluate → register) where each step is independently versioned and the whole flow can be scheduled. What should you build?

- A. A single monolithic notebook
- B. A pipeline job composed of components
- C. A managed online endpoint
- D. A data drift monitor

**Q22.** After running 30 training jobs with different configurations, you need to compare their logged metrics to choose the best model. Where do you do this most efficiently?

- A. By reading raw stdout logs for each job
- B. In the Machine Learning studio Jobs view, comparing logged MLflow metrics across runs
- C. By re-running every job
- D. In the Azure billing portal

**Q23.** You registered a model with MLflow. Which advantage does the **MLflow model format** provide when you deploy to a managed online endpoint?

- A. It requires you to write a custom scoring script and explicit environment for every deployment.
- B. It enables no-code deployment because the model packaging includes signature and dependencies.
- C. It disables autoscaling.
- D. It prevents versioning.

**Q24.** You want to evaluate a trained classification model for fairness across sensitive groups and inspect feature importance before approving it for production. Which Machine Learning capability supports this?

- A. The Responsible AI dashboard / scorecard
- B. A datastore
- C. A compute schedule
- D. A SAS token

**Q25.** You need to keep older model versions for audit but prevent them from being used in new deployments. What is the appropriate lifecycle action?

- A. Delete the models permanently
- B. Archive the model version
- C. Move them to a different subscription
- D. Rename the workspace

**Q26.** A trained model must serve **low-latency, synchronous** predictions to a web app, one request at a time. Which deployment target is appropriate?

- A. A managed batch endpoint
- B. A managed online endpoint
- C. A compute instance notebook
- D. A datastore

**Q27.** You need to score **millions of records on a schedule** with no requirement for immediate per-request responses. Which deployment target is appropriate?

- A. A managed online endpoint
- B. A batch endpoint
- C. A real-time Kubernetes endpoint with autoscale to 1
- D. A compute instance

**Q28.** You deploy a new model version to a managed online endpoint but want to send only **10% of live traffic** to it while the previous version handles the rest, so you can validate before full rollout. What should you configure?

- A. Two separate endpoints with manual DNS switching
- B. Traffic split / mirrored traffic across deployments under one endpoint
- C. A batch endpoint
- D. Data drift monitoring

**Q29.** A newly rolled-out deployment shows elevated error rates. You need to quickly return all traffic to the previous known-good deployment. Which capability enables this safe rollback?

- A. Re-training the model
- B. Shifting the endpoint traffic allocation back to the previous deployment (blue/green)
- C. Deleting the workspace
- D. Archiving the dataset

**Q30.** You call a managed online endpoint and receive HTTP 502/503 errors. Which is the most appropriate first troubleshooting step?

- A. Delete the endpoint and recreate the workspace
- B. Inspect the deployment/container logs (`get-logs`) and check the scoring script and health probe
- C. Increase the exam timeout
- D. Switch to a batch endpoint

**Q31.** A model deployed three months ago is producing degraded predictions. Incoming feature distributions have shifted away from the training data. What is this phenomenon called?

- A. Data drift
- B. Overfitting at training time
- C. Hyperparameter leakage
- D. Quantization

**Q32.** You want to be alerted automatically and trigger retraining when data drift exceeds a configured threshold. Which combination achieves this?

- A. A data drift monitor with a threshold plus an alert/trigger that starts a retraining pipeline
- B. A single static accuracy report run once
- C. A compute instance schedule only
- D. Manual weekly inspection only

**Q33.** Which metric is most appropriate to monitor for a deployed **regression** model's prediction quality over time?

- A. Accuracy
- B. Precision
- C. Root Mean Squared Error (RMSE) / MAE
- D. F1 score

**Q34.** You package a model that depends on a feature retrieval specification so the same feature transformations are applied at inference as during training. Why is bundling the feature retrieval spec with the model artifact important?

- A. It reduces the model file size only
- B. It prevents training/serving skew by ensuring consistent feature computation
- C. It disables logging
- D. It is required to create a datastore

**Q35.** Two training jobs produced models A and B. You must decide which to promote. Which approach gives the most reliable comparison?

- A. Compare on the metric logged on each job's own training split
- B. Compare both on the same held-out evaluation dataset using the same primary metric
- C. Pick the one that finished fastest
- D. Pick the one with the larger file size

**Q36.** You want to run experimentation and quick data exploration interactively before formalizing a training pipeline. Which Machine Learning resource is best suited?

- A. A batch endpoint
- B. A compute instance running notebooks
- C. A managed online endpoint
- D. A registry

---

# Section 3 — Design and implement a GenAIOps infrastructure (20–25%)

**Q37.** You are setting up Microsoft Foundry for a team building generative AI apps. Which statement best describes the relationship between a Foundry **resource/hub** and a **project**?

- A. A project contains multiple hubs, each with separate billing
- B. A hub provides shared configuration, security, and connections; projects are workspaces created under it for specific apps
- C. Hubs and projects are the same object with different names
- D. Projects must be created before any hub exists

**Q38.** You need Foundry to access Azure OpenAI and Azure AI Search without storing keys in application code. Which approach should you configure?

- A. Embed API keys in the prompt
- B. Use managed identity and RBAC with connections in Foundry
- C. Store keys in a public GitHub repo
- D. Disable authentication

**Q39.** Your organization requires that traffic to Foundry and its dependent resources stay off the public internet. Which two configurations support this? Each correct answer presents part of the solution.

- A. Private endpoints for the resources
- B. A managed virtual network for the Foundry hub
- C. Assigning the Owner role to all users
- D. Publishing the endpoint with anonymous access

**Q40.** You want to deploy Foundry infrastructure repeatably across dev, test, and prod subscriptions as code. Which tools are appropriate? Each correct answer presents a complete solution.

- A. Bicep templates
- B. Azure CLI (`az`) deployment commands
- C. Manually clicking through the portal each time
- D. Editing resources directly in production only

**Q41.** A workload needs to call a large language model with **predictable, reserved capacity** and consistent latency at high volume, rather than pay-as-you-go shared capacity. What should you configure for the deployment?

- A. Serverless API endpoint with default quota
- B. Provisioned throughput units (PTUs)
- C. A batch endpoint
- D. A compute instance

**Q42.** You want to quickly consume a foundation model via a pay-per-token HTTP endpoint without managing underlying compute. Which deployment option fits?

- A. Managed compute with dedicated VMs
- B. Serverless API endpoint
- C. Provisioned throughput only
- D. A Kubernetes cluster you manage

**Q43.** A team needs to host an open-weight model that is not offered as a serverless API and requires dedicated GPU compute they control. Which deployment option fits?

- A. Serverless API endpoint
- B. Managed compute deployment
- C. A datastore
- D. A prompt flow only

**Q44.** You must choose a model for a customer-support summarization feature that is cost-sensitive and high-volume, where a smaller, cheaper model meets quality bars. Which selection principle is most appropriate?

- A. Always choose the largest, most capable model regardless of cost
- B. Select the smallest/cheapest model that meets the quality and latency requirements, validated by evaluation
- C. Choose a model at random
- D. Choose based only on context window size

**Q45.** Your team revises prompts frequently and needs to track changes, review them, and roll back. What is the recommended practice?

- A. Store prompts only in a chat window
- B. Version-control prompts in a Git repository with reviews
- C. Keep prompts in a single shared document edited live
- D. Hard-code prompts and never change them

**Q46.** You want to compare two different prompt designs against the same test inputs to see which yields better responses before shipping. What should you create?

- A. Prompt variants and compare their performance
- B. Two separate Foundry hubs
- C. A new subscription
- D. A batch endpoint

**Q47.** You are deploying multiple model versions to production and need a strategy to introduce a new version safely. Which approach mirrors safe ML rollout practices for GenAI deployments?

- A. Replace the production version instantly with no validation
- B. Progressive/staged rollout with the ability to roll back
- C. Delete the old version before testing the new one
- D. Deploy only to a developer laptop

**Q48.** Which identity construct should back a Foundry connection to Azure AI Search so that access can be granted via RBAC and rotated centrally?

- A. A user-assigned or system-assigned managed identity
- B. A shared password in the app config
- C. An anonymous connection
- D. A SAS token embedded in the prompt

**Q49.** You need to grant a data scientist permission to use a Foundry project and run evaluations, but not to manage the hub's networking or role assignments. What is the correct principle?

- A. Grant Owner at the subscription scope
- B. Apply least-privilege RBAC by assigning a scoped project-level role
- C. Disable RBAC entirely
- D. Share the admin's credentials

**Q50.** You want infrastructure-as-code for Foundry to be validated in a pull request before being applied. Which GitHub Actions pattern supports this?

- A. Run a what-if/validation step on `pull_request`, then deploy on merge to main
- B. Deploy directly to production on every commit with no review
- C. Only deploy manually from a laptop
- D. Store the Bicep file but never run it

**Q51.** When deploying a foundation model, which factor is **least** relevant to selecting between a serverless API endpoint and managed compute?

- A. Whether the model is offered as a serverless API
- B. Throughput, latency, and cost predictability requirements
- C. Need for dedicated/isolated compute and custom configuration
- D. The font used in the client application

**Q52.** Which statement about provisioned throughput units (PTUs) is correct?

- A. PTUs reserve dedicated model-processing capacity for stable high-volume throughput
- B. PTUs are billed strictly per token with no reserved capacity
- C. PTUs are only available for batch endpoints
- D. PTUs disable monitoring

**Q53.** You need to ensure prompt changes flow through the same review/CI process as code. Which artifact should live in the repo alongside application code?

- A. Prompt templates / prompt flow definitions
- B. The model weights binary only
- C. Customer PII
- D. The Azure subscription key

**Q54.** A Foundry project must connect to an existing Azure OpenAI deployment in another resource group. What is the correct mechanism?

- A. Copy the model weights into the project
- B. Create a connection in the project that references the Azure OpenAI resource
- C. Recreate the model from scratch
- D. Embed the endpoint key in every prompt

---

# Section 4 — Generative AI quality assurance and observability (10–15%)

**Q55.** You must evaluate whether a RAG chatbot's answers are supported by the retrieved source documents and not fabricated. Which AI quality metric measures this?

- A. Fluency
- B. Groundedness
- C. Latency
- D. Throughput

**Q56.** Which set of metrics are the standard **AI quality** (generation quality) metrics in Foundry evaluations?

- A. Groundedness, relevance, coherence, fluency
- B. CPU, memory, disk, network
- C. RMSE, MAE, R²
- D. Precision, recall, accuracy, F1 only

**Q57.** You want to detect whether the model produces hateful, violent, sexual, or self-harm content. Which evaluation category should you configure?

- A. Performance metrics
- B. Risk and safety evaluations (content harm)
- C. Token cost metrics
- D. Data drift

**Q58.** To run a comprehensive evaluation, you need a curated set of inputs with expected/ground-truth references mapped to the app's inputs and outputs. What must you prepare?

- A. A test dataset with data mapping
- B. A managed online endpoint
- C. A PTU reservation
- D. A private endpoint

**Q59.** You want evaluations to run automatically whenever a new prompt or model version is committed, gating release on quality thresholds. What should you set up?

- A. A one-time manual evaluation
- B. An automated evaluation workflow integrated into CI
- C. A data drift monitor for tabular features
- D. A compute cluster autoscaler

**Q60.** Which metric specifically asks "Is the answer pertinent to the user's question?"

- A. Relevance
- B. Fluency
- C. Groundedness
- D. Coherence

**Q61.** You need to track end-to-end request behavior of a deployed GenAI app, including the steps a request takes through retrieval and generation, to debug a slow path. Which capability should you use?

- A. Tracing
- B. A datastore
- C. A model registry
- D. A sweep job

**Q62.** Which three are key **operational/performance** metrics to monitor for a production GenAI endpoint? Each correct answer presents part of the solution.

- A. Latency
- B. Throughput
- C. Response time
- D. Disk fragmentation of the client device

**Q63.** Your finance team needs to control GenAI spend. Which metric is the primary cost driver to track for LLM usage?

- A. Token consumption
- B. Number of Git branches
- C. Number of datastores
- D. Compute instance color

**Q64.** Foundry continuous monitoring of a deployed app reports rising groundedness failures over a week. What is the most appropriate response?

- A. Ignore it; quality metrics don't change over time
- B. Investigate retrieval quality and source data, and consider re-tuning RAG / prompts
- C. Delete the evaluation dataset
- D. Increase PTUs to fix groundedness

**Q65.** You want detailed logs and the ability to debug a production issue by replaying what the model received and returned. Which two capabilities support this? Each correct answer presents part of the solution.

- A. Detailed logging
- B. Tracing of requests/spans
- C. Disabling all telemetry
- D. Removing the endpoint

**Q66.** A custom business rule must be checked on every model response (e.g., the answer must include a disclaimer). How can you incorporate this into evaluation?

- A. Use a custom evaluation metric/evaluator alongside built-in metrics
- B. It is impossible to add custom checks
- C. Only built-in metrics can ever be used
- D. Change the model architecture

---

# Section 5 — Optimize generative AI systems and model performance (10–15%)

**Q67.** Your RAG system returns too many irrelevant chunks, diluting answer quality. Which two tuning levers most directly improve retrieval precision? Each correct answer presents part of the solution.

- A. Adjusting the similarity threshold
- B. Tuning chunk size and overlap
- C. Increasing the model's temperature
- D. Changing the client's screen resolution

**Q68.** You combine keyword (BM25) search with vector similarity search and re-rank results to improve recall and precision. What is this approach called?

- A. Hybrid search
- B. Pure lexical search
- C. Fine-tuning
- D. Quantization

**Q69.** For a highly domain-specific corpus (legal terminology), generic embeddings retrieve poorly. Which action most directly improves retrieval relevance?

- A. Select or fine-tune a domain-appropriate embedding model
- B. Increase the chat model temperature
- C. Reduce the number of PTUs
- D. Remove the system prompt

**Q70.** You want to objectively compare two retrieval configurations in production-like conditions. Which approach is most appropriate?

- A. A/B testing with relevance metrics
- B. Guessing based on a single query
- C. Choosing the configuration with the prettier UI
- D. Disabling evaluation

**Q71.** Very large chunks cause the model to receive too much irrelevant text per retrieval, while very small chunks lose context. What does this illustrate?

- A. Chunk size is a tunable tradeoff affecting retrieval and answer quality
- B. Chunk size has no effect on RAG
- C. Smaller is always better
- D. Larger is always better

**Q72.** When should you choose **fine-tuning** over RAG?

- A. When you need the model to learn a consistent style/format or specialized task behavior that prompting/retrieval can't reliably achieve
- B. Whenever you have any documents to reference at runtime
- C. Only to reduce token cost on a single query
- D. Never; RAG always replaces fine-tuning

**Q73.** You lack enough labeled examples to fine-tune a model for a niche task. Which technique can help create additional training examples?

- A. Generate and curate synthetic data
- B. Delete the existing data
- C. Lower the temperature to 0
- D. Increase chunk overlap

**Q74.** After fine-tuning, the model performs well on training examples but poorly on new inputs. What is the most likely problem and remedy?

- A. Overfitting; use more/diverse data, regularization, and validate on held-out data
- B. Underfitting; remove all data
- C. Data drift in the datastore
- D. The embedding dimension is too small only

**Q75.** You must manage a fine-tuned model from development through production. Which practice aligns with GenAIOps lifecycle management?

- A. Version the fine-tuned model, evaluate it, and promote through environments with rollback
- B. Deploy directly to production with no evaluation
- C. Keep only one copy and overwrite it each time
- D. Never track which dataset produced it

**Q76.** Which two metrics best indicate whether a fine-tuned model is improving during training? Each correct answer presents part of the solution.

- A. Training loss
- B. Validation loss/metric on held-out data
- C. Number of GitHub stars
- D. Client device battery level

**Q77.** A RAG answer is grounded but the model occasionally rephrases facts inaccurately. Lowering which generation parameter typically reduces creative deviation?

- A. Temperature (and/or top-p)
- B. Chunk overlap
- C. Number of datastores
- D. PTU count

**Q78.** You want to improve recall so relevant documents aren't missed, while controlling precision with re-ranking. Which combined strategy is appropriate?

- A. Hybrid search (semantic + keyword) followed by a re-ranking step
- B. Reducing the index to a single document
- C. Disabling vector search
- D. Setting temperature to maximum

**Q79.** Which statement about embeddings is correct in a RAG context?

- A. Embeddings convert text into vectors so semantically similar text is close in vector space, enabling similarity search
- B. Embeddings are the final chat responses returned to users
- C. Embeddings are only used for billing
- D. Embeddings replace the need for any retrieval index

**Q80.** You fine-tuned a model and now must decide whether it is production-ready. Which evidence best supports the decision?

- A. Evaluation results on a representative held-out dataset meeting defined quality and safety thresholds
- B. The model trained without errors
- C. The fine-tuning job was cheap
- D. The model file is small

---

# Section 6 — Case Study 1: Contoso Manufacturing (MLOps)

> **Scenario.** Contoso Manufacturing runs predictive-maintenance models that estimate the probability a machine fails within 30 days. A central platform team owns a Machine Learning workspace and wants reproducible infrastructure, automated retraining, and safe production deployment. Data scientists work in feature branches in GitHub. Models must be auditable, and production scoring runs nightly over millions of sensor records. A separate real-time API also needs single-record predictions for the operations dashboard with sub-second latency.

**CS1-Q1.** The platform team wants every workspace (dev, test, prod) provisioned identically and re-creatable on demand. What should they implement?

- A. Manually create each workspace in the portal and document the clicks
- B. Bicep templates deployed via GitHub Actions
- C. Copy the dev workspace storage account into prod
- D. A single shared workspace for all environments

**CS1-Q2.** For the **nightly scoring over millions of records**, which deployment is correct?

- A. Managed online endpoint
- B. Batch endpoint
- C. Compute instance notebook run manually
- D. A registry

**CS1-Q3.** For the **operations dashboard's sub-second single-record predictions**, which deployment is correct?

- A. Batch endpoint
- B. Managed online endpoint
- C. A pipeline job
- D. A datastore

**CS1-Q4.** Data scientists must compare many training runs and reproduce the winning run later. Which practice should the team standardize?

- A. MLflow experiment tracking with logged params, metrics, and artifacts
- B. Saving screenshots of accuracy numbers
- C. Emailing model files
- D. Deleting runs after training

**CS1-Q5.** Sensor feature distributions change seasonally. The team must detect this and trigger retraining automatically. What should they configure?

- A. A data drift monitor with thresholds wired to a retraining pipeline trigger
- B. A manual quarterly review only
- C. A larger compute instance
- D. A second subscription

**CS1-Q6.** A new model version must be validated on live traffic before full cutover on the real-time endpoint. Which strategy fits?

- A. Blue/green deployment with traffic split, enabling rollback
- B. Delete the old deployment first
- C. Deploy only to a laptop
- D. Skip validation

**CS1-Q7.** Before promoting a model, the team must check fairness across machine types and review feature importance. Which tool should they use?

- A. Responsible AI dashboard
- B. A datastore
- C. A SAS token
- D. A sweep job

---

# Section 7 — Case Study 2: Fabrikam Support Copilot (GenAIOps)

> **Scenario.** Fabrikam is building a customer-support copilot in Microsoft Foundry. It uses RAG over a product-documentation corpus stored in Azure AI Search and an Azure OpenAI chat model. Requirements: no keys in code, private networking, prompt changes reviewed like code, automated quality and safety evaluation gating releases, production observability for latency and token cost, and ongoing RAG accuracy improvements. Peak traffic requires predictable latency.

**CS2-Q1.** Fabrikam must connect Foundry to Azure OpenAI and Azure AI Search without keys in application code. What should they configure?

- A. Managed identity with RBAC and Foundry connections
- B. Hard-coded keys in the prompt
- C. Anonymous access
- D. SAS tokens in the client

**CS2-Q2.** Peak traffic requires predictable latency and reserved capacity for the chat model. What should they deploy?

- A. Pay-as-you-go serverless with default quota
- B. Provisioned throughput units (PTUs)
- C. A batch endpoint
- D. A compute instance

**CS2-Q3.** Prompt changes must be reviewed and reversible. What should Fabrikam do?

- A. Version-control prompts in Git with pull-request review
- B. Edit prompts live in production chat
- C. Store prompts in screenshots
- D. Never change prompts

**CS2-Q4.** Releases must be gated on answer quality and safety. Which evaluation setup is correct?

- A. Automated evaluation workflow measuring groundedness/relevance/coherence/fluency plus risk-and-safety checks, integrated into CI
- B. One manual review at launch only
- C. Only measure latency
- D. Only measure token cost

**CS2-Q5.** The copilot sometimes invents details not in the docs. Which metric detects this, and which RAG levers help fix it?

- A. Groundedness; tune retrieval (similarity threshold, chunk size, hybrid search, better embeddings) and lower temperature
- B. Fluency; increase temperature
- C. Throughput; add PTUs
- D. Accuracy; delete the index

**CS2-Q6.** Finance wants to track and control spend. Which metric is primary, and where is it observed?

- A. Token consumption, via Foundry observability/monitoring
- B. Number of Git commits, via the portal
- C. Disk usage on user laptops
- D. Count of prompt variants

**CS2-Q7.** All traffic to Foundry and dependent resources must avoid the public internet. Which two configurations apply? Each correct answer presents part of the solution.

- A. Private endpoints
- B. Managed virtual network for the hub
- C. Anonymous public endpoint
- D. Owner role for everyone

**CS2-Q8.** To improve answer relevance on Fabrikam's domain-specific corpus, which action is most effective?

- A. Select/fine-tune a domain-appropriate embedding model and use hybrid search with re-ranking
- B. Increase temperature to maximum
- C. Reduce the corpus to one document
- D. Remove the system prompt

---

# Section 8 — Answer Key and Explanations

> Score yourself: **Section 1–5** = 80 questions. **Case studies** = 15 questions. Total 95 items. Target ≥80% overall, and ≥75% in every individual domain before sitting the real exam.

## Section 1 — MLOps infrastructure

**Q1: A, B, C.** Creating a Machine Learning workspace automatically provisions an associated **Storage account** (data/artifacts), **Key Vault** (secrets), and **Application Insights** (metrics/monitoring); a container registry is created on first image build. SQL Database and Cosmos DB are not workspace dependencies.

**Q2: B.** A **datastore** stores the connection information to an Azure storage service so data can be referenced without embedding credentials. A data asset points to specific data; a datastore holds the secure connection.

**Q3: C.** **AzureML Data Scientist** allows running experiments and creating assets but cannot create/delete the workspace or manage role assignments. Owner/Contributor are too broad; Reader is too narrow.

**Q4: B.** A **compute cluster (AmlCompute)** scales between min (often 0) and max nodes on demand for jobs. A compute instance is single-node and for interactive work.

**Q5: A and C.** Bicep is **declarative** (compiles to ARM JSON) and **idempotent**. B and D are false—Bicep is not imperative and can run in any CI/CD pipeline.

**Q6: B.** **OIDC workload identity federation** with a federated credential avoids storing long-lived secrets in GitHub. Storing secrets, SAS tokens, or workspace keys is less secure.

**Q7: B.** A **managed virtual network / private endpoint** restricts workspace access to a VNet. The other options don't control workspace network ingress.

**Q8: A.** A **component** is a reusable, versioned, self-contained step (code + interface + environment) shared across pipelines.

**Q9: B.** A **registry** shares models, components, and environments across multiple workspaces/regions. Datastores and compute images don't do cross-workspace asset sharing.

**Q10: B.** A **user-assigned managed identity** can be attached to multiple resources and managed independently. System-assigned identities are tied 1:1 to a single resource.

**Q11: B.** An **environment** defines the Docker base image plus conda/pip dependencies used to run jobs.

**Q12: A.** The **`az ml` CLI v2** with Azure CLI auth is the standard tool for scripted workspace operations in CI/CD.

**Q13: C.** A **trigger / `on:` event** (e.g., `push`, `pull_request`) defines when a GitHub Actions workflow runs.

**Q14: B.** Use **Git with branches and pull requests** integrated with the workspace for collaboration and traceability.

## Section 2 — ML model lifecycle and operations

**Q15: B.** **MLflow** is natively integrated for tracking params, metrics, and artifacts.

**Q16: B.** Enable **early termination/early stopping** to stop spending compute once the metric plateaus.

**Q17: B.** **Accuracy is misleading on imbalanced data**; prefer AUC-weighted or precision/recall-based metrics for rare-positive problems.

**Q18: A.** A **sweep job** automates hyperparameter tuning over a search space with early termination policies.

**Q19: C.** **Bayesian sampling** uses results from prior runs to focus on promising regions. Grid/random don't adapt.

**Q20: A.** Machine Learning supports **distributed training** (e.g., PyTorch DDP via the distribution config and `process_count_per_instance`).

**Q21: B.** A **pipeline job composed of components** gives repeatable, independently versioned, schedulable multi-step workflows.

**Q22: B.** Use the **studio Jobs view to compare logged MLflow metrics** across runs.

**Q23: B.** The **MLflow model format enables no-code deployment** because signature and dependencies are packaged with the model.

**Q24: A.** The **Responsible AI dashboard/scorecard** provides fairness assessment and feature importance/explanations.

**Q25: B.** **Archive** the model version to retain it for audit while keeping it out of new deployments.

**Q26: B.** A **managed online endpoint** serves low-latency synchronous, per-request predictions.

**Q27: B.** A **batch endpoint** handles large-volume scheduled scoring without per-request latency needs.

**Q28: B.** Configure a **traffic split** across deployments under one endpoint (e.g., 10%/90%) for canary validation.

**Q29: B.** **Shift endpoint traffic back to the previous deployment (blue/green)** for instant safe rollback.

**Q30: B.** **Inspect deployment/container logs** (`get-logs`) and check the scoring script and health probe first.

**Q31: A.** This is **data drift**—input feature distributions shifting away from training data over time.

**Q32: A.** Use a **data drift monitor with a threshold plus an alert/trigger that starts a retraining pipeline**.

**Q33: C.** For regression, monitor **RMSE/MAE**. Accuracy/precision/F1 are classification metrics.

**Q34: B.** Bundling the **feature retrieval spec prevents training/serving skew** by ensuring identical feature computation at inference.

**Q35: B.** Compare both models **on the same held-out evaluation dataset with the same primary metric** for a fair decision.

**Q36: B.** A **compute instance running notebooks** is best for interactive experimentation and exploration.

## Section 3 — GenAIOps infrastructure

**Q37: B.** A **hub provides shared config/security/connections**; **projects** are created under it for specific apps.

**Q38: B.** Use **managed identity and RBAC with Foundry connections**—no keys in code.

**Q39: A and B.** **Private endpoints** plus a **managed virtual network** keep traffic off the public internet. C and D do the opposite.

**Q40: A and B.** Both **Bicep** and **Azure CLI** are valid IaC approaches; manual portal clicks and prod-only edits are not.

**Q41: B.** **Provisioned throughput units (PTUs)** reserve dedicated capacity for predictable latency at high volume.

**Q42: B.** A **serverless API endpoint** offers pay-per-token consumption without managing compute.

**Q43: B.** **Managed compute deployment** gives dedicated GPU compute for models not offered as serverless APIs.

**Q44: B.** Select the **smallest/cheapest model that meets quality and latency requirements**, validated by evaluation.

**Q45: B.** **Version-control prompts in Git with reviews** for traceability and rollback.

**Q46: A.** Create **prompt variants and compare performance** on the same inputs.

**Q47: B.** Use **progressive/staged rollout with rollback**, mirroring safe deployment practice.

**Q48: A.** Back the connection with a **managed identity** so access is RBAC-governed and centrally rotated.

**Q49: B.** Apply **least-privilege RBAC with a scoped project-level role**.

**Q50: A.** Run **what-if/validation on `pull_request`, deploy on merge to main**.

**Q51: D.** The **client application's font** is irrelevant to choosing serverless vs managed compute.

**Q52: A.** **PTUs reserve dedicated model-processing capacity** for stable high-volume throughput.

**Q53: A.** **Prompt templates / prompt flow definitions** belong in the repo with app code. Never commit keys or PII.

**Q54: B.** **Create a connection in the project that references the Azure OpenAI resource** (cross-resource-group is fine).

## Section 4 — Quality assurance and observability

**Q55: B.** **Groundedness** measures whether answers are supported by the retrieved sources.

**Q56: A.** The standard AI quality metrics are **groundedness, relevance, coherence, fluency**.

**Q57: B.** **Risk and safety evaluations** detect harmful content (hate, violence, sexual, self-harm).

**Q58: A.** Prepare a **test dataset with data mapping** to the app's inputs/outputs.

**Q59: B.** Set up an **automated evaluation workflow integrated into CI** to gate releases.

**Q60: A.** **Relevance** measures whether the answer is pertinent to the question.

**Q61: A.** **Tracing** captures the steps/spans of a request for debugging slow paths.

**Q62: A, B, C.** **Latency, throughput, response time** are key operational metrics. Client disk fragmentation is irrelevant.

**Q63: A.** **Token consumption** is the primary LLM cost driver to track.

**Q64: B.** **Investigate retrieval quality/source data and re-tune RAG/prompts.** Adding PTUs doesn't fix groundedness.

**Q65: A and B.** **Detailed logging** and **tracing** enable debugging/replay. Disabling telemetry or removing the endpoint do not.

**Q66: A.** Add a **custom evaluation metric/evaluator** alongside built-in metrics.

## Section 5 — Optimize GenAI systems and model performance

**Q67: A and B.** Tune the **similarity threshold** and **chunk size/overlap** to improve retrieval precision. Temperature and screen resolution don't affect retrieval.

**Q68: A.** Combining keyword + vector search with re-ranking is **hybrid search**.

**Q69: A.** **Select/fine-tune a domain-appropriate embedding model** to improve domain retrieval.

**Q70: A.** Use **A/B testing with relevance metrics** for objective comparison.

**Q71: A.** **Chunk size is a tunable tradeoff**—too large adds noise, too small loses context.

**Q72: A.** Choose **fine-tuning when you need consistent style/format or specialized behavior** that prompting/RAG can't reliably deliver.

**Q73: A.** **Generate and curate synthetic data** to supplement scarce labeled examples.

**Q74: A.** This is **overfitting**; remedy with more/diverse data, regularization, and held-out validation.

**Q75: A.** **Version, evaluate, and promote the fine-tuned model through environments with rollback.**

**Q76: A and B.** **Training loss** and **validation loss/metric on held-out data** indicate learning progress (watch the gap for overfitting).

**Q77: A.** Lowering **temperature (and/or top-p)** reduces creative deviation/rephrasing.

**Q78: A.** Use **hybrid search followed by re-ranking** to balance recall and precision.

**Q79: A.** **Embeddings map text to vectors** so similar text is near in vector space, enabling similarity search.

**Q80: A.** Production-readiness is best supported by **evaluation on a representative held-out dataset meeting quality and safety thresholds**.

## Case Study 1 — Contoso Manufacturing

**CS1-Q1: B** (Bicep + GitHub Actions for identical, re-creatable environments).
**CS1-Q2: B** (Batch endpoint for nightly millions-of-records scoring).
**CS1-Q3: B** (Managed online endpoint for sub-second single-record predictions).
**CS1-Q4: A** (MLflow tracking for comparison and reproducibility).
**CS1-Q5: A** (Data drift monitor with thresholds wired to a retraining trigger).
**CS1-Q6: A** (Blue/green with traffic split and rollback).
**CS1-Q7: A** (Responsible AI dashboard for fairness and feature importance).

## Case Study 2 — Fabrikam Support Copilot

**CS2-Q1: A** (Managed identity + RBAC + Foundry connections; no keys in code).
**CS2-Q2: B** (PTUs for predictable latency/reserved capacity at peak).
**CS2-Q3: A** (Version-control prompts in Git with PR review).
**CS2-Q4: A** (Automated quality + risk/safety evaluation gating CI).
**CS2-Q5: A** (Groundedness detects fabrication; fix via retrieval tuning + lower temperature).
**CS2-Q6: A** (Token consumption via Foundry observability).
**CS2-Q7: A and B** (Private endpoints + managed VNet).
**CS2-Q8: A** (Domain embedding model + hybrid search with re-ranking).

---

# Section 9 — Last-week revision checklist

Use this to triage the final days. Tick each only when you can explain it out loud.

**Domain 1 — MLOps infra (15–20%)**
- [ ] Workspace dependent resources (Storage, Key Vault, App Insights, Container Registry)
- [ ] Datastores vs data assets; compute instance vs compute cluster vs serverless Spark
- [ ] RBAC roles (AzureML Data Scientist, Reader, Contributor) and least privilege
- [ ] Managed identities (system- vs user-assigned)
- [ ] Environments and components; registries for cross-workspace sharing
- [ ] Bicep (declarative, idempotent) + `az ml` CLI + GitHub Actions + OIDC federation
- [ ] Private networking / managed VNet for the workspace

**Domain 2 — Model lifecycle (25–30%, biggest weight)**
- [ ] MLflow tracking and run comparison
- [ ] AutoML (primary metric choice, featurization, early stopping, child jobs)
- [ ] Sweep jobs (grid/random/Bayesian sampling, early termination)
- [ ] Distributed training; pipeline jobs from components
- [ ] MLflow model registration, versioning, archiving; feature retrieval spec
- [ ] Responsible AI evaluation
- [ ] Online vs batch endpoints; traffic split, blue/green, rollback; endpoint troubleshooting
- [ ] Data drift detection + retraining/alert triggers; regression vs classification metrics

**Domain 3 — GenAIOps infra (20–25%)**
- [ ] Foundry hub vs project; connections; managed identity + RBAC
- [ ] Private endpoints + managed VNet; Bicep/CLI deployment
- [ ] Serverless API vs managed compute vs PTUs; model selection criteria
- [ ] Prompt versioning in Git; prompt variants/comparison; progressive rollout

**Domain 4 — Quality & observability (10–15%)**
- [ ] AI quality metrics: groundedness, relevance, coherence, fluency
- [ ] Risk & safety (content harm) evaluations; test datasets + data mapping
- [ ] Automated evaluation in CI; custom evaluators
- [ ] Continuous monitoring; latency/throughput/response time; token cost; logging + tracing

**Domain 5 — Optimization (10–15%)**
- [ ] RAG retrieval tuning: similarity threshold, chunk size/overlap, hybrid search, re-ranking
- [ ] Embedding model selection/fine-tuning; A/B testing with relevance metrics
- [ ] Fine-tuning vs RAG decision; synthetic data; overfitting
- [ ] Fine-tuned model lifecycle (version, evaluate, promote, rollback); training vs validation loss

**Exam-day reminders**
- 700/1000 to pass; read case-study requirements carefully and match each requirement to a feature.
- Watch for "each correct answer presents a complete solution" (each option works alone) vs "part of the solution" (multi-select).
- Prefer **least privilege**, **IaC over manual**, **managed identity over keys**, and **evaluate before promote** — these themes recur across the whole exam.

---

# SET B — Fresh question bank (Q81–Q164)

> No answer overlap with Set A. Heavier on hands-on details the AI-300T00 trainer demonstrated (command jobs, MLflow autolog, sweep early-termination policies, pipeline YAML, GitHub Actions workflows, scoring scripts, Foundry agents/tools, tracing, prompt variants, automated evaluators, quotas). Answer key: **Section 15**.

## Section 10 — Design and implement an MLOps infrastructure (Set B)

**Q81.** You author a Bicep template that, when deployed, creates a Machine Learning workspace plus its dependent resources. You run the same template again with no changes. What happens?

- A. A second duplicate workspace is created
- B. The deployment is idempotent and converges to the same declared state with no duplicate resources
- C. The deployment fails because Bicep cannot run twice
- D. All existing resources are deleted and recreated from scratch

**Q82.** A GitHub Actions workflow must run `az ml` commands against a workspace. The workflow uses an Azure login action with OIDC. Which Azure object must you configure with a **federated credential** that trusts the GitHub repo?

- A. A storage account
- B. A Microsoft Entra ID app registration / service principal
- C. A compute cluster
- D. A managed online endpoint

**Q83.** You want data scientists to read data from a storage account through a datastore, but the **credentials must never be visible** to them. Which datastore authentication approach best meets this?

- A. Account key stored and shown in the notebook
- B. Credential-based datastore using a key vault-backed secret, or identity-based access via the workspace/compute managed identity
- C. Anonymous public access
- D. Hard-coded SAS token in each script

**Q84.** Match the need to the asset: "a packaged, versioned, reusable training step that exposes typed inputs and outputs." Which asset is it?

- A. Data asset
- B. Environment
- C. Component
- D. Endpoint

**Q85.** Which statement correctly distinguishes a **compute instance** from a **compute cluster**?

- A. A compute instance is a single-node, personal, interactive box; a compute cluster is multi-node and scales for jobs
- B. They are identical
- C. A compute instance auto-scales to many nodes; a cluster is single-node
- D. A cluster is only for notebooks

**Q86.** You need to publish a curated training environment so all jobs use the exact same Python/conda dependencies. After defining it, what should you do so it is reusable and versioned?

- A. Register the environment in the workspace (or a registry) and reference it by name:version
- B. Paste dependencies into each script
- C. Install packages manually on every node each run
- D. Use a different environment for every run intentionally

**Q87.** Your security team requires that the Machine Learning workspace have **no public endpoint** and be reachable only through the corporate network. Which design meets this? Each correct answer presents part of the solution.

- A. Configure a private endpoint for the workspace
- B. Enable the workspace managed virtual network and set public network access to disabled
- C. Assign every user the Owner role
- D. Expose the workspace with a public IP and key auth

**Q88.** In a `uri_file` vs `uri_folder` vs `mltable` decision, which data asset type should you choose when you need to reference a **schema/parsing definition over one or more files** (e.g., for AutoML or pandas loading)?

- A. `uri_file`
- B. `uri_folder`
- C. `mltable`
- D. `secret`

**Q89.** A team wants the **same** workload identity used by both a compute cluster and an online endpoint, centrally managed. Which identity should they create?

- A. System-assigned managed identity on each resource
- B. A single user-assigned managed identity assigned to both
- C. A personal user account
- D. A SAS token

**Q90.** Which Azure CLI extension provides the v2 commands (`az ml job create`, `az ml model create`, `az ml online-endpoint create`)?

- A. `az aks`
- B. `az ml`
- C. `az storage`
- D. `az network`

**Q91.** You want a pull request to **validate** infrastructure changes without applying them, and only apply on merge to `main`. Which two GitHub Actions practices support this? Each correct answer presents part of the solution.

- A. Run `az deployment ... what-if` (or Bicep build/validate) on `pull_request`
- B. Gate the apply step behind a push/merge to `main` (and optionally an environment approval)
- C. Apply directly to production on every commit
- D. Disable the workflow entirely

**Q92.** What is the primary purpose of storing a workspace's secrets in the associated **Azure Key Vault**?

- A. To store training data
- B. To securely hold connection strings, keys, and credentials referenced by the workspace
- C. To serve model predictions
- D. To run notebooks

**Q93.** You must restrict which users can deploy to production endpoints while letting all data scientists train models. Which approach aligns with least privilege?

- A. Give everyone Owner
- B. Use scoped RBAC: data scientists get a training-capable role; a smaller group gets deployment permissions
- C. Disable RBAC
- D. Share one admin account

**Q94.** Application Insights is provisioned with the workspace primarily to support which capability?

- A. Storing model files
- B. Telemetry, logging, and monitoring of jobs and deployed endpoints
- C. Hyperparameter sampling
- D. Datastore authentication

## Section 11 — Implement ML model lifecycle and operations (Set B)

**Q95.** You run training in a notebook and call `mlflow.autolog()` before fitting a scikit-learn model. What does this do?

- A. Automatically logs parameters, metrics, and the model without manual log calls
- B. Deletes prior runs
- C. Deploys the model to an endpoint
- D. Creates a datastore

**Q96.** You submit a training script to a compute cluster using a **command job**. Which elements must the command job specify? Each correct answer presents part of the solution.

- A. The command to run (e.g., `python train.py --reg 0.1`)
- B. The environment
- C. The compute target
- D. The exam pass score

**Q97.** In AutoML for classification, you enable featurization. Which task does featurization perform automatically?

- A. Handling missing values, encoding categoricals, and scaling/normalizing features
- B. Deploying the model
- C. Creating a private endpoint
- D. Writing the scoring script

**Q98.** You configure an AutoML job and set both a **timeout** and **max trials**, and enable **early termination**. What is the combined effect?

- A. It bounds cost/time by limiting how long and how many models are tried and abandoning unpromising runs
- B. It guarantees the global optimal model
- C. It disables metric logging
- D. It forces grid search

**Q99.** In a sweep job you choose the **Bandit** early-termination policy with a slack factor. What does it do?

- A. Terminates runs whose primary metric falls outside a slack range of the best run so far
- B. Doubles the number of trials
- C. Disables sampling
- D. Increases the learning rate automatically

**Q100.** Which sweep early-termination policy stops runs that fall below the **median** of running averages of all runs?

- A. Median stopping policy
- B. Bandit policy
- C. Truncation selection policy
- D. No policy

**Q101.** You want a sweep job to try learning_rate sampled from a uniform range and batch_size from a fixed choice set, exploring randomly across a large space. Which sampling method fits best?

- A. Random sampling
- B. Grid sampling
- C. Bayesian sampling without a search space
- D. No sampling

**Q102.** A pipeline has three components: prep, train, evaluate. The `train` step must receive the output of `prep`. How is this wired in a pipeline job?

- A. By passing the prep component's output as the input to the train component
- B. By emailing the file between steps
- C. By hard-coding a local path
- D. Steps cannot share data

**Q103.** You register a model produced by an MLflow run. Which two artifacts are typically captured to enable reproducibility and no-code deployment? Each correct answer presents part of the solution.

- A. The model signature (input/output schema)
- B. The conda/pip dependencies
- C. The trainer's laptop wallpaper
- D. The Azure billing invoice

**Q104.** After comparing 20 sweep trials in the studio, you select the best trial by the primary metric. What is the next lifecycle step to make it usable in production?

- A. Register the model (and version it)
- B. Delete the workspace
- C. Disable MLflow
- D. Convert it to a datastore

**Q105.** You deploy an **MLflow model** to a managed online endpoint. Why might you NOT need to author a custom scoring script?

- A. Because the MLflow flavor provides the inference logic and dependencies automatically
- B. Because online endpoints never run code
- C. Because scoring scripts are illegal
- D. Because the model is not used at inference

**Q106.** For a **custom (non-MLflow) model** deployment to an online endpoint, which two files do you typically provide? Each correct answer presents part of the solution.

- A. A scoring script with `init()` and `run()` functions
- B. An environment specifying dependencies
- C. A billing report
- D. A drift threshold

**Q107.** In the scoring script, what is the purpose of the `init()` function?

- A. It runs once when the deployment starts, typically to load the model into memory
- B. It runs on every request to load the model fresh each time
- C. It deletes the endpoint
- D. It sends alerts

**Q108.** In the scoring script, what is the purpose of the `run(data)` function?

- A. It executes for each scoring request, performs prediction, and returns the result
- B. It runs only at deployment startup
- C. It provisions compute
- D. It configures RBAC

**Q109.** You deploy a batch endpoint to score a large dataset. Which compute is appropriate and how is output typically handled?

- A. A compute cluster that scales out; results written to a datastore/output location
- B. A single compute instance returning each row synchronously to the caller
- C. A serverless API endpoint per record
- D. A Key Vault

**Q110.** Two deployments (blue and green) sit under one online endpoint. You set traffic to blue=100, green=0, then gradually shift to green. What is this pattern called?

- A. Blue/green (progressive) deployment
- B. Data drift
- C. Featurization
- D. Bayesian sampling

**Q111.** An online endpoint returns errors after deployment. You run the get-logs command. Which two common root causes do logs help you find? Each correct answer presents part of the solution.

- A. A scoring script exception (e.g., model path wrong)
- B. Missing dependency in the environment
- C. The pass mark of the exam
- D. The color of the dashboard

**Q112.** You must compute data drift between the training baseline and recent production inputs. Which comparison does a drift monitor make?

- A. Statistical comparison of feature distributions between baseline and current data
- B. Comparison of two source-code branches
- C. Comparison of token counts
- D. Comparison of RBAC roles

**Q113.** A production classification model's monitored performance degrades and drift exceeds threshold. Which automated response best fits MLOps?

- A. Trigger a retraining pipeline and/or fire an alert to the team
- B. Delete all logs
- C. Increase the model file size
- D. Switch to a batch endpoint with no retraining

**Q114.** Which statement about model **registration and versioning** is correct?

- A. Registering a model with an existing name creates a new version, preserving prior versions
- B. Registering overwrites and deletes prior versions
- C. Models cannot be versioned
- D. Versions are random and unordered

**Q115.** You evaluate a model with the Responsible AI dashboard. Which two insights does it provide? Each correct answer presents part of the solution.

- A. Fairness/disparity across cohorts
- B. Feature importance / explanations
- C. The Azure region price list
- D. The Git commit message

**Q116.** You want to keep a model version for audit/compliance but stop it appearing as a candidate for new deployments. What do you do?

- A. Archive the version
- B. Delete the workspace
- C. Rename the storage account
- D. Remove MLflow

**Q117.** Which primary metric is appropriate for an AutoML **regression** task?

- A. Normalized RMSE or R²
- B. Accuracy
- C. AUC weighted
- D. Precision

**Q118.** You need distributed training across 4 GPUs on 2 nodes for a deep learning model. Which configuration concept applies?

- A. Set a distribution (e.g., PyTorch) with process_count_per_instance and instance_count on a GPU cluster
- B. Use a single CPU compute instance
- C. Use a batch endpoint
- D. Use AutoML featurization only

**Q119.** You want every training run's metrics centrally comparable in the studio. Which logging approach is recommended?

- A. Log metrics with MLflow (`mlflow.log_metric`) or autolog
- B. Print to stdout only
- C. Save metrics to the local laptop
- D. Don't log metrics

**Q120.** A model is promoted from a sweep job's best trial. To guard against picking a model that only looks good due to the metric on its own split, what should you do before promotion?

- A. Evaluate the candidate on a common held-out test set
- B. Promote whichever trial finished first
- C. Promote the largest model
- D. Skip evaluation

## Section 12 — Design and implement a GenAIOps infrastructure (Set B)

**Q121.** In Microsoft Foundry, you create a project to build a support agent. Which statement about projects and the hub is correct?

- A. The project inherits shared connections, security, and compute config from its hub
- B. Each project needs its own separate hub with no sharing
- C. Projects cannot use connections
- D. Hubs are created automatically inside projects

**Q122.** Your agent uses GPT-4.1 connected to built-in tools such as **code interpreter** and **file search**. What does connecting tools to the model enable?

- A. The model can call the tool to perform actions/retrieve data and use the returned values in its response
- B. The model is replaced by the tool
- C. Tools disable the model
- D. Tools only change billing

**Q123.** You must connect a Foundry project to Azure AI Search and Azure OpenAI without storing keys in code. What should you configure?

- A. Foundry connections backed by managed identity + RBAC
- B. Keys pasted into the system prompt
- C. Anonymous access
- D. A SAS token in the agent name

**Q124.** A high-volume production chat workload requires predictable latency and reserved capacity. Which deployment option should you choose?

- A. Provisioned throughput units (PTUs)
- B. Pay-as-you-go serverless with shared quota
- C. A batch endpoint
- D. A compute instance notebook

**Q125.** A team wants to consume a model on a pay-per-token basis with no infrastructure to manage. Which option fits?

- A. Serverless API endpoint
- B. Managed compute with dedicated VMs
- C. PTUs only
- D. A datastore

**Q126.** You hit a **quota limitation error** when deploying a model in Foundry. What are two appropriate remedies? Each correct answer presents part of the solution.

- A. Request a quota increase for the model/region
- B. Choose a different region or a smaller deployment within available quota
- C. Delete the Foundry hub permanently
- D. Disable evaluation

**Q127.** You want to manage prompts the same way as code, with branches, reviews, and rollback. Where should prompts live?

- A. In a Git repository, versioned alongside the app
- B. Only in the chat playground
- C. In screenshots
- D. In an email thread

**Q128.** You create a **prompt variant** on a new Git branch and want to know if it outperforms the baseline. What should you do?

- A. Evaluate both variants on the same test data and compare metrics
- B. Merge it without testing
- C. Delete the baseline
- D. Pick the longer prompt

**Q129.** Which two are valid IaC tools for deploying Foundry infrastructure repeatably? Each correct answer presents a complete solution.

- A. Bicep
- B. Azure CLI
- C. Manual portal clicks
- D. Editing prod by hand

**Q130.** You must select a foundation model for a task. Which factors should drive the choice? Each correct answer presents part of the solution.

- A. Required quality on the task (validated by evaluation)
- B. Latency and cost constraints
- C. Context window and modality needs
- D. The developer's favorite color

**Q131.** You deploy an open-weight model that is not available as a serverless API and needs dedicated GPUs you control. Which option fits?

- A. Managed compute deployment
- B. Serverless API endpoint
- C. A prompt variant
- D. A datastore

**Q132.** Which statement about RBAC and managed identity in Foundry is correct?

- A. Managed identity lets resources authenticate without secrets; RBAC grants least-privilege access to those identities
- B. Managed identity requires a password in code
- C. RBAC disables managed identity
- D. They cannot be used together

**Q133.** You want network isolation so Foundry and its dependencies aren't reachable from the public internet. Which two configurations apply? Each correct answer presents part of the solution.

- A. Managed virtual network for the hub
- B. Private endpoints on dependent resources
- C. Public anonymous endpoints
- D. Owner role for all users

**Q134.** A new model version must be introduced to production gradually with the ability to revert. Which strategy applies?

- A. Progressive rollout with rollback capability
- B. Instant full replacement, no test
- C. Delete old version first
- D. Deploy only to a laptop

**Q135.** You connect a Foundry project to an Azure OpenAI deployment that lives in a different resource group. What mechanism do you use?

- A. A connection referencing the external Azure OpenAI resource
- B. Copy the weights into the project
- C. Recreate the model
- D. Put the key in the prompt

**Q136.** Which artifact, stored in source control, ensures prompt changes flow through CI review like code?

- A. Prompt template / prompt flow definition files
- B. Model weights binary
- C. The subscription key
- D. Customer PII

## Section 13 — Generative AI quality assurance and observability (Set B)

**Q137.** A RAG agent answers from connected documents. Which metric measures how well the answer is supported by those documents?

- A. Groundedness
- B. Fluency
- C. Latency
- D. Token count

**Q138.** You configure an evaluation with four built-in AI quality metrics. Which set is standard?

- A. Groundedness, relevance, coherence, fluency
- B. Precision, recall, RMSE, MAE
- C. CPU, RAM, disk, net
- D. Cost, latency, drift, RBAC

**Q139.** You must run **manual evaluation** today and **automated evaluation** later. Which statement contrasts them correctly?

- A. Manual evaluation has a human review responses; automated evaluation uses evaluators/metrics to score at scale, suitable for CI
- B. They are identical
- C. Manual evaluation runs in CI; automated needs a human for each item
- D. Automated evaluation cannot use built-in metrics

**Q140.** You want to detect harmful content (hate, sexual, violence, self-harm) in model outputs. Which evaluation category applies?

- A. Risk and safety evaluations
- B. AI quality metrics only
- C. Token cost metrics
- D. Data drift

**Q141.** To evaluate at scale you provide a dataset of inputs and expected references, mapped to the agent's input/output fields. What is this called?

- A. Test dataset with data mapping
- B. A datastore
- C. A PTU plan
- D. A private endpoint

**Q142.** You want a record of each request's steps (retrieval, tool calls, generation) to debug a slow or wrong answer. Which capability provides this?

- A. Tracing (spans for each step)
- B. A model registry
- C. A sweep job
- D. A datastore

**Q143.** Which three operational metrics should you monitor for a production GenAI endpoint? Each correct answer presents part of the solution.

- A. Latency
- B. Throughput
- C. Response time
- D. Laptop battery level

**Q144.** Finance needs to forecast GenAI spend. Which metric is the main cost driver?

- A. Token consumption (input + output tokens)
- B. Number of branches
- C. Number of datastores
- D. Number of evaluators

**Q145.** Continuous monitoring shows groundedness declining over two weeks. What is the best first action?

- A. Investigate retrieval quality and source documents; re-tune RAG/prompts
- B. Add PTUs
- C. Delete the test dataset
- D. Ignore it

**Q146.** You add a business rule check (each answer must include a safety disclaimer) to your evaluation suite. How?

- A. Implement a custom evaluator alongside built-in metrics
- B. It cannot be done
- C. Change the model architecture
- D. Remove all built-in metrics

**Q147.** During batch testing of an agent you log traces for each interaction. What benefit does this provide?

- A. You can inspect inputs, intermediate steps, and outputs to diagnose failures
- B. It increases token cost only with no benefit
- C. It deletes the agent
- D. It disables evaluation

**Q148.** Which metric answers "Is the response logically consistent and well-structured?"

- A. Coherence
- B. Groundedness
- C. Latency
- D. Throughput

**Q149.** You set quality thresholds (e.g., groundedness ≥ 4) that a release must meet. Where is this best enforced?

- A. In an automated evaluation step in the CI pipeline that gates deployment
- B. By manual memory
- C. In the billing portal
- D. In a datastore

**Q150.** Which statement about token cost monitoring is correct?

- A. Both prompt (input) and completion (output) tokens contribute to cost and should be tracked
- B. Only output tokens cost anything
- C. Tokens are free
- D. Token count is unrelated to cost

## Section 14 — Optimize generative AI systems and model performance (Set B)

**Q151.** Your RAG app retrieves too many loosely related chunks. Which two levers most directly improve precision? Each correct answer presents part of the solution.

- A. Raise the similarity threshold
- B. Reduce/optimize chunk size and overlap
- C. Increase temperature
- D. Change client screen resolution

**Q152.** You combine vector search with keyword (BM25) and then re-rank. What is this called and what does re-ranking add?

- A. Hybrid search; re-ranking reorders candidates by relevance to improve top-k precision
- B. Fine-tuning; re-ranking trains the model
- C. Quantization; re-ranking compresses vectors
- D. Drift; re-ranking detects distribution change

**Q153.** Generic embeddings retrieve poorly on a specialized medical corpus. Which action most directly helps?

- A. Select or fine-tune a domain-appropriate embedding model
- B. Increase temperature
- C. Remove the retrieval index
- D. Reduce PTUs

**Q154.** You must objectively choose between two retrieval configs. Which method gives statistically meaningful comparison?

- A. A/B testing with relevance metrics over many queries
- B. One query gut-check
- C. Picking the prettier config
- D. Disabling evaluation

**Q155.** When is **fine-tuning** preferable to RAG?

- A. When you need consistent style/format/specialized behavior that prompting and retrieval can't reliably produce
- B. Whenever any documents exist
- C. To save cost on one query
- D. Never

**Q156.** You lack labeled examples for a niche classification-style generation task. Which technique helps create training data?

- A. Generate and curate synthetic data (then review for quality)
- B. Delete data
- C. Set temperature to 0 permanently
- D. Increase chunk overlap

**Q157.** A fine-tuned model scores high on training data but poorly on new inputs. What is happening and what's the fix?

- A. Overfitting; add more/diverse data, regularize, and validate on held-out data
- B. Underfitting; remove all data
- C. Drift in a datastore
- D. The index is too large

**Q158.** Which two signals indicate a fine-tuning run is progressing well? Each correct answer presents part of the solution.

- A. Decreasing training loss
- B. Decreasing/stable validation loss on held-out data
- C. More GitHub stars
- D. Higher client battery

**Q159.** A grounded RAG answer still occasionally rephrases facts loosely. Which generation parameter should you lower to reduce deviation?

- A. Temperature (and/or top-p)
- B. Chunk overlap
- C. PTU count
- D. Number of datastores

**Q160.** To avoid missing relevant documents (improve recall) while keeping precision via reordering, which strategy fits?

- A. Hybrid search plus a re-ranking step
- B. Index only one document
- C. Disable vector search
- D. Max temperature

**Q161.** Which statement about embeddings in RAG is correct?

- A. Embeddings map text to vectors so similar meanings are nearby, enabling semantic similarity search
- B. Embeddings are the final user-facing answers
- C. Embeddings only affect billing
- D. Embeddings remove the need for an index

**Q162.** You manage a fine-tuned model from dev to prod. Which practice aligns with GenAIOps?

- A. Version it, evaluate against held-out data and safety thresholds, promote through environments with rollback
- B. Deploy to prod with no evaluation
- C. Overwrite one copy each time
- D. Don't track its training data

**Q163.** Chunk size is set very large. What is the likely retrieval-quality effect?

- A. Each retrieved chunk carries more irrelevant text, diluting the signal the model sees
- B. Retrieval always improves
- C. No effect at all
- D. It removes the need for embeddings

**Q164.** You decide a fine-tuned model is production-ready. Which evidence best supports that decision?

- A. Evaluation on a representative held-out dataset meeting defined quality and safety thresholds
- B. The job finished without errors
- C. It was cheap to train
- D. The file is small

---

# Case Study 3 — Adventure Works End-to-End AIOps (mixed domains)

> **Scenario.** Adventure Works runs both a traditional ML model (demand forecasting) and a generative AI agent (a travel-planning assistant in Foundry). A single platform team must operationalize both. Requirements: all infrastructure as code in Bicep deployed via GitHub Actions with OIDC (no stored secrets); experiment tracking and reproducibility; AutoML to find a baseline forecaster then a sweep job to tune it; a training pipeline of reusable components; real-time online endpoint for the forecaster with blue/green rollout; data drift monitoring with automated retraining; the Foundry agent uses RAG over a knowledge base with tools, PTUs at peak, prompt variants version-controlled, automated quality+safety evaluation gating releases, and observability for latency and token cost.

**CS3-Q1.** The team must deploy identical infra to dev/test/prod with no stored service-principal secret in GitHub. Which combination meets this?

- A. Bicep + GitHub Actions authenticating via OIDC workload identity federation
- B. Manual portal clicks documented in a wiki
- C. A client secret stored in a repo variable
- D. Copy resources between environments by hand

**CS3-Q2.** For the demand forecaster, the team first wants a strong baseline with minimal manual modeling, then fine-grained tuning. Which sequence fits?

- A. AutoML to find a baseline model, then a sweep job to tune hyperparameters
- B. A sweep job only, never AutoML
- C. Manual single training run only
- D. Skip training; deploy a random model

**CS3-Q3.** The training workflow (prep → train → evaluate → register) must be reusable and independently versioned. What should they build?

- A. A pipeline job composed of registered components
- B. One giant notebook cell
- C. A batch endpoint
- D. A datastore

**CS3-Q4.** The forecaster serves real-time predictions; a new version must be validated on a slice of live traffic before full cutover. Which approach?

- A. Blue/green deployment with traffic split and rollback on one online endpoint
- B. Two endpoints with manual DNS edits
- C. A batch endpoint
- D. Delete the old deployment first

**CS3-Q5.** Forecast inputs shift seasonally; the team needs automatic detection and retraining. What should they configure?

- A. A data drift monitor with thresholds wired to a retraining pipeline trigger/alert
- B. A manual annual review
- C. A larger compute instance
- D. A second subscription

**CS3-Q6.** The travel agent must keep predictable latency during peak booking season. Which model deployment option fits?

- A. Provisioned throughput units (PTUs)
- B. Pay-as-you-go shared quota only
- C. A batch endpoint
- D. A compute instance

**CS3-Q7.** The agent sometimes invents attractions not in the knowledge base. Which metric flags this and which fixes apply? Each correct answer presents part of the solution.

- A. Groundedness flags it
- B. Tune retrieval (threshold, chunk size, hybrid search, better embeddings) and lower temperature
- C. Increase temperature to be more creative
- D. Delete the knowledge base

**CS3-Q8.** Releases of the agent must be blocked unless quality and safety thresholds are met. What should the team implement?

- A. An automated evaluation workflow (groundedness/relevance/coherence/fluency + risk-and-safety) gating the CI/CD release
- B. A single manual check at launch
- C. Only latency monitoring
- D. No evaluation

**CS3-Q9.** Prompt changes for the agent must be reviewed and reversible, with variants compared before shipping. What should they do?

- A. Version prompts in Git, create variants on branches, evaluate and compare before merge
- B. Edit prompts live in production
- C. Store prompts in screenshots
- D. Never change prompts

**CS3-Q10.** Finance needs ongoing visibility into agent spend and performance. Which two should observability track? Each correct answer presents part of the solution.

- A. Token consumption (input + output)
- B. Latency / response time
- C. Number of Git branches
- D. Datastore color

---

# Section 15 — Set B Answer Key and Explanations

> Set B = Q81–Q164 (84 questions) + Case Study 3 (10 questions). Combine with Set A for ~175 total practice items. Target ≥80% overall and ≥75% per domain.

## Section 10 — MLOps infrastructure (Set B)

**Q81: B.** Bicep is idempotent; re-running converges to the declared state without duplicates.
**Q82: B.** Configure a federated credential on a **Microsoft Entra app registration / service principal** that trusts the GitHub repo (OIDC).
**Q83: B.** Use a **credential-based datastore backed by a Key Vault secret, or identity-based access** via managed identity—credentials stay hidden.
**Q84: C.** A **component** is the packaged, versioned, reusable step with typed inputs/outputs.
**Q85: A.** Compute instance = single-node interactive; compute cluster = multi-node scalable for jobs.
**Q86: A.** **Register the environment** and reference it by `name:version` for reuse and reproducibility.
**Q87: A and B.** **Private endpoint** plus **managed VNet with public access disabled** removes the public endpoint.
**Q88: C.** **`mltable`** carries a schema/parsing definition over one or more files (used by AutoML and pandas loading).
**Q89: B.** A single **user-assigned managed identity** can be shared and centrally managed across resources.
**Q90: B.** The **`az ml`** extension provides v2 CLI commands.
**Q91: A and B.** Run **what-if/validate on `pull_request`** and **gate apply behind merge to main** (optionally with environment approval).
**Q92: B.** Key Vault **securely holds secrets/keys/connection strings** referenced by the workspace.
**Q93: B.** Use **scoped RBAC**—broad training rights for data scientists, deployment rights for a smaller group.
**Q94: B.** Application Insights supports **telemetry/logging/monitoring** of jobs and endpoints.

## Section 11 — ML lifecycle (Set B)

**Q95: A.** `mlflow.autolog()` **auto-logs params, metrics, and the model** without manual calls.
**Q96: A, B, C.** A command job specifies the **command**, **environment**, and **compute**. (The exam pass score is irrelevant.)
**Q97: A.** Featurization **handles missing values, encodes categoricals, and scales features** automatically.
**Q98: A.** Timeout + max trials + early termination **bound cost/time** and abandon unpromising runs (no global-optimum guarantee).
**Q99: A.** The **Bandit policy** terminates runs whose metric falls outside a slack factor/amount of the best run.
**Q100: A.** The **Median stopping policy** stops runs below the median of running averages.
**Q101: A.** **Random sampling** explores a large mixed space (uniform + choice) efficiently.
**Q102: A.** Wire the **prep component's output as the train component's input** in the pipeline.
**Q103: A and B.** MLflow captures the **signature** and **dependencies**, enabling reproducibility and no-code deployment.
**Q104: A.** **Register (and version) the model** to make the best trial usable in production.
**Q105: A.** The **MLflow flavor provides inference logic + dependencies**, so no custom scoring script is needed.
**Q106: A and B.** Custom deployments need a **scoring script (`init`/`run`)** and an **environment**.
**Q107: A.** `init()` runs **once at startup**, typically to load the model.
**Q108: A.** `run(data)` executes **per request** to predict and return results.
**Q109: A.** Batch endpoints use a **compute cluster that scales out** and write **results to a datastore/output location**.
**Q110: A.** Gradually shifting traffic from blue to green is **blue/green (progressive) deployment**.
**Q111: A and B.** Logs reveal **scoring-script exceptions** and **missing environment dependencies**.
**Q112: A.** Drift monitors do a **statistical comparison of feature distributions** (baseline vs current).
**Q113: A.** **Trigger retraining and/or alert** the team when drift/perf thresholds are exceeded.
**Q114: A.** Registering with an existing name **creates a new version and preserves prior versions**.
**Q115: A and B.** The RAI dashboard shows **fairness/disparity** and **feature importance/explanations**.
**Q116: A.** **Archive** the version to retain it for audit while excluding it from new deployments.
**Q117: A.** For regression, use **Normalized RMSE or R²**.
**Q118: A.** Use a **distribution config (e.g., PyTorch) with process_count_per_instance and instance_count on a GPU cluster**.
**Q119: A.** **Log with MLflow** so metrics are centrally comparable.
**Q120: A.** **Evaluate the candidate on a common held-out test set** before promotion.

## Section 12 — GenAIOps infrastructure (Set B)

**Q121: A.** A project **inherits shared connections/security/compute config from its hub**.
**Q122: A.** Connected tools let the model **call them and use returned values** in its response (agentic behavior).
**Q123: A.** Use **Foundry connections backed by managed identity + RBAC**.
**Q124: A.** **PTUs** give reserved capacity and predictable latency at high volume.
**Q125: A.** A **serverless API endpoint** is pay-per-token with no infra to manage.
**Q126: A and B.** **Request a quota increase** or **use a different region/smaller deployment** within quota.
**Q127: A.** Keep prompts in a **Git repository** versioned with the app.
**Q128: A.** **Evaluate both variants on the same test data and compare metrics.**
**Q129: A and B.** **Bicep** and **Azure CLI** are valid IaC tools.
**Q130: A, B, C.** Drive model choice by **quality, latency/cost, and context window/modality** (not favorite color).
**Q131: A.** **Managed compute deployment** gives dedicated GPUs for non-serverless models.
**Q132: A.** **Managed identity authenticates without secrets; RBAC grants least privilege** to those identities.
**Q133: A and B.** **Managed VNet** + **private endpoints** isolate from the public internet.
**Q134: A.** **Progressive rollout with rollback** introduces a new version safely.
**Q135: A.** Use a **connection referencing the external Azure OpenAI resource** (cross-RG is fine).
**Q136: A.** Store **prompt template / prompt flow definition files** in source control.

## Section 13 — Quality & observability (Set B)

**Q137: A.** **Groundedness** measures support by source documents.
**Q138: A.** Standard AI quality metrics: **groundedness, relevance, coherence, fluency**.
**Q139: A.** **Manual = human review; automated = evaluators/metrics at scale, CI-suitable.**
**Q140: A.** **Risk and safety evaluations** detect harmful content categories.
**Q141: A.** A **test dataset with data mapping** maps inputs/references to the agent's fields.
**Q142: A.** **Tracing** records spans for each request step (retrieval/tool/generation).
**Q143: A, B, C.** Operational metrics: **latency, throughput, response time**.
**Q144: A.** **Token consumption (input + output)** is the main cost driver.
**Q145: A.** **Investigate retrieval/source data and re-tune RAG/prompts**; PTUs don't fix groundedness.
**Q146: A.** Implement a **custom evaluator** alongside built-in metrics.
**Q147: A.** Traces let you **inspect inputs, intermediate steps, and outputs** to diagnose failures.
**Q148: A.** **Coherence** = logical consistency/structure.
**Q149: A.** Enforce thresholds in an **automated evaluation step that gates deployment** in CI.
**Q150: A.** **Both input and output tokens** contribute to cost and should be tracked.

## Section 14 — Optimization (Set B)

**Q151: A and B.** Raise the **similarity threshold** and **optimize chunk size/overlap** to improve precision.
**Q152: A.** **Hybrid search**; re-ranking **reorders candidates by relevance** to improve top-k precision.
**Q153: A.** **Select/fine-tune a domain embedding model**.
**Q154: A.** **A/B testing with relevance metrics over many queries** gives meaningful comparison.
**Q155: A.** **Fine-tune when you need consistent style/format/specialized behavior** beyond prompting/RAG.
**Q156: A.** **Generate and curate synthetic data** (then review).
**Q157: A.** **Overfitting**; fix with more/diverse data, regularization, held-out validation.
**Q158: A and B.** **Training loss decreasing** and **validation loss stable/decreasing** indicate good progress.
**Q159: A.** Lower **temperature/top-p** to reduce loose rephrasing.
**Q160: A.** **Hybrid search + re-ranking** balances recall and precision.
**Q161: A.** **Embeddings map text to vectors** for semantic similarity search.
**Q162: A.** **Version, evaluate, promote with rollback** through environments.
**Q163: A.** Very large chunks **dilute signal with irrelevant text**.
**Q164: A.** **Evaluation on a representative held-out dataset meeting quality/safety thresholds** supports production readiness.

## Case Study 3 — Adventure Works

**CS3-Q1: A** (Bicep + GitHub Actions with OIDC; no stored secret).
**CS3-Q2: A** (AutoML baseline, then sweep job to tune).
**CS3-Q3: A** (Pipeline job of registered components).
**CS3-Q4: A** (Blue/green traffic split with rollback on one online endpoint).
**CS3-Q5: A** (Drift monitor + threshold wired to retraining trigger/alert).
**CS3-Q6: A** (PTUs for predictable peak latency).
**CS3-Q7: A and B** (Groundedness flags fabrication; fix via retrieval tuning + lower temperature).
**CS3-Q8: A** (Automated quality + risk/safety evaluation gating release).
**CS3-Q9: A** (Version prompts in Git, branch variants, evaluate before merge).
**CS3-Q10: A and B** (Token consumption + latency/response time).

---

# Section 16 — Quick-reference glossary (high-yield)

**MLOps / Azure Machine Learning**
- **Workspace dependent resources:** Storage (data/artifacts), Key Vault (secrets), Application Insights (telemetry), Container Registry (images, on first build).
- **Datastore:** secure connection info to storage; **Data asset:** pointer to specific data (`uri_file`, `uri_folder`, `mltable`).
- **Compute instance:** single-node interactive; **Compute cluster (AmlCompute):** scalable multi-node for jobs (min can be 0).
- **Environment:** Docker base image + conda/pip deps; **Component:** reusable versioned step; **Registry:** cross-workspace asset sharing.
- **RBAC:** least privilege; **AzureML Data Scientist** can run jobs/register models but not manage the workspace.
- **Managed identity:** system-assigned (1:1) vs user-assigned (shared/reusable); avoids secrets.
- **IaC:** Bicep (declarative, idempotent) + `az ml` CLI v2; **GitHub Actions** with **OIDC federation** (no stored secrets); `pull_request` validate → merge apply.
- **Networking:** private endpoint + managed VNet; disable public access.

**Model lifecycle**
- **MLflow:** tracking (`log_metric`, `autolog`), model format (signature + deps → no-code deploy), registration/versioning.
- **AutoML:** auto featurization, primary metric (AUC-weighted for imbalanced classification; Normalized RMSE/R² for regression), early stopping, child/trial jobs.
- **Command job:** command + environment + compute. **Sweep job:** search space + sampling (grid/random/Bayesian) + early-termination (Bandit, Median, Truncation).
- **Pipeline job:** components wired output→input; schedulable/reusable.
- **Endpoints:** Online (real-time, low-latency, per-request) vs Batch (large-volume, scheduled, writes to datastore). Scoring script: `init()` loads model once, `run(data)` scores per request.
- **Deployment safety:** blue/green traffic split, progressive rollout, rollback; troubleshoot with `get-logs`.
- **Monitoring:** data drift (distribution comparison) → alert/retrain trigger; regression=RMSE/MAE, classification=accuracy/precision/recall/F1.
- **Responsible AI:** fairness across cohorts + feature importance; archive old model versions for audit.

**GenAIOps / Foundry**
- **Hub** = shared config/security/connections; **Project** = app workspace under a hub.
- **Connections** + **managed identity + RBAC** (no keys in code). **Tools** (code interpreter, file search) make models agentic.
- **Deployment options:** serverless API (pay-per-token, no infra), managed compute (dedicated GPUs for non-serverless models), **PTUs** (reserved capacity, predictable latency at scale).
- **Model selection:** smallest/cheapest model meeting quality + latency + context/modality needs, validated by evaluation.
- **Prompts:** version-control in Git; create variants; compare before merge; progressive rollout.
- **Quota errors:** request increase or change region/size.

**Quality & observability**
- **AI quality metrics:** groundedness (supported by sources), relevance (pertinent), coherence (logical/structured), fluency (well-written).
- **Risk & safety:** hate/violence/sexual/self-harm content detection.
- **Evaluation:** test dataset + data mapping; built-in + custom evaluators; automated eval in CI gates release; manual vs automated.
- **Observability:** latency, throughput, response time; **token consumption** (input+output) = cost driver; logging + tracing (spans) for debugging.

**Optimization**
- **RAG tuning:** similarity threshold, chunk size/overlap, **hybrid search** (semantic + keyword) + **re-ranking**; domain embedding model selection/fine-tuning; A/B testing with relevance metrics.
- **Fine-tuning vs RAG:** fine-tune for consistent style/format/specialized behavior; RAG for current/external knowledge. Synthetic data fills label gaps. Watch overfitting (train vs validation loss).
- **Generation params:** lower temperature/top-p to reduce hallucination/loose rephrasing.
- **Fine-tuned model lifecycle:** version → evaluate (held-out + safety thresholds) → promote with rollback.

---

*End of combined mock exam. Good luck on Tuesday — focus extra time on Domain 2 (25–30%) and Domain 3 (20–25%), the two heaviest sections.*
