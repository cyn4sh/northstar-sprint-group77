# MVP End-to-End Demo Script

## Overview
This script outlines the step-by-step walkthrough for presentation day.

## Presentation Steps

### 1. Order Status Check
* **Presenter:** "First, we will demonstrate automated order status lookup."
* **Action:** Enter Order ID `ORD-101` in the lookup prompt.
* **Expected Result:** Chat returns current tracking status and delivery date.

### 2. Return Eligibility Check
* **Presenter:** "Next, we will check return eligibility for a customer."
* **Action:** Select 'Start a Return' and submit Order ID `ORD-101`.
* **Expected Result:** System verifies the 30-day window and generates a mock shipping label.

### 3. Edge Case Handling
* **Presenter:** "Finally, here is our error handling for missing orders."
* **Action:** Enter invalid Order ID `ORD-999`.
* **Expected Result:** System shows clear error copy and provides option to connect with support.
