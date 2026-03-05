#!/usr/bin/env bash
set -e
fiona-agent --text "${1:-New AI agent architecture released today}" --author "${2:-@someone}"
