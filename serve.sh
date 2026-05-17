#!/bin/bash
cd "/Users/lorisfauville/Documents/Claude/Projects/SIte portfolio"
python3 -m http.server ${PORT:-8080}
