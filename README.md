# ATM System Server-Side Implementation

**Author:** Shahar Friedmann  
**Company:** Double Verify  
**Assignment:** Home Assignment - simple ATM System  
**Date:** August 2025

## Project Overview

This project implements a RESTful API server for a simple ATM system that allows users to check their balance, withdraw money, and deposit money. The server is deployed on Heroku and provides three main endpoints for ATM operations.

## Live Application

**Deployed URL:** https://dv-hw1-atm-shahar-f-202508.herokuapp.com

## API Endpoints

### 1. Get Balance
- **Endpoint:** `GET /accounts/{account_number}/balance`
- **Description:** Retrieve the current balance for a specific account
- **Response:** JSON object containing account number and balance

### 2. Withdraw Money
- **Endpoint:** `POST /accounts/{account_number}/withdraw`
- **Description:** Withdraw money from a specific account
- **Request Body:** `{"amount": <number>}`
- **Response:** JSON object with transaction details and new balance

### 3. Deposit Money
- **Endpoint:** `POST /accounts/{account_number}/deposit`
- **Description:** Deposit money to a specific account
- **Request Body:** `{"amount": <number>}`
- **Response:** JSON object with transaction details and new balance

## Technology Stack

- **Backend Framework:** Flask (Python)
- **Production Server:** Gunicorn
- **Deployment Platform:** Heroku

## Design Decisions and Architecture

### 1. Framework Choice
I chose **Flask** over other frameworks because:
- Lightweight and perfect for REST APIs
- Simple syntax suitable for basic coding experience
- Easy integration with Heroku deployment
- Excellent JSON handling capabilities

### 2. Code Organization
- **Helper Functions:** Created `validate_account_and_amount()` to eliminate code duplication
- **Error Handling:** Comprehensive validation with appropriate HTTP status codes

### 3. API Design
- **RESTful Principles:** Used appropriate HTTP methods (GET for retrieval, POST for modifications)
- **Status Codes:** Proper HTTP status codes (200 for success, 400 for bad request, 404 for not found)
- **JSON Responses:** Consistent JSON format for all responses including errors

### 4. System Assumptions
- **Accounts Existence:** The assignment did not specify which accounts should be in the system, which also begs whether we should make a way to create and delete accounts.
- **Decision:** I decided to assume that the system starts with pre-existing accounts for testing purposes, as adding or removing accounts was not part of the assignment and may be seen as scope creep. It also represents a realistic scenario, since real ATMs cannot create or delete accounts.
- See also "Sample Test Data" below for the accounts created for testing purposes.
- **Additional Assumptions:** No authentication required, and the money currency (for example USD) is precise up to two decimals.  

## Challenges Faced and Solutions

First of all, I have to note that most of the work involved in this exercise was new to me.
At first glance, the core of the assignment seemed really easy to me, since if I had to implement an ATM system in one .py file, it would not take long.
However, I have never worked on a server-side application, so most of what I had to do were things that I have never encountered before, especially working with Flask and Heroku.
Of course, a lot of the work was done using AI assistants, as should be done these days.

### 1. Working with Flask
As I never worked with Flask before, I had to learn the syntax from scratch, including what each part represents and how to use it properly.

### 2. Working with Heroku
Same as before, I never worked with Heroku, and had to learn how to use it and how to sync it with GitHub.

### 3. A couple of challenges along the way
A few bugs like using a different name for the file from the one I used in my code, which crashed the program when I ran it on Heroku, but nothing major. Also, the assumptions and design decisions were somewhat challenging, as stated above.


## File Structure

```
atm-system/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── Procfile           # Heroku deployment configuration
├── runtime.txt        # Python version specification
└── README.md          # This documentation
```

## Sample Test Data

The application includes three sample accounts for testing:
- Account `12345`: Balance $1,000.00
- Account `67890`: Balance $500.00
- Account `11111`: Balance $250.75

## API Testing Instructions

### Using curl (Command Line):

**1. Check Balance:**
```bash
curl https://dv-hw1-atm-shahar-f-202508-5cd41b03ef58.herokuapp.com/accounts/12345/balance
```

**2. Withdraw Money:**
```bash
curl -X POST https://dv-hw1-atm-shahar-f-202508-5cd41b03ef58.herokuapp.com/accounts/12345/withdraw -H "Content-Type: application/json" -d '{"amount": 100}'
```

**3. Deposit Money:**
```bash
curl -X POST https://dv-hw1-atm-shahar-f-202508-5cd41b03ef58.herokuapp.com/accounts/12345/deposit -H "Content-Type: application/json" -d '{"amount": 200}'
```

## Repository Information

**GitHub Repository:** https://github.com/Shaharocks/Double_Verify_Home_Assignment_ATM