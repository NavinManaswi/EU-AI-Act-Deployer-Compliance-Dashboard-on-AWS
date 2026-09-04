#!/bin/bash
# One-click deployment script for EU AI Act Deployer Compliance Dashboard

set -e

echo "🇪🇺 EU AI Act Deployer Compliance Dashboard"
echo "==========================================="
echo ""

# Check prerequisites
echo "🔍 Checking prerequisites..."
command -v aws >/dev/null 2>&1 || { echo "❌ AWS CLI not found. Please install it."; exit 1; }
command -v sam >/dev/null 2>&1 || { echo "❌ AWS SAM CLI not found. Please install it."; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "❌ Python 3 not found. Please install it."; exit 1; }
echo "✅ Prerequisites satisfied."
echo ""

# Get user input
read -p "Enter your email for SNS alerts: " EMAIL
read -p "Enter QuickSight user ARN: " QUICKSIGHT_ARN

# Build SAM application
echo "📦 Building SAM application..."
sam build
echo "✅ Build complete."
echo ""

# Deploy SAM application
echo "🚀 Deploying SAM application..."
sam deploy --guided \
  --stack-name eu-ai-act-deployer-dashboard \
  --capabilities CAPABILITY_IAM \
  --parameter-overrides \
    NotificationEmail="$EMAIL" \
    QuickSightUserArn="$QUICKSIGHT_ARN"
echo "✅ Deployment complete."
echo ""

# Deploy Audit Manager framework
echo "📋 Deploying AWS Audit Manager framework..."
aws auditmanager create-assessment-framework \
  --name "EU AI Act Deployer Framework" \
  --description "Automated evidence collection for EU AI Act deployer obligations" \
  --control-sets file://audit-framework/eu-ai-act-deployer-framework.json || echo "Framework may already exist"
echo "✅ Audit Manager framework deployed."
echo ""

# Deploy Config conformance pack
echo "⚙️ Deploying AWS Config conformance pack..."
aws config put-conformance-pack \
  --conformance-pack-name eu-ai-act-deployer-controls \
  --template-body file://config-rules/eu-ai-act-config-rules.yaml
echo "✅ Config conformance pack deployed."
echo ""

echo "🎉 Deployment complete!"
echo ""
echo "📊 QuickSight dashboard available at:"
echo "   https://quicksight.aws.amazon.com/"
echo ""
echo "🔍 Security Hub findings available at:"
echo "   https://console.aws.amazon.com/securityhub/"
echo ""
echo "📋 Audit Manager assessments available at:"
echo "   https://console.aws.amazon.com/auditmanager/"
echo ""
echo "📧 SNS alerts configured for: $EMAIL"
echo ""
echo "✅ Your EU AI Act Deployer Compliance Dashboard is now operational!"
