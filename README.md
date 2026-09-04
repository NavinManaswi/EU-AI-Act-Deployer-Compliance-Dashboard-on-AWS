# 🇪🇺 EU AI Act Deployer Compliance Dashboard

## Continuous Transparency & Accountability for High-Risk AI Systems

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Status](https://img.shields.io/badge/status-active-brightgreen.svg)]()
[![AWS](https://img.shields.io/badge/AWS-Certified-orange.svg)]()
[![EU AI Act](https://img.shields.io/badge/EU%20AI%20Act-Deployer%20Ready-blue.svg)]()
[![Art. 13](https://img.shields.io/badge/Art.13-Transparency-green.svg)]()
[![Art. 14](https://img.shields.io/badge/Art.14-Human%20Oversight-purple.svg)]()
[![Art. 72-73](https://img.shields.io/badge/Art.72--73-Post--Market%20Monitoring-red.svg)]()

---

## 📋 Table of Contents

- [About This Project](#-about-this-project)
- [Why This Matters](#-why-this-matters)
- [EU AI Act Deployer Obligations](#-eu-ai-act-deployer-obligations)
- [Architecture](#-architecture)
- [AWS Services Used](#-aws-services-used)
- [Quick Start](#-quick-start)
- [What's Inside](#-whats-inside)
- [Key Artifacts](#-key-artifacts)
- [Compliance Dashboard](#-compliance-dashboard)
- [Deployment](#-deployment)
- [References](#-references)
- [License](#-license)

---

## 🎯 About This Project

This project implements an **end-to-end EU AI Act Deployer Compliance Dashboard** on AWS. It provides continuous monitoring, transparency, and accountability for high-risk AI systems, addressing the obligations of **deployers** (organizations that use high-risk AI systems developed by third parties) under the EU AI Act.

**What it does:**

| Capability | EU AI Act Article | Description |
|------------|-------------------|-------------|
| 📊 **Real-Time Compliance Dashboard** | Art. 9, 11 | Executive visibility into AI system compliance posture |
| 🔍 **Model Drift & Bias Monitoring** | Art. 15 | Continuous detection of data drift, concept drift, and bias drift |
| 📝 **Automated Evidence Collection** | Art. 11, 12 | Annex IV technical documentation evidence aggregation |
| 👁️ **Human Oversight Tracking** | Art. 14 | Logging and reporting of human review and override actions |
| 🚨 **Incident & Anomaly Alerting** | Art. 72-73 | Real-time alerts for model degradation, bias, and incidents |
| 📁 **Audit-Ready Evidence** | Art. 11, 18 | Centralized evidence repository for regulatory audits |

**Organization:** NovaTech Financial Group *(hypothetical)*  
**Effective Date:** September 2026  
**Version:** 1.0

---

## 🚨 Why This Matters

### The Enforcement Era Is Here

The **EU AI Act enforcement provisions went live on 2 August 2026**. Deployers of high-risk AI systems now have legal obligations under:

| Article | Obligation | Deployer Responsibility |
|---------|------------|------------------------|
| **Art. 9** | Risk Management | Implement and maintain risk management system |
| **Art. 10** | Data Governance | Ensure data governance for system operation |
| **Art. 11** | Technical Documentation | Verify provider holds compliant Annex IV documentation |
| **Art. 12** | Record-Keeping | Maintain logs for 10 years |
| **Art. 13** | Transparency | Provide clear information to users |
| **Art. 14** | Human Oversight | Implement meaningful human oversight |
| **Art. 15** | Accuracy & Robustness | Monitor accuracy and robustness |
| **Art. 72-73** | Post-Market Monitoring | Continuously monitor system performance |

### The Deployer's Challenge

> *"The EU AI Act's supply chain obligations apply to you right now."*

Deployers face a unique challenge: **you may not control the AI model's development, but you are legally responsible for its compliance in production.** This project solves that problem by providing continuous visibility and accountability.

---

## 📋 EU AI Act Deployer Obligations

| Obligation | Article | How This Project Addresses It |
|------------|---------|-------------------------------|
| **Verify Annex IV Documentation** | Art. 11, 26 | Audit Manager framework collects evidence; dashboard tracks documentation status |
| **Maintain Records** | Art. 12 | CloudTrail + CloudWatch Logs with 10-year retention |
| **Provide Transparency** | Art. 13 | QuickSight dashboard with model explanations and decision logs |
| **Implement Human Oversight** | Art. 14 | Human review logging; override tracking; escalation dashboards |
| **Monitor Accuracy & Robustness** | Art. 15 | SageMaker Model Monitor for drift and bias detection |
| **Post-Market Monitoring** | Art. 72-73 | Continuous monitoring dashboards; incident alerting |

---

## 🏗️ Architecture
┌─────────────────────────────────────────────────────────────────────────────┐
│ EU AI ACT DEPLOYER COMPLIANCE DASHBOARD │
├─────────────────────────────────────────────────────────────────────────────┤
│ │
│ ┌─────────────────────────────────────────────────────────────────────┐ │
│ │ DATA COLLECTION LAYER │ │
│ │ │ │
│ │ ┌──────────────┐ ┌──────────────┐ ┌──────────────┐ │ │
│ │ │ SageMaker │ │ Bedrock │ │ CloudTrail │ │ │
│ │ │ Model Monitor│ │ Guardrails │ │ (Audit) │ │ │
│ │ │ (Drift & │ │ (Runtime │ │ & CloudWatch│ │ │
│ │ │ Bias) │ │ Policies) │ │ (Metrics) │ │ │
│ │ └──────┬───────┘ └──────┬───────┘ └──────┬───────┘ │ │
│ │ │ │ │ │ │
│ │ └─────────────────┼─────────────────┘ │ │
│ │ ▼ │ │
│ │ ┌─────────────────────────────────────┐ │ │
│ │ │ EventBridge Rules │ │ │
│ │ │ (Scheduled & Event-Driven) │ │ │
│ │ └────────────────┬────────────────────┘ │ │
│ │ ▼ │ │
│ │ ┌─────────────────────────────────────┐ │ │
│ │ │ Lambda Aggregator │ │ │
│ │ │ (Consolidates Compliance Data) │ │ │
│ │ └────────────────┬────────────────────┘ │ │
│ └──────────────────────────┼────────────────────────────────────────┘ │
│ │ │
│ ▼ │
│ ┌─────────────────────────────────────────────────────────────────────┐ │
│ │ STORAGE & EVIDENCE LAYER │ │
│ │ │ │
│ │ ┌──────────────┐ ┌──────────────┐ ┌──────────────────────────┐ │ │
│ │ │ S3 │ │ DynamoDB │ │ AWS Audit Manager │ │ │
│ │ │ (Raw Logs) │ │ (Compliance │ │ (Automated Evidence) │ │ │
│ │ │ │ │ State) │ │ │ │ │
│ │ └──────────────┘ └──────────────┘ └──────────────────────────┘ │ │
│ └──────────────────────────┼────────────────────────────────────────┘ │
│ │ │
│ ▼ │
│ ┌─────────────────────────────────────────────────────────────────────┐ │
│ │ VISUALIZATION LAYER │ │
│ │ │ │
│ │ ┌─────────────────────────────────────────────────────────────┐ │ │
│ │ │ Amazon QuickSight Dashboard │ │ │
│ │ │ │ │ │
│ │ │ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │ │ │
│ │ │ │Compliance│ │ Model │ │ Bias │ │ Human │ │ │ │
│ │ │ │ Score │ │ Drift │ │ Metrics │ │ Oversight│ │ │ │
│ │ │ └──────────┘ └──────────┘ └──────────┘ └──────────┘ │ │ │
│ │ │ ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌──────────┐ │ │ │
│ │ │ │Incidents │ │ Annex │ │ Audit │ │ Human │ │ │ │
│ │ │ │ & Alerts│ │ IV │ │Evidence │ │ Review │ │ │ │
│ │ │ └──────────┘ └──────────┘ └──────────┘ └──────────┘ │ │ │
│ │ └─────────────────────────────────────────────────────────────┘ │ │
│ └─────────────────────────────────────────────────────────────────────┘ │
│ │
│ ┌─────────────────────────────────────────────────────────────────────┐ │
│ │ ALERTING LAYER │ │
│ │ │ │
│ │ ┌──────────────┐ ┌──────────────┐ ┌──────────────────────────┐ │ │
│ │ │ Security Hub│ │ SNS │ │ CloudWatch Alarms │ │ │
│ │ │ (Findings) │ │ (Alerts) │ │ (Threshold Breaches) │ │ │
│ │ └──────────────┘ └──────────────┘ └──────────────────────────┘ │ │
│ └─────────────────────────────────────────────────────────────────────┘ │
│ │

---

## 🔧 AWS Services Used

| Service | Purpose | EU AI Act Alignment |
|---------|---------|---------------------|
| **Amazon SageMaker Model Monitor** | Detect data drift, concept drift, and bias drift in production | Art. 15 (Accuracy & Robustness) |
| **Amazon SageMaker Clarify** | Bias detection and explainability reports | Art. 13 (Transparency) |
| **Amazon Bedrock Guardrails** | Runtime safety and compliance policies | Art. 9 (Risk Management) |
| **AWS CloudTrail** | Complete audit trail of all API calls | Art. 12 (Record-Keeping) |
| **Amazon CloudWatch** | Performance metrics and alerting | Art. 72-73 (Post-Market Monitoring) |
| **AWS Lambda** | Data aggregation and transformation | Art. 11 (Technical Documentation) |
| **Amazon EventBridge** | Scheduled and event-driven compliance scans | Art. 9 (Risk Management) |
| **Amazon QuickSight** | Executive compliance dashboards | Art. 13 (Transparency) |
| **AWS Audit Manager** | Automated evidence collection | Art. 11, 12, 18 (Documentation & Records) |
| **AWS Security Hub** | Centralized security and compliance findings | Art. 72-73 (Post-Market Monitoring) |
| **Amazon SNS** | Alerting on violations and incidents | Art. 73 (Serious Incident Reporting) |
| **Amazon DynamoDB** | Compliance state storage | Art. 12 (Record-Keeping) |
| **Amazon S3** | Raw logs and evidence storage | Art. 11, 18 (Documentation) |

---

## 🚀 Quick Start

| Step | Action | Command |
|------|--------|---------|
| **1** | Clone the repository | `git clone https://github.com/yourusername/eu-ai-act-deployer-dashboard.git` |
| **2** | Navigate to the project | `cd eu-ai-act-deployer-dashboard` |
| **3** | Deploy the infrastructure | `./scripts/deploy.sh` |
| **4** | Configure the sample model | `python scripts/configure-sample-model.py` |
| **5** | View the dashboard | Open QuickSight and navigate to the EU AI Act Compliance Dashboard |

---

## 📂 What's Inside

| Folder | Description |
|--------|-------------|
| **infrastructure/** | SAM / CloudFormation templates for one-click deployment |
| **src/aggregator/** | Lambda aggregator that consolidates compliance data |
| **src/monitor/** | Lambda monitor that evaluates model performance |
| **src/remediator/** | Lambda remediator for automated compliance fixes |
| **policies/guardrails/** | Bedrock Guardrails policies for runtime enforcement |
| **audit-framework/** | AWS Audit Manager framework for EU AI Act compliance |
| **dashboard/** | QuickSight dashboard definition |
| **config-rules/** | AWS Config rules for AI compliance |
| **scripts/** | Deployment and testing scripts |
| **.github/workflows/** | CI/CD pipeline |

---

## 🏆 Key Artifacts

### 1. EU AI Act Audit Manager Framework

Automated evidence collection for deployer obligations:

| Control Set | Evidence Sources |
|-------------|------------------|
| **Annex IV Documentation** | S3, Config, CloudTrail |
| **Risk Management** | SageMaker Model Monitor, Bedrock Guardrails |
| **Data Governance** | Data lineage, quality metrics |
| **Transparency** | Model explanations, user disclosures |
| **Human Oversight** | Review logs, override tracking |
| **Post-Market Monitoring** | Performance metrics, incident logs |

### 2. Compliance Dashboard

Executive-ready QuickSight dashboard with:

- **Compliance Score** — Overall percentage of AI systems in compliance
- **Model Drift Monitoring** — Data drift, concept drift, bias drift trends
- **Bias Metrics** — Disparate impact ratio, equalized odds
- **Human Oversight** — Review rates, override patterns
- **Incident Log** — Severity, status, resolution
- **Annex IV Status** — Documentation completeness
- **Audit Evidence** — Evidence collection status

### 3. SageMaker Model Monitor Configuration

Continuous monitoring for:

- **Data Quality** — Missing values, outliers, data types
- **Model Quality** — Accuracy, precision, recall, F1
- **Bias Drift** — Fairness metrics over time
- **Feature Attribution** — SHAP value changes

### 4. Bedrock Guardrails Policy

Runtime safety and compliance policies:

- **Topic Policies** — Prohibited topics (Art. 5)
- **Content Filters** — Harmful content filtering
- **Sensitive Information** — PII detection and redaction
- **Prompt Injection** — Input validation

### 5. Human Oversight Tracking

Logging and reporting for Art. 14:

- **Review Logs** — Every human review recorded
- **Override Tracking** — Override decisions and justifications
- **Escalation Paths** — Automated escalation for high-risk decisions
- **Performance Metrics** — Reviewer accuracy and timeliness

---

## 📊 Compliance Dashboard

The QuickSight dashboard provides real-time visibility into:

| Dashboard Section | Metrics | EU AI Act Article |
|-------------------|---------|-------------------|
| **Compliance Score** | Overall compliance percentage; by system | Art. 9 |
| **Model Health** | Drift status, bias metrics, accuracy trends | Art. 15 |
| **Human Oversight** | Review rates, override rates, escalation logs | Art. 14 |
| **Incident Log** | Incident severity, status, resolution time | Art. 72-73 |
| **Annex IV Status** | Documentation completeness, evidence collection | Art. 11, 18 |
| **Audit Trail** | API calls, data access, model changes | Art. 12 |

---

## 🚀 Deployment

### Prerequisites

- AWS CLI installed and configured
- AWS SAM CLI installed
- Python 3.11+ installed
- QuickSight Enterprise edition (for dashboard)

### One-Click Deployment

```bash
# Clone the repository
git clone https://github.com/yourusername/eu-ai-act-deployer-dashboard.git
cd eu-ai-act-deployer-dashboard

# Make the deployment script executable
chmod +x scripts/deploy.sh

# Run the deployment
./scripts/deploy.sh
└─────────────────────────────────────────────────────────────────────────────┘

## Manual Deployment
# Deploy infrastructure
aws cloudformation deploy \
  --template-file infrastructure/template.yaml \
  --stack-name eu-ai-act-deployer-dashboard \
  --parameter-overrides file://infrastructure/parameter-overrides.json \
  --capabilities CAPABILITY_IAM

# Deploy Audit Manager framework
aws auditmanager create-assessment-framework \
  --name "EU AI Act Deployer Framework" \
  --description "Automated evidence collection for EU AI Act deployer obligations" \
  --control-sets file://audit-framework/eu-ai-act-deployer-framework.json

# Configure SageMaker Model Monitor
aws sagemaker create-monitoring-schedule \
  --monitoring-schedule-name eu-ai-act-model-monitor \
  --monitoring-schedule-config file://infrastructure/monitoring-schedule-config.json

🔗 References
Resource	Link
EU AI Act Deployer Obligations	Articles 9-15, 72-73
AWS Audit Manager Generative AI Framework	v2 framework
SageMaker Model Monitor	Drift and bias detection
AWS CloudTrail for AI Services	Data events for Bedrock
QuickSight Governance Dashboards	SageMaker Catalog integration
📝 License
This project is licensed under the MIT License.

⭐ Star This Repository
If you find this project helpful, please star this repository and share it with your network!
