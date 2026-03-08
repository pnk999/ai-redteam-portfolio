\# AI Red Teaming \& Model Evaluation Portfolio



\## Overview



This repository contains my work in \*\*AI red teaming and large language model evaluation\*\*.

The focus of these projects is analyzing \*\*safety behavior, adversarial vulnerabilities, and instruction robustness\*\* in modern language models.



Rather than collecting isolated jailbreaks, these studies aim to understand \*\*systematic behavioral patterns\*\* and identify potential weaknesses in model safety mechanisms.



---



\## Research Focus



My work explores several areas relevant to AI safety and adversarial testing:



\* Prompt injection and instruction hierarchy failures

\* Safety refusal consistency across prompt framing

\* Multi-turn conversational manipulation

\* Behavioral analysis of model responses to adversarial inputs



Each project follows a structured evaluation process including \*\*threat modeling, hypothesis-driven testing, and behavioral analysis\*\*.



---



\## Methodology



The evaluation workflow used in these projects typically includes:



1\. Defining a \*\*threat model\*\* and risk scenario

2\. Designing adversarial prompt sets or conversation scripts

3\. Running structured evaluations across models

4\. Labeling responses using consistent safety categories

5\. Analyzing behavioral patterns and failure modes

6\. Proposing potential mitigation strategies



The goal is to understand \*\*why models behave the way they do\*\*, not just whether a single attack succeeds.



---



\## Tools and Environment



Tools used in these experiments include:



Python 3.11 (conda)

Promptfoo (structured evals)

Garak (LLM vulnerability scanning)

Jupyter Notebooks





---



\## Projects



\### Refusal Consistency Across Prompt Framing



Study of how safety refusals change when restricted requests are framed differently (direct request, fictional narrative, academic discussion, etc.).



Key focus:



\* consistency of refusal behavior

\* influence of prompt framing

\* safety explanation patterns



---



\### Prompt Injection and Instruction Hierarchy



Evaluation of how models handle \*\*instructions embedded inside documents or external content\*\*.



Key focus:



\* instruction hierarchy conflicts

\* hidden prompt injections

\* detection of malicious instructions



---



\### Multi-Turn Manipulation in Conversations



Analysis of how model responses evolve across \*\*multi-turn interactions\*\* where requests gradually escalate.



Key focus:



\* compliance drift across conversation turns

\* gradual reframing attacks

\* conversational safety boundaries



---



\## Key Questions Explored



Across these studies I investigate questions such as:



\* How consistent are model safety refusals across different prompt framings?

\* Do models follow instructions embedded inside documents?

\* How does conversation history influence safety behavior?

\* What behavioral patterns reveal weaknesses in safety mechanisms?



---



\## Repository Structure



```

ai-redteam-portfolio



projects/

\\\\\\\&nbsp;  refusal-consistency

\\\\\\\&nbsp;  prompt-injection

\\\\\\\&nbsp;  multi-turn-manipulation



notebooks/

\\\\\\\&nbsp;  evaluation-analysis



reports/

\\\\\\\&nbsp;  project-reports

```



Each project includes:



\* prompt sets or conversation scripts

\* evaluation results

\* analysis notebooks

\* structured research reports



---



\## Purpose of This Portfolio



This portfolio documents ongoing work in \*\*AI red teaming and model safety analysis\*\*.



The goal is to contribute to understanding how large language models behave under adversarial or ambiguous conditions, and how their safety mechanisms might be improved.



