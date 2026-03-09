# Agile-CI-CD-Lab

## CI/CD Benchmark Findings

### The imperative of CI/CD

- CI integrates code changes frequently and validates each change with automated builds and quality checks.
- Continuous Delivery keeps every successful change release-ready, usually with a manual approval gate.
- Continuous Deployment pushes every validated change to production automatically.
- Business outcomes: faster release cycles, lower deployment risk, stronger quality, and better collaboration.

### Benchmark dimensions

- Platform architecture and operating model
- Business fit ("when to use")
- Pricing and total cost of ownership
- Deployment settings, controls, and governance

### Platform differences at a glance

| Dimension | Jenkins | AWS CodePipeline | GitHub Actions |
| --- | --- | --- | --- |
| Core model | Self-hosted automation server with plugin ecosystem | Fully managed AWS-native pipeline orchestration | Fully managed, event-driven automation inside GitHub |
| Best business fit (when to use) | Complex hybrid/on-prem or highly customized legacy environments | AWS-first organizations needing native cloud delivery and managed operations | Teams centered on GitHub needing fast developer workflows and strong repo-native governance |
| Pricing model | No license fee, but high hidden TCO (infra + maintenance + DevOps labor) | Pay-as-you-go (V2 action-minute billing) + separate service/storage costs | Included minutes/storage per plan, then per-minute overage by runner OS/size |
| Deployment settings | `Jenkinsfile` (Declarative or Scripted Groovy), controller/agent topology, plugin-based integrations | Pipelines/stages/actions/transitions, CodeBuild `buildspec.yml`, CloudFormation/CLI/Console configuration | YAML workflows in `.github/workflows`, matrix builds, environments with approval rules, hosted or self-hosted runners |
| Operational overhead | High | Low | Low to medium (higher with self-hosted runners) |

### Pricing notes (from the benchmark text)

- Jenkins: software is free, but infrastructure, plugin management, security patching, and staffing can dominate cost.
- AWS CodePipeline: V2 pricing is action-duration based (quoted as `$0.002` per action-minute) with related AWS service costs billed separately.
- GitHub Actions: plan-based quotas plus runner-based overage rates; Linux is typically cheapest, macOS is the most expensive.

### Decision guidance

- Choose Jenkins when deep customization and infrastructure control matter more than operational simplicity.
- Choose AWS CodePipeline when your delivery stack is tightly integrated with AWS services.
- Choose GitHub Actions when developer productivity, PR workflows, and repo-native CI/CD governance are top priorities.
