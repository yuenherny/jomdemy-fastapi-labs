Revision Day 1


Revision Day 2


Revision Day 3
- ORM - object relational mapping
- SQLModel - but FastAPI has yet to update its docs on SQLModel integration
- Chap 07: Security
    - Protect nodes / paths using JWT and OAuth2
    - Passlib[bcrypt]
    - Depends(authenticate)
    - CORS -  to allow web browser to access our API


Revision Day 4
- Chap 08: testing the API
- Chap 09: Deployment
    - On DEV: pip freeze > requirements.txt
    - On PROD: Create env, pip install -r requirements.txt, python main.py
    - High performance: Integration with NGINX and Apache
- Create client app:
    - Browser + JS (JS + jQuery) + (JS + VueJS = SPA)
    - Other program than browser (Java, Python, C# backend)
    - Uses the secret token method, not JWT token