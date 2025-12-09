# TestCaseGenerator for Confluence (Python + Render)

This service:
- Generates full test cases using OpenAI
- Converts to HTML
- Publishes directly to Confluence Cloud
- Works through a simple REST endpoint

## How to deploy to Render

1. Push this repo to GitHub
2. Go to https://render.com
3. Create → Web service
4. Select this repository
5. Render detects render.yaml automatically
6. Add environment variables:
   - OPENAI_API_KEY
   - CONFLUENCE_EMAIL
   - CONFLUENCE_API_TOKEN
   - CONFLUENCE_BASE_URL
   - CONFLUENCE_PARENT_ID

### Example usage:

POST https://your-app.onrender.com/generate?topic=User%20Renewal%20Statuses
