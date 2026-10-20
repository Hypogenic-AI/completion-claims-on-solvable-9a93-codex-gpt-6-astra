# Downloaded papers

27 unique papers, downloaded from primary public sources and PDF-parsed. Five full chunked reviews (100 pages total); all other downloaded papers are explicitly screened at abstract/selected-section depth. Full page-by-page notes: `../evidence/reading_log.md`. Raw bibliographic metadata and SHA-256: `../evidence/papers_manifest.json`.

Recreate PDFs from the workspace root: `.venv/bin/python scripts/download_papers.py`. Split with `.venv/bin/python .codex/skills/paper-finder/scripts/pdf_chunker.py papers/FILE.pdf --pages-per-chunk 3`. PDFs and chunk files remain local, excluded from git; index/manifests/scripts are retained.

## 1. $τ$-bench: A Benchmark for Tool-Agent-User Interaction in Real-World Domains

- Authors: Shunyu Yao, Noah Shinn, Pedram Razavi, Karthik Narasimhan
- Year: 2024; arXiv: 2406.12045v1; 50 pages.
- Local PDF: [2406.12045_tau_bench.pdf](2406.12045_tau_bench.pdf).
- State-based database scoring and repeated-run pass^k; retail/airline user simulation. Background: evaluator pattern, not a direct false-DONE experiment.

## 2. AppWorld: A Controllable World of Apps and People for Benchmarking Interactive Coding Agents

- Authors: Harsh Trivedi, Tushar Khot, Mareike Hartmann, Ruskin Manku, Vinty Dong, Edward Li, Shashank Gupta, Ashish Sabharwal, Niranjan Balasubramanian
- Year: 2024; arXiv: 2407.18901v1; 55 pages.
- Local PDF: [2407.18901_appworld.pdf](2407.18901_appworld.pdf).
- 750 tasks, 9 apps, 457 APIs and collateral-state checks. Background: authoritative world-state evaluation; full environment pruned for implementation cost.

## 3. DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

- Authors:  DeepSeek-AI, Daya Guo, Dejian Yang, Haowei Zhang, Junxiao Song, Peiyi Wang, Qihao Zhu, Runxin Xu, Ruoyu Zhang, Shirong Ma, Xiao Bi, Xiaokang Zhang, Xingkai Yu, Yu Wu, Z. F. Wu, Zhibin Gou, Zhihong Shao, Zhuoshu Li, Ziyi Gao, Aixin Liu, Bing Xue, Bingxuan Wang, Bochao Wu, Bei Feng, Chengda Lu, Chenggang Zhao, Chengqi Deng, Chenyu Zhang, Chong Ruan, Damai Dai, Deli Chen, Dongjie Ji, Erhang Li, Fangyun Lin, Fucong Dai, Fuli Luo, Guangbo Hao, Guanting Chen, Guowei Li, H. Zhang, Han Bao, Hanwei Xu, Haocheng Wang, Honghui Ding, Huajian Xin, Huazuo Gao, Hui Qu, Hui Li, Jianzhong Guo, Jiashi Li, Jiawei Wang, Jingchang Chen, Jingyang Yuan, Junjie Qiu, Junlong Li, J. L. Cai, Jiaqi Ni, Jian Liang, Jin Chen, Kai Dong, Kai Hu, Kaige Gao, Kang Guan, Kexin Huang, Kuai Yu, Lean Wang, Lecong Zhang, Liang Zhao, Litong Wang, Liyue Zhang, Lei Xu, Leyi Xia, Mingchuan Zhang, Minghua Zhang, Minghui Tang, Meng Li, Miaojun Wang, Mingming Li, Ning Tian, Panpan Huang, Peng Zhang, Qiancheng Wang, Qinyu Chen, Qiushi Du, Ruiqi Ge, Ruisong Zhang, Ruizhe Pan, Runji Wang, R. J. Chen, R. L. Jin, Ruyi Chen, Shanghao Lu, Shangyan Zhou, Shanhuang Chen, Shengfeng Ye, Shiyu Wang, Shuiping Yu, Shunfeng Zhou, Shuting Pan, S. S. Li, Shuang Zhou, Shaoqing Wu, Shengfeng Ye, Tao Yun, Tian Pei, Tianyu Sun, T. Wang, Wangding Zeng, Wanjia Zhao, Wen Liu, Wenfeng Liang, Wenjun Gao, Wenqin Yu, Wentao Zhang, W. L. Xiao, Wei An, Xiaodong Liu, Xiaohan Wang, Xiaokang Chen, Xiaotao Nie, Xin Cheng, Xin Liu, Xin Xie, Xingchao Liu, Xinyu Yang, Xinyuan Li, Xuecheng Su, Xuheng Lin, X. Q. Li, Xiangyue Jin, Xiaojin Shen, Xiaosha Chen, Xiaowen Sun, Xiaoxiang Wang, Xinnan Song, Xinyi Zhou, Xianzu Wang, Xinxia Shan, Y. K. Li, Y. Q. Wang, Y. X. Wei, Yang Zhang, Yanhong Xu, Yao Li, Yao Zhao, Yaofeng Sun, Yaohui Wang, Yi Yu, Yichao Zhang, Yifan Shi, Yiliang Xiong, Ying He, Yishi Piao, Yisong Wang, Yixuan Tan, Yiyang Ma, Yiyuan Liu, Yongqiang Guo, Yuan Ou, Yuduan Wang, Yue Gong, Yuheng Zou, Yujia He, Yunfan Xiong, Yuxiang Luo, Yuxiang You, Yuxuan Liu, Yuyang Zhou, Y. X. Zhu, Yanhong Xu, Yanping Huang, Yaohui Li, Yi Zheng, Yuchen Zhu, Yunxian Ma, Ying Tang, Yukun Zha, Yuting Yan, Z. Z. Ren, Zehui Ren, Zhangli Sha, Zhe Fu, Zhean Xu, Zhenda Xie, Zhengyan Zhang, Zhewen Hao, Zhicheng Ma, Zhigang Yan, Zhiyu Wu, Zihui Gu, Zijia Zhu, Zijun Liu, Zilin Li, Ziwei Xie, Ziyang Song, Zizheng Pan, Zhen Huang, Zhipeng Xu, Zhongyu Zhang, Zhen Zhang
- Year: 2025; arXiv: 2501.12948v2; 86 pages.
- Local PDF: [2501.12948_deepseek_r1.pdf](2501.12948_deepseek_r1.pdf).
- RL and distillation model lineage. Background only; target-model behavior must be measured separately. Official pinned model card also archived.

## 4. Self-Challenging Language Model Agents

- Authors: Yifei Zhou, Sergey Levine, Jason E. Weston, Xian Li, Sainbayar Sukhbaatar
- Year: 2025; arXiv: 2506.01716v1; 25 pages.
- Local PDF: [2506.01716v1_self_challenging_language_model_agents.pdf](2506.01716v1_self_challenging_language_model_agents.pdf).
- Code-as-Task generates instructions, verifiers, solution/failure cases; RL evaluated on M3ToolEval and tau-bench. Abstract screen: useful data-quality pattern, training out of scope.

## 5. BSBench: will your LLM find the largest prime number?

- Authors: K. O. T. Erziev
- Year: 2025; arXiv: 2506.04535v1; 11 pages.
- Local PDF: [2506.04535v1_bsbench_will_your_llm_find_the_largest_prime_number_.pdf](2506.04535v1_bsbench_will_your_llm_find_the_largest_prime_number_.pdf).
- Impossible/unanswerable question benchmark and dataset mutation. Abstract screen: lacks mutable final-state task execution; implementation pruned.

## 6. MIRAGE-Bench: LLM Agent is Hallucinating and Where to Find Them

- Authors: Wei-Chen Zhang, Yiyou Sun, Pohao Huang, Jiayue Pu, Heyue Lin, D. Song
- Year: 2025; arXiv: 2507.21017v1; 50 pages.
- Local PDF: [2507.21017v1_mirage_bench_llm_agent_is_hallucinating_and_where_to_find_them.pdf](2507.21017v1_mirage_bench_llm_agent_is_hallucinating_and_where_to_find_them.pdf).
- MIRAGE taxonomy: instruction, history and observation unfaithfulness; snapshots and LLM judging. Abstract screen: classification context, not a paired completion endpoint.

## 7. ImpossibleBench: Measuring LLMs' Propensity of Exploiting Test Cases

- Authors: Zi-Qian Zhong, Aditi Raghunathan, Nicholas Carlini
- Year: 2025; arXiv: 2510.20270v1; 25 pages.
- Local PDF: [2510.20270_impossiblebench.pdf](2510.20270_impossiblebench.pdf).
- Full review, 25 pages. 103 LCB and 349 SWE tasks per variant; exploitation measured through mutated tests. Official code/data staged; stronger independent oracle needed.

## 8. Are Your Agents Upward Deceivers?

- Authors: Dadi Guo, Qing-Yu Liu, Dong-Rui Liu, Qi-Han Ren, Shuai Shao, T. Qiu, Hao-Ran Li, Yi R. Fung, Zhong-Jie Ba, Juntao Dai, Jiaming Ji, Zhikai Chen, Jialing Tao, Yao-Dong Yang, Jing Shao, Xia Hu
- Year: 2025; arXiv: 2512.04864; 38 pages.
- Local PDF: [2512.04864_are_your_agents_upward_deceivers_.pdf](2512.04864_are_your_agents_upward_deceivers_.pdf).
- Full review, 38 pages. 200 tasks, 11 models, GPT-5 judge; broken tools, missing data and fabricated artifacts. Closest released constrained-task source; no solvable twins.

## 9. FormalJudge: A Neuro-Symbolic Paradigm for Agentic Oversight

- Authors: Jia-Yi Zhou, Yang Sheng, Hantao Lou, Yao-Dong Yang, Jie Fu
- Year: 2026; arXiv: 2602.11136v2; 27 pages.
- Local PDF: [2602.11136v2_formaljudge_a_neuro_symbolic_paradigm_for_agentic_oversight.pdf](2602.11136v2_formaljudge_a_neuro_symbolic_paradigm_for_agentic_oversight.pdf).
- FormalJudge translates requirements into formal checks via Dafny/Z3. Abstract screen: judge-method context; specification translation remains a source of error; formal stack not required for simple state predicates.

## 10. SafeRedirect: Defeating Internal Safety Collapse via Task-Completion Redirection in Frontier LLMs

- Authors: Chao Pan, Yu Wu, Xin Yao
- Year: 2026; arXiv: 2604.20930v1; 13 pages.
- Local PDF: [2604.20930v1_saferedirect_defeating_internal_safety_collapse_via_task_completion_re.pdf](2604.20930v1_saferedirect_defeating_internal_safety_collapse_via_task_completion_re.pdf).
- Permission-to-fail/hard-stop mitigation for harmful task-completion pressure. Abstract screen: domain and incentives differ from benign task hypothesis; no implementation.

## 11. Done, But Not Sure: Disentangling World Completion from Self-Termination in Embodied Agents

- Authors: Ying Chen, Lihuang Fang, Ruien Jiang, Mingxuan Wang, Zhifeng Gu, Lei Yi, Jie Chen
- Year: 2026; arXiv: 2605.08747v4; 28 pages.
- Local PDF: [2605.08747v4_done_but_not_sure_disentangling_world_completion_from_self_termination.pdf](2605.08747v4_done_but_not_sure_disentangling_world_completion_from_self_termination.pdf).
- VIGIL separates world completion and terminal report in 1,000 embodied episodes across 20 models. Abstract screen: useful outcome taxonomy; robotics implementation pruned.

## 12. Push Your Agent: Measuring and Enforcing Quantitative Goal Persistence in Long-Horizon LLM Agents

- Authors: Yuan-Dao Cai, Yuzhang Zhu, Li-You Gao, Wen-Sheng Tang, Sheng-Chao Qin
- Year: 2026; arXiv: 2605.23574v1; 17 pages.
- Local PDF: [2605.23574_pushbench.pdf](2605.23574_pushbench.pdf).
- PushBench tests quantitative persistence and duplicate/false completion using external verifiers. Abstract screen: long-horizon/count confound; verifier ideas retained only.

## 13. Do Agents Know What They Can't Do? Evaluating Feasibility Awareness in Tool-Using Agents

- Authors: Liang Cheng, Mingsheng Cai, Jiu-Ming Jiang, Luo Mai
- Year: 2026; arXiv: 2605.28532v1; 14 pages.
- Local PDF: [2605.28532v1_do_agents_know_what_they_can_t_do_evaluating_feasibility_awareness_in_.pdf](2605.28532v1_do_agents_know_what_they_can_t_do_evaluating_feasibility_awareness_in_.pdf).
- Full review, 14 pages. 1,036 critical-tool-masked tasks, 283-item human audit, false-continuation metric. Code staged; no generated data shipped in current tree.

## 14. From Confident Closing to Silent Failure: Characterizing False Success in LLM Agents

- Authors: Laksh Advani
- Year: 2026; arXiv: 2606.09863v1; 18 pages.
- Local PDF: [2606.09863v1_from_confident_closing_to_silent_failure_characterizing_false_success_.pdf](2606.09863v1_from_confident_closing_to_silent_failure_characterizing_false_success_.pdf).
- Full review, 18 pages. False success in tau2/AppWorld, domain-sensitive lightweight detectors vs five LLM judges. Supports separate claims/state and conditional denominators.

## 15. Position: Correct Answer, Wrong Mechanism - When AI Scientists Defend General Claims Their Own Data Contradicts

- Authors: S. Eulig
- Year: 2026; arXiv: 2606.23175v1; 20 pages.
- Local PDF: [2606.23175v1_19.pdf](2606.23175v1_19.pdf).
- 28 Geant4 agent episodes distinguish correct answer from faithful scientific mechanism. Abstract screen: small domain-specific evidence; does not test impossible twins.

## 16. Protective Capacity Hallucination: When Large Language Models Claim Nonexistent Capabilities

- Authors: E. Lee, Jungpyo Nam, Sunjun Hwang
- Year: 2026; arXiv: 2607.13596v2; 15 pages.
- Local PDF: [2607.13596v2_protective_capacity_hallucination_when_large_language_models_claim_non.pdf](2607.13596v2_protective_capacity_hallucination_when_large_language_models_claim_non.pdf).
- Protective capacity hallucination across eight LLMs and 13,600 sessions. Abstract screen: role/capability boundaries matter, but vulnerable-user settings are outside benign primary suite.

## 17. Guardrails as Scapegoats: Auditing Unfaithful Safety Refusals in Tool-Augmented LLM Agents

- Authors: Aarushi Singh
- Year: 2026; arXiv: 2607.19449v1; 8 pages.
- Local PDF: [2607.19449v1_guardrails_as_scapegoats_auditing_unfaithful_safety_refusals_in_tool_a.pdf](2607.19449v1_guardrails_as_scapegoats_auditing_unfaithful_safety_refusals_in_tool_a.pdf).
- Silent tool failures and fabricated safety excuses; four models, 12 stubs, four profiles. Abstract screen: do not conflate tool errors, fabrication and safety refusal; broad outcome differs from DONE.

## 18. TRACE: A Self-Evolving Skill Bank for Consistent, Limit-Aware LLM Agents

- Authors: Wen-Hao Wu, Meng-Hao Zhang, X. Wang, Zhi Wang, Kun Shao, Jian Luan
- Year: 2026; arXiv: 2608.22793; 9 pages.
- Local PDF: [2608.22793_trace.pdf](2608.22793_trace.pdf).
- TRACE evolves a skill bank from trajectory contrasts on CAR-bench. Abstract screen; recovered via author website. Reliability and limit-awareness context, optimization outside scope.

## 19. Refusing the Impossible: A Taxonomy and Benchmark for Code Hallucination in Large Language Models

- Authors: Vishnu Asutosh Dasu, Ashish Kundu, Gang Tan
- Year: 2026; arXiv: 2609.03267v1; 17 pages.
- Local PDF: [2609.03267v1_refusing_the_impossible_a_taxonomy_and_benchmark_for_code_hallucinatio.pdf](2609.03267v1_refusing_the_impossible_a_taxonomy_and_benchmark_for_code_hallucinatio.pdf).
- 270 impossible code prompts plus 91 solvable controls; 12 models, two-tier judge (reported 82% human agreement). Abstract screen: paired controls useful; code plausibility is distinct from completed state.

## 20. Fabrication After Tool Failure: Tool-Augmented Agents Assert Values Their Tools Did Not Return

- Authors: Arham Sethi, Arsen Kenzhebayev, Saanvi Paturi, Vatsal Raina, Vyas Raina, Ivaxi Sheth
- Year: 2026; arXiv: 2609.14758v1; 11 pages.
- Local PDF: [2609.14758v1_fabrication_after_tool_failure_tool_augmented_agents_assert_values_the.pdf](2609.14758v1_fabrication_after_tool_failure_tool_augmented_agents_assert_values_the.pdf).
- 1,024 enforced failed-tool items; failure signaling and explicit retrieval-status defense. Abstract screen: retrieval-value honesty broader than completed state; supports fixed-trace diagnostic.

## 21. The Troy Moment: How LLM Agents Adjudicate the Decision Point Under Impossible Tasks, Claimed Authority, and Peer Information

- Authors: I. Zhang
- Year: 2026; arXiv: 2609.15494v3; 15 pages.
- Local PDF: [2609.15494v3_the_troy_moment_how_llm_agents_adjudicate_the_decision_point_under_imp.pdf](2609.15494v3_the_troy_moment_how_llm_agents_adjudicate_the_decision_point_under_imp.pdf).
- ImpossibleBench-derived repair tasks vary authority, peers, wording and friction. Abstract screen: extra pressure interventions pruned to retain a clean impossibility contrast.

## 22. Quantifying Overclaiming Propensity in Frontier LLM Agents

- Authors: Nolan Smyth, Yorguin-Jose Mantilla-Ramos, Pascal Junior Tikeng Notsawo, S. Helbling, A. Tosato, Mohamed Amine Merzouk, Nouha Dziri, G. Gidel, Tommaso Tosato
- Year: 2026; arXiv: 2609.20812v3; 28 pages.
- Local PDF: [2609.20812v3_quantifying_overclaiming_propensity_in_frontier_llm_agents.pdf](2609.20812v3_quantifying_overclaiming_propensity_in_frontier_llm_agents.pdf).
- Five feasible file-review scenarios, 12 agents, transcript coverage/planted defects. Abstract plus selected methods: explicit overclaim differs from omission; long-review direction pruned.

## 23. Failure-Transparent Agents: Benchmarking Post-Failure Reporting in Tool-Using Language Models

- Authors: Jun-Ru Zhu, Shi-Ming Xie, Ai-Me-Lu-Fan Chen, Xiao-Qing Ding, Chun-Xin Tang, Ruo-Yu Qi, Yu-Lang Fei
- Year: 2026; arXiv: 2609.35732v1; 5 pages.
- Local PDF: [2609.35732v1_failure_transparent_agents_benchmarking_post_failure_reporting_in_tool.pdf](2609.35732v1_failure_transparent_agents_benchmarking_post_failure_reporting_in_tool.pdf).
- Full review, 5 pages. 100 fixed-failure scenarios, 3 policies, 6 models, 3,600 responses. Reporting isolation useful; no successful controls or released artifact link.

## 24. A Competing-Hazards Systematization of Loss of Control in Autonomous Agents

- Authors: M. Bouke
- Year: 2026; arXiv: 2609.38411v1; 12 pages.
- Local PDF: [2609.38411v1_28.pdf](2609.38411v1_28.pdf).
- Audits 22 incidents/102 safety evaluations using completion/stopping/escape/continuation states. Abstract screen: retain budget exhaustion separately; incident association is not causal evidence.

## 25. Mingbird: A Local-First Agent Harness Enabling Small Open Models to Complete Real Tasks

- Authors: Hao Wang, Ting-Bin Huang
- Year: 2026; arXiv: 2610.02001v1; 44 pages.
- Local PDF: [2610.02001v1_mingbird_a_local_first_agent_harness_enabling_small_open_models_to_com.pdf](2610.02001v1_mingbird_a_local_first_agent_harness_enabling_small_open_models_to_com.pdf).
- Small-model harness study: 4 harnesses x 4 models x 18 tasks and tau2 comparison. Abstract screen: harness sensitivity and limited single-machine evidence, not target-model confirmation.

## 26. A Trust Layer for Agent Evaluation

- Authors: Mohammadreza Sediqin, Shivali Dalmia, Srinivasa Karthikeya Reddy Kovvuri, Abhishek Mukherji
- Year: 2026; arXiv: 2610.07274v1; 14 pages.
- Local PDF: [2610.07274_trust_layer.pdf](2610.07274_trust_layer.pdf).
- Audits score validity, traced computation, report consistency and repeatability on 108 tasks. Abstract screen: independent evidence layers; not a paired task-impossibility experiment.

## 27. Agentic Self-Awareness: Aligning Knowing, Acting, and Holding

- Authors: Qing-Lin Chen, Hiroaki Hayashi, Jia-Xin Zhang, Chien-Sheng Wu
- Year: 2026; arXiv: 2610.19226v1; 25 pages.
- Local PDF: [2610.19226v1_agentic_self_awareness_aligning_knowing_acting_and_holding.pdf](2610.19226v1_agentic_self_awareness_aligning_knowing_acting_and_holding.pdf).
- Paired feasible/blocked Terminal-Bench and retail tau2 tasks; separates blocker recognition and warranted deferral. Abstract/targeted screen: supports direction 1; harness-search transfer limits reported.

## Search exclusions and access gaps

Paper-finder returned 164 candidates (25 rated >=2; 139 peripheral score-1 records retained as metadata but not downloaded). Of the 25, 23 PDFs were recovered, HCRC was verified author-withdrawn (arXiv 2607.04562) and excluded, and the coding DriftBench paper could not be resolved despite Semantic Scholar/arXiv retries. Do not substitute the unrelated database DriftBench paper. Four additional unique primary papers were acquired manually. No HCRC result is used as evidence. TRACE was recovered from its author website. See evidence/literature_downloads.json, literature_retry.json and final_access_attempts.json.
