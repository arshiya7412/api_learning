# API Fundamentals

## What is an API?

An API allows different software systems to communicate with each other.

## Client and Server

Client → makes the request
Server → receives and processes the request

Example:

React → FastAPI → PostgreSQL

React = Client
FastAPI = Server
PostgreSQL = Database

## Request → Processing → Response

Client
  ↓
Request
  ↓
Server
  ↓
Processing
  ↓
Response
  ↓
Client

## Endpoint

An endpoint is a specific route through which
a client interacts with an API.

Example:

GET /users/25
