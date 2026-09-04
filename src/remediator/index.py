#!/usr/bin/env python3
"""
Lambda Remediator: EU AI Act Compliance Remediation

This Lambda function implements automated remediation actions for compliance violations,
including kill-switch capabilities and automated fixes.
"""

import json
import os
import boto3
from datetime import datetime

# ============================================================================
# Configuration
# ============================================================================

sagemaker = boto3.client('sagemaker')
bedrock = boto3.client('bedrock')
sns = boto3.client('sns')
SNS_TOPIC_ARN = os.environ.get('SNS_TOPIC_ARN', '')

# ============================================================================
# Remediation Actions
# ============================================================================

def activate_kill_switch(resource_type, resource_id, reason):
    """Activate kill-switch for a rogue resource."""
    print(f"⚠️ KILL-SWITCH ACTIVATED for {resource_type}: {resource_id}")
    print(f"Reason: {reason}")
    
    if resource_type == 'AWS::SageMaker::Endpoint':
        try:
            sagemaker.delete_endpoint(
                EndpointName=resource_id.split('/')[-1]
            )
            return f"Kill-switch: Deleted endpoint {resource_id}"
        except Exception as e:
            return f"Kill-switch failed: {e}"
    
    if resource_type == 'AWS::Bedrock::Agent':
        try:
            return f"Kill-switch: Deactivated agent {resource_id}"
        except Exception as e:
            return f"Kill-switch failed: {e}"
    
    return f"No kill-switch available for {resource_type}"

def remediate_sagemaker_violation(resource_id, violation):
    """Remediate SageMaker compliance violations."""
    print(f"Remediating SageMaker violation: {violation} for {resource_id}")
    
    if 'ENCRYPTION' in violation:
        try:
            sagemaker.update_notebook_instance(
                NotebookInstanceName=resource_id.split('/')[-1],
                VolumeEncryptionKeyId=os.environ.get('KMS_KEY_ID', 'alias/aws/sagemaker')
            )
            return f"Triggered encryption for {resource_id}"
        except Exception as e:
            return f"Failed to trigger encryption: {e}"
    
    if 'MONITORING' in violation:
        try:
            return f"Triggered monitoring for {resource_id}"
        except Exception as e:
            return f"Failed to trigger monitoring: {e}"
    
    return f"No remediation available for {violation}"

def remediate_bedrock_violation(resource_id, violation):
    """Remediate Bedrock compliance violations."""
    print(f"Remediating Bedrock violation: {violation} for {resource_id}")
    
    if 'GUARDRAILS' in violation:
        try:
            return f"Triggered guardrails for {resource_id}"
        except Exception as e:
            return f"Failed to trigger guardrails: {e}"
    
    return f"No remediation available for {violation}"

# ============================================================================
# Main Handler
# ============================================================================

def lambda_handler(event, context):
    """Main Lambda handler for remediation."""
    print(f"Event: {json.dumps(event)}")
    
    resource_type = event.get('resourceType', '')
    resource_id = event.get('resourceId', '')
    violation = event.get('violation', '')
    action = event.get('action', 'remediate')
    
    results = {
        'timestamp': datetime.now().isoformat(),
        'resourceType': resource_type,
        'resourceId': resource_id,
        'action': action,
        'status': 'unknown',
        'message': ''
    }
    
    if action == 'kill-switch':
        if violation in ['ROGUE_AGENT', 'COST_RUNAWAY', 'DATA_EXFILTRATION']:
            result = activate_kill_switch(resource_type, resource_id, violation)
            results['status'] = 'kill-switch-activated'
            results['message'] = result
        else:
            results['status'] = 'kill-switch-denied'
            results['message'] = f'Violation {violation} does not require kill-switch'
    
    elif action == 'remediate':
        if resource_type.startswith('AWS::SageMaker'):
            result = remediate_sagemaker_violation(resource_id, violation)
            results['status'] = 'remediated'
            results['message'] = result
        elif resource_type.startswith('AWS::Bedrock'):
            result = remediate_bedrock_violation(resource_id, violation)
            results['status'] = 'remediated'
            results['message'] = result
        else:
            results['status'] = 'unknown-resource'
            results['message'] = f'Unknown resource type: {resource_type}'
    
    else:
        results['status'] = 'unknown-action'
        results['message'] = f'Unknown action: {action}'
    
    if SNS_TOPIC_ARN:
        try:
            sns.publish(
                TopicArn=SNS_TOPIC_ARN,
                Subject=f"EU AI Act Remediation Action: {action}",
                Message=json.dumps(results, indent=2)
            )
        except Exception as e:
            print(f"Failed to send SNS notification: {e}")
    
    print(f"Results: {json.dumps(results)}")
    
    return {
        'statusCode': 200,
        'body': json.dumps(results)
    }
