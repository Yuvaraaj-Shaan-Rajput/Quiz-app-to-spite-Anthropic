questions = [

# --- Worksheet 14: Causal Inference ---

{"id":"causal_001","topic":"Causal Inference","question":"A counterfactual refers to:",
 "choices":[
     "An observed outcome that goes against our intuition",
     "A hypothetical alternative outcome",
     "A confounder or mediator",
     "The opposite of the opposite"
 ],
 "answer":"A hypothetical alternative outcome"},

{"id":"causal_002","topic":"Causal Inference","question":"Why does A/B testing estimate a causal effect rather than correlation?",
 "choices":[
     "Sample size ignores confounders",
     "Random assignment ensures groups are identical in expectation",
     "Measured at same time",
     "Control for all confounders"
 ],
 "answer":"Random assignment ensures groups are identical in expectation"},

{"id":"causal_003","topic":"Causal Inference","question":"Randomization ensures:",
 "choices":[
     "Zero variance",
     "Ignorability",
     "No bias ever",
     "No sampling error"
 ],
 "answer":"Ignorability"},

{"id":"causal_004","topic":"Causal Inference","question":"Small samples in experiments lead to:",
 "choices":[
     "Bias always",
     "High variance",
     "No randomness",
     "Deterministic results"
 ],
 "answer":"High variance"},

{"id":"causal_005","topic":"Causal Inference","question":"CATE conditions on:",
 "choices":[
     "Treatment only",
     "Covariates",
     "Outcome",
     "Noise"
 ],
 "answer":"Covariates"},

{"id":"causal_006","topic":"Causal Inference","question":"ATE can be obtained from CATE by:",
 "choices":[
     "Differentiation",
     "Integration over X",
     "Conditioning",
     "Randomizing again"
 ],
 "answer":"Integration over X"},

{"id":"causal_007","topic":"Causal Inference","question":"Ignorability means:",
 "choices":[
     "Treatment independent of outcomes given X",
     "No confounders anywhere",
     "Random assignment",
     "No bias in measurements"
 ],
 "answer":"Treatment independent of outcomes given X"},

{"id":"causal_008","topic":"Causal Inference","question":"Propensity score equals:",
 "choices":[
     "P(Y = 1)",
     "P(T = 1 | X)",
     "P(X | T = 1)",
     "P(Y | T)"
 ],
 "answer":"P(T = 1 | X)"},

{"id":"causal_009","topic":"Causal Inference","question":"Observational difference E[Y|T=1] − E[Y|T=0] fails when:",
 "choices":[
     "No confounders",
     "Confounding exists",
     "Randomized",
     "Large sample"
 ],
 "answer":"Confounding exists"},

{"id":"causal_010","topic":"Causal Inference","question":"Difference between conditioning and do(X):",
 "choices":[
     "Algebraic",
     "Structural removal of incoming arrows",
     "Numerical",
     "Statistical"
 ],
 "answer":"Structural removal of incoming arrows"},

# --- Graphical Models ---

{"id":"causal_011","topic":"Causal Inference","question":"A DAG must be:",
 "choices":[
     "Undirected",
     "Cyclic",
     "Acyclic",
     "Weighted"
 ],
 "answer":"Acyclic"},

{"id":"causal_012","topic":"Causal Inference","question":"d-separation means:",
 "choices":[
     "Every path has confounder",
     "All paths blocked by S",
     "Collider exists",
     "No directed path"
 ],
 "answer":"All paths blocked by S"},

# --- Graphical models with interventions ---

{"id":"causal_013","topic":"Causal Inference","question":"P(Y | X) differs from P(Y | do(X)) because:",
 "choices":[
     "Conditioning equals intervention",
     "Intervention breaks dependencies",
     "Bayes rule fails",
     "Always equal"
 ],
 "answer":"Intervention breaks dependencies"},

# --- Worksheet 15: Confidence Intervals ---

{"id":"stats_014","topic":"Confidence Intervals","question":"A 95% confidence interval for µ means:",
 "choices":[
     "There is a 95% probability that µ lies in the interval",
     "95% of sample means lie in the interval",
     "95% of intervals constructed contain µ",
     "Interval contains 95% of population"
 ],
 "answer":"95% of intervals constructed contain µ"},

{"id":"stats_015","topic":"Confidence Intervals","question":"As sample size n increases, a confidence interval:",
 "choices":[
     "Widens",
     "Narrows",
     "Stays the same",
     "Widens if variance unknown"
 ],
 "answer":"Narrows"},

{"id":"stats_016","topic":"Confidence Intervals","question":"The z-statistic is defined as:",
 "choices":[
     "x̄ − µ",
     "(x̄ − µ)√n",
     "(x̄ − µ)/(σ/√n)",
     "σ/√n"
 ],
 "answer":"(x̄ − µ)/(σ/√n)"},

{"id":"stats_017","topic":"Confidence Intervals","question":"Standard error for proportion is:",
 "choices":[
     "p(1-p)",
     "√(p(1-p)·n)",
     "√(p(1-p)/n)",
     "p/√n"
 ],
 "answer":"√(p(1-p)/n)"},

{"id":"stats_018","topic":"Confidence Intervals","question":"Null hypothesis represents:",
 "choices":[
     "Preferred outcome",
     "Baseline or no-effect assumption",
     "Strongest effect",
     "Most likely explanation"
 ],
 "answer":"Baseline or no-effect assumption"},

{"id":"stats_019","topic":"Confidence Intervals","question":"A p-value measures:",
 "choices":[
     "Probability null is true",
     "Probability of observing data as extreme given H0",
     "Chance of Type II error",
     "Confidence level"
 ],
 "answer":"Probability of observing data as extreme given H0"},

{"id":"stats_020","topic":"Confidence Intervals","question":"Zohran poll drop (26% → 25%, p=0.41) implies:",
 "choices":[
     "Reject H0",
     "Fail to reject H0",
     "Accept H1",
     "Inconclusive due to size"
 ],
 "answer":"Fail to reject H0"},

{"id":"stats_021","topic":"Confidence Intervals","question":"When sample size increases and p-value drops, why?",
 "choices":[
     "Effect size increased",
     "Standard error decreased",
     "Null changed",
     "Threshold lowered"
 ],
 "answer":"Standard error decreased"},

{"id":"stats_022","topic":"Confidence Intervals","question":"Why does two-sided test fail when one-sided rejects?",
 "choices":[
     "Data changed",
     "Alpha split across tails",
     "Sample smaller",
     "Null stricter"
 ],
 "answer":"Alpha split across tails"},

{"id":"stats_023","topic":"Confidence Intervals","question":"Why do two-sided tests make rejection harder?",
 "choices":[
     "Need more samples",
     "More stringent critical value",
     "Lower power always",
     "Not for proportions"
 ],
 "answer":"More stringent critical value"},

{"id":"stats_024","topic":"Confidence Intervals","question":"Type I error is:",
 "choices":[
     "Fail to reject false H0",
     "Reject true H0",
     "Correct rejection",
     "Correct non-rejection"
 ],
 "answer":"Reject true H0"},

{"id":"stats_025","topic":"Confidence Intervals","question":"Type II error is:",
 "choices":[
     "Fail to reject false H0",
     "Reject true H0",
     "Correct rejection",
     "Correct non-rejection"
 ],
 "answer":"Fail to reject false H0"},

{"id":"stats_026","topic":"Confidence Intervals","question":"Power of a test equals:",
 "choices":[
     "α",
     "1 - α",
     "β",
     "1 - β"
 ],
 "answer":"1 - β"},

{"id":"stats_027","topic":"Confidence Intervals","question":"Control group in A/B testing is:",
 "choices":[
     "New design",
     "Baseline condition",
     "High engagement users",
     "Excluded users"
 ],
 "answer":"Baseline condition"},

{"id":"stats_028","topic":"Confidence Intervals","question":"Conversion rate is:",
 "choices":[
     "Total users",
     "Exposure count",
     "Fraction completing action",
     "Difference in outcomes"
 ],
 "answer":"Fraction completing action"},

{"id":"stats_029","topic":"Confidence Intervals","question":"Pooled proportion is:",
 "choices":[
     "(pA + pB)/2",
     "(xA + xB)/(nA + nB)",
     "pA * pB",
     "|xA - xB|/(nA + nB)"
 ],
 "answer":"(xA + xB)/(nA + nB)"},

{"id":"stats_030","topic":"Confidence Intervals","question":"Variance of difference in proportions under H0:",
 "choices":[
     "p(1-p)(nA+nB)",
     "p(1-p)(1/nA + 1/nB)",
     "pA(1-pA)/nA + pB(1-pB)/nB",
     "(pA - pB)^2"
 ],
 "answer":"p(1-p)(1/nA + 1/nB)"},

{"id":"stats_031","topic":"Confidence Intervals","question":"Familywise error rate without correction:",
 "choices":[
     "α",
     "α/K",
     "Up to Kα",
     "α^K"
 ],
 "answer":"Up to Kα"},

{"id":"stats_032","topic":"Confidence Intervals","question":"Bonferroni correction threshold:",
 "choices":[
     "α",
     "α*K",
     "α/K",
     "√(α/K)"
 ],
 "answer":"α/K"},

{"id":"stats_033","topic":"Confidence Intervals","question":"Bonferroni is based on:",
 "choices":[
     "CLT",
     "Union bound",
     "Bayes theorem",
     "LLN"
 ],
 "answer":"Union bound"},

{"id":"stats_034","topic":"Confidence Intervals","question":"Repeated p-value checking does what?",
 "choices":[
     "Valid",
     "Inflates Type I error",
     "Reduces power",
     "Equals SPRT"
 ],
 "answer":"Inflates Type I error"},

{"id":"stats_035","topic":"Confidence Intervals","question":"Wald’s SPRT compares:",
 "choices":[
     "Means",
     "Confidence intervals",
     "Likelihood ratio",
     "p-values"
 ],
 "answer":"Likelihood ratio"},

# --- Worksheet 16: Calibration ---

{"id":"calib_036","topic":"Calibration","question":"A well-calibrated model means:",
 "choices":[
     "High accuracy",
     "Predicted probability matches observed frequency",
     "Confident predictions",
     "Low variance"
 ],
 "answer":"Predicted probability matches observed frequency"},

{"id":"calib_037","topic":"Calibration","question":"Brier Score formula is:",
 "choices":[
     "Log loss",
     "Partial log loss",
     "(xi - yi)^2",
     "(pi - yi)^2",
     "|pi - yi|"
 ],
 "answer":"(pi - yi)^2"},

{"id":"calib_038","topic":"Calibration","question":"Brier Score decomposition reveals:",
 "choices":[
     "Train + test loss",
     "Bias + variance",
     "Calibration error + refinement",
     "Accuracy + precision"
 ],
 "answer":"Calibration error + refinement"},

{"id":"calib_039","topic":"Calibration","question":"Perfect calibration in reliability diagram:",
 "choices":[
     "y = 0.5",
     "y = x",
     "Vertical line",
     "Random scatter"
 ],
 "answer":"y = x"},

{"id":"calib_040","topic":"Calibration","question":"Curve above diagonal y=x indicates:",
 "choices":[
     "Perfect calibration",
     "Overconfidence",
     "Underconfidence",
     "Need more data"
 ],
 "answer":"Overconfidence"},

{"id":"calib_041","topic":"Calibration","question":"A proper loss function is:",
 "choices":[
     "Always positive",
     "Minimized when predicted probability equals true probability",
     "Symmetric",
     "Test-only"
 ],
 "answer":"Minimized when predicted probability equals true probability"},

{"id":"calib_042","topic":"Calibration","question":"Why do competitions incentivize overconfidence?",
 "choices":[
     "Higher accuracy",
     "More confident predictions win ties",
     "Uses Brier score",
     "Faster training"
 ],
 "answer":"More confident predictions win ties"},

{"id":"calib_043","topic":"Calibration","question":"If proper losses replaced accuracy rewards:",
 "choices":[
     "More overconfidence",
     "Encourage honest probabilities",
     "Lower accuracy",
     "Calibration impossible"
 ],
 "answer":"Encourage honest probabilities"},

{"id":"calib_044","topic":"Calibration","question":"Why does isotonic regression overfit on small datasets?",
 "choices":[
     "Too few parameters",
     "Non-parametric flexibility overfits noise",
     "Uses sigmoid",
     "Needs normalization"
 ],
 "answer":"Non-parametric flexibility overfits noise"},

{"id":"calib_045","topic":"Calibration","question":"Which is NOT quantile mapping for calibration?",
 "choices":[
     "Platt scaling",
     "Isotonic regression",
     "Temperature scaling",
     "All are examples"
 ],
 "answer":"Temperature scaling"},

# --- Worksheet 17: Vision ---

{"id":"vision_046","topic":"Vision","question":"What distinguishes convolutional layers from fully connected layers?","choices":["Larger parameter count","Non-linear activations only","Requires labels","Weight sharing across spatial locations"],"answer":"Weight sharing across spatial locations"},
{"id":"vision_047","topic":"Vision","question":"Weight sharing in CNNs enables:","choices":["Faster convergence","Detect same feature anywhere","Exact rotation invariance","Remove bias"],"answer":"Detect same feature anywhere"},
{"id":"vision_048","topic":"Vision","question":"ResNet residual connections address:","choices":["Overfitting","Vanishing/exploding gradients","Spatial locality","Class imbalance"],"answer":"Vanishing/exploding gradients"},
{"id":"vision_049","topic":"Vision","question":"Why was ImageNet influential?","choices":["Introduced unsupervised learning","Large labeled dataset","Removed CNNs","Focused on segmentation"],"answer":"Large labeled dataset"},
{"id":"vision_050","topic":"Vision","question":"Grad-CAM visualizes:","choices":["Filters","Reconstruction errors","Gradients over image regions","Training distribution"],"answer":"Gradients over image regions"},
{"id":"vision_051","topic":"Vision","question":"Segmentation differs from classification because:","choices":["Pixel-level labels","Unsupervised","Needs bounding boxes","Structured outputs"],"answer":"Pixel-level labels"},
{"id":"vision_052","topic":"Vision","question":"Challenge specific to segmentation:","choices":["Deep optimization","Balancing resolution vs receptive field","Too much capacity","Shared representations"],"answer":"Balancing resolution vs receptive field"},
{"id":"vision_053","topic":"Vision","question":"Core idea of U-Net:","choices":["Fully connected bottleneck","Skip connections","Adversarial training","Recurrent layers"],"answer":"Skip connections"},
{"id":"vision_054","topic":"Vision","question":"Image embedding is:","choices":["Pixel probability map","Compressed vector representation","Text description","Generative output"],"answer":"Compressed vector representation"},
{"id":"vision_055","topic":"Vision","question":"Linear probe means:","choices":["Train all layers","Train final classifier only","Contrastive loss","Remove embedding"],"answer":"Train final classifier only"},
{"id":"vision_056","topic":"Vision","question":"Few-shot learning addresses:","choices":["Large datasets","Abundant supervision","Limited labeled data","Training instability"],"answer":"Limited labeled data"},
{"id":"vision_057","topic":"Vision","question":"Zero-shot learning requires:","choices":["Pixel labels","New labeled data","External semantic info","Bayesian inference"],"answer":"External semantic info"},
{"id":"vision_058","topic":"Vision","question":"Self-supervised learning:","choices":["No data","Synthetic labels from data","Human labels","Reinforcement"],"answer":"Synthetic labels from data"},
{"id":"vision_059","topic":"Vision","question":"Why is self-supervised attractive?","choices":["Avoids NN","Interpretability","Replaces supervised","Uses unlabeled data"],"answer":"Uses unlabeled data"},
{"id":"vision_060","topic":"Vision","question":"Inpainting trains model to:","choices":["Predict labels","Segment objects","Generate captions","Fill missing regions"],"answer":"Fill missing regions"},
{"id":"vision_061","topic":"Vision","question":"Colorization teaches:","choices":["Exact pixels","Discrete labels","Camera calibration","Semantic understanding"],"answer":"Semantic understanding"},
{"id":"vision_062","topic":"Vision","question":"Image captioning is:","choices":["Classification","Image-to-image","Image-to-text generation","Clustering"],"answer":"Image-to-text generation"},
{"id":"vision_063","topic":"Vision","question":"Captioning is multimodal because:","choices":["Multiple cameras","Vision + language","Multiple datasets","Multiple losses"],"answer":"Vision + language"},
{"id":"vision_064","topic":"Vision","question":"Image embeddings in captioning:","choices":["Replace LM","Initialize pixels","Provide visual context","Enforce grammar"],"answer":"Provide visual context"},
{"id":"vision_065","topic":"Vision","question":"Generative vs discriminative models:","choices":["Generative predicts labels","Generative models distribution","Discriminative needs no data","Discriminative generates"],"answer":"Generative models distribution"},
{"id":"vision_066","topic":"Vision","question":"Core idea of GANs:","choices":["Likelihood optimization","Adversarial training","Bayesian modeling","Supervised prediction"],"answer":"Adversarial training"},
{"id":"vision_067","topic":"Vision","question":"Mode collapse is:","choices":["Noisy samples","Ignore discriminator","Limited diversity","Discriminator overfits"],"answer":"Limited diversity"},
{"id":"vision_068","topic":"Vision","question":"Why is tabular data hard for GANs?","choices":["No labels","Mixed types + imbalance","Small datasets","No correlations"],"answer":"Mixed types + imbalance"},
{"id":"vision_069","topic":"Vision","question":"CTGAN conditional generator addresses:","choices":["Normalization","Rare categories","CNN overfitting","Resolution"],"answer":"Rare categories"},
{"id":"vision_070","topic":"Vision","question":"CTGAN log-frequency sampling:","choices":["Uniform distributions","Oversample rare categories","Reduce compute","Simplify eval"],"answer":"Oversample rare categories"},
{"id":"vision_071","topic":"Vision","question":"WGAN-GP role:","choices":["Pixel normalization","Stable training via gradients","Faster convergence","Discrete sampling"],"answer":"Stable training via gradients"},
{"id":"vision_072","topic":"Vision","question":"PacGAN reduces mode collapse by:","choices":["Add noise","Multiple samples to critic","Remove discriminator","KL divergence"],"answer":"Multiple samples to critic"},
{"id":"vision_073","topic":"Vision","question":"Gumbel-Softmax is used to:","choices":["Sample noise","Differentiable categorical sampling","Reduce loss","Normalize features"],"answer":"Differentiable categorical sampling"},

# --- Worksheet 18: Text and NLP ---

{"id":"nlp_074","topic":"NLP","question":"Phonemes are:","choices":["Semantic units","Minimal sound units","Frequency representations","Characters"],"answer":"Minimal sound units"},
{"id":"nlp_075","topic":"NLP","question":"Markov property assumes:","choices":["All history matters","Current state summarizes history","Observations independent","Stationary transitions"],"answer":"Current state summarizes history"},
{"id":"nlp_076","topic":"NLP","question":"In HMMs, observations are:","choices":["Deterministic","Independent given hidden states","Dependent on past","Identical"],"answer":"Independent given hidden states"},
{"id":"nlp_077","topic":"NLP","question":"RNN is:","choices":["Feedforward per step","Hidden state sequence model","Graphical model","CNN"],"answer":"Hidden state sequence model"},
{"id":"nlp_078","topic":"NLP","question":"LSTM is:","choices":["Fixed state RNN","Gated memory network","Attention model","Bidirectional"],"answer":"Gated memory network"},
{"id":"nlp_079","topic":"NLP","question":"Bidirectional LSTM:","choices":["Fixed state","Gated memory","Attention","Processes both directions"],"answer":"Processes both directions"},
{"id":"nlp_080","topic":"NLP","question":"Word embeddings useful because:","choices":["Discrete IDs","Geometric similarity","No labels needed","Interpretable"],"answer":"Geometric similarity"},
{"id":"nlp_081","topic":"NLP","question":"Contextual embedding example:","choices":["Bank changes meaning by context","Fish averaged","Jessica fixed window","Tesseract fixed"],"answer":"Bank changes meaning by context"},
{"id":"nlp_082","topic":"NLP","question":"Co-occurrence embeddings assume:","choices":["Rare words important","Similar context = similar meaning","Syntax dominates","Order irrelevant"],"answer":"Similar context = similar meaning"},
{"id":"nlp_083","topic":"NLP","question":"Transformer innovation:","choices":["CNN","Self-attention","Sparse features","Grammar"],"answer":"Self-attention"},
{"id":"nlp_084","topic":"NLP","question":"Self-attention allows:","choices":["All tokens","Neighbors only","Past only","Fixed window"],"answer":"All tokens"},
{"id":"nlp_085","topic":"NLP","question":"Multi-head attention improves by:","choices":["Multiple subspaces","Longer sequences","Shared weights","Shallow models"],"answer":"Multiple subspaces"},
{"id":"nlp_086","topic":"NLP","question":"Transformer drawback:","choices":["Vanishing gradients","Quadratic complexity","No generalization","Unstable"],"answer":"Quadratic complexity"},
{"id":"nlp_087","topic":"NLP","question":"Language model estimates:","choices":["Similarity","Sequence probability","Syntax","Topics"],"answer":"Sequence probability"},
{"id":"nlp_088","topic":"NLP","question":"Causal LM trains to:","choices":["Masked tokens","Next token","Sentiment","Bidirectional"],"answer":"Next token"},
{"id":"nlp_089","topic":"NLP","question":"Masked LM:","choices":["Left-to-right","Predict masked tokens","RL","No self-supervision"],"answer":"Predict masked tokens"},
{"id":"nlp_090","topic":"NLP","question":"Pretraining helps because:","choices":["No task data","Guaranteed optimal","Learns general representations","Prevents overfitting"],"answer":"Learns general representations"},
{"id":"nlp_091","topic":"NLP","question":"Fine-tuning:","choices":["Train from scratch","Freeze all","Update for task","Increase size"],"answer":"Update for task"},
{"id":"nlp_092","topic":"NLP","question":"Zero-shot learning:","choices":["No data at all","Synthetic data","No task-specific training","Remove output"],"answer":"No task-specific training"},
{"id":"nlp_093","topic":"NLP","question":"Adapters are:","choices":["Replace layers","Small trainable modules","Latency only","Sparse activations"],"answer":"Small trainable modules"},
{"id":"nlp_094","topic":"NLP","question":"LoRA reduces cost by:","choices":["Fewer layers","Low-rank updates","Shared embeddings","Quantization"],"answer":"Low-rank updates"},

# --- Worksheet 19: Data and Labels ---

{"id":"data_095","topic":"Data","question":"Labels are a bottleneck because:","choices":["Hard to store","Costly and time-consuming","Always inconsistent","Unnecessary"],"answer":"Costly and time-consuming"},
{"id":"data_096","topic":"Data","question":"Poor label quality affects:","choices":["Architecture","Training time","Generalization","Feature dimension"],"answer":"Generalization"},
{"id":"data_097","topic":"Data","question":"Semi-supervised learning combines:","choices":["Multiple labeled datasets","Few labeled + many unlabeled","Synthetic only","RL + supervision"],"answer":"Few labeled + many unlabeled"},
{"id":"data_098","topic":"Data","question":"Label propagation relies on:","choices":["Expert rules","Graph structure","Neural networks","Random labels"],"answer":"Graph structure"},
{"id":"data_099","topic":"Data","question":"ImageNet labels came from:","choices":["Web scraping","Experts only","Crowdsourcing","Self-supervised"],"answer":"Crowdsourcing"},
{"id":"data_100","topic":"Data","question":"Mechanical Turk advantage:","choices":["Perfect accuracy","GPU speed","Scalable annotation","No bias"],"answer":"Scalable annotation"},
{"id":"data_101","topic":"Data","question":"Multiple annotators help:","choices":["Increase imbalance","Reduce noise","Remove aggregation","Guarantee truth"],"answer":"Reduce noise"},
{"id":"data_102","topic":"Data","question":"Majority voting is:","choices":["Weak supervision","Label aggregation","Active learning","Self-training"],"answer":"Label aggregation"},
{"id":"data_103","topic":"Data","question":"Gold-standard checks:","choices":["Speed up labeling","Measure reliability","Remove rare classes","Generate labels"],"answer":"Measure reliability"},
{"id":"data_104","topic":"Data","question":"Dawid–Skene assumes:","choices":["Equal annotators","Annotator confusion matrix","Noise-free labels","Linear separability"],"answer":"Annotator confusion matrix"},
{"id":"data_105","topic":"Data","question":"Active learning reduces cost by:","choices":["Smaller models","Query informative points","Remove humans","Synthetic labels"],"answer":"Query informative points"},
{"id":"data_106","topic":"Data","question":"Uncertainty sampling selects:","choices":["High confidence","Majority class","Least confident","Highest loss"],"answer":"Least confident"},
{"id":"data_107","topic":"Data","question":"Query-by-committee relies on:","choices":["Agreement","Disagreement","Human disagreement","Random"],"answer":"Disagreement"},
{"id":"data_108","topic":"Data","question":"Weak supervision uses:","choices":["Heuristics/noisy sources","Experts only","Exact labels","No aggregation"],"answer":"Heuristics/noisy sources"},
{"id":"data_109","topic":"Data","question":"Reinforcement learning differs because:","choices":["Needs labels","Delayed rewards","Unsupervised only","No neural nets"],"answer":"Delayed rewards"},
{"id":"data_110","topic":"Data","question":"RLHF reward function is:","choices":["Hand-coded","Learned from humans","Fixed","Removed"],"answer":"Learned from humans"},
{"id":"data_111","topic":"Data","question":"PPO differs from DPO because PPO:","choices":["Needs reward model","No KL","Supervised only","No sampling"],"answer":"Needs reward model"},
{"id":"data_112","topic":"Data","question":"DPO avoids reward model by:","choices":["Contrastive preference loss","Online sampling","No human feedback","Freezing params"],"answer":"Contrastive preference loss"},
{"id":"data_113","topic":"Data","question":"Bayesian Network represents distribution by:","choices":["Independence","Global likelihood","Factorization","Embeddings"],"answer":"Factorization"},
{"id":"data_114","topic":"Data","question":"Bayesian Networks can generate data because:","choices":["Memorization","Joint distribution","Need labels","Discriminator"],"answer":"Joint distribution"},
{"id":"data_115","topic":"Data","question":"Why not used at scale:","choices":["No uncertainty","Tables scale poorly","Continuous only","No dependencies"],"answer":"Tables scale poorly"},
{"id":"data_116","topic":"Data","question":"Simulated data useful when:","choices":["Abundant","Cheap","Scarce/dangerous","Perfect labels"],"answer":"Scarce/dangerous"},
{"id":"data_117","topic":"Data","question":"Self-play generates labels via:","choices":["Humans","Self-competition","Random","Replay"],"answer":"Self-competition"},
{"id":"data_118","topic":"Data","question":"Distillation trains using:","choices":["Teacher outputs","Ground truth only","RL reward","Human feedback"],"answer":"Teacher outputs"},
{"id":"data_119","topic":"Data","question":"Soft targets are:","choices":["Hard labels","Gradients","Random labels","Full probability distributions"],"answer":"Full probability distributions"},
{"id":"data_120","topic":"Data","question":"Benefit of distillation:","choices":["Higher accuracy","Faster/cheaper deployment","No data needed","No bias"],"answer":"Faster/cheaper deployment"},

# --- Multi-select (unchanged logic) ---

{"id":"data_121","topic":"Data","question":"Which of the following are examples of knowledge-distilled models or distillation frameworks?",
 "choices":["ResNet","DistilNet","PCA","FitNets","Word2Vec","TinyNet","AlexNet","DeepSeek"],
 "answer":["DistilNet","FitNets","TinyNet","DeepSeek"],
 "multi":True},

# --- Worksheet 20: Big Data Science ---

{"id":"bigdata_122","topic":"Big Data","question":"Which distinguish parallel vs distributed computing?",
 "choices":[
     "Parallel uses multiple processors in one machine",
     "Distributed uses multiple networked nodes",
     "Distributed partitions data/tasks",
     "Parallel requires network communication",
     "Distributed involves node communication"
 ],
 "answer":[
     "Parallel uses multiple processors in one machine",
     "Distributed uses multiple networked nodes",
     "Distributed partitions data/tasks",
     "Distributed involves node communication"
 ],
 "multi":True},

{"id":"bigdata_123","topic":"Big Data","question":"High Performance Computing refers to:",
 "choices":["Consumer laptops","Supercomputers/clusters","Cloud storage","Small scripts"],
 "answer":"Supercomputers/clusters"},

{"id":"bigdata_124","topic":"Big Data","question":"Advantages of parallel computing include:",
 "choices":["Reduced execution time","Handle larger datasets","Guaranteed cost reduction","Improved throughput"],
 "answer":["Reduced execution time","Handle larger datasets","Improved throughput"],
 "multi":True},

{"id":"bigdata_125","topic":"Big Data","question":"GPU suited for parallel workloads because:",
 "choices":["Many small cores","Higher single-thread","Slower memory","Sequential only"],
 "answer":"Many small cores"},

{"id":"bigdata_126","topic":"Big Data","question":"A data lake stores:",
 "choices":["Structured only","Raw unprocessed data","Relational only","Normalized records"],
 "answer":"Raw unprocessed data"},

{"id":"bigdata_127","topic":"Big Data","question":"Data warehouses are characterized by:",
 "choices":["Structured schema-on-write","Optimized for analytics","Raw storage","ETL processes"],
 "answer":["Structured schema-on-write","Optimized for analytics","ETL processes"],
 "multi":True},

{"id":"bigdata_128","topic":"Big Data","question":"Schema means:",
 "choices":["Data organization definition","Database engine","Raw data","Query language"],
 "answer":"Data organization definition"},

{"id":"bigdata_129","topic":"Big Data","question":"Schema-on-read means:",
 "choices":["Schema at write","Schema at read","No schema","Strict relational rules"],
 "answer":"Schema at read"},

{"id":"bigdata_130","topic":"Big Data","question":"Examples of big data file formats:",
 "choices":["CSV","JSON","Parquet","JPEG"],
 "answer":["CSV","JSON","Parquet"],
 "multi":True},

{"id":"bigdata_131","topic":"Big Data","question":"ETL stands for:",
 "choices":["Extract Transform Load","Evaluate Test Learn","Execute Transfer Log","Encode Train Label"],
 "answer":"Extract Transform Load"},

{"id":"bigdata_132","topic":"Big Data","question":"Workflow orchestration tools:",
 "choices":["Schedule pipelines","Retry failures","Only ML models","Handle dependencies"],
 "answer":["Schedule pipelines","Retry failures","Handle dependencies"],
 "multi":True},

{"id":"bigdata_133","topic":"Big Data","question":"MapReduce is:",
 "choices":["Distributed programming model","Visualization library","GPU framework","SQL engine"],
 "answer":"Distributed programming model"},

{"id":"bigdata_134","topic":"Big Data","question":"Advantages of Spark over MapReduce:",
 "choices":["In-memory speed","Iterative support","ML/graph libraries","Guaranteed lower cost"],
 "answer":["In-memory speed","Iterative support","ML/graph libraries"],
 "multi":True},

{"id":"bigdata_135","topic":"Big Data","question":"Dashboard in big data:",
 "choices":["Visual metrics","Runs ETL","Stores raw data","Controls GPU"],
 "answer":"Visual metrics"},

{"id":"bigdata_136","topic":"Big Data","question":"Monitoring pipelines includes:",
 "choices":["Track jobs","Measure throughput","Ignore anomalies","Detect drift"],
 "answer":["Track jobs","Measure throughput","Detect drift"],
 "multi":True},

{"id":"bigdata_137","topic":"Big Data","question":"Differential privacy aims to:",
 "choices":["Protect individual data","Speed computation","Compress data","Remove redundancy"],
 "answer":"Protect individual data"},

{"id":"bigdata_138","topic":"Big Data","question":"Data drift refers to:",
 "choices":["Distribution changes","Static data","Label noise","Loss of parallelism"],
 "answer":"Distribution changes"},

{"id":"bigdata_139","topic":"Big Data","question":"Serverless computing:",
 "choices":["Auto-managed cloud execution","Local only","No servers exist","On-prem only"],
 "answer":"Auto-managed cloud execution"},

{"id":"bigdata_140","topic":"Big Data","question":"A/B testing goal:",
 "choices":["Compare variants","Assign servers","Remove stats","Test all params"],
 "answer":"Compare variants"},

{"id":"bigdata_141","topic":"Big Data","question":"Good workflow practices:",
 "choices":["Define dependencies","Auto retries","No monitoring","Optimize scheduling"],
 "answer":["Define dependencies","Auto retries","Optimize scheduling"],
 "multi":True},

{"id":"bigdata_142","topic":"Big Data","question":"Serverless benefit:",
 "choices":["Auto scaling","Pay per execution","Zero latency","No logic needed"],
 "answer":"Auto scaling"},

{"id":"bigdata_143","topic":"Big Data","question":"Inverted index maps:",
 "choices":["Docs to links","Terms to docs","Queries to ranks","Docs to embeddings"],
 "answer":"Terms to docs"},

{"id":"bigdata_144","topic":"Big Data","question":"IDF in BM25:",
 "choices":["Penalize repeats","Downweight common terms","Normalize length","Smooth TF"],
 "answer":"Downweight common terms"},

{"id":"bigdata_145","topic":"Big Data","question":"PageRank represents:",
 "choices":["Shortest path","Random walk probability","Degree centrality","Clustering coeff"],
 "answer":"Random walk probability"},

{"id":"bigdata_146","topic":"Big Data","question":"Personalized PageRank:",
 "choices":["Weighted edges","Biased teleportation","Remove dangling nodes","Normalize scores"],
 "answer":"Biased teleportation"},

{"id":"bigdata_147","topic":"Big Data","question":"MIPS is used to:",
 "choices":["Compute PageRank","Find similar vectors","Sort by length","Graph traversal"],
 "answer":"Find similar vectors"},

{"id":"bigdata_148","topic":"Big Data","question":"KD-trees perform poorly when:",
 "choices":["High dimensions","Duplicate points","Few queries","Clustered data"],
 "answer":"High dimensions"},

{"id":"bigdata_149","topic":"Big Data","question":"Graph ANN differs because:",
 "choices":["Compare all vectors","Needs labels","Traverse local neighbors","Tree partitioning"],
 "answer":"Traverse local neighbors"},

{"id":"bigdata_150","topic":"Big Data","question":"Search graph connects to:",
 "choices":["Random docs","Keyword docs","Nearest neighbors","Same length docs"],
 "answer":"Nearest neighbors"},

{"id":"bigdata_151","topic":"Big Data","question":"Local optimum means:",
 "choices":["Neighbors worse than node","Global best","Cluster center","Max degree"],
 "answer":"Neighbors worse than node"},

{"id":"bigdata_152","topic":"Big Data","question":"Greedy graph search fails because:",
 "choices":["Needs full traversal","Gets stuck locally","Quadratic scaling","Uniform degree"],
 "answer":"Gets stuck locally"},

{"id":"bigdata_153","topic":"Big Data","question":"Parallel graph search helps to:",
 "choices":["Reduce dimensions","Remove reranking","Guarantee exact","Escape local regions"],
 "answer":"Escape local regions"},

{"id":"bigdata_154","topic":"Big Data","question":"HNSW improves search by:",
 "choices":["Hierarchical layers","Hashing","Vector compression","Distance thresholds"],
 "answer":"Hierarchical layers"},

{"id":"bigdata_155","topic":"Big Data","question":"Second-stage reranker purpose:",
 "choices":["Speed ANN","Refine results","Remove index","Calibrate similarity"],
 "answer":"Refine results"},

# --- Worksheet 21: Agentic AI ---

{"id":"agent_156","topic":"Agentic AI","question":"LLM is best described as:","choices":["Symbolic engine","Neural next-token predictor","Database","Rule chatbot"],"answer":"Neural next-token predictor"},
{"id":"agent_157","topic":"Agentic AI","question":"Prompt programming refers to:","choices":["Fine-tuning","Optimizing latency","Filtering outputs","Designing input prompts"],"answer":"Designing input prompts"},
{"id":"agent_158","topic":"Agentic AI","question":"Few-shot works because:","choices":["Memorization","Infers structure from examples","Updates weights","Acts as training"],"answer":"Infers structure from examples"},
{"id":"agent_159","topic":"Agentic AI","question":"Compared to fine-tuning, prompting:","choices":["No labels or parameter updates","Always better","Eliminates hallucinations","Guarantees reproducibility"],"answer":"No labels or parameter updates"},
{"id":"agent_160","topic":"Agentic AI","question":"Context in LLMs refers to:","choices":["Last question only","Hidden state","Full token sequence","Training data"],"answer":"Full token sequence"},
{"id":"agent_161","topic":"Agentic AI","question":"Increasing context length enables:","choices":["Faster inference","More params","Multi-step reasoning","Guaranteed logic"],"answer":"Multi-step reasoning"},
{"id":"agent_162","topic":"Agentic AI","question":"Limitation of long context:","choices":["Attention scales poorly","No tools","Needs labels","No retrieval"],"answer":"Attention scales poorly"},
{"id":"agent_163","topic":"Agentic AI","question":"Chain-of-thought improves performance by:","choices":["Reveal weights","Intermediate reasoning","Fewer tokens","No hallucination"],"answer":"Intermediate reasoning"},
{"id":"agent_164","topic":"Agentic AI","question":"Chain-of-thought works best when:","choices":["Small models","No reasoning","Large models","Strict format"],"answer":"Large models"},
{"id":"agent_165","topic":"Agentic AI","question":"RAG combines:","choices":["SL + RL","Symbolic + neural","Retrieval + generation","Compression + encryption"],"answer":"Retrieval + generation"},
{"id":"agent_166","topic":"Agentic AI","question":"Purpose of retrieval in RAG:","choices":["Replace pretraining","Inject external knowledge","Reduce parameters","Speed up"],"answer":"Inject external knowledge"},
{"id":"agent_167","topic":"Agentic AI","question":"RAG reduces hallucinations because:","choices":["Stops generation","Retrained models","Uses retrieved context","Logical constraints"],"answer":"Uses retrieved context"},
{"id":"agent_168","topic":"Agentic AI","question":"In RAG, retrieved docs are:","choices":["Update weights","Appended to prompt","Symbolic rules","Stored permanently"],"answer":"Appended to prompt"},
{"id":"agent_169","topic":"Agentic AI","question":"Toolformer showed LLMs can:","choices":["Call tools without labels","Replace tools","Exact computation","Remove prompts"],"answer":"Call tools without labels"},
{"id":"agent_170","topic":"Agentic AI","question":"Function calling APIs allow:","choices":["Modify weights","Structured tool calls","Access private data","Bypass safety"],"answer":"Structured tool calls"},
{"id":"agent_171","topic":"Agentic AI","question":"ReAct combines:","choices":["RL + SL","Reasoning + actions","Retrieval + compression","Symbolic planning"],"answer":"Reasoning + actions"},
{"id":"agent_172","topic":"Agentic AI","question":"ReAct vs CoT adds:","choices":["Removes reasoning","Tool interaction","Smaller models","Needs labels"],"answer":"Tool interaction"},
{"id":"agent_173","topic":"Agentic AI","question":"Agentic AI is:","choices":["Single forward pass","Stateless chatbot","Multi-step planning system","Classifier"],"answer":"Multi-step planning system"},
{"id":"agent_174","topic":"Agentic AI","question":"Agentic systems feature:","choices":["Stateless","Autonomous decisions","Optimal planning","Deterministic"],"answer":"Autonomous decisions"},
{"id":"agent_175","topic":"Agentic AI","question":"Memory in agents is used to:","choices":["Store weights","Track state","Replace retrieval","Improve GPU"],"answer":"Track state"},
{"id":"agent_176","topic":"Agentic AI","question":"Hallucination means:","choices":["Fluent but incorrect","Short outputs","Memorization","No generalization"],"answer":"Fluent but incorrect"},
{"id":"agent_177","topic":"Agentic AI","question":"Hallucinations occur because:","choices":["Bad retrieval","Optimize likelihood not truth","RL training","Attention"],"answer":"Optimize likelihood not truth"},
{"id":"agent_178","topic":"Agentic AI","question":"RAG preferred over fine-tuning because:","choices":["Cheaper and updatable","Bigger models","More labels","No eval"],"answer":"Cheaper and updatable"},
{"id":"agent_179","topic":"Agentic AI","question":"Reranker purpose:","choices":["Replace index","Improve precision","Reduce dimension","Normalize queries"],"answer":"Improve precision"}

]