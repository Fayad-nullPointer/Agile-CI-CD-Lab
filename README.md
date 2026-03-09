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

### Detailed pricing (USD, from the benchmark text)

| Platform | Pricing detail |
| --- | --- |
| Jenkins | Software license: `$0`. Main costs are infrastructure (VMs/storage/network), plugin maintenance, security operations, and DevOps staffing. |
| AWS CodePipeline | V2 model: `$0.002` per action-minute. Manual approvals and custom actions are not billed by action-minute in the benchmark notes. Additional charges apply for related services like S3, CodeBuild, and CodeDeploy. |
| GitHub Actions | Plan + usage model: included monthly minutes/storage by plan, then per-minute overage by runner type. |

#### GitHub plan pricing (private repositories)

| Plan | Price | Included CI/CD minutes | Included storage |
| --- | --- | --- | --- |
| GitHub Free | `$0` / user / month | `2,000` minutes | `500 MB` |
| GitHub Team | `$4` / user / month (first 12 months, per benchmark text) | `3,000` minutes | `2 GB` |
| GitHub Enterprise | Starts at `$21` / user / month | `50,000` minutes | `50 GB` |

#### GitHub hosted runner overage rates

| Runner type | Cost (USD/minute) |
| --- | --- |
| Linux 1-core (x64) | `$0.002` |
| Linux 2-core (arm64) | `$0.005` |
| Linux 2-core (x64) | `$0.006` |
| Windows 2-core (x64/arm64) | `$0.010` |
| macOS (M1/Intel) | `$0.062` |

Additional cache/storage overage in the benchmark text: `$0.07` per GiB per month.

Note: cloud pricing changes frequently. Treat these as benchmark reference values and confirm current pricing on vendor billing pages before budgeting.

### Decision guidance

- Choose Jenkins when deep customization and infrastructure control matter more than operational simplicity.
- Choose AWS CodePipeline when your delivery stack is tightly integrated with AWS services.
- Choose GitHub Actions when developer productivity, PR workflows, and repo-native CI/CD governance are top priorities.
