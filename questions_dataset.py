questions = [

{
  "worksheet": "14 Causal inference",
  "questions": [
    {
      "id": "1",
      "type": "single",
      "question": "1. A counterfactual refers to:",
      "options": [
        "A. An observed outcome that goes against our intuition",
        "B. A hypothetical alternative outcome",
        "C. A confounder or mediator",
        "D. The opposite of the opposite"
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "2",
      "type": "single",
      "question": "2. A/B testing estimates a causal effect rather than a mere correlation. Why?",
      "options": [
        "A. Because the sample size is large enough to ignore confounders",
        "B. Because random assignment ensures the treatment and control groups are identical in expectation,replicating a do(X) intervention",
        "C. Because we measure both groups at the same time, eliminating time-based confounders",
        "D. Because we can control for all confounders by collecting enough data"
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "4",
      "type": "single",
      "question": "4. Randomization ensures:",
      "options": [
        "A. Zero variance",
        "B. Ignorability",
        "C. No bias ever",
        "D. No sampling error"
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "5",
      "type": "single",
      "question": "5. Small samples in experiments lead to:",
      "options": [
        "A. Bias always",
        "B. High variance",
        "C. No randomness",
        "D. Deterministic results"
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "6",
      "type": "single",
      "question": "6. CATE conditions on:",
      "options": [
        "A. Treatment only",
        "B. Covariates",
        "C. Outcome",
        "D. Noise"
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "7",
      "type": "single",
      "question": "7. ATE can be obtained from CATE by:",
      "options": [
        "A. Differentiation",
        "B. Integration over X",
        "C. Conditioning",
        "D. Randomizing again"
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "8",
      "type": "single",
      "question": "8. Ignorability means:",
      "options": [
        "A. Treatment assignment is independent of potential outcomes given covariates X",
        "B. There are no confounders anywhere in the causal graph",
        "C. Units are randomly assigned to treatment and control groups",
        "D. There is no systematic bias in the outcome measurements"
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "9",
      "type": "single",
      "question": "9. Propensity score equals:",
      "options": [
        "A. P(Y = 1)",
        "B. P(T = 1|X)",
        "C. P(X|T = 1)",
        "D. P(Y |T)"
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "10",
      "type": "single",
      "question": "10. Observational E[Y |T = 1] − E[Y |T = 0] fails when:",
      "options": [
        "A. No confounders",
        "B. Confounding exists",
        "C. Randomized",
        "D. Large sample"
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "11",
      "type": "single",
      "question": "11. The main difference between conditioning on X and intervening with do(X) is:",
      "options": [
        "A. Algebraic, since conditioning and intervention use different mathematical operators",
        "B. Structural, since do(X) removes all incoming arrows to X in the causal graph",
        "C. Numerical, since the two operations produce different probability values",
        "D. Statistical, since conditioning requires larger sample sizes than intervention"
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "12",
      "type": "single",
      "question": "1. A DAG must be:",
      "options": [
        "A. Undirected",
        "B. Cyclic",
        "C. Acyclic",
        "D. Weighted"
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "13",
      "type": "single",
      "question": "2. Two nodes X and Y are d-separated by a set S in a DAG if:",
      "options": [
        "A. Every path between X and Y contains a confounder in S",
        "B. Every path between X and Y is blocked by S, implying X ⊥ Y | S",
        "C. Every path between X and Y contains a collider not in S",
        "D. X and Y have no directed path between them"
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "14",
      "type": "single",
      "question": "1. P(Y |X) differs from P(Y |do(X)) because:",
      "options": [
        "A. Conditioning equals intervention",
        "B. Intervention breaks dependencies",
        "C. Bayes rule fails",
        "D. They are always equal"
      ],
      "correct_answers": ["B"]
    }
  ]
},

{
  "worksheet": "15 Confidence intervals",
  "questions": [
    {
      "id": "3",
      "type": "single",
      "question": "3. A 95% confidence interval for µ means:",
      "options": [
        "A. There is a 95% probability that µ lies in the interval.",
        "B. 95% of sample means lie in the interval.",
        "C. 95% of such intervals constructed from repeated samples contain µ.",
        "D. The interval contains 95% of the population."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "4",
      "type": "single",
      "question": "4. As sample size n increases, a confidence interval for µ:",
      "options": [
        "A. Widens, because more data increases uncertainty.",
        "B. Narrows, because the standard error decreases.",
        "C. Stays the same width.",
        "D. Widens only if the population variance is unknown."
      ],
      "correct_answers": ["B"]
    },
    {
     "id": "5",
     "type": "single",
     "question": "5. The z-statistic is defined as:",
     "options": [
       "A. z = x̄ − μ",
       "B. z = (x̄ − μ) × σ",
       "C. z = (x̄ − μ) / (σ / √n)",
       "D. z = σ / √n"
         ],
     "correct_answers": ["C"]
    },
    {
     "id": "6",
     "type": "single",
     "question": "6. In the NYC mayoral race example, the poll shows p̂ = 26% with n = 1000. Which statement correctly describes the standard error?",
     "options": [
        "A. SE = p̂(1 − p̂)",
        "B. SE = p̂",
        "C. SE = √(p̂(1 − p̂) / n)",
        "D. SE = p̂ / √n"
        ],
     "correct_answers": ["C"]
    },
    {
      "id": "7",
      "type": "single",
      "question": "7. The null hypothesis H0 typically represents:",
      "options": [
        "A. The researcher’s preferred outcome.",
        "B. A baseline or no-effect assumption.",
        "C. The strongest possible effect.",
        "D. The most likely explanation."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "8",
      "type": "single",
      "question": "8. A p-value measures:",
      "options": [
        "A. The probability the null hypothesis is true.",
        "B. The probability of observing data at least as extreme as observed, assuming H0 is true.",
        "C. The chance of making a Type II error.",
        "D. The confidence level of the test."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "9",
      "type": "single",
      "question": "9. In the Zohran example, a poll of 100 respondents shows support dropping from 26% to 25%. The p-value is approximately 0.41. The correct conclusion is:",
      "options": [
        "A. Reject H0; the drop is statistically significant.",
        "B. Fail to reject H0; the drop is within normal sampling variation.",
        "C. Accept H1; Trump’s video hurt Zohran.",
        "D. The test is inconclusive because the sample is too large."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "10",
      "type": "single",
      "question": "10. When the same poll uses n = 10,000 respondents, the p-value drops to 0.011. What changed?",
      "options": [
        "A. The effect size increased.",
        "B. The standard error decreased, making the same 1% drop more detectable.",
        "C. The null hypothesis changed.",
        "D. The significance threshold was lowered."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "11",
      "type": "single",
      "question": "11. In the Yifania exam example, a one-sided test rejects H0 at the 5% level (z = 1.854 > z0.05 = 1.644). When a two-sided test is used instead, the result fails to reject H0 (z0.025 = 1.960). This happens because:",
      "options": [
        "A. The data changed.",
        "B. A two-sided test splits α across both tails, requiring a larger z to reject.",
        "C. The sample size was reduced.",
        "D. The null hypothesis was made stricter."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "12",
      "type": "single",
      "question": "12. The tobacco lobby historically insisted on two-sided tests when evidence suggested smoking caused harm. Why does this make rejection harder?",
      "options": [
        "A. Two-sided tests require twice the sample size.",
        "B. Two-sided tests use a more stringent critical value (zα/2 vs zα) for the same α.",
        "C. Two-sided tests have lower power by definition.",
        "D. Two-sided tests do not apply to proportions."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "13",
      "type": "single",
      "question": "13. Type I error corresponds to:",
      "options": [
        "A. Failing to reject a false null hypothesis.",
        "B. Rejecting a true null hypothesis.",
        "C. Correctly rejecting a false null hypothesis.",
        "D. Correctly failing to reject a true null hypothesis."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "14",
      "type": "single",
      "question": "14. Type II error corresponds to:",
      "options": [
        "A. Failing to reject a false null hypothesis.",
        "B. Rejecting a true null hypothesis.",
        "C. Correctly rejecting a false null hypothesis.",
        "D. Correctly failing to reject a true null hypothesis."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "15",
      "type": "single",
      "question": "15. The power of a test is defined as:",
      "options": [
        "A. α",
        "B. 1 − α",
        "C. β",
        "D. 1 − β"
      ],
      "correct_answers": ["D"]
    },
    {
      "id": "17",
      "type": "single",
      "question": "17. In A/B testing, the control group represents:",
      "options": [
        "A. The new design being tested.",
        "B. The baseline or existing condition.",
        "C. Users with the highest engagement.",
        "D. Randomly excluded participants."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "18",
      "type": "single",
      "question": "18. Conversion rate is defined as:",
      "options": [
        "A. Total number of users.",
        "B. Number of exposures to treatment.",
        "C. Fraction of users completing a desired action.",
        "D. Difference between treatment and control outcomes."
      ],
      "correct_answers": ["C"]
    },
    {
     "id": "19",
     "type": "single",
     "question": "19. In the pooled A/B test, the pooled proportion p̂ is estimated as:",
     "options": [
       "A. (p̂A + p̂B) / 2",
       "B. (xA + xB) / (nA + nB)",
       "C. p̂A × p̂B",
       "D. |xA − xB| / (nA + nB)"
        ],
     "correct_answers": ["B"]
    },
    {
      "id": "20",
      "type": "single",
      "question": "20. Under H0 : pA = pB, the variance of p̂A − p̂B equals:",
      "options": [
        "A. p(1 − p)(nA + nB)",
        "B. p(1 − p)(1/nA + 1/nB)",
        "C. pA(1 − pA)/nA + pB(1 − pB)/nB",
        "D. (pA − pB)^2"
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "21",
      "type": "single",
      "question": "21. Testing K hypotheses simultaneously at level α without correction gives a familywise false positive rate of approximately:",
      "options": [
        "A. α",
        "B. α/K",
        "C. Up to Kα",
        "D. α^K"
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "22",
      "type": "single",
      "question": "22. Bonferroni correction requires each individual test to use significance threshold:",
      "options": [
        "A. α",
        "B. α · K",
        "C. α/K",
        "D.  √α/K"
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "23",
      "type": "single",
      "question": "23. The Bonferroni correction is based on:",
      "options": [
        "A. The central limit theorem.",
        "B. The union bound: Pr(∪i Ai) ≤ ∑i Pr(Ai)",
        "C. Bayes’ theorem.",
        "D. The law of large numbers."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "24",
      "type": "single",
      "question": "24. In classical fixed-sample testing, repeatedly checking the p-value and stopping early when p < 0.05:",
      "options": [
        "A. Is valid because the significance level is still respected.",
        "B. Inflates the Type I error rate above the stated α.",
        "C. Reduces power.",
        "D. Is equivalent to the SPRT."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "25",
      "type": "single",
      "question": "25. Wald’s SPRT compares:",
      "options": [
        "A. Sample means to fixed thresholds.",
        "B. Confidence intervals over time.",
        "C. The likelihood ratio Λt to thresholds A and B.",
        "D. p-values to α at each step."
      ],
      "correct_answers": ["C"]
    }
  ]
},

{
  "worksheet": "16 Calibration",
  "questions": [
    {
      "id": "1",
      "type": "single",
      "question": "1. In the context of model calibration, what does it mean for a model to be well-calibrated?",
      "options": [
        "A. The model achieves high accuracy on the test set.",
        "B. When the model predicts probability p, approximately p fraction of those predictions are actually",
        "C. The model produces confident predictions close to 0 or 1.",
        "D. The model has low variance across different training runs."
      ],
      "correct_answers": ["B"]
    },
    
    {
      "id": "3",
      "type": "single",
      "question": "3. The Brier Score decomposition reveals:",
      "options": [
        "A. Training loss + Test loss.",
        "B. Bias + Variance.",
        "C. Calibration error + Refinement (inherent uncertainty).",
        "D. Accuracy + Precision."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "4",
      "type": "single",
      "question": "4. In a reliability diagram, perfect calibration is represented by:",
      "options": [
        "A. A horizontal line at y = 0.5.",
        "B. The diagonal line y = x.",
        "C. A vertical line at x = 0.5.",
        "D. A random scattered pattern."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "5",
      "type": "single",
      "question": "5. When a reliability diagram shows the model’s curve above the diagonal y = x, this indicates:",
      "options": [
        "A. Perfect calibration (predicted positives = actually occurred).",
        "B. Overconfidence (predicted more positives than actually occurred).",
        "C. Underconfidence (predicted fewer positives than actually occurred).",
        "D. The model needs more training data."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "6",
      "type": "single",
      "question": "6. A proper loss function is one where:",
      "options": [
        "A. The loss is always positive.",
        "B. The loss is minimized when predicted probability equals true probability.",
        "C. The loss is symmetric around zero.",
        "D. The loss can only be computed on test data."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "7",
      "type": "single",
      "question": "7. Why do compititions incentivize model overconfidence?",
      "options": [
        "A. Overconfident models always achieve higher accuracy on the test set.",
        "B. When two models are equally accurate, the one with more confident predictions is more likely to",
        "C. The Brier score is used as the primary evaluation metric for ranking submissions.",
        "D. Overconfident models converge faster during training, reducing computational cost."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "8",
      "type": "single",
      "question": "8. If proper losses were used for rewards instead of accuracy-based winning, what would change?",
      "options": [
        "A. Models would be incentivized to become even more overconfident to maximize rewards.",
        "B. The incentive to extremify predictions would be reduced, rewarding honest probability estimates",
        "C. Overall model accuracy on the test set would significantly decrease across all submissions.",
        "D. The ability to calibrate models after training would become theoretically impossible."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "10",
      "type": "single",
      "question": "10. Why might isotonic regression overfit on small calibration sets?",
      "options": [
        "A. It has too few parameters.",
        "B. It is non-parametric and can learn spurious patterns.",
        "C. It uses sigmoid functions.",
        "D. It requires normalizing features."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "12",
      "type": "single",
      "question": "12. Which of the following is NOT an example of quantile mapping for calibration?",
      "options": [
        "A. Platt scaling.",
        "B. Isotonic regression.",
        "C. Temperature scaling.",
        "D. All of the above are examples."
      ],
      "correct_answers": ["D"]
    }
  ]
},


{
  "worksheet": "17 Vision",
  "questions": [
    {
      "id": "1",
      "type": "single",
      "question": "1. What key property distinguishes convolutional layers from fully connected layers?",
      "options": [
        "A. Larger parameter count.",
        "B. Use of non-linear activations only.",
        "C. Requirement of labeled data.",
        "D. Weight sharing across spatial locations."
      ],
      "correct_answers": ["D"]
    },
    {
      "id": "2",
      "type": "single",
      "question": "2. Weight sharing in CNNs primarily enables:",
      "options": [
        "A. Detection of the same feature at different spatial locations.",
        "B. Faster convergence due to higher learning rates and stochastic gradients.",
        "C. Exact translation and rotational invariance.",
        "D. Removal of bias terms."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "3",
      "type": "single",
      "question": "3. What problem do residual connections in ResNet address?",
      "options": [
        "A. Overfitting due to large datasets.",
        "B. Vanishing and exploding gradients.",
        "C. Lack of spatial locality.",
        "D. Class imbalance."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "4",
      "type": "single",
      "question": "4. Why was ImageNet influential for deep learning in vision?",
      "options": [
        "A. It introduced the concept of unsupervised learning.",
        "B. It provided large-scale labeled visual data.",
        "C. It eliminated the need for CNNs.",
        "D. It focused only on segmentation."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "5",
      "type": "single",
      "question": "5. What does Grad-CAM visualize for an image classifier?",
      "options": [
        "A. Learned convolutional filter patterns.",
        "B. Pixel-wise reconstruction errors.",
        "C. Gradients of the class score over image regions.",
        "D. The distribution of training samples."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "6",
      "type": "single",
      "question": "6. How does image segmentation differ from classification?",
      "options": [
        "A. Segmentation predicts a label per pixel.",
        "B. Segmentation uses unsupervised learning.",
        "C. Classification requires bounding boxes.",
        "D. Classification outputs structured predictions."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "7",
      "type": "single",
      "question": "7. Which challenge is specific to image segmentation?",
      "options": [
        "A. Difficulty optimizing very deep networks.",
        "B. Balancing fine spatial resolution with large receptive fields.",
        "C. Excessive model capacity relative to data size.",
        "D. Sharing representations across different objectives."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "8",
      "type": "single",
      "question": "8. What architectural idea is central to U-Net?",
      "options": [
        "A. Fully connected bottlenecks between encoder and decoder.",
        "B. Skip connections between encoder and decoder.",
        "C. Adversarial training.",
        "D. Recurrent layers."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "9",
      "type": "single",
      "question": "9. What is an image embedding?",
      "options": [
        "A. A pixel-wise probability map over an image.",
        "B. A compressed vector representation of an image.",
        "C. A textual description of an image.",
        "D. A generative model output."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "10",
      "type": "single",
      "question": "10. What is a linear probe in transfer learning?",
      "options": [
        "A. Training all layers jointly, and with similar learning rates.",
        "B. Training only the final classifier on fixed embeddings.",
        "C. Using contrastive loss between positive and negative samples.",
        "D. Removing the embedding layer."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "11",
      "type": "single",
      "question": "11. Few-shot learning primarily addresses:",
      "options": [
        "A. Large-scale labeled datasets.",
        "B. Learning with abundant supervision.",
        "C. Generalization with very limited labeled data.",
        "D. Training instability."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "12",
      "type": "single",
      "question": "12. Zero-shot learning requires:",
      "options": [
        "A. Pixel-level annotations.",
        "B. New labeled examples.",
        "C. External semantic information.",
        "D. Bayesian inference."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "13",
      "type": "single",
      "question": "13. What defines self-supervised learning?",
      "options": [
        "A. Learning with no data.",
        "B. Learning using synthetic labels derived from data.",
        "C. Learning with human annotations only.",
        "D. Learning using reinforcement signals."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "14",
      "type": "single",
      "question": "14. Why is self-supervised learning attractive?",
      "options": [
        "A. It avoids neural networks.",
        "B. It guarantees interpretability.",
        "C. It replaces supervised learning entirely.",
        "D. It leverages large amounts of unlabeled data."
      ],
      "correct_answers": ["D"]
    },
    {
      "id": "15",
      "type": "single",
      "question": "15. Inpainting as a self-supervised task trains a model to:",
      "options": [
        "A. Predict object labels.",
        "B. Segment objects.",
        "C. Generate captions.",
        "D. Fill in missing image regions."
      ],
      "correct_answers": ["D"]
    },
    {
      "id": "16",
      "type": "single",
      "question": "16. Colorization tasks encourage models to learn:",
      "options": [
        "A. Exact pixel reconstruction.",
        "B. Discrete class labels.",
        "C. Camera calibration.",
        "D. Semantic understanding of objects."
      ],
      "correct_answers": ["D"]
    },
    {
      "id": "17",
      "type": "single",
      "question": "17. Image captioning is best described as:",
      "options": [
        "A. Image classification.",
        "B. Image-to-image translation.",
        "C. Image-to-text sequence generation.",
        "D. Unsupervised clustering."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "18",
      "type": "single",
      "question": "18. Why is image captioning considered multimodal?",
      "options": [
        "A. It uses multiple cameras.",
        "B. It combines vision and language.",
        "C. It requires multiple datasets.",
        "D. It uses multiple loss functions."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "19",
      "type": "single",
      "question": "19. What role do image embeddings play in captioning?",
      "options": [
        "A. They replace the language model.",
        "B. They initialize pixel values.",
        "C. They provide visual context for text generation.",
        "D. They enforce grammatical structure."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "20",
      "type": "single",
      "question": "20. What distinguishes generative models from discriminative models?",
      "options": [
        "A. Generative models predict labels only.",
        "B. Generative models model the data distribution.",
        "C. Discriminative models require no data.",
        "D. Discriminative models generate samples."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "21",
      "type": "single",
      "question": "21. What is the core idea behind GANs?",
      "options": [
        "A. Direct optimization of likelihood.",
        "B. Adversarial training between two models.",
        "C. Explicit Bayesian probabilistic modeling.",
        "D. Supervised prediction with labels."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "22",
      "type": "single",
      "question": "22. What is mode collapse?",
      "options": [
        "A. Generator produces overly noisy samples.",
        "B. Generator ignores discriminator feedback.",
        "C. Generator produces limited diversity.",
        "D. Discriminator overfits."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "23",
      "type": "single",
      "question": "23. Why is tabular data difficult for GANs?",
      "options": [
        "A. Lack of labels.",
        "B. Mixed data types and imbalance.",
        "C. Small datasets only.",
        "D. Absence of correlations."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "24",
      "type": "single",
      "question": "24. What problem does CTGANs conditional generator address?",
      "options": [
        "A. Continuous normalization.",
        "B. Rare category underrepresentation.",
        "C. Overfitting of CNNs.",
        "D. Image resolution."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "25",
      "type": "single",
      "question": "25. Why does CTGAN use log-frequency sampling?",
      "options": [
        "A. To enforce uniform distributions.",
        "B. To oversample rare categories during training.",
        "C. To reduce computation.",
        "D. To simplify evaluation."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "26",
      "type": "single",
      "question": "26. What role does WGAN-GP play in CTGAN?",
      "options": [
        "A. Pixel normalization.",
        "B. Stable training via gradient control.",
        "C. Faster convergence via momentum.",
        "D. Discrete sampling."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "27",
      "type": "single",
      "question": "27. PacGAN reduces mode collapse by:",
      "options": [
        "A. Adding noise to inputs.",
        "B. Feeding multiple samples jointly to the critic.",
        "C. Removing the discriminator altogether.",
        "D. Enforcing KL divergence."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "28",
      "type": "single",
      "question": "28. Gumbel-Softmax is used to:",
      "options": [
        "A. Sample continuous noise.",
        "B. Enable differentiable categorical sampling.",
        "C. Reduce reconstruction loss.",
        "D. Normalize features."
      ],
      "correct_answers": ["B"]
    }
  ]
},

{
  "worksheet": "18 Text and NLP",
  "questions": [
    {
      "id": "1",
      "type": "single",
      "question": "1. Phonemes are best described as:",
      "options": [
        "A. Semantic units representing word meaning.",
        "B. Minimal sound units distinguishing speech sounds.",
        "C. Frequency-domain representations of speech.",
        "D. Characters used in written language."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "2",
      "type": "single",
      "question": "2. The Markov property assumes that:",
      "options": [
        "A. Future states depend on all past observations.",
        "B. The current state summarizes all relevant history.",
        "C. Observations are conditionally independent over time.",
        "D. Transition probabilities must be stationary."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "3",
      "type": "single",
      "question": "3. In a Hidden Markov Model, observations are:",
      "options": [
        "A. Deterministic functions of hidden states.",
        "B. Independent given the hidden state sequence.",
        "C. Dependent on all previous observations.",
        "D. Identical across time steps."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "4",
      "type": "single",
      "question": "4. A recurrent neural network (RNN) is:",
      "options": [
        "A. A feedforward network applied independently at each time step.",
        "B. A neural network that updates a hidden state across a sequence.",
        "C. A probabilistic graphical model with latent variables.",
        "D. A convolutional model for sequential data."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "5",
      "type": "single",
      "question": "5. A long short-term memory network (LSTM) is:",
      "options": [
        "A. A recurrent network that stores a fixed-size hidden state.",
        "B. A gated recurrent network designed to preserve long-term information.",
        "C. A sequence model built around self-attention mechanisms.",
        "D. A recurrent architecture that processes input in two directions."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "6",
      "type": "single",
      "question": "6. A bidirectional LSTM is:",
      "options": [
        "A. A recurrent network that stores a fixed-size hidden state.",
        "B. A gated recurrent network designed to preserve long-term information.",
        "C. A sequence model built around self-attention mechanisms.",
        "D. A recurrent architecture that processes input in two directions."
      ],
      "correct_answers": ["D"]
    },
    {
      "id": "7",
      "type": "single",
      "question": "7. Word embeddings are useful because they:",
      "options": [
        "A. Encode words as discrete symbolic identifiers.",
        "B. Represent semantic similarity geometrically.",
        "C. Eliminate the need for labeled data.",
        "D. Guarantee interpretability of features."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "8",
      "type": "single",
      "question": "8. An example of a contextual word embedding is:",
      "options": [
        "A. The embedding for 'bank' changing between financial and river contexts.",
        "B. The embedding for 'fish' being averaged over all different types of fish.",
        "C. The embedding for 'Jessica' determined by nearby word counts in a fixed window.",
        "D. The embedding for 'tesseract' learned once and reused across all sentences."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "9",
      "type": "single",
      "question": "9. Co-occurrence-based embeddings rely on the assumption that:",
      "options": [
        "A. Rare words often carry more semantic information.",
        "B. Words appearing in similar contexts have similar meanings.",
        "C. Syntax dominates semantics.",
        "D. Word order is usually irrelevant."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "10",
      "type": "single",
      "question": "10. The key innovation of transformers is:",
      "options": [
        "A. Convolution over word sequences.",
        "B. Self-attention replacing recurrence.",
        "C. Sparse feature representations.",
        "D. Explicit grammar modeling."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "11",
      "type": "single",
      "question": "11. Self-attention allows tokens to:",
      "options": [
        "A. Attend to all tokens in the sequence.",
        "B. Attend only to neighboring tokens.",
        "C. Attend only to earlier tokens.",
        "D. Attend only within fixed windows."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "12",
      "type": "single",
      "question": "12. Multi-head attention improves performance by:",
      "options": [
        "A. Allowing multiple representation subspaces.",
        "B. Increasing sequence length.",
        "C. Sharing attention weights across heads.",
        "D. Reducing model depth."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "13",
      "type": "single",
      "question": "13. A major computational drawback of transformers is:",
      "options": [
        "A. Vanishing gradients across layers.",
        "B. Quadratic complexity in sequence length.",
        "C. Inability to generalize.",
        "D. Poor optimization stability."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "14",
      "type": "single",
      "question": "14. A language model estimates:",
      "options": [
        "A. The semantic similarity between words.",
        "B. The probability of word sequences.",
        "C. The syntactic parse of sentences.",
        "D. The topic distribution of documents."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "15",
      "type": "single",
      "question": "15. Causal language models are trained to:",
      "options": [
        "A. Predict masked tokens anywhere in a sentence.",
        "B. Predict the next token given previous ones.",
        "C. Classify sentence sentiment.",
        "D. Encode bidirectional context."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "16",
      "type": "single",
      "question": "16. Masked language models differ by:",
      "options": [
        "A. Enforcing left-to-right decoding.",
        "B. Predicting randomly masked tokens.",
        "C. Using reinforcement learning.",
        "D. Avoiding self-supervision."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "17",
      "type": "single",
      "question": "17. Pretraining is valuable because it:",
      "options": [
        "A. Eliminates the need for task-specific data.",
        "B. Guarantees optimal downstream performance.",
        "C. Learns general representations from large corpora.",
        "D. Prevents overfitting entirely."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "18",
      "type": "single",
      "question": "18. Fine-tuning adapts models by:",
      "options": [
        "A. Retraining from scratch on new data.",
        "B. Freezing all parameters permanently.",
        "C. Updating representations for specific tasks.",
        "D. Increasing model size."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "19",
      "type": "single",
      "question": "19. Zero-shot learning refers to:",
      "options": [
        "A. Training without any labeled data at all.",
        "B. Using synthetic data for supervised learning over task-specific data.",
        "C. Applying a pretrained model without task-specific training.",
        "D. Removing the output layer."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "20",
      "type": "single",
      "question": "20. Adapters are designed to:",
      "options": [
        "A. Replace certain layers of pretrained models.",
        "B. Add small trainable modules to frozen networks.",
        "C. Reduce inference latency only.",
        "D. Enforce sparsity in activations."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "21",
      "type": "single",
      "question": "21. Low-rank adaptation (LoRA) reduces cost by:",
      "options": [
        "A. Training fewer layers.",
        "B. Learning low-rank updates.",
        "C. Sharing embeddings across tasks.",
        "D. Quantizing model parameters."
      ],
      "correct_answers": ["B"]
    }
  ]
},


{
  "worksheet": "19 Data and Labels",
  "questions": [
    {
      "id": "1",
      "type": "single",
      "question": "1. Labels are often the bottleneck in machine learning because they are:",
      "options": [
        "A. Expensive to store and compress.",
        "B. Costly and time-consuming to obtain.",
        "C. Always inconsistent across datasets.",
        "D. Unnecessary for modern models."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "2",
      "type": "single",
      "question": "2. Poor label quality most directly affects:",
      "options": [
        "A. Model architecture design.",
        "B. Training time complexity.",
        "C. Generalization performance.",
        "D. Feature dimensionality."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "3",
      "type": "single",
      "question": "3. Semi-supervised learning primarily combines:",
      "options": [
        "A. Multiple labeled datasets.",
        "B. Few labeled examples with many unlabeled ones.",
        "C. Human labels with synthetic labels only.",
        "D. Reinforcement learning with supervision."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "4",
      "type": "single",
      "question": "4. Label propagation methods rely on:",
      "options": [
        "A. Explicit rules provided by experts.",
        "B. Graph structure among data points.",
        "C. High-capacity neural networks.",
        "D. Random label assignment."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "5",
      "type": "single",
      "question": "5. ImageNet labels were primarily obtained via:",
      "options": [
        "A. Automated web scraping.",
        "B. Expert-only annotation teams.",
        "C. Crowdsourcing with verification.",
        "D. Self-supervised learning."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "6",
      "type": "single",
      "question": "6. A key advantage of Amazon Mechanical Turk was:",
      "options": [
        "A. Perfect label accuracy.",
        "B. Low latency GPU computation.",
        "C. Massive scalability of annotation.",
        "D. Elimination of human bias."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "7",
      "type": "single",
      "question": "7. Showing each item to multiple annotators helps to:",
      "options": [
        "A. Increase class imbalance.",
        "B. Reduce individual annotator noise.",
        "C. Remove the need for aggregation.",
        "D. Guarantee ground-truth labels."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "8",
      "type": "single",
      "question": "8. Majority voting is an example of:",
      "options": [
        "A. Weak supervision.",
        "B. Label aggregation.",
        "C. Active learning.",
        "D. Self-training."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "9",
      "type": "single",
      "question": "9. Gold-standard checks are used to:",
      "options": [
        "A. Speed up annotation.",
        "B. Measure annotator reliability.",
        "C. Remove rare classes.",
        "D. Generate synthetic labels."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "10",
      "type": "single",
      "question": "10. The Dawid-Skene model assumes:",
      "options": [
        "A. All annotators are equally accurate.",
        "B. Each annotator has a confusion matrix.",
        "C. Labels are noise-free.",
        "D. Classes are linearly separable."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "11",
      "type": "single",
      "question": "11. Active learning reduces labeling cost by:",
      "options": [
        "A. Training on smaller models.",
        "B. Querying only informative examples.",
        "C. Eliminating human annotators.",
        "D. Using synthetic labels exclusively."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "12",
      "type": "single",
      "question": "12. Uncertainty sampling selects points where the model:",
      "options": [
        "A. Has highest confidence.",
        "B. Predicts the majority class.",
        "C. Is least confident.",
        "D. Has highest loss historically."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "13",
      "type": "single",
      "question": "13. Query-by-committee relies on:",
      "options": [
        "A. Agreement across multiple models.",
        "B. Disagreement across multiple models.",
        "C. Human disagreement only.",
        "D. Randomized selection."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "14",
      "type": "single",
      "question": "14. Weak supervision differs from full supervision because it:",
      "options": [
        "A. Uses heuristics or noisy sources.",
        "B. Requires expert annotators only.",
        "C. Guarantees exact labels.",
        "D. Avoids aggregation."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "15",
      "type": "single",
      "question": "15. Reinforcement learning differs from supervised learning because it:",
      "options": [
        "A. Requires labeled input-output pairs.",
        "B. Learns from delayed reward signals.",
        "C. Uses only unsupervised objectives.",
        "D. Cannot use neural networks."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "16",
      "type": "single",
      "question": "16. In RLHF, the reward function is:",
      "options": [
        "A. Hand-coded by engineers.",
        "B. Learned from human preferences.",
        "C. Fixed by the environment.",
        "D. Eliminated entirely."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "17",
      "type": "single",
      "question": "17. PPO differs from DPO because PPO:",
      "options": [
        "A. Requires explicit reward models.",
        "B. Avoids KL regularization.",
        "C. Uses supervised labels only.",
        "D. Eliminates sampling."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "18",
      "type": "single",
      "question": "18. DPO avoids training a reward model by:",
      "options": [
        "A. Using contrastive preference losses.",
        "B. Sampling trajectories online.",
        "C. Removing human feedback.",
        "D. Freezing all parameters."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "19",
      "type": "single",
      "question": "19. A Bayesian Network represents a joint distribution by:",
      "options": [
        "A. Assuming all variables are independent.",
        "B. Modeling variables with a single global likelihood.",
        "C. Factorizing the distribution using conditional dependencies.",
        "D. Learning embeddings for each variable."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "20",
      "type": "single",
      "question": "20. Why can a Bayesian Network be used to generate synthetic data?",
      "options": [
        "A. It memorizes training samples exactly.",
        "B. It defines a joint distribution over all variables.",
        "C. It requires labeled outputs for sampling.",
        "D. It optimizes a discriminator loss."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "21",
      "type": "single",
      "question": "21. Why are Bayesian Networks rarely used for large-scale synthetic data generation today?",
      "options": [
        "A. They cannot model uncertainty.",
        "B. Conditional tables scale poorly with many parents or categories.",
        "C. They require continuous variables only.",
        "D. They cannot represent dependencies between variables."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "22",
      "type": "single",
      "question": "22. Simulated data is most useful when real data is:",
      "options": [
        "A. Abundant and unbiased.",
        "B. Cheap and fast to collect.",
        "C. Scarce or dangerous to obtain.",
        "D. Perfectly labeled."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "23",
      "type": "single",
      "question": "23. Self-play generates labels by:",
      "options": [
        "A. Human annotation.",
        "B. Model competition against itself.",
        "C. Random exploration only.",
        "D. Offline replay."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "24",
      "type": "single",
      "question": "24. Knowledge distillation trains a student model using:",
      "options": [
        "A. Outputs of a teacher model.",
        "B. Ground-truth labels only.",
        "C. Reinforcement learning rewards.",
        "D. Human feedback directly."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "25",
      "type": "single",
      "question": "25. Soft targets in distillation refer to:",
      "options": [
        "A. Hard class assignments.",
        "B. Intermediate gradients.",
        "C. Randomized labels.",
        "D. Full probability distributions."
      ],
      "correct_answers": ["D"]
    },
    {
      "id": "26",
      "type": "multiple",
      "question": "26. Which of the following are examples of knowledge-distilled models or distillation frameworks? (Select all that apply.)",
      "options": [
        "A. ResNet",
        "B. DistilNet",
        "C. PCA",
        "D. FitNets",
        "E. Word2Vec",
        "F. TinyNet",
        "G. AlexNet",
        "H. DeepSeek"
      ],
      "correct_answers": ["B","D","F"]
    },
    {
      "id": "27",
      "type": "single",
      "question": "27. A major benefit of distillation is:",
      "options": [
        "A. Higher theoretical accuracy.",
        "B. Faster and cheaper deployment.",
        "C. Elimination of training data.",
        "D. Removal of bias."
      ],
      "correct_answers": ["B"]
    }
  ]
},


{
  "worksheet": "20 Big Data Science",
  "questions": [
    {
      "id": "1",
      "type": "multiple",
      "question": "1. (Multiple correct) Which of the following correctly distinguish parallel computing from distributed computing?",
      "options": [
        "A. Parallel computing uses multiple processors (or cores) within a single machine to perform computations simultaneously.",
        "B. Distributed computing uses multiple nodes connected via a network.",
        "C. Distributed computing partitions data and tasks across machines.",
        "D. Parallel computing necessarily involves communication over a network.",
        "E. Distributed computing involves communication between nodes."
      ],
      "correct_answers": ["A","B","C","E"]
    },
    {
      "id": "2",
      "type": "single",
      "question": "2. High Performance Computing (HPC) typically refers to",
      "options": [
        "A. Using consumer laptops for large-scale analytics",
        "B. Supercomputers or large clusters for intensive computation",
        "C. Cloud storage systems",
        "D. Running small scripts"
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "3",
      "type": "multiple",
      "question": "3. (Multiple correct) Advantages of parallel computing include",
      "options": [
        "A. Reduced execution time for large tasks",
        "B. Ability to handle larger datasets",
        "C. Guaranteed cost reduction",
        "D. Improved throughput"
      ],
      "correct_answers": ["A","B","D"]
    },
    {
      "id": "4",
      "type": "single",
      "question": "4. A GPU is well-suited for parallel workloads because",
      "options": [
        "A. It has thousands of small cores optimized for data-parallel operations",
        "B. It has higher single-thread performance",
        "C. It uses slower memory",
        "D. It runs only sequential algorithms"
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "5",
      "type": "single",
      "question": "5. A data lake stores",
      "options": [
        "A. Only structured data with a fixed schema",
        "B. Raw, unprocessed data in various formats",
        "C. Only relational data tables",
        "D. Normalized transactional records only"
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "6",
      "type": "multiple",
      "question": "6. (Multiple correct) Data warehouses are characterized by",
      "options": [
        "A. Structured data with schema-on-write",
        "B. Optimized for analytics and reporting",
        "C. Raw unstructured storage",
        "D. ETL processes to transform and load data"
      ],
      "correct_answers": ["A","B","D"]
    },
    {
      "id": "7",
      "type": "single",
      "question": "7. What is a schema in the context of databases?",
      "options": [
        "A. A structured definition describing the organization of data (tables, fields, relationships)",
        "B. A database engine used to execute queries",
        "C. An unstructured collection of raw data",
        "D. A query language for interacting with databases"
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "8",
      "type": "single",
      "question": "8. Schema-on-read means",
      "options": [
        "A. Data schema is applied when writing to storage",
        "B. Schema is applied only when reading/processing data",
        "C. Data has no schema ever",
        "D. Schema must match relational database rules"
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "9",
      "type": "multiple",
      "question": "9. (Multiple correct) Examples of file formats for big data include",
      "options": [
        "A. CSV",
        "B. JSON",
        "C. Parquet",
        "D. JPEG"
      ],
      "correct_answers": ["A","B","C"]
    },
    {
      "id": "10",
      "type": "single",
      "question": "10. ETL stands for",
      "options": [
        "A. Extract, Transform, Load",
        "B. Evaluate, Test, Learn",
        "C. Execute, Transfer, Log",
        "D. Encode, Train, Label"
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "11",
      "type": "multiple",
      "question": "11. (Multiple correct) Workflow orchestration tools typically",
      "options": [
        "A. Schedule and monitor data pipelines",
        "B. Retry failed tasks",
        "C. Only run machine learning models",
        "D. Handle dependencies between steps"
      ],
      "correct_answers": ["A","B","D"]
    },
    {
      "id": "12",
      "type": "single",
      "question": "12. MapReduce is a",
      "options": [
        "A. Programming model for distributed computation over large datasets",
        "B. Visualization library",
        "C. GPU acceleration framework",
        "D. SQL engine"
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "13",
      "type": "multiple",
      "question": "13. (Multiple correct) Advantages of Spark over MapReduce include",
      "options": [
        "A. Faster in-memory processing",
        "B. Support for iterative algorithms",
        "C. Built-in libraries for ML and graph processing",
        "D. Guaranteed lower cost"
      ],
      "correct_answers": ["A","B","C"]
    },
    {
      "id": "14",
      "type": "single",
      "question": "14. A dashboard in big data systems",
      "options": [
        "A. Displays real-time or aggregated metrics visually",
        "B. Runs ETL jobs",
        "C. Stores raw data",
        "D. Controls GPU allocation"
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "15",
      "type": "multiple",
      "question": "15. (Multiple correct) Monitoring big data pipelines can involve",
      "options": [
        "A. Tracking job completion/failures",
        "B. Measuring throughput and latency",
        "C. Ignoring anomalies",
        "D. Detecting data drift"
      ],
      "correct_answers": ["A","B","D"]
    },
    {
      "id": "16",
      "type": "single",
      "question": "16. (Single correct) Differential privacy aims to",
      "options": [
        "A. Prevent disclosure of individual data points",
        "B. Increase computation speed",
        "C. Compress datasets",
        "D. Remove redundant records"
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "18",
      "type": "single",
      "question": "18. Data drift refers to",
      "options": [
        "A. Changes in input data distribution over time",
        "B. Static datasets remaining unchanged",
        "C. Label noise",
        "D. Loss of parallelism"
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "19",
      "type": "single",
      "question": "19. Serverless computing refers to",
      "options": [
        "A. Running code without provisioning or managing servers, with resources allocated automatically by",
        "B. Running applications entirely on local machines without any server interaction",
        "C. A compute model where there are no servers involved at all",
        "D. Deploying applications only in on-premise data centers"
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "20",
      "type": "single",
      "question": "20. In A/B testing, the main goal is to",
      "options": [
        "A. Compare two or more variants to determine which performs better on a defined metric",
        "B. Randomly assign users to different servers",
        "C. Eliminate the need for statistical analysis",
        "D. Test all possible parameter combinations exhaustively"
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "21",
      "type": "multiple",
      "question": "21. (Multiple correct) Good practices in workflow management systems include",
      "options": [
        "A. Defining clear task dependencies",
        "B. Enabling automatic retries for failed tasks",
        "C. Avoiding any form of monitoring or logging",
        "D. Scheduling tasks to optimize resource usage"
      ],
      "correct_answers": ["A","B","D"]
    },
    {
      "id": "22",
      "type": "multiple",
      "question": "22. Which of the following is a benefit of serverless architectures for data workflows?",
      "options": [
        "A. Automatic scaling to match workload",
        "B. Pay-per-execution cost model",
        "C. Guaranteed zero latency",
        "D. No need for writing application logic"
      ],
      "correct_answers": ["A","B"]
    },
    {
      "id": "23",
      "type": "single",
      "question": "23. An inverted index primarily maps:",
      "options": [
        "A. Documents to their outgoing hyperlinks.",
        "B. Terms to the list of documents containing them.",
        "C. Queries to ranked result lists.",
        "D. Documents to dense embedding vectors."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "24",
      "type": "single",
      "question": "24. In BM25, the role of inverse document frequency (IDF) is to:",
      "options": [
        "A. Penalize documents with repeated words.",
        "B. Downweight very common query terms.",
        "C. Normalize document length differences.",
        "D. Smooth term frequencies within documents."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "25",
      "type": "single",
      "question": "25. PageRank can be interpreted as:",
      "options": [
        "A. The shortest-path distance between web pages.",
        "B. The steady-state probability of a random walk.",
        "C. The degree centrality of a node.",
        "D. The clustering coefficient of the graph."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "26",
      "type": "single",
      "question": "26. Personalized PageRank differs from standard PageRank because it:",
      "options": [
        "A. Uses weighted edges instead of binary links.",
        "B. Biases teleportation toward a specific distribution.",
        "C. Removes dangling nodes from the graph.",
        "D. Normalizes scores per query term."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "27",
      "type": "single",
      "question": "27. Maximum Inner Product Search (MIPS) is used to:",
      "options": [
        "A. Compute PageRank efficiently.",
        "B. Find vectors most similar to a query embedding.",
        "C. Sort documents by length-normalized frequency.",
        "D. Traverse nearest-neighbor graphs greedily."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "28",
      "type": "single",
      "question": "28. KD-trees tend to perform poorly when:",
      "options": [
        "A. The dimensionality of the data is high.",
        "B. The dataset contains duplicate points.",
        "C. The number of queries is small.",
        "D. The data distribution is clustered."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "29",
      "type": "single",
      "question": "29. Graph-based ANN methods differ from brute-force MIPS because they:",
      "options": [
        "A. Compare the query to every stored vector.",
        "B. Require labeled relevance judgments.",
        "C. Traverse only local neighborhoods of similar items.",
        "D. Use tree-based partitioning of space."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "30",
      "type": "single",
      "question": "30. A search graph typically connects each document to:",
      "options": [
        "A. Randomly sampled documents.",
        "B. All documents sharing at least one keyword.",
        "C. Its nearest neighbors under a similarity metric.",
        "D. Documents with similar lengths."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "31",
      "type": "single",
      "question": "31. In graph-based nearest neighbor search, a local optimum refers to:",
      "options": [
        "A. A node whose neighbors all have lower similarity to the query.",
        "B. A globally nearest document under the similarity metric.",
        "C. A cluster center produced by vector quantization.",
        "D. A node with maximum degree in the search graph."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "32",
      "type": "single",
      "question": "32. Greedy graph search may fail because it:",
      "options": [
        "A. Requires full graph traversal.",
        "B. Can become trapped in local optima.",
        "C. Scales quadratically with corpus size.",
        "D. Assumes uniform node degree."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "33",
      "type": "single",
      "question": "33. Running multiple parallel graph searches helps to:",
      "options": [
        "A. Reduce embedding dimensionality.",
        "B. Eliminate the need for reranking.",
        "C. Guarantee exact nearest neighbors.",
        "D. Escape poor local regions of the graph."
      ],
      "correct_answers": ["D"]
    },
    {
      "id": "34",
      "type": "single",
      "question": "34. HNSW improves search efficiency primarily by:",
      "options": [
        "A. Organizing nodes into hierarchical layers.",
        "B. Using randomized hash functions.",
        "C. Compressing vectors with product quantization.",
        "D. Replacing similarity with distance thresholds."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "35",
      "type": "single",
      "question": "35. The main purpose of a second-stage reranker in retrieval systems is to:",
      "options": [
        "A. Accelerate approximate nearest neighbor graph traversal.",
        "B. Refine coarse retrieval results using a more expressive model.",
        "C. Eliminate the need for an index structure.",
        "D. Calibrate similarity scores across different queries."
      ],
      "correct_answers": ["B"]
    }
  ]
},

{
  "worksheet": "21 Agentic AI",
  "questions": [
    {
      "id": "1",
      "type": "single",
      "question": "1. A large language model (LLM) is best described as:",
      "options": [
        "A. A symbolic reasoning engine that applies hand-coded grammar rules to large corpora of text.",
        "B. A neural network trained on massive text corpora to predict the next token given a context.",
        "C. A database that retrieves memorized sentences from its web-based training data.",
        "D. A rule-based chatbot augmented with search and heuristics."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "2",
      "type": "single",
      "question": "2. Prompt programming refers to:",
      "options": [
        "A. Updating a pretrained model’s parameters using labeled task-specific datasets.",
        "B. Optimizing prompt length to reduce latency and inference cost.",
        "C. Filtering or rewriting model outputs after generation to enforce constraints.",
        "D. Designing textual input containing instructions, examples, and context for a desired task."
      ],
      "correct_answers": ["D"]
    },
    {
      "id": "3",
      "type": "single",
      "question": "3. Few-shot prompting works primarily because:",
      "options": [
        "A. The model memorizes the examples exactly.",
        "B. The model infers task structure from examples in context.",
        "C. The examples update the model weights temporarily.",
        "D. The examples act as labeled training data."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "4",
      "type": "single",
      "question": "4. Compared to fine-tuning, prompting",
      "options": [
        "A. Requires no labeled data and no parameter updates.",
        "B. Produces strictly better performance on all tasks.",
        "C. Eliminates hallucinations entirely.",
        "D. Guarantees reproducible outputs."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "5",
      "type": "single",
      "question": "5. In LLMs, the context refers to:",
      "options": [
        "A. Only the user’s most recent question.",
        "B. The hidden state stored between sessions.",
        "C. The full sequence of tokens used to generate output.",
        "D. The training corpus used during pretraining."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "6",
      "type": "single",
      "question": "6. Increasing context length primarily enables:",
      "options": [
        "A. Faster inference times.",
        "B. Larger model parameter counts.",
        "C. Multi-step reasoning over long documents.",
        "D. Guaranteed logical consistency."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "7",
      "type": "single",
      "question": "7. A limitation of long-context models is that:",
      "options": [
        "A. Attention computation scales poorly with length.",
        "B. They cannot use external tools.",
        "C. They require labeled documents.",
        "D. They eliminate the need for retrieval."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "8",
      "type": "single",
      "question": "8. Chain-of-thought prompting improves performance by:",
      "options": [
        "A. Forcing the model to reveal internal weights at each step.",
        "B. Encouraging intermediate reasoning steps before answers.",
        "C. Reducing the number of tokens generated.",
        "D. Preventing hallucinations by design."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "9",
      "type": "single",
      "question": "9. Chain-of-thought prompting is most effective when:",
      "options": [
        "A. The model is small and highly regularized.",
        "B. The task requires no reasoning.",
        "C. The model has sufficient scale and capacity.",
        "D. The output format is strictly constrained."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "10",
      "type": "single",
      "question": "10. Retrieval-Augmented Generation (RAG) combines:",
      "options": [
        "A. Supervised learning and reinforcement learning.",
        "B. Symbolic reasoning and neural decoding.",
        "C. Document retrieval and conditional text generation.",
        "D. Compression and encryption."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "11",
      "type": "single",
      "question": "11. The main purpose of retrieval in RAG systems is to:",
      "options": [
        "A. Eliminate the need for large-scale pretraining on text corpora.",
        "B. Inject relevant external knowledge into the model during inference.",
        "C. Decrease the number of parameters required by the language model.",
        "D. Guarantee faster response times through reduced computation."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "12",
      "type": "single",
      "question": "12. RAG reduces hallucinations primarily because:",
      "options": [
        "A. The model stops generating tokens.",
        "B. The model is retrained on verified data.",
        "C. The model conditions on retrieved factual context.",
        "D. The model enforces logical constraints."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "13",
      "type": "single",
      "question": "13. In a typical RAG pipeline, retrieved documents are:",
      "options": [
        "A. Used to update model weights online.",
        "B. Appended to the prompt context.",
        "C. Converted into symbolic rules.",
        "D. Stored permanently in memory."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "14",
      "type": "single",
      "question": "14. Toolformer demonstrated that LLMs can:",
      "options": [
        "A. Learn to call tools without supervised tool labels.",
        "B. Replace external tools entirely by their internal knowledge.",
        "C. Perform exact symbolic computation reliably.",
        "D. Eliminate prompt engineering."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "15",
      "type": "single",
      "question": "15. Function calling APIs enable LLMs to:",
      "options": [
        "A. Modify their own weights through html calls.",
        "B. Output structured calls to external services.",
        "C. Access private training data across networks.",
        "D. Bypass safety constraints."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "16",
      "type": "single",
      "question": "16. ReAct agents combine:",
      "options": [
        "A. Reinforcement learning and supervised fine-tuning.",
        "B. Reasoning steps and tool-based actions.",
        "C. Retrieval and compression.",
        "D. Symbolic planners and SAT solvers."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "17",
      "type": "single",
      "question": "17. Compared to pure chain-of-thought, ReAct additionally:",
      "options": [
        "A. Eliminates reasoning traces.",
        "B. Allows intermediate tool interaction.",
        "C. Reduces model size.",
        "D. Requires labeled action datasets."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "18",
      "type": "single",
      "question": "18. An agentic AI system is best described as:",
      "options": [
        "A. A forward pass of an LLM that is constantly being trained.",
        "B. A static chatbot with memory disabled.",
        "C. A system that plans, acts, and iterates over multiple steps.",
        "D. A fine-tuned classifier."
      ],
      "correct_answers": ["C"]
    },
    {
      "id": "19",
      "type": "single",
      "question": "19. A defining feature of agentic systems is:",
      "options": [
        "A. Stateless inference.",
        "B. Autonomous multi-step decision making.",
        "C. Guaranteed optimal planning for robots.",
        "D. Deterministic outputs."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "20",
      "type": "single",
      "question": "20. Memory in agentic systems is used to:",
      "options": [
        "A. Store model weights permanently.",
        "B. Track state across interactions.",
        "C. Replace retrieval systems.",
        "D. Improve GPU utilization."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "21",
      "type": "single",
      "question": "21. In the context of large language models, a hallucination refers to:",
      "options": [
        "A. The generation of fluent but factually incorrect or unsupported content.",
        "B. The production of outputs that are shorter than expected due to truncation.",
        "C. The memorization and repetition of training data verbatim.",
        "D. The inability of a model to generalize beyond its training distribution."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "22",
      "type": "single",
      "question": "22. Hallucinations occur primarily because:",
      "options": [
        "A. Models retrieve incorrect documents.",
        "B. Models optimize likelihood, not truth.",
        "C. Models are trained with reinforcement learning.",
        "D. Models use attention mechanisms."
      ],
      "correct_answers": ["B"]
    },
    {
      "id": "23",
      "type": "single",
      "question": "23. In production systems, RAG is often preferred over fine-tuning because it:",
      "options": [
        "A. Is cheaper and easier to update.",
        "B. Produces larger models.",
        "C. Requires more labeled data.",
        "D. Eliminates the need for evaluation."
      ],
      "correct_answers": ["A"]
    },
    {
      "id": "24",
      "type": "single",
      "question": "24. A reranker in a retrieval system is used to:",
      "options": [
        "A. Replace the vector index with a more descriptive transfer function.",
        "B. Improve precision using a more expressive model.",
        "C. Reduce embedding dimensionality.",
        "D. Enforce query normalization."
      ],
      "correct_answers": ["B"]
    }
  ]
}

]



