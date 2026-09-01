# IDOR Response Analyzer
A custom Python tool built to automate the detection of Insecure Direct Object References (IDOR) during manual web application penetration testing.

## The Problem
Automated vulnerability scanners often miss business logic and access control flaws, requiring manual intervention.

## The Solution
This script rapidly enumerates object references and detects hidden data leaks by analyzing HTTP response length anomalies, replicating the anomaly-hunting workflow of Burp Suite Intruder.
