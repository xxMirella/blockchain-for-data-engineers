# Blockchain for Data Engineers

This repository demonstrates how blockchain data can be treated as an immutable, event-driven data source using a very simple Python pipeline.

## Context

From a data engineering perspective, blockchains behave similarly to distributed logs:
- Blocks are immutable
- Transactions are append-only events
- State is derived from a sequence of events

This project explores that concept by extracting basic on-chain data from Ethereum and storing it in a structured format for further analysis.

## What this project does

- Connects to an Ethereum public RPC
- Reads the latest block
- Extracts basic metadata (block number, timestamp, transaction count)
- Stores the result as a structured JSON file

## Architecture (conceptual)

- Blockchain node as an event source
- Block data as immutable events
- Append-only data ingestion
- Analytics-ready structured output

## Why this matters

Many concepts used in blockchain systems overlap with modern data engineering:
- Event-driven architectures
- Immutable data models
- Distributed systems
- Append-only storage patterns

Understanding blockchain data helps reinforce strong foundations in scalable and reliable data platform design.

## Tech stack

- Python
- Web3.py
- Ethereum public RPC
