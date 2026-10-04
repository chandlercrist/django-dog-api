# Submission checklist and version references

## Implementations completed

- Initial explicit APIView version: `1599dcf6544f8f2043e93f4c3bd0aafa33c19358` (tag `v1-class-based`). DogList and BreedList have get/post; DogDetail and BreedDetail have get/put/delete in controllers.py.
- Bonus ModelViewSet version: `4919f1392c1efc80c97730d82810e4e124274350` (tag `v2-viewsets`). Main uses this implementation.
- Both versions passed the five automated test methods, including all ten required CRUD requests and invalid-input checks.
- Final version passed ten real HTTP requests against a running Django server. See evidence/live-http-results.json. This evidence was generated with Python, not Postman.
- Database migrations were generated and applied successfully. Recreate the local database using `python manage.py migrate`.

## Still required before submission

1. Create the GitHub repository and push this existing Git history and tags using README instructions. No GitHub repository was created in this environment.
2. Run the included Postman collection and capture ten genuine screenshots using README instructions. No Postman screenshots were captured in this environment.
3. Replace YOUR_USERNAME below with your actual GitHub username and attach the screenshots.

## Submission link templates (not published links)

Repository: https://github.com/YOUR_USERNAME/django-dog-api

Initial version: https://github.com/YOUR_USERNAME/django-dog-api/commit/1599dcf6544f8f2043e93f4c3bd0aafa33c19358

Bonus version: https://github.com/YOUR_USERNAME/django-dog-api/commit/4919f1392c1efc80c97730d82810e4e124274350

## Sources used

Official GitHub repository creation instructions and Django REST framework APIView/ViewSet documentation are linked in README.md.
