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
