# Log Report Analysis

There is an Apache-style access log located in the working directory at `/app/access.log`.

Your task is to analyze this traffic and summarize your findings into a JSON report.

**Success Criteria:**
1. Parse the `/app/access.log` file.
2. Calculate three specific metrics: the total number of requests, the total number of unique client IPs, and the most popular path requested.
3. Save your findings to a file named `/app/report.json`.
4. The JSON object must contain exactly these three keys:
   - "total_requests" (integer)
   - "unique_ips" (integer)
   - "top_path" (string)